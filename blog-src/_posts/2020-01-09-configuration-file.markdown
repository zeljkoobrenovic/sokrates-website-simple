---
layout: post
title:  "Appendix: Sokrates Configuration File"
date:   2020-05-25 19:12:01 +0100
author: by Željko Obrenović (zeljkoobrenovic.com)
permalink: configuration
icon: configuration-file
excerpt: "Sokrates configuration is a JSON file. You can use create this file manually from scratch, or use the init command to generate a default file for your project."
---

### Configuration File for Individual Projects

Sokrates configuration is defined in a JSON file ([see an example here](https://d3axxy9bcycpv7.cloudfront.net/java/tomcat/config.json)).

You can use the **init** command to generate default file for your project.

The default location of the configuration file is  <your-project>/_sokrates/config.json

Based on this configuration Sokrates will generate a number of [reports](reports). The default reports folders is  <your-project>/_sokrates/reports/

![](assets/images/sokrates/config-overview.png)

***Figure 1**: The Sokrates' configuration file describes how Sokrates should view and analyze the source code.*.

The configuration file has several sections, you can use to:
* describe your project with a name, logo, summary text, and to add external links
* [define the scope](scoping), including the location of the source code root, file extensions and files to analyze, ignored files, files classification, defining what is main code, test code, generated code, build & deployment code, or other code…
* identify [logical decompositions](logical-decomposition): one or more ways to looks at components in the system
* define [concerns](concerns): aspects of a software system that cannot be cleanly decomposed from the rest of the system
* set goals and controls: define measurements and alarms to keep your system within the desired values
* provide analysis reference points: for comparison and trend analysis
* add summary findings: manually added one-line insights and notes
* perform advanced configuration: meta-rules for components, concerns and dependencies


### Description of the project

Describes your project with a name, logo, summary text, and to add external links.

{% highlight json %}
"metadata":{
  "name":"Sokrates",
  "description":"A pragmatic source code analyzer.",
  "logoLink":"https://sokrat.org/assets/logo.png",
  "links":[
     {
        "label":"sokrat.org",
        "href":"https://sokrat.org/"
     }
  ]
}
{% endhighlight %}

## Define the scope

[Defines the scope](scoping), including the location of the source code root, file extensions and files to analyze, ignored files, files classification, defining what is main code, test code, generated code, build & deployment code, or other code.

{% highlight json %}
{
"srcRoot":"..",
"extensions":[
  "java",
  "html",
  "xml",
  "md",
  "txt"
],
"ignore":[
  {
     "pathPattern":".*/node_modules/.*",
     "contentPattern":"",
     "include":true,
     "note":""
  },
  {
     "pathPattern":".*/target/.*",
     "contentPattern":"",
     "include":true,
     "note":"Compiled files"
  }
]
}
{% endhighlight %}


* For analysis purposes Sokrates separate files in scope into several categories: main, test, generated, deployment and build, and other.
* The main category contains all manually created source code files that are being used in the production.
* Files in the main category are used as input for other analyses: logical decomposition, concerns, duplication, file size, unit size, and conditional complexity.
* Test source code files are used only for testing of the product. These files are normally not deployed to production.
* Build and deployment source code files are used to configure or support build and deployment process.
* Generated source code files are automatically generated files that have not been manually changed after generation.
* While a source code folder may contain a number of files, Sokrates is primarily interested in the source code files that are being written and maintained by developers.
* Files containing binaries, documentation, or third-party libraries, for instance, are excluded from analysis. The exception are third-party libraries that have been changed by developers.

{% highlight json %}
{
    "main": {
        "name": "main",
        "sourceFileFilters": [
            {
                "pathPattern": ".*",
                "contentPattern": "",
                "exception": false,
                "note": ""
            }
        ],
        "files": []
    },
    "test": {
        "name": "test",
        "sourceFileFilters": [
            {
                "pathPattern": ".*/[Tt]est/.*",
                "contentPattern": "",
                "exception": false,
                "note": "Test files"
            }
        ],
        "files": []
    },
    "generated": {
        "name": "generated",
        "sourceFileFilters": [],
        "files": []
    },
    "buildAndDeployment": {
        "name": "build and deployment",
        "sourceFileFilters": [],
        "files": []
    },
    "other": {
        "name": "other",
        "sourceFileFilters": [],
        "files": []
    }
}
{% endhighlight %}


### Define logical decompositions: one or more ways to looks at components in the system

Identifies [logical decompositions](logical-decomposition): one or more ways to looks at components in the system.

{% highlight json %}
{
   "logicalDecompositions":[
      {
         "name":"primary",
         "scope":"main",
         "filters":[

         ],
         "componentsFolderDepth":0,
         "components":[
            {
               "name":"Logging",
               "sourceFileFilters":[
                  {
                     "pathPattern":".*/LoggingService/.*",
                     "contentPattern":"",
                     "exception":false,
                     "note":""
                  },
                  {
                     "pathPattern":".*/LogQueueProbe/.*",
                     "contentPattern":"",
                     "exception":false,
                     "note":""
                  },
                  {
                     "pathPattern":".*/Logging/.*",
                     "contentPattern":"",
                     "exception":false,
                     "note":""
                  }
               ],
               "files":[

               ]
            }
         ],
         "metaComponents":[

         ],
         "includeRemainingFiles":true,
         "dependenciesFinder":{
            "useBuiltInDependencyFinders":true,
            "rules":[

            ],
            "metaRules":[

            ]
         },
         "renderingOptions":{
            "orientation":"TB"
         },
         "includeExternalComponents":true,
         "duplicationLinkThreshold":50
      }
   ]
}
{% endhighlight %}


### Define concerns: aspects of a software system that cannot be cleanly decomposed from the rest of the system

Defines [concerns](concerns): aspects of a software system that cannot be cleanly decomposed from the rest of the system.

{% highlight json %}
{
   "concernGroups":[
      {
         "name":"general",
         "concerns":[
            {
               "name":"exception handling",
               "sourceFileFilters":[
                  {
                     "pathPattern":".*[.]java",
                     "contentPattern":".* try \\{.*",
                     "include":true,
                     "note":""
                  }
               ]
            },
            {
               "name":"logging",
               "sourceFileFilters":[
                  {
                     "pathPattern":"",
                     "contentPattern":"import .*logging[.]Log.*",
                     "include":true,
                     "note":""
                  }
               ]
            },
            {
               "name":"file operations",
               "sourceFileFilters":[
                  {
                     "pathPattern":"",
                     "contentPattern":"import .*java[.]io[.]File.*",
                     "include":true,
                     "note":""
                  }
               ]
            },
            {
               "name":"javafx",
               "sourceFileFilters":[
                  {
                     "pathPattern":"",
                     "contentPattern":"import javafx.*",
                     "include":true,
                     "note":""
                  }
               ]
            }
         ]
      }
   ]
}
{% endhighlight %}


### Set goals and controls: define measurements and alarms to keep your system within the desired values

Sets goals and controls: define measurements and alarms to keep your system within the desired values.

{% highlight json %}
{
    "goalsAndControls": [
        {
            "goal": "Keep the system simple and easy to change",
            "description": "Aim at keeping the system size modest (less than 200,000 LOC is good), duplication low (less than 5% is good), files small (no files longer than 1000 LOC is good), and units simple (no units with more than 25 decision points is good).",
            "controls": [
                {
                    "metric": "LINES_OF_CODE_MAIN",
                    "description": "Total number of lines of main code",
                    "desiredRange": {
                        "min": "0",
                        "max": "200000",
                        "tolerance": "20000"
                    }
                },
                {
                    "metric": "DUPLICATION_PERCENTAGE",
                    "description": "System duplication",
                    "desiredRange": {
                        "min": "0",
                        "max": "5",
                        "tolerance": "1"
                    }
                },
                {
                    "metric": "NUMBER_OF_FILES_1001_PLUS",
                    "description": "The number of very large files",
                    "desiredRange": {
                        "min": "0",
                        "max": "0",
                        "tolerance": "1"
                    }
                },
                {
                    "metric": "CONDITIONAL_COMPLEXITY_DISTRIBUTION_26_PLUS_COUNT",
                    "description": "Number of very complex units",
                    "desiredRange": {
                        "min": "0",
                        "max": "0",
                        "tolerance": "1"
                    }
                }
            ]
        }
    ]
}
{% endhighlight %}


### Provide analysis reference points: for comparison and trend analysis

Controls enable you to set alarms for any of the Sokrates metrics. An alarm is defined with a desired range and tolerance.

{% highlight json %}
{
   "compareResultsWith": [
     {
        "label": "reference",
        "analysisResultsPath": "history/start/analysisResults.json"
    }
  ]
}
{% endhighlight %}


### Add summary findings: manually added one-line insights and notes

Optional few bullets to summarize the systems.

{% highlight json %}
{
    "summaryFindings": [
        "note 1",
        "note 2"
    ]
}
{% endhighlight %}


### Perform advanced configuration: meta-rules for components, concerns and dependencies


One of the most powerful features of Sokrates is the possibility to use [Sokrates String Transformation Language](sstl) to define meta rules to define components, concerns and dependencies.

A meta rule is a search pattern (content and/or path) combined with the string operations to process found string to get the name that to define a component, concern or a dependency to a component.

Meta rules can be used in logical decompositions (the metaComponents field), dependency finders (the metaRules field), and in concerns (the metaConcerns field)

The following [SSTL](sstl) operations are supported:

* extract (regex1, regex2,...)
* replace (regex, replaceString)
* append (text)
* prepend (text)
* trim
* tolowercase
* touppercase

Example (components and dependencies finder with meta rules):

{% highlight json %}
{
    "logicalDecompositions": [
        {
            "name": "package level",
            "scope": "main",
            "filters": [],
            "componentsFolderDepth": 0,
            "components": [],
            "metaComponents": [
                {
                    "pathPattern": ".*[.]java",
                    "contentPattern": "package nl[.]obren[.]sokrates[.].*",
                    "use": "content",
                    "ignoreComments": true,
                    "nameOperations": [
                        {
                            "op": "extract",
                            "params": [
                                "nl[.]obren[.]sokrates[.][a-zA-Z0-9_]+[.][a-zA-Z0-9_]+"
                            ]
                        },
                        {
                            "op": "replace",
                            "params": [
                                "nl[.]obren[.]sokrates[.]",
                                ""
                            ]
                        }
                    ]
                }
            ],
            "includeRemainingFiles": false,
            "dependenciesFinder": {
                "useBuiltInDependencyFinders": false,
                "rules": [],
                "metaRules": [
                    {
                        "pathPattern": ".*[.]java",
                        "contentPattern": "import nl[.]obren[.]sokrates[.].*",
                        "use": "content",
                        "ignoreComments": true,
                        "nameOperations": [
                            {
                                "op": "extract",
                                "params": [
                                    "nl[.]obren[.]sokrates[.][a-zA-Z0-9_]+[.][a-zA-Z0-9_]+"
                                ]
                            },
                            {
                                "op": "replace",
                                "params": [
                                    "nl[.]obren[.]sokrates[.]",
                                    ""
                                ]
                            }
                        ]
                    }
                ]
            },
            "renderingOptions": {
                "orientation": "TB"
            }
        }
    ]
}
{% endhighlight %}

Example (concerns with meta rules):

{% highlight json %}
{
    "concernGroups": [
        {
            "name": "java technology",
            "concerns": [ ],
            "metaConcerns": [
                {
                    "pathPattern": "",
                    "contentPattern": "import[ ]+java[.].*",
                    "use": "content",
                    "ignoreComments": false,
                    "nameOperations": [
                        {
                            "op": "extract",
                            "params": [
                                "java[.][a-zA-Z0-9_]+"
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}
{% endhighlight %}







