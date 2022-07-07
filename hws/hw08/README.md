# Homework 8: Regular Expressions, BNF

## Instructions

Download [hw08.zip](https://inst.eecs.berkeley.edu/~cs61a/sp22/hw/hw08/hw08.zip).

**Submission:** When you are done, submit with `python3 ok --submit`. You may submit more than once before the deadline; only the final submission will be scored. Check that you have successfully submitted your code on [okpy.org](https://okpy.org/). See [Lab 0](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab00#submitting-the-assignment) for more instructions on submitting assignments.

**Using Ok:** If you have any questions about using Ok, please refer to [this guide](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/using-ok).

**Grading:** Homework is graded based on correctness. Each incorrect problem will decrease the total score by one point. There is a homework recovery policy as stated in the syllabus. **This homework is out of 2 points.**

# Questions

## RegEx

### Q1: CS Classes

On reddit.com, there is an /r/berkeley subreddit for discussions about everything UC Berkeley. However, there is such a large amount of EE and CS-related posts that those posts are auto-tagged so that readers can choose to ignore them or read only them.

Write a regular expression that finds strings that resemble a CS or EE class- starting with "CS" or "EE", followed by a number, and then optionally followed by "A", "B", or "C". Your search should be case insensitive, so both "CS61A" and "cs61a" would match.

```py
import re

def cs_classes(post):
    """
    Returns strings that look like a Berkeley CS or EE class,
    starting with "CS" or "EE", followed by a number, optionally ending with A, B, or C
    and potentially with a space between "CS" or "EE" and the number.
    Case insensitive.

    >>> cs_classes("Is it unreasonable to take CS61A, CS61B, CS70, and EE16A in the summer?")
    True
    >>> cs_classes("how do I become a TA for cs61a? that job sounds so fun")
    True
    >>> cs_classes("Can I take ECON101 as a CS major?")
    False
    >>> cs_classes("Should I do the lab lites or regular labs in EE16A?")
    True
    >>> cs_classes("thoughts on ee127?")
    True
    >>> cs_classes("Is 70 considered an EECS class?")
    False
    >>> cs_classes("What are some good CS upper division courses? I was thinking about CS 161 or CS 169a")
    True
    """
    return bool(re.search(__________, post))
```

Use Ok to test your code:

```py
python3 ok -q cs_classes
```

### Q2: Time for Times

You're given a body of text and told that within it are some times. Times can be written in two different ways:

- 12-hour AM/PM clock: 07:23AM, 05:24PM
- 24-hour clock: 23:59, 12:22, 00:00

Write a regular expression which, for a few examples, would match the following:

`['07:23AM', '05:24PM', '23:59', '12:22', '00:00']`

but would not match these invalid "times"

`['05:64', '70:23']`

```py
import re

def match_time(text):
    """
    >>> match_time("At 07:23AM, I woke up and had some coffee.")
    True
    >>> match_time("I looked at my phone at 12:22 to check the weather.")
    True
    >>> match_time("At 05:24PM, I had sesame bagels with cream cheese.")
    True
    >>> match_time("At 23:59 I was sound asleep.")
    True
    >>> match_time("After, the clocked turned to 00:00.")
    True
    >>> match_time("Mix water in a 1:2 ratio with chicken stock.")
    False
    >>> match_time("At work, I pinged 127.0.0.1:80.")
    False
    >>> match_time("The tennis score was 40:30.")
    False
    """
    return bool(re.search(__________, text))
```

Use Ok to test your code:

```py
python3 ok -q match_time
```

## BNF

### Q3: Linked List BNF

> For the next two problems, you can test your code on [code.cs61a.org](https://code.cs61a.org/) by adding the following line at the beginning before the problem's skeleton code:
>
> ```
> ?start: link
> -- replace link with tree_node for the next question
> ```

In this problem, we're going to define a BNF that parses integer Linked Lists created in Python. We won't be handling `Link.empty`.

For reference, here are some examples of Linked Lists:

*Your implementation should be able to handle nested Linked Lists, such as the third example below.*

- `Link(2)`
- `Link(12, Link(2))`
- `Link(5, Link(7, Link(Link(8, Link(9)))))`

```
link: "null"

?link_first: "null"

?link_rest: "null"

%ignore /\s+/
%import common.NUMBER
```

Use Ok to test your code:

```py
python3 ok -q linked_list
```

### Q4: Tree BNF

Now, we will define a BNF to parse Trees with integer leaves created in Python.

Here are some examples of Trees:

*Your implementation should be able to handle Trees with no branches and one or more branches.*

- `Tree(2)`
- `Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2)])])`

```
tree_node: "null"

?label: "null"

branches: "null"

%ignore /\s+/
%import common.NUMBER
```

Use Ok to test your code:

```py
python3 ok -q tree
```

## Regex Parser

Previously in CS61A you studied regular expressions (regex), a grammar for pattern matching in strings. In this question you will create a BNF grammar for parsing through regular expression patterns, which we will denote as an `rstring`. Below, we've defined the following skeleton for `rstring` grammar:

```
rstring: "r\"" regex* "\""

?regex: character | word

character: LETTER | NUMBER
word: WORD

%ignore /\s+/
%import common.LETTER
%import common.NUMBER
%import common.WORD
```

The current implementation is very limited, and can only support alphanumeric patterns which directly match the input. In the following questions, you will implement support for a limited subset of regular expression features.

> NOTE: for the purposes of testing, we require that your syntax trees match the doctests'. Be sure to define all expressions as noted in the question, and prefix all extra expressions not mentioned in the question with a `?` (such as `?rstring`).

### Q5: Grouping and Pipes

In this question, you will add support for grouping and piping.

Recall that grouping allows for an entire regular expression to be treated as a single unit, and piping allows for a pattern to match an expression on either side. Combined, these will let us create patterns which match multiple strings!

Define the `group` and `pipe` expressions in your grammar.

1. A `group` consists of any `regex` expression surrounded by parentheses (`()`).
2. A `pipe` operator consists of a `regex` expression, followed by a pipe (`|`) character, and lastly followed by another `regex` expression.

For example, `r"apples"` would match exactly the phrase "apples" in an input. If we wanted our pattern from before to match "oranges" as well, we could expand our `rstring` to do so using groupings and pipes: `r"(apples)|(oranges)"`.

> Hint: note that `group`s and `pipe`s are valid `regex` expressions on their own! You may need to update a previously defined expression.

Use Ok to test your code:

```py
python3 ok -q regex_grouping
```

### Q6: Classes

Now, we will add support for character classes.

Recall that character classes allow for the pattern to match any singular `character` defined within the class. The class itself consists either of individual `character`s, or `range`s of `characters`.

Specifically, we define the following:

1. A `range` consists of either `NUMBER`s or `LETTER`s separated by a hyphen (`-`).
2. A `class` expression consists of any number of `character`s or character `range`s surrounded by square brackets (`[]`).

Note that for this question, a range may only consist of either `NUMBER`s or `LETTER`s; this means that while `[0-9]` and `[A-Z]` are valid ranges, `[0-Z]` would not be a valid range. In addition, the `character`s and `range`s in a `class` may appear in any order and any number of times. For example, `[ad-fc0-9]`, `[ad-f0-9c]`, `[a0-9d-fc]`, and `[0-9ad-fc]` are all valid classes.

Use Ok to test your code:

```py
python3 ok -q regex_classes
```

## Submit

Make sure to submit this assignment by running:

```py
python3 ok --submit
```