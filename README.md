<div align="center" markdown>
<img src="https://i.imgur.com/XhsFGR3.png"/>

# Create Foreground Mask

<p align="center">
  <a href="#Overview">Overview</a> •
  <a href="#How-To-Use">How To Use</a>
</p>


[![](https://img.shields.io/badge/supervisely-ecosystem-brightgreen)](https://ecosystem.supervise.ly/apps/create-foreground-mask)
[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervise.ly/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/create-foreground-mask)
[![views](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/create-foreground-mask&counter=views&label=views)](https://supervise.ly)
[![used by teams](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/create-foreground-mask&counter=downloads&label=used%20by%20teams)](https://supervise.ly)
[![runs](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/create-foreground-mask&counter=runs&label=runs)](https://supervise.ly)

</div>

# Overview

App adds `foreground` and `fuzzy` classes to the project and then for every image with alpha channel creates two masks: foreground object (pixels with opacity >= threshold) and fuzzy object (semi-transparent pixels - with opacity in range [1, 254]). 

Usage example: foreground objects (blue) can be used during research with synthetic training data, fuzzy objects (gray) are helpful for analyzing quality of alpha channel. 
