# Homework 8 Solution

## Q1: CS Classes

**hw08/hw08.py**

```py
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
    return bool(re.search(r"(ee|EE|cs|CS)\s?\d+[a-cA-C]?", post))
```

## Q2: Time for Times

**hw08/hw08.py**

```py
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
    return bool(re.search(r"\b(([01]?\d)|(2[0123])):[012345]\d([AaPp][Mm])?\b", text))
```

## Q3: Linked List BNF

**hw08/hw08.lark**

```py
link: "Link(" link_first link_rest? ")"

?link_first: link|NUMBER

?link_rest: ", " link

%ignore /\s+/
%import common.NUMBER
```

## Q4: Tree BNF

**hw08/hw08.lark**

```py
tree_node: "Tree(" label branches? ")"


?label: NUMBER

branches: ", [" (tree_node ",")* tree_node "]"

%ignore /\s+/
%import common.NUMBER
```

## Q5: Grouping and Pipes

**hw08/hw08.lark**

```py
rstring: "r\"" regex* "\""

?regex: group | pipe | character | word

group: "(" regex ")"
pipe: regex "|" regex

character: LETTER | NUMBER
word: WORD

%ignore /\s+/
%import common.LETTER
%import common.NUMBER
%import common.WORD
```

## Q6: Classes

**hw08/hw08.lark**

```py
rstring: "r\"" regex* "\""

?regex: group | pipe | character | word | class

group: "(" regex ")"
pipe: regex "|" regex

class: "["(range | character)+"]"
range: (LETTER "-" LETTER) | (NUMBER "-" NUMBER)

character: LETTER | NUMBER
word: WORD

%ignore /\s+/
%import common.LETTER
%import common.NUMBER
%import common.WORD
```

## Running tests

```py
$ python3 ok
=====================================================================
Assignment: Homework 8
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    6 test cases passed! No cases failed.
```