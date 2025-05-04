---
layout: post
title:  "Appendix: Sokrates String Transformation Language (SSTL)"
date:   2020-05-25 19:12:01 +0100
author: by Željko Obrenović (zeljkoobrenovic.com)
permalink: sstl
icon: transformation
excerpt: "The Sokrates String Transformation Language (SSTL) is a simple embedded programming language enabling you to transform a phrase extracted from a file path or file content into another string. You can use SSTL to define the names of components and identify dependencies among the components."
---


The Sokrates String Transformation Language (SSTL) is a simple embedded programming language enabling you to transform a phrase extracted from a file path or file content into another string.

You define SSTL scripts as a simple list of commands with parameters, a processing pipeline. Each next command takes as an input the result of the previous command.

SSTL supports the following commands:
* extract (regex1)
* replace (regex, string)
* append (text)
* prepend (text)
* trim
* lowercase
* uppercase

 Sokrates uses SSTL in several places:
 - to define dynamic names of components in [logical decompositions](logical-decomposition) (the meta components section)
 - to define dynamic names of [concerns](concerns) (the meta concerns section)
 - to find components names for [dependencies](dependencies) (the meta rules section)

### Examples

The following fragment of a Sokrates configuration files uses SSTL to find dependencies of files to org.apache modules:

{% highlight json %}
{
    "pathPattern": ".*[.]java",
    "contentPattern": "import org[.]apache[.].*",
    "use": "content",
    "ignoreComments": true,
    "nameOperations": [
        {
            "op": "extract",
            "params": [
                "import org[.]apache[.][a-zA-Z0-9_]+"
            ]
        },
        {
            "op": "replace",
            "params": [
                "import org[.]apache[.]",
                ""
            ]
        }
    ]
}
{% endhighlight %}


This script does the following:
* looks for any Java file that contains at least one line starting with "import org.apache." (matches the regex expression "import org[.]apache[.].*")
* it then uses as an input for pressing the found line (the parameter use is set to "content")
* for each such line Sokrates performs two chained SSTL trafsormations:
  * extract the regex pattern "import org[.]apache[.][a-zA-Z0-9_]+"
  * remove "import org[.]apache[.]" (replace it with an empty string)

Figure 2 illustrates this processing on two examples.


***Figure 1:** A fragment of a Sokrates configuration files uses SSTL to find dependencies of files to org.apache modules.*

![](assets/images/sokrates/sstl-example-1.png)

***Figure 2:** The steps of SSTL processing for two import statements for a script defined in Figure 1.*






