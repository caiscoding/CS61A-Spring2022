# Lab 13: Regular Expressions

## 起始文件

下载 [lab13.zip](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab13/lab13.zip) 。在该压缩包中，你将找到本实验中问题的起始文件，以及 [Ok](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab13/ok) 自动评分器的副本。

# 主题

如果你需要复习本实验的材料，请参考这一部分。你可以直接跳到问题上，如果遇到困难，可以回到这里。

## 正则表达式

正则表达式是一种描述符合某些标准的字符串集的方法，对于模式匹配来说非常有用。

最简单的正则表达式是匹配一个字符序列的表达式，比如 `aardvark` 可以匹配一个字符串中的任何“ardvark”子串。

然而，你通常想寻找更有趣的模式。我们建议使用 [regexr.com](https://regexr.com/) 或 [regex101.com](https://regex101.com/) 这样的在线工具来尝试模式，因为你会得到关于匹配结果的即时反馈。

### 字符类

一个字符类使得搜索一组字符中的任何一个成为可能。你可以指定字符集或使用预先定义的字符集。

<table>
<tr>
<th>
种类
</th>
<th>
描述
</th>
</tr>
<tr>
<td>

`[abc]`

</td>
<td>

匹配 a、 b 或 c

</td>
</tr>
<tr>
<td>

`[a-z]`

</td>
<td>

匹配 a 和 z 之间的任何字符

</td>
</tr>
<tr>
<td>

`[^A-Z]`

</td>
<td>

匹配任何不在 A 和 Z 之间的字符。

</td>
</tr>
<tr>
<td>

`\w`

</td>
<td>

匹配任何“单词”字符。等效于 `[A-Za-z0-9_]` 。

</td>
</tr>
<tr>
<td>

`\d`

</td>
<td>

匹配任何数字。相当于 `[0-9]` 。

</td>
</tr>
<tr>
<td>

`[0-9]`

</td>
<td>

匹配 0 - 9 范围内的单个数字。等效于 `\d` 。

</td>
</tr>
<tr>
<td>

`\s`

</td>
<td>

匹配任何空白字符（空格、制表符、换行符）。

</td>
</tr>
<tr>
<td>

`.`

</td>
<td>

匹配除换行符以外的任何字符。

</td>
</tr>
</table>

字符类可以组合，如 `[a-zA-Z0-9]` 。

### 组合模式

在正则表达式中，有多种方法可以将模式组合在一起。

<table>
<tr>
<th>
组合
</th>
<th>
描述
</th>
</tr>
<tr>
<td>

`AB`

</td>
<td>

例如： `x[.,]y` 匹配 “x.y” 或 “x,y” 。

</td>
</tr>
<tr>
<td>

`A|B`

</td>
<td>

匹配 A 或 B ，例如。 `\d+|Inf` 匹配包含 1 个或多个数字的序列 **或** "Inf"。

</td>
</tr>
</table>

一个模式后面可以有一个这样的量词来指定该模式可以出现多少个实例。

<table>
<tr>
<th>
符合
</th>
<th>
描述
</th>
</tr>
<tr>
<td>

`*`

</td>
<td>

前面的模式出现了 0 次或更多次。例子： `[a-z]*` 匹配任何小写字母的序列或空字符串。

</td>
</tr>
<tr>
<td>

`+`

</td>
<td>

1 个或更多前面模式的出现。例子： `\d+` 匹配任何非空的数字序列。

</td>
</tr>
<tr>
<td>

`?`

</td>
<td>

0 或 1 个前面模式的出现。例子： `[-+]?` 匹配一个可选的符号。

</td>
</tr>
<tr>
<td>

`{1,3}`

</td>
<td>

匹配前面模式的指定数量。 `{1,3}` 将匹配 1 到 3 个实例。 `{3}` 将精确地匹配 3 个实例。 `{3,}` 将匹配 3 个或更多的实例。例子： `\d{5,6}` 匹配 5 或 6 位数的数字。

</td>
</tr>
</table>

### 组别

圆括号的使用与算术表达式类似，用于创建分组。例如， `(Mahna)+` 匹配有 1 个或更多“Mahna”的字符串，如“MahnaMahna”。如果没有括号， `Mahna+` 将匹配带有“Mahn”和 1 个或多个“a”字符的字符串，如 “Mahnaaaa”。

### 锚点

- `^`： 匹配一个字符串的开头。例如： `^(I|You)` 匹配字符串开头的 I 或 You 。
- `$`： 通常匹配字符串末尾的空字符串或字符串末尾的换行前的空字符串。例如： `(\.edu|\.org|\.com)$` 匹配字符串末尾的 .edu、 .org 或 .com 。
- `\b`： 匹配“单词边界”，即一个单词的开始或结束。例如： `s\b` 匹配词尾的 s 字符。

### 特殊字符

以下是用于表示模式类型的特殊字符：

```
\ ( ) [ ] { } + * ? | $ ^ .
```

这意味着如果你真的想匹配其中一个字符，你必须用反斜杠来转义。例如， `\(1\+3\)` 匹配“(1+3)”。

### 在 Python 中使用正则表达式

许多编程语言都有内置的函数用于将字符串与正则表达式相匹配。我们将在 61A 中使用 Python re 模块，但你也可以在 SQL、JavaScript、Excel、shell 脚本等中使用类似的功能。

搜索方法是在字符串的任何地方搜索一个模式：

```py
re.search(r"(Mahna)+", "Mahna Mahna Ba Dee Bedebe")
```

该方法返回一个匹配对象，它在 Python 中被认为是真实的，可以通过检查来找到匹配的字符串。如果没有找到匹配，则返回 `None` 。

更多细节，请参考 [re 模块文档](https://docs.python.org/3/library/re.html) 或 [re 教程](https://docs.python.org/3/howto/regex.html) 。

# 问题

## 正则表达式

### Q1: What Would RegEx Match?

对于以下每一个正则表达式，建议一个可以完全匹配的字符串。

> 使用 Ok 来检查你对知识的理解，为以下每个问题选择最佳答案：
>
> ```
> python3 ok -q wwrm -u
> ```

> 一个十六进制的颜色代码以 `#` 开头，后面正好是六个十六进制的数字，可以是数字 0-9 或字母 a-f 。

```py
Q: #[a-f0-9]{6}
Choose the number of the correct choice:
0) A hexadecimal color code with 3 letters and 3 numbers
1) A hexadecimal color code that starts with letters and ends with numbers, like #gg1234
2) Any 6-digit hexadecimal color code, like #fdb515
3) Any hexadecimal color code with 0-6 digits

Q: (fizz(buzz|)|buzz)
Choose the number of the correct choice:
0) Only fizzbuzz or buzz
1) Only fizzbuzzbuzz
2) Only fizz
3) Only fizzbuzz, fizz, and buzz
4) Only fizzbuzz

Q: [-+]?\d*\.?\d+
Choose the number of the correct choice:
0) Only signed numbers like +1000, -1.5
1) Only signed or unsigned integers like +1000, -33
2) Signed or unsigned numbers like +1000, -1.5, .051
3) Only unsigned numbers like 0.051

Q: [1-9]+[05]+
Choose the number of the correct choice:
0) Any positive number
1) Numbers that are both greater than 5 and divisible by 5 like 10, 25, 800
2) Numbers that are divisible by 5 but do not have the digits 0 and 5 adjacent to each other as the last 2 digits
3) Numbers that are divisible by 5 like 5, 20, 6325
```

### Q2: Scientific Name

返回输入的字符串 `name` 是否遵循科学名称的正确格式。学名的格式如下：以大写字母开始，后面是句号（ `.` ）或一系列小写字母，后面是空格，后面是一系列小写字母。关于有效和无效的字符串的例子，请参考 doctests 。

```py
import re

def scientific_name(name):
    """
    Returns True for strings that are in the correct notation for scientific names;
    i.e. contains a capital letter followed by a period or lowercase letters, 
    followed by a space, followed by more lowercase letters. Returns False for 
    invalid strings.

    >>> scientific_name("T. rex")
    True
    >>> scientific_name("t. rex")
    False
    >>> scientific_name("tyrannosurus rex")
    False
    >>> scientific_name("t rex")
    False
    >>> scientific_name("Falco peregrinus")
    True
    >>> scientific_name("F peregrinus")
    False
    >>> scientific_name("Annie the F. peregrinus")
    False
    >>> scientific_name("I want a pet T. rex right now")
    False
    """
    return bool(re.search(__________, name))
```

使用 Ok 来测试你的代码：

```py
python3 ok -q scientific_name
```

### Q3: Calculator Ops

编写一个正则表达式，解析用 61A 计算器语言编写的字符串，如果任何表达式正好有两个数字操作数，则返回 `True` 。否则返回 `False` 。

> 注意：允许的运算符是 `+` 、 `-` 、 `*` 和 `/` 。查看这些 [讲座幻灯片](https://cs61a.org/assets/slides/27-Interpreters_Calculator.html#/15) ，了解什么是 61A 计算器语言。

```py
import re

def calculator_ops(calc_str):
    """
    Returns True if an expression from the Calculator language that has two
    numeric operands exists in calc_str, False otherwise.

    >>> calculator_ops("(* 2 4)")
    True
    >>> calculator_ops("(+ (* 3 (+ (* 2 4) (+ 3 5))) (+ (- 10 7) 6))")
    True
    >>> calculator_ops("(* 2)")
    False
    >>> calculator_ops("(/ 8 4 2)")
    False
    >>> calculator_ops("(- 8 3)")
    True
    >>> calculator_ops("+ 3 23")
    False
    """
    return bool(re.search(__________, calc_str))
```

使用 Ok 来测试你的代码：

```py
python3 ok -q calculator_ops
```

### Q4: Roman Numerals

如果 `text` 中存在任何类似于罗马数字的字母串，并且不是另一个单词的一部分，则返回 `True` 。罗马数字是由字母 `I` 、 `V` 、 `X` 、 `L` 、 `C` 、 `D` 、 `M` 组成的，至少有一个字母长。

> 在这个问题上，不要担心一个罗马数字是否有效。例如，“VIIIII”不是一个罗马数字，但如果你的重码与之匹配，它是可以的。

```py
import re

def roman_numerals(text):
    """
    Returns True if any string of letters that could be a Roman numeral
    (made up of the letters I, V, X, L, C, D, M) is found. Returns False otherwise.

    >>> roman_numerals("Sir Richard IIV, can you tell Richard VI that Richard IV is on the phone?")
    True
    >>> roman_numerals("My TODOs: I. Groceries II. Learn how to count in Roman IV. Profit")
    True
    >>> roman_numerals("I. Act 1 II. Act 2 III. Act 3 IV. Act 4 V. Act 5")
    True
    >>> roman_numerals("Let's play Civ VII")
    True
    >>> roman_numerals("i love vi so much more than emacs.")
    False
    >>> roman_numerals("she loves ALL editors equally.")
    False
    """
    return bool(re.search(__________, text))
```

使用 Ok 来测试你的代码：

```py
python3 ok -q roman_numerals
```

## 提交

请确保提交本实验：

```py
python3 ok --submit
```