<div align="center" markdown>
<img src="https://i.imgur.com/KtnbrQe.png"/>



# Tags to image URLs

<p align="center">
  <a href="#Overview">Overview</a> •
  <a href="#How-To-Run">How To Run</a> •
  <a href="#How-To-Use">How To Use</a>
</p>

  
[![](https://img.shields.io/badge/supervisely-ecosystem-brightgreen)](https://ecosystem.supervise.ly/apps/tags-to-image-urls)
[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervise.ly/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/tags-to-image-urls)
[![views](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/tags-to-image-urls&counter=views&label=views)](https://supervise.ly)
[![used by teams](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/tags-to-image-urls&counter=downloads&label=used%20by%20teams)](https://supervise.ly)
[![runs](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/tags-to-image-urls&counter=runs&label=runs&123)](https://supervise.ly)

</div>

## Overview

Application creates report from Supervisely images project that contains images URLs with tags to which these images belong in `json` format.

**Example `.json` file:**

```json
{
    "cat": [
        "https://app.supervise.ly/...png",
        "https://app.supervise.ly/...png"
    ],
    "dog": [
         "https://app.supervise.ly/...png",
         "https://app.supervise.ly/...png",
    ]
}
```



## How To Run 
**Step 1**: Add app to your team from [Ecosystem](https://ecosystem.supervise.ly/apps/tags-to-image-urls) if it is not there.

**Step 2**: Open context menu of images project -> `Report` -> `Tags to image URLs` 

<img src="https://i.imgur.com/8nhsBKH.png" width="800px"/>


## How to use

After running the application, you will be redirected to the `Tasks` page. Once application processing has finished, your file will be available for downloading. 
Click on the `file name` to open file folder.

Your file will placed to the following path: `Team Files`->`tags_to_urls`->`<taskId>_<TeamId>_<projectName>.json`. 

<img src="https://i.imgur.com/wTB9VFu.png"/>

In the file folder simply right click on the file name and choose `Download` option to download it.

<img src="https://i.imgur.com/GIiuw7O.gif"/>
