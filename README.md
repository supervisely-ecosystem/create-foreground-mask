<div align="center" markdown>
<img src="https://user-images.githubusercontent.com/48245050/182598346-c78d96d0-cc59-4c97-9c36-fe0a39cb57cf.png"/>

# Create Foreground Mask

<p align="center">
  <a href="#Overview">Overview</a> •
  <a href="#How-To-Use">How To Use</a>
</p>


[![](https://img.shields.io/badge/supervisely-ecosystem-brightgreen)](https://ecosystem.supervisely.com/apps/create-foreground-mask)
[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervisely.com/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/create-foreground-mask)
[![views](https://app.supervisely.com/img/badges/views/supervisely-ecosystem/create-foreground-mask.png)](https://supervisely.com)
[![runs](https://app.supervisely.com/img/badges/runs/supervisely-ecosystem/create-foreground-mask.png)](https://supervisely.com)

</div>

# Overview

App adds `foreground` and `fuzzy` classes to the project and then for every image with alpha channel creates two masks: foreground object (pixels with opacity >= threshold) and fuzzy object (semi-transparent pixels - with opacity in range [1, 254]). 

Usage example: foreground objects (blue) can be used during research with synthetic training data, fuzzy objects (gray) are helpful for analyzing quality of alpha channel. 

<img src="https://media4.giphy.com/media/E5cYcp1zHcTesS0ef7/giphy.gif"/>

# How To Use

1. Add app from ecosystem to your team
2. Prepare project with alpha-channel images. Or add [example project](https://ecosystem.supervisely.com/projects/images-with-alpha-channel) from ecosystem.
   
<img  data-key="sly-module-link" data-module-slug="supervisely-ecosystem/images-with-alpha-channel" src="https://i.imgur.com/2XZyVXy.png" width="300"/>

3. Run it from context menu of images project

<img src="https://i.imgur.com/K1h6P4K.png" width="600"/>

4. (Optional) change input parameters: threshold and fuzzy flag

<img src="https://i.imgur.com/y1IeZ54.png" width="450"/>

4. What until task finished. Masks will be added to existing project on top of existing annotations. If image doesn't have alpha channel, app will print corresponding warning to task log.
