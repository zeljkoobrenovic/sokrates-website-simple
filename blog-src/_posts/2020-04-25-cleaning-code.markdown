---
layout: post
title:  "Code Cleaning"
date:   2020-05-25 19:12:01 +0100
author: by Željko Obrenović (zeljkoobrenovic.com)
permalink: cleaning
icon: cleaning
excerpt: "As the first step in its analysis, Sokrates cleans the code to simplify analyses and to improve their reliability. Cleaning includes removal of comments, empty lines, and long string constants."
---

*“Storms don't come to teach us painful lessons, rather they were meant to wash us clean.”* - Socrates

As the first step in its analysis, Sokrates cleans the code to simplify analyses and to improve their reliability. Cleaning includes removal of comments, empty lines, and long string constants.

### Cleaning for Lines of Code Calculations

The central unit of measurement in Sokrates analyses is a line of code. When counting lines fo code, however, Sokrates removes comments and empty lines. Sokrates expresses the size of files and other objects, such as components and concerns in lines of code that do not include blank lines and comments.

For example, the following fragment of code has **35 lines of uncleaned code**:

{% highlight java %}
package junit.framework;

/**
 * A set of assert methods.  Messages are only displayed when an assert fails.
 */

public class Assert {
   /**
    * Protect constructor since it is a static only class
    */
   protected Assert() {
   }

   /**
    * Asserts that a condition is true. If it isn't it throws
    * an AssertionFailedError with the given message.
    */
   static public void assertTrue(String message, boolean condition) {
      if (!condition)
         fail(message);
   }
   /**
    * Asserts that a condition is true. If it isn't it throws
    * an AssertionFailedError.
    */
   static public void assertTrue(boolean condition) {
      assertTrue(null, condition);
   }
   /**
    * Asserts that a condition is false. If it isn't it throws
    * an AssertionFailedError with the given message.
    */
   static public void assertFalse(String message, boolean condition) {
      assertTrue(message, !condition);
   }
{% endhighlight %}

After cleaning the code to remove comment and empty lines, **only 17 lines ode code** are left, and these lines are counted for size calculations:

{% highlight java%}
package junit.framework;
public class Assert {
    protected Assert() {
    }
    static public void assertTrue(String message, boolean condition) {
        if (!condition)
            fail(message);
    }
    static public void assertTrue(boolean condition) {
        assertTrue(null, condition);
    }
    static public void assertFalse(String message, boolean condition) {
        assertTrue(message, !condition);
    }
    static public void assertFalse(boolean condition) {
        assertFalse(null, condition);
    }
{% endhighlight %}

### Cleaning for Duplication Calculations

Before duplication measurements, Sokrates cleanes the code to remove empty lines, comments, and frequently duplicated constructs such as import statements.

Here is an example of code cleaning for duplication calculations:

Before the cleaning, the code has **25 lines**:

{% highlight java %}
/*
 * Copyright (c) 2019 Željko Obrenović. All rights reserved.
 */

package nl.obren.sokrates.sourcecode.operations.impl;

import nl.obren.sokrates.sourcecode.operations.StringOperation;

import java.util.List;

public class LowerCaseOperation extends StringOperation {
    public LowerCaseOperation() {
        super("lowercase");
    }

    public LowerCaseOperation(List<String> params) {
        this();
        this.setParams(params);
    }

    @Override
    public String exec(String input) {
        return input.toLowerCase();
    }
}
{% endhighlight %}

After removal of empty lines and comments, **16 lines** are left:

{% highlight java %}
package nl.obren.sokrates.sourcecode.operations.impl;
import nl.obren.sokrates.sourcecode.operations.StringOperation;
import java.util.List;
public class LowerCaseOperation extends StringOperation {
    public LowerCaseOperation() {
        super("lowercase");
    }
    public LowerCaseOperation(List<String> params) {
        this();
        this.setParams(params);
    }
    @Override
    public String exec(String input) {
        return input.toLowerCase();
    }
}
{% endhighlight %}

Lastly, Sokrates removes statements that are frequenlty automatically inserted and highly duplicated, such as import statements. Sokrates also removes leading and trailing or repeated whitespaces in each line, to be able to identify pieces of code that only differ by their whitespace distribution. This process leads to the following **9 lines** that are used to detect duplication:

{% highlight java %}
public class LowerCaseOperation extends StringOperation {
public LowerCaseOperation() {
super("lowercase");
public LowerCaseOperation(List<String> params) {
this();
this.setParams(params);
@Override
public String exec(String input) {
return input.toLowerCase();
{% endhighlight %}


### Preview the Cleaning in Sokrates Explorer

Sokrates values transparency, so to better understand Sokrates cleaning process, you can use [Sokrates Explorer](/book/explorer) file preview panel to see how the content of each file looks after cleaning:

![](assets/images/sokrates/cleaning-explorer-preview.png)

***Figure 1:** You can use [Sokrates Explorer](/book/explorer) file preview panel to see how the content of each file looks after cleaning.*
