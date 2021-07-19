import os
import supervisely_lib as sly
from supervisely_lib.annotation.annotation import TagCollection
from supervisely_lib.io.json import dump_json_file


my_app = sly.AppService()

TEAM_ID = int(os.environ['context.teamId'])
WORKSPACE_ID = int(os.environ['context.workspaceId'])
PROJECT_ID = int(os.environ['modal.state.slyProjectId'])
TASK_ID = int(os.environ["TASK_ID"])
MODE = os.environ['modal.state.saveMode']


@my_app.callback("tags_to_images_urls")
@sly.timeit
def tags_to_images_urls(api: sly.Api, task_id, context, state, app_logger):
    tags_to_urls = {}
    project = api.project.get_info_by_id(PROJECT_ID)
    project_name = project.name
    file_remote = f"/tags_to_urls/{TASK_ID}_{TEAM_ID}_{project_name}.json"
    meta_json = api.project.get_meta(PROJECT_ID)
    meta = sly.ProjectMeta.from_json(meta_json)

    for tag_meta in meta.tag_metas:
        tags_to_urls[tag_meta.name] = []
    id_to_tag_meta = meta.tag_metas.get_id_mapping()
    datasets = api.dataset.get_list(PROJECT_ID)
    progress = sly.Progress('Writing tags to images URLs', project.images_count, app_logger)
    for dataset in datasets:
        images = api.image.get_list(dataset.id)
        for batch in sly.batched(images):
            image_ids = [image_info.id for image_info in batch]
            if MODE == "both" or MODE == "images":
                for image_info in batch:
                    img_tags = TagCollection.from_api_response(image_info.tags, meta.tag_metas, id_to_tag_meta)
                    for img_tag in img_tags:
                        tags_to_urls[img_tag.name].append(image_info.full_storage_url)
            if MODE == "both" or MODE == "objects":
                ann_infos = api.annotation.download_batch(dataset.id, image_ids)
                for ann_info in ann_infos:
                    ann = sly.Annotation.from_json(ann_info.annotation, meta)
                    image_info = api.image.get_info_by_id(ann_info.image_id)
                    for label in ann.labels:
                        for lbl_tag in label.tags:
                            tags_to_urls[lbl_tag.name].append(image_info.full_storage_url)
        progress.iters_done_report(len(batch))

    file_local = os.path.join(my_app.data_dir, file_remote.lstrip("/"))
    app_logger.info("Local file path: {!r}".format(file_local))
    sly.fs.ensure_base_path(file_local)
    dump_json_file(tags_to_urls, file_local)

    upload_progress = []
    def _print_progress(monitor, upload_progress):
        if len(upload_progress) == 0:
            upload_progress.append(sly.Progress(message=f"Processing {TASK_ID}_{TEAM_ID}_{project_name}.json",
                                                total_cnt=monitor.len,
                                                ext_logger=app_logger,
                                                is_size=True))
        upload_progress[0].set_current_value(monitor.bytes_read)

    file_info = api.file.upload(TEAM_ID, file_local, file_remote, lambda m: _print_progress(m, upload_progress))
    api.task._set_custom_output(task_id, file_info.id, sly.fs.get_file_name_with_ext(file_remote))
    app_logger.info("File has been successfully saved to team files")

    my_app.stop()


def main():
    sly.logger.info("Script arguments", extra={
        "TEAM_ID": TEAM_ID,
        "WORKSPACE_ID": WORKSPACE_ID,
        "modal.state.slyProjectId": PROJECT_ID,
        "modal.state.saveMode": MODE
    })

    my_app.run(initial_events=[{"command": "tags_to_images_urls"}])


if __name__ == '__main__':
    sly.main_wrapper("main", main)
