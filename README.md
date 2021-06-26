<div align="center" markdown>
<img src=""/>



# Tags to images urls

<p align="center">
  <a href="#Overview">Overview</a> •
  <a href="#How-To-Run">How To Run</a> •
  <a href="#How-To-Use">How To Use</a>
</p>


[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervise.ly/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/tags-to-image-urls)
[![views](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/tags-to-image-urls&counter=views&label=views)](https://supervise.ly)
[![used by teams](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/tags-to-image-urls&counter=downloads&label=used%20by%20teams)](https://supervise.ly)
[![runs](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/tags-to-image-urls&counter=runs&label=runs&123)](https://supervise.ly)

</div>

## Overview

icon idea - https://icons8.com/icon/110286/networking-manager


App create report from [Supervisely](https://app.supervise.ly) images project and prepares downloadable `json` file. Report contain matching tags to lists of images to which these tags belong. 



## How To Run 
**Step 1**: Add app to your team from [Ecosystem](https://ecosystem.supervise.ly/apps/convert-supervisely-to-MOT) if it is not there.

**Step 2**: Open context menu of images project -> `Report` -> `Tags to images urls` 

<img src="https://i.imgur.com/8nhsBKH.png" width="800px"/>



## How to use

After running the application, you will be redirected to the `Tasks` page. Once application processing has finished, your link for downloading will be available. Click on the `file name` to download it.

<img src="https://i.imgur.com/wTB9VFu.png"/>

**Note:** You can also find your converted project in `Team Files`->`tags_to_urls`->`<taskId>_<TeamId>_<projectName>.json`.

<img src="https://i.imgur.com/StJZzSY.png"/>
