<div align="center" markdown>
<img src=""/>



# Tags to images urls.

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

App converts [Supervisely](https://app.supervise.ly) images project to matching tags to lists of images to which these tags belong and prepares downloadable `json` file. 



## How To Run 
**Step 1**: Add app to your team from [Ecosystem](https://ecosystem.supervise.ly/apps/convert-supervisely-to-MOT) if it is not there.

**Step 2**: Open context menu of video project -> `Download via App` -> `Convert Supervisely to MOT format` 

<img src="https://i.imgur.com/2U1invp.png" width="800px"/>

**Step 3**: Select project export mode.

<img src="https://i.imgur.com/dZIp3g7.png" width="600px"/>

**Note:** For case `Export all geometry shapes` all object shapes(polygons, bitmaps, etc) other than rectangle will be converted to rectangles.

## How to use

After running the application, you will be redirected to the `Tasks` page. Once application processing has finished, your link for downloading will be available. Click on the `file name` to download it.

<img src="https://i.imgur.com/61Ghukb.png"/>

**Note:** You can also find your converted project in `Team Files`->`Convert Supervisely to MOT`->`<taskId>_<projectId>_<projectName>.tar.gz`

<img src="https://i.imgur.com/aKCI2Iq.png"/>
