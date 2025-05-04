---
layout: post
title:  "Background: Sokrates Philosophy"
date:   2020-05-25 19:12:01 +0100
author: by Željko Obrenović (zeljkoobrenovic.com)
permalink: philosophy
icon: sokrates
excerpt: "\"Know your code! The unexamined code is not worth maintaining.\" Sokrates helps you understand your code by making visible the size, complexity, and coupling of software."
---

"*Socrates believed that philosophy – the love of wisdom – was the most important pursuit above all else. For some, he exemplifies more than anyone else in history the pursuit of wisdom through questioning and logical argument, by examining and by thinking. **His 'examination' of life in this way spilled out into the lives of others, such that they began their own 'examination' of life,** but he knew they would all die one day, as saying that a life without philosophy – an 'unexamined' life – was not worth living.*"

Sokrates is a tool that can help you to understand your code by making visible the size, complexity, and coupling of software. With Sokrates, my goal was to create a tool that ordinary software developers and software architects could use in daily work, regardless of how big or small their project is, irrespective of technology.

My primary motivation for building Sokrates was dealing with issues in my daily practice. I am always surprised how difficult it can be to get quick answers to basic, simple questions about your source code:

* How much code do you here?
* How much of it you've written yourself?
* How much of it do you maintain?
* What part of your code has not changed recently?
* Which programming languages do you use?
* What is your primary or main code, the one used to define the structure and logic of the system in production?
* What is your secondary code, the one needed to test and build your system, but itself is not running in production?
* Do you generate some part of your codebase? How?
* How duplicated is your codebase? Why?
* How big are your files?
* How many units do you have? How big are they? How complex?
* How files in your codebase depend on each other?

To answer these and many other questions, Sokrates offers tools, which we will discuss later in the book.

## Sokrates: A Practical Tool vs. An Experiment

Sokrates implements my vision on how to document and analyze software architectures of software systems. Sokrates is an experimental tool that also explores how far following a simple approach to building code analysis tools can get you. In creating Sokrates, I also wanted to prove that it is possible to develop a practical tool but without all complexity frequently associated with static code analysis tools.

The result of my experiment is dual. First, I think I have managed to build a pretty useful and elegant tool. At least for my daily work, it provides a handy addition. But I have also learned a lot, and with this book, I want to share the lessons learned and hopefully influence new generations of practical and straightforward software analysis tools.

This book describes what I have learned during my work and building Sokrates. It is, in many aspects, subjective, presenting my view, experiences, and ideas. Nevertheless, I do think that you can learn something from it.  Most importantly, all that I will describe has been validated in practice in a complex, messy reality.

The journey to this book was through building Sokrates software. But the book and the software are the two sides of the same coin. On the one hand, as I was using Sokrates in my daily work, I made notes for this book. On the other hand, while reflecting on what I wrote, I also started to change some parts of Sokrates based on what I have learned.

![](assets/images/sokrates/intro-book-vs-software.png)

***Figure 1**: The Sokrates project consists of a book and an open-source software tool. They are the two sides of the same coin. Developing software enabled me to implement ideas, test them in practice, and build a useful, proven tool. Writing a book helped me organize ideas, obtain new insights, improve the software, and share the lessons learned.*


## Design Principles

*"Anyone who holds a true opinion without understanding is like a blind man on the right road." Sokrates*

*"Give a man a fish and you feed him for a day; teach a man to fish and you feed him for a lifetime."*

Sokrates follows the following design principles:

* **Teach you how to fish.** With the Sokrates project, I do not want only to promote a software tool. I want to teach you how to build similar tools yourself. Whether you decided to use Sokrates or only its ideas, I believe that understanding how the tool work will help you to understand the analysis results better and to use them better to make decisions.

* **Transparency.** Sokrates' analyses contain no magic. Sokrates reports explicitly explain why some values are there and give you lists of files to double-check the results.

* **Technology independence.** Sokrates is technology independent; in essence, any textual representation could be analyzed at least to some extend by Sokrates. However, Sokrates does offer helpers for accelerating configuration and analysis of standard technologies.

* **Using Metrics to Start a Discussion, Not to Kill It.** Sokrates gives you insights into your code, and some pointer to probe further, but not advice that you can follow blindly.



## Sokrates Pragmatic Approach

Sokrates is a practical source code analysis tool. Sokrates does not aim at replicating the level of details of many other tools, such as SonarQube. Instead, it leans on a few basic principles and techniques to get insights about your code without building a massive and complex tool.

The first thing I have learned pretty fast when building Sokrates is that it is extremely tough to build a proper fully-featured parser for any programming language.  Any software analysis tool needs a handful of such parsers. Contemporary software projects frequently include a dozen or more of different programming languages and dialects.

So how have I solved this problem? By not building fully-featured parsers.

 I've also learned when building Sokrates that you can go a long way with using a few simple, heuristic parsing techniques. You may lose details in the process, but if you focus on the essence, such simple heuristic techniques can offer you incredible value for money. In many instances, you may get the same details as more complex and expensive tools. And performance-wise, simple heuristic techniques often work order of magnitude faster.

In the following chapters, we outline a few of these techniques. The following is useful for those who want to contribute or use the Sokrates source code. But it may also offer few insights into power and limitation of Sokrates analyses.


### Background

Sokrates looks on the source code from a perspective of maintenance, making visible the size, complexity and coupling of software.

For more details see my O'Reilly Video Training (from my time at Software Improvement Group): [Building Maintainable Software](https://player.oreilly.com/videos/9781491950791) (4 hours), and O'Reilly Webcast: [Building Maintainable Software](https://www.oreilly.com/pub/e/3535) (1 hour, together with [Rob van der Leek](https://www.linkedin.com/in/rob-van-der-leek-66596962/)).

The fragment of my training video on building maintainable software is freely avaliable at Youtube:
<br/><br/>
<iframe style="max-width: 560px" width="100%" height="315"
        src="https://www.youtube.com/embed/8k14k3q5zDs?start=334" frameborder="0"
        allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen></iframe>
