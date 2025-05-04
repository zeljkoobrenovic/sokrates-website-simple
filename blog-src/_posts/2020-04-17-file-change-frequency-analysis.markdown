---
layout: post
title:  "File-Level Measurements: File Change Frequency Analysis"
date:   2020-05-25 19:12:01 +0100
author: by Željko Obrenović (zeljkoobrenovic.com)
permalink: history
icon: file-history
excerpt: "File history analysis takes as an input the list of dates on which source code files changes and studies these dates to understand how frequently developers have changed the files, how old the files are, and how recently developers have updated them."
---

File change analysis takes as an input the list of dates on which source code files changes, and analyses these dates to understand how frequently developers have changed the files, how old are the files, and how recently developers have updated them.

Sokrates cannot itself get the dates of file changes from the source code files and folders. You need to provide a data changes list as a textual file and configure the link to this file in the Sokrates configuration file (you need to enter the path to this file in the field "filesAgeImportPath" in the analysis section of the configuration file).

Sokrates uses as a convention the output that you can generate using git command-line tools. The following command is
 recommended for creating the list of changes for Sokrates analysis:

{% highlight bash %}
java -jar sokrates-LATEST.jar extractGitHistory
{% endhighlight %}

![](assets/images/sokrates/history-git-ls-files.png)

***Figure 1:** Extracting the history of file changes with git commands.*

The previous command assumes that you are running it in the root of your source code project and that your source code project is a proper git repository (i.e., there should be a .git subfolder in the root folder of your project).

The command generates a textual file named **git-history.txt**. The following fragment illustrates the format of this file:

{% highlight txt %}
date       email          commit id                                path
2020-08-18 user@email.com 41c4f5676a3645872d62541d301aca3a20ac6a4f cli/src/main/java/nl/obren/sokrates/cli/CommandLineInterface.java
2020-07-09 user@email.com d41b874bc3a29f20f6673a463cbdd9a324f74f67 cli/src/main/java/nl/obren/sokrates/cli/CommandLineInterface.java
2020-07-09 user@email.com b1a2ccd041ae515ea432bcf3d327acc938d8c8e3 cli/src/main/java/nl/obren/sokrates/cli/CommandLineInterface.java
2020-07-06 user@email.com f6c80d9ede62d6281a1fbacfc9118d33b74a4247 cli/src/main/java/nl/obren/sokrates/cli/CommandLineInterface.java
2020-07-05 user@email.com ae1a0d2cb31470a983fbe8c30003317181b14f23 cli/src/main/java/nl/obren/sokrates/cli/CommandLineInterface.java
2020-07-04 user@email.com f6754747d765df3e6b1a2af67923e396a0cc3aef cli/src/main/java/nl/obren/sokrates/cli/CommandLineInterface.java
2020-07-04 user@email.com 5bea89f5e87772944e836871eb0a988408e9c6c2 cli/src/main/java/nl/obren/sokrates/cli/CommandLineInterface.java
2020-06-14 user@email.com fae3e2934fc0df5d779671f05e1f0685cf1adf7a cli/src/main/java/nl/obren/sokrates/cli/CommandLineInterface.java
2020-06-07 user@email.com b7c0e1cb48b03c22f9002b620389e8af40ea684f cli/src/main/java/nl/obren/sokrates/cli/CommandLineInterface.java
2020-06-06 user@email.com 68a6ec8df5e4b0dc4421930d2bd7c71f5f33f258 cli/src/main/java/nl/obren/sokrates/cli/CommandLineInterface.java
2020-05-18 user@email.com cff81f4b4e05ce19c5ba81fe47c06fba83bb5cdf cli/src/main/java/nl/obren/sokrates/cli/CommandLineInterface.java
2020-05-17 user@email.com 8a79078a674c042b0b57cc3fd7179243fd3e82cc cli/src/main/java/nl/obren/sokrates/cli/CommandLineInterface.java
2020-01-02 user@email.com ec1922c44222244530db0dc8f6306368c5cd39d4 cli/src/main/java/nl/obren/sokrates/cli/CommandLineInterface.java
2019-12-15 user@email.com 14997b6634411b5f0b96410be49b8d901196d42e cli/src/main/java/nl/obren/sokrates/cli/CommandLineInterface.java
2019-12-15 user@email.com 7f4a5cd8ebc9c5aa7f0a6c9714c970cfa035b82c cli/src/main/java/nl/obren/sokrates/cli/CommandLineInterface.java
{% endhighlight %}

***Figure 2:** The example content from a file with a history of file changes. The first 26 characters describe the date and time of a change. After that follows the file path relative to the source code root.*

Each line in the file represents one change of one file. The first 26 characters of each line represent the date and time of a file update (e.g., a git commit). Sokrates currently uses only the date part of this string and ignores the time. The rest of the line contains the relative path to the file.

 While the command we used to generate a history file is a git specific command, Sokrates itself does not have any git dependencies. If you create this file using another tool, respecting the described format of each line, Sokrates will work with it.

After you have generated the input file and configured Sokrates, you can create reports on file changes. A Sokrates file history report answers the following questions:
  * What is the overall distribution of frequency of changes, file age, and recent updates?
  * What is the distribution of frequency of changes, file age, and recent updates per file type?
  * What is the distribution of frequency of changes, file age, and recent updates per component?
  * What are the most frequently changed files?
  * What are the oldest files?
  * What are the most recent changed files?
  * What files have not been changed files?

The example of this report you can [find here](https://d3axxy9bcycpv7.cloudfront.net/java/tomcat/reports/html/FileHistory.html).

![](assets/images/sokrates/history-report-generation.png)

***Figure 3:** Based on the history file, Sokrates generates special reports, data files, and additional configurations for further zooming into the details of file changes.*


 Sokrates provides three types of analyses on file changes:
 * **file changes frequency**,
 * **file age**,
 * **file recency**.

**The Sokrates' file changes frequency analysis** identifies the most and least frequently changed files. Sokrates uses five categories to group files: files changed five or fewer times, files changed 6 to 20 times, files changed 21 to 50 times, files changed 51 to 100 times, and files changed over 100 times.

![](assets/images/sokrates/history-report-example-1.png)

***Figure 4:** A fragment of a Sokrates file change history report, displaying the distribution of recorded file updates (in days with at least one update, multiple updates on one day count as one).*


**The Sokrates' file age analysis** looks when the file creation date, assuming that the oldest date of the file update is its creation date. Sokrates groups files in the following five categories according to their age: less than a month old, one to three months old, three to six months old, six to 12 months old, and more than a year old.

![](assets/images/sokrates/history-report-example-2.png)

***Figure 5:** A fragment of a Sokrates file change history report, displaying the distribution of file ages (based on the dates of the first update).*



**The Sokrates' file changes frequency analysis** looks at the latest date fo file change. Sokrates groups files in the following five categories according to the recency of their changes: files changes in the past month, files changes one to three months ago, files changed three to six months ago, files changed six to 12 months ago, and files changed more than a year ago.

![](assets/images/sokrates/history-report-example-3.png)

***Figure 6:** A fragment of a Sokrates file change history report, displaying the distribution of file update recency (based on the dates of last update).*


 Once you have an overview of files in their age, freshness, or update frequency categories, it may be interesting to compare the quality of code in these categories. Sokrates facilitates this process, creating the configuration files that you can use to automatically analyze source code so that each of the discussed categories is visible as a logical component. You can see if there are differences in code quality between files that are more or less frequently charged, older and new code, and so on. Sokrates creates three such configuration files in the **_sokrates/reports/data/extra_analysis** folder:

 * **config_by_file_change_frequency.json**, configuring analysis so that componentization follows the frequency of file updates,
 * **config_by_file_age.json**, configuring analysis so that componentization follows the age of files, and
 * **config_by_file_freshness.json**, configuring analysis so that componentization follows the last modification date of files.


