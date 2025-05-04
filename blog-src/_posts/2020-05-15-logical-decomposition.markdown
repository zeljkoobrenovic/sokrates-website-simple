---
layout: post
title:  "Logical Decompositions"
date:   2020-05-25 19:12:01 +0100
author: by Željko Obrenović (zeljkoobrenovic.com)
permalink: logical-decomposition
icon: logical-decomposition
excerpt: "Logical decomposition is a view on the organization of the main source code. In a logical decomposition, you define components and rules to include files in the components so that each file ends in exactly one component."
---

Logical decomposition is a representation of, or a view on the organization of the main source code. In such a view every and each file is put in exactly one **logical component**. A logical decompostion contains rules that classifies files in components. Sokrates puts the files taht do not match any of the classification rules into a special "Unclassified" component.

In Sokrates, a logical decomposition is considered invalid if a file is classified into two or more components.This constraint is introduced in order to facilitate measuring of dependencies among components.

A Sokrates enables defining multiple logical decompositions for each system. Each logical decomposition can be defined in one of the three ways:

* First approach is based on the folders structure. Components are mapped to folders at defined folder depth relative to the source code root folder.
* Second approach is based on explicit definition of each component. In such explicit definitions, components are explicitly named and their files are selected based on explicitly defined path and content filters.
* Third approach is based on dynamic definition of components and their names. In such dynamic descriptions, components are not explicitly named, but the name is derived based on script with string transformations of file path or content.


### Folder Structure Componentization

The first approach to define logical decompositions works in projects where physical file structure reflects well the logical project structure. For instance, many projects organize source code into subprojects where each subfolder in the root of the project contains a subproject. Sokrates code follows this organization, see [the Sokrates' GitHub source code root](https://github.com/zeljkoobrenovic/sokrates/).

To define a logical decomposition based on the file structure, all you need to do is to specify the folder depth you want to use.

![](assets/images/sokrates/logical-decomposition-folder-depth.png)

***Figure 1:** A logical decomposition based on the file structure. Based on the folder depth (relative to the source coe root), you get different componentizations.*.


{% highlight json %}
{
    "logicalDecompositions": [
        {
            "name": "level-1",
            "scope": "main",
            "filters": [],
            "componentsFolderDepth": 1,
            ...
        },
        {
            "name": "level-2",
            "scope": "main",
            "filters": [],
            "componentsFolderDepth": 2,
            ...
        },
        {
            "name": "level-3",
            "scope": "main",
            "filters": [],
            "componentsFolderDepth": 3,
            ...
        },
    ]
}
{% endhighlight %}

***Figure 2:** A simplified fragment of the Sokrates configuration file defining three folder-based logical decompositions.*.


### Explicit Definition of Each Component

Defining logical decomposition with regular expressions is a more complex but much more flexible and powerful approach.

In its simplest form, you can use regular expressions to classify files into pre-defined components. For each such component, you need to specify a name and a list of regular expressions for including the files. This approach is straightforward, but its main drawback is the need to explicitly define and name each component.

![](assets/images/sokrates/logical-decomposition-static.png)

***Figure 3**: Componentisation based on the static list of component rules. For each such rule, you need to specify a name of the component and a list of regular expressions for including the files in the component.*.

{% highlight json %}
{
    "logicalDecompositions": [
        {
            "name": "primary",
            "scope": "main",
            "filters": [],
            "componentsFolderDepth": 0,
            "components": [
                {
                    "name": "Common",
                    "sourceFileFilters": [
                        {
                            "pathPattern": ".*/common/.*",
                            "contentPattern": "",
                            "exception": false,
                            "note": ""
                        }
                    ],
                    "files": []
                },
                {
                    "name": "Reports",
                    "sourceFileFilters": [
                        {
                            "pathPattern": ".*/reports/.*",
                            "contentPattern": "",
                            "exception": false,
                            "note": ""
                        }
                    ],
                    "files": []
                }
            ],
            ...
        }
    ]
}
{% endhighlight %}
***Figure 4:** A simplified fragment of the Sokrates configuration file for expectedly defining components.*.


### Dynamic Definition of Components

An even more flexible approach is to name components dynamically based on the string transformations of file paths or content. For instance, in one of the projects I worked on, we defined each component with a "lib-" prefix. Instead of listing all components manually, we can define a simple rule that will add components dynamically. This rule will work perfectly as long as we use the "lib-" convention in naming components.

![](assets/images/sokrates/logical-decomposition-dynamic-1.png)
![](assets/images/sokrates/logical-decomposition-dynamic-2.png)

***Figure 5**: Componentisation based on the dynamic component rules. Sokrates derives names of components dynamically based on the string transformations of file paths or content.*.

{% highlight json %}
{
    "logicalDecompositions": [
        {
            "name": "primary",
            "scope": "main",
            "filters": [],
            "componentsFolderDepth": 0,
            "components": [],
            "metaComponents": [
                {
                    "pathPattern": "",
                    "contentPattern": "package nl[.]obren[.]sokrates[.].*",
                    "use": "content",
                    "ignoreComments": true,
                    "nameOperations": [
                        {
                            "op": "extract",
                            "params": [
                                "nl[.]obren[.]sokrates[.][a-z0-9_]+"
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
            ...
        }
    ]
}
{% endhighlight %}

***Figure 6:** A simplified fragment of the Sokrates configuration file for dynamically defining components.*.
