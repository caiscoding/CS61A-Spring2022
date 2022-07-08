# Homework 8: Regular Expressions, BNF

## 说明

下载 [hw08.zip](https://inst.eecs.berkeley.edu/~cs61a/sp22/hw/hw08/hw08.zip) 。

**提交：** 完成后，用 `python3 ok --submit` 提交。你可以在截止日期前多次提交，但只有最后一次提交才会被计分。检查你是否已经在 [okpy.org](https://okpy.org/) 上成功提交了你的代码。关于提交作业的更多说明，请参见 [Lab 0](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab00#submitting-the-assignment) 。

**使用 Ok：** 如果你有任何关于使用 Ok 的问题，请参考 [本指南](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/using-ok) 。

**评分：** 作业是根据正确率来评分的。每一个错误的问题将使总分减少一分。如教学大纲中所述，有一个家庭作业政策。 **这个家庭作业满分为 2 分。**

# 问题

## RegEx

### Q1: CS Classes

在 reddit.com 上，有一个 /r/berkeley 的子 reddit ，用于讨论加州大学伯克利分校的一切。然而，有如此大量的 EE 和 CS 相关的帖子，这些帖子被自动标记，以便读者可以选择忽略它们或只阅读它们。

写一个正则表达式，找到类似于 CS 或 EE 课程的字符串——以“CS”或“EE ”开头，后面是一个数字，然后可以选择后面是“A”、“B”或“C”。你的搜索应该是不区分大小写的，所以“CS61A”和“cs61a”都可以匹配。

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

使用 Ok 来测试你的代码：

```py
python3 ok -q cs_classes
```

### Q2: Time for Times

给你一个文本，并告诉你其中有一些时间。时间可以用两种不同的方式来表示：

- 12 小时 AM/PM 时钟：07:23AM、 05:24PM
- 24 小时时钟：23:59、 12:22、 00:00

写一个正则表达式，就几个例子而言，它可以匹配以下内容：

`['07:23AM', '05:24PM', '23:59', '12:22', '00:00']`

但不会匹配这些无效的“时间”

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

使用 Ok 来测试你的代码：

```py
python3 ok -q match_time
```

## BNF

### Q3: Linked List BNF

> 对于接下来的两个问题，你可以在 [code.cs61a.org](https://code.cs61a.org/) 上测试你的代码，方法是在问题的骨架代码前的开头添加以下一行：
>
> ```
> ?start: link
> -- replace link with tree_node for the next question
> ```

在这个问题中，我们将定义一个 BNF ，解析在 Python 中创建的整数关联列表。我们将不处理 `Link.empty` 。

作为参考，这里有一些关联列表的例子：

*你的实现应该能够处理嵌套的关联列表，比如下面的第三个例子。*

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

使用 Ok 来测试你的代码：

```py
python3 ok -q linked_list
```

### Q4: Tree BNF

现在，我们将定义一个 BNF 来解析 Python 中创建的带有整数叶子的树。

这里有一些树的例子：

*你的实现应该能够处理没有分支和有一个或多个分支的树。*

- `Tree(2)`
- `Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2)])])`

```
tree_node: "null"

?label: "null"

branches: "null"

%ignore /\s+/
%import common.NUMBER
```

使用 Ok 来测试你的代码：

```py
python3 ok -q tree
```

## Regex Parser

之前在 CS61A 中你学习了正则表达式（regex），这是一种用于字符串中模式匹配的语法。在本题中，你将创建一个用于解析正则表达式模式的 BNF 语法，我们将其表示为 `rstring` 。下面，我们为 `rstring` 语法定义了以下骨架：

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

目前的实现非常有限，只能支持直接匹配输入的字母数字模式。在下面的问题中，你将实现对有限的正则表达式特征子集的支持。

> 注意：为了测试的目的，我们要求你的语法树与 doctests 的一致。请确保定义问题中提到的所有表达式，并在问题中没有提到的所有额外表达式前加上 `?` （如 `?rstring` ）。

### Q5: Grouping and Pipes

在这个问题中，你将添加对分组和管道的支持。

回顾一下，分组允许将整个正则表达式作为一个单元来处理，而管道允许一个模式在两侧匹配一个表达式。两者结合起来，可以让我们创建匹配多个字符串的模式！

在你的语法中定义 `group` 和 `pipe` 表达式。

1. 一个 `group` 由任何用圆括号（ `()` ）包围的 `regex` 表达式组成。
2. `pipe` 运算符由一个 `regex` 表达式组成，后面是一个管道（ `|` ）字符，最后是另一个 `regex` 表达式。

例如， `r"apples"` 将完全匹配输入中的“apples”短语。如果我们希望之前的模式也能匹配“oranges”，我们可以使用分组和管道来扩展我们的 `rstring`： `r"(apples)|(oranges)"` 。

> 提示：请注意， `group` 和 `pipe` 本身就是有效的 `regex` 表达式。你可能需要更新一个先前定义的表达式。

使用 Ok 来测试你的代码：

```py
python3 ok -q regex_grouping
```

### Q6: Classes

现在，我们将添加对字符类的支持。

回顾一下，字符类允许模式匹配该类中定义的任何单一 `character` 。该类本身由单个 `character` 或 `characters` 的 `range` 组成。

具体来说，我们定义如下：

1. 一个 `range` 由 `NUMBER` 或 `LETTER` 组成，用连字符（ `-` ）分隔。
2. 一个 `class` 表达式由任何数量的 `character` 或字符 `range` 组成，周围有方括号（ `[]` ）。

请注意，对于这个问题，一个范围只能由 `NUMBER` 或 `LETTER` 组成；这意味着虽然 `[0-9]` 和 `[A-Z]` 是有效的范围，但 `[0-Z]` 不是一个有效的范围。此外，一个 `class` 中的 `character` 和 `range` 可以以任何顺序和任何次数出现。例如， `[ad-fc0-9]` 、 `[ad-f0-9c]` 、 `[a0-9d-fc]` 和 `[0-9ad-fc]` 都是有效的类别。

使用 Ok 来测试你的代码：

```py
python3 ok -q regex_classes
```

## 提交

请确保提交本作业：

```py
python3 ok --submit
```