---
layout: post
title:  "Appendix: Regular Expressions"
date:   2020-05-25 19:12:01 +0100
author: by Željko Obrenović (zeljkoobrenovic.com)
permalink: regex
icon: regex
excerpt: "You cannot efficiently use Sokrates if you do not know at least the basics of regular expressions. Sokrates uses regular expressions for two purposes: to filter and classify files, extract and manipulate text, name components, or identify dependencies."
---

Jeff Atwood, the co-founder of StackOverflow.com, is a big fan of regular expressions. On a shortlist of his mandatory readings for software engineering is the [Regular Expression Cookbook](https://www.amazon.com/dp/1449319432/), and this is what he says:

> I may be a card carrying member of the "Keep It Simple Stupid" club, but I'm making a meteor sized exception for regular expressions. Written properly, they will save you a tremendous amount of time in string manipulation, and I've never run across a project where they didn't come in handy somewhere.
>
> Once you delve into the world of regular expressions, you may become drunk with the amazing power and potential they have, which results in things like Perl. Remember, absolute power corrupts absolutely. But it also rocks absolutely.

You cannot efficiently use Sokrates if you do not know at least the basics of regular expressions. Sokrates uses regular expressions for two purposes: to filter and classify files, extract and manipulate text, name components, or identify dependencies.

### Regular Expressions in Sokrates

Sokrates is all about regular expressions. Sokrates is inspired by [**grep**](https://en.wikipedia.org/wiki/Grep), a command-line tool for searching text data sets for lines that match a regular expression. Its name comes from the ed command g/re/p (globally search for a regular expression and print matching lines). grep was originally developed for the Unix operating system, but later available for all Unix-like systems and some others.

Sokrates uses regular expressions for two main purposes:
* Filter and classify files (see the [Scoping section](scoping) for details), and
* Regular expressions as a part of [Sokrates String Transformation Language (SSTL)](sstl). You can use SSTL to define the names of components and identify dependencies among the components.


### To Probe Further

#### Online resources:

* [Regex One](https://regexone.com/)

* [Regex Crossword](https://regexcrossword.com/)

* [TryRegEX](http://tryregex.com/)

* [Regexr](https://regexr.com/)

* [Regex 101](https://regex101.com/)

* [Python Course on Regular Expressions](https://www.python-course.eu/re.php)


#### Books:

<a href="https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/" target="_blank">
  <img src="assets/images/sokrates/book-regex-cookbook.png" width="300"
       style="box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2), 0 3px 10px 0 rgba(0, 0, 0, 0.19);"/>
</a>

<a href="https://www.oreilly.com/library/view/mastering-regular-expressions/0596528124/" target="_blank">
  <img src="assets/images/sokrates/book-regex.png" width="300"
       style="box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2), 0 3px 10px 0 rgba(0, 0, 0, 0.19);"/>
</a>

<a href="https://www.oreilly.com/library/view/introducing-regular-expressions/9781449338879/" target="_blank">
  <img src="assets/images/sokrates/book-regex-intro.png" width="300"
       style="box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2), 0 3px 10px 0 rgba(0, 0, 0, 0.19);"/>
</a>
