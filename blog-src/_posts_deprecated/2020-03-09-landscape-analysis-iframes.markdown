---
layout: post
title:  "Landscape Analysis: iFrames"
date:   2020-05-25 19:12:01 +0100
author: by Željko Obrenović (zeljkoobrenovic.com)
permalink: landscape
icon: landscape
excerpt: "The Socrates landscape analysis a utility that aggregates and indexes the results of Sokrates analyses,  providing a centralized and uniform on the results of multiple Sokrates projects."
---

The Socrates landscape analysis a utility that aggregates and indexes the results of Sokrates analyses,  providing a centralized and uniform on the results of multiple Sokrates projects. The analysis is called landscape because it draws a map of all projects that you want to view from one place.

The landscape analyses provide a helicopter view on huge code bases. The uniform centralized index page provides an easy way to find and get access to details of individual Sokrates projects. On the other hand, the landscape analysis, in an efficient way, also aggregates and compares basic basing findings from dozens or hundreds of such projects.

To run a Sokrates landscape analysis, you need to get to the root folder, under which are other Sokrates projects. Sokrates landscape analysis assumes that your projects are somewhere in deep folders. Sokrates will recursively go through all folders, looking for all configuration and analysis result files. For details on Sokrates landscape commands, visit [the command line interface page](cli).

![](assets/images/sokrates/cmd-init-landscape.png)

***Figure 1:** The **initLandscape** command goes through all folders to find Sokrates projects, adding them to the index list.*

An alternative to the landscape analysis is to scope a whole codebase one Sokrate project, scoping each sub-project as a component. However, for code bases of dozens of millions of lines of code, such an approach may not be practical enough due to length of analysis. Instead, you can define many smaller projects, and use the landscape analysis to provide a bigger picture.

You can find [an example Sokrates landscape report at the sokrates.dev site](https://d3axxy9bcycpv7.cloudfront.net/_sokrates_landscape/index.html). In this report, I have aggregated and indexed all 65 Sokrates example projects, with more than 11 million lines of code.

The following screenshot shows this report as well:

![](assets/images/sokrates/reports-landscape.png)

***Figure 2:** A screenshot of a Sokrates Landscape report.*

