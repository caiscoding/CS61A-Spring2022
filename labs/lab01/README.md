# Lab 1: Variables & Functions, Control

## Starter Files

Download [lab01.zip](https://cs61a.org/lab/lab01/lab01.zip). Inside the archive, you will find starter files for the questions in this lab, along with a copy of the [Ok](https://cs61a.org/lab/lab01/ok) autograder.

Additionally, please fill out [this survey](https://go.cs61a.org/setup-survey) with any issues you might have faced in Lab 0 Python installation or if you used the Windows automated installer.

**For quickly generating ok commands, you can now use** [the ok command generator](https://go.cs61a.org/ok-help).

# Quick Logistics Review

## Using Python

When running a Python file, you can use options on the command line to inspect your code further. Here are a few that will come in handy. If you want to learn more about other Python command-line options, take a look at the [documentation](https://docs.python.org/3.9/using/cmdline.html).

- Using no command-line options will run the code in the file you provide and return you to the command line. For example, if we want to run `lab00.py` this way, we would write in the terminal:

    ```
    python3 lab00.py
    ```

- `-i`: The `-i` option runs your Python script, then opens an interactive session. In an interactive session, you run Python code line by line and get immediate feedback instead of running an entire file all at once. To exit, type `exit()` into the interpreter prompt. You can also use the keyboard shortcut `Ctrl-D` on Linux/Mac machines or `Ctrl-Z Enter` on Windows.

    If you edit the Python file while running it interactively, you will need to exit and restart the interpreter in order for those changes to take effect.

    Here's how we can run `lab00.py` interactively:

    ```
    python3 -i lab00.py
    ```

- `-m doctest`: Runs doctests in a particular file. Doctests are surrounded by triple quotes (`"""`) within functions.

    Each test in the file consists of `>>>` followed by some Python code and the expected output (though the `>>>` are not seen in the output of the doctest command).

    To run doctests for `lab00.py`, we can run:

    ```
    python3 -m doctest lab00.py
    ```

## Using OK

In 61A, we use a program called Ok for autograding labs, homeworks, and projects. You should have Ok in the starter files downloaded at the start of this lab. For more information on using Ok commands, learn more [here](https://cs61a.org/articles/using-ok/).

**You can quickly generate most ok commands at** [ok-help](https://ok-help.cs61a.org/).

To use Ok to run doctests for a specified function, run the following command:

```
python3 ok -q <specified function>
```

By default, only tests that did not pass will show up. You can use the `-v` option to show all tests, including tests you have passed:

```
python3 ok -v
```

You can also use the debug printing feature in OK by writing

```
print("DEBUG:", x)
```

Finally, when you have finished all the questions in [lab01.py](https://cs61a.org/lab/lab01/lab01.py), you must submit the assignment using the `--submit` option:

```
python3 ok --submit
```

## Pair programming

You can use this lab as a way to try out pair programming. Check out the [pair programming page](https://cs61a.org/articles/pair-programming/).

# Topics

Consult this section if you need a refresher on the material for this lab. It's okay to skip directly to [the questions](https://cs61a.org/lab/lab01/#required-questions) and refer back here should you get stuck.

## Division, Floor Div, and Modulo

Let's compare the different division-related operators in Python 3:

<table>
<tr>
<th>True Division: / (decimal division)
</th>
<th>
Floor Division: // (integer division)
</th>
<th>
Modulo: % (remainder)
</th>
</tr>
<tr>
<td>

```py
>>> 1 / 5
0.2

>>> 25 / 4
6.25

>>> 4 / 2
2.0

>>> 5 / 0
ZeroDivisionError
```

</td>
<td>

```py
>>> 1 // 5
0

>>> 25 // 4
6

>>> 4 // 2
2

>>> 5 // 0
ZeroDivisionError
```

</td>
<td>

```py
>>> 1 % 5
1

>>> 25 % 4
1

>>> 4 % 2
0

>>> 5 % 0
ZeroDivisionError
```

</td>
</tr>
</table>

Notice that Python outputs `ZeroDivisionError` for certain cases. We will go over this later in this lab under [Error Messages](https://cs61a.org/lab/lab01/#error-messages).

One useful technique involving the `%` operator is to check whether a number x is divisible by another number `y`:

```
x % y == 0
```

For example, in order to check if `x` is an even number:

```
x % 2 == 0
```

## Functions

If we want to execute a series of statements over and over, we can abstract them away into a function to avoid repeating code.

For example, let's say we want to know the results of multiplying the numbers 1-3 by 3 and then adding 2 to it. Here's one way to do it:

```
>>> 1 * 3 + 2
5
>>> 2 * 3 + 2
8
>>> 3 * 3 + 2
11
```

If we wanted to do this with a larger set of numbers, that'd be a lot of repeated code! Let's write a function to capture this operation given any input number.

```py
def foo(x):
    return x * 3 + 2
```

This function, called `foo`, takes in a single **argument** and will **return** the result of multiplying that argument by 3 and adding 2.

Now we can **call** this function whenever we want this operation to be done:

```py
>>> foo(1)
5
>>> foo(2)
8
>>> foo(1000)
3002
```

Applying a function to some arguments is done with a **call expression**.

### Call expressions

A call expression applies a function, which may or may not accept arguments. The call expression evaluates to the function's return value.

The syntax of a function call:

```
  add   (    2   ,    3   )
   |         |        |
operator  operand  operand
```

Every call expression requires a set of parentheses delimiting its comma-separated operands.

To evaluate a function call:

1. Evaluate the operator, and then the operands (from left to right).
2. Apply the operator to the operands (the values of the operands).

If an operand is a nested call expression, then these two steps are applied to that inner operand first in order to evaluate the outer operand.

### `return` and `print`

Most functions that you define will contain a `return` statement. The `return` statement will give the result of some computation back to the caller of the function and exit the function. For example, the function `square` below takes in a number `x` and returns its square.

```py
def square(x):
    """
    >>> square(4)
    16
    """
    return x * x
```

When Python executes a `return` statement, the function terminates immediately. If Python reaches the end of the function body without executing a `return` statement, it will automatically return `None`.

In contrast, the `print` function is used to display values in the Terminal. This can lead to some confusion between `print` and `return` because calling a function in the Python interpreter will print out the function's return value.

However, unlike a `return` statement, when Python evaluates a `print` expression, the function does not terminate immediately.

```py
def what_prints():
    print('Hello World!')
    return 'Exiting this function.'
    print('61A is awesome!')

>>> what_prints()
Hello World!
'Exiting this function.'
```

> Notice also that `print` will display text **without the quotes**, but `return` will preserve the quotes.

## Control

### Boolean Operators

Python supports three boolean operators: `and`, `or`, and `not`:

```py
>>> a = 4
>>> a < 2 and a > 0
False
>>> a < 2 or a > 0
True
>>> not (a > 0)
False
```

- `and` evaluates to `True` only if both operands evaluate to `True`. If at least one operand is `False`, then `and` evaluates to `False`.
- `or` evaluates to `True` if at least one operand evaluates to `True`. If both operands are `False`, then `or` evaluates to `False`.
- `not` evaluates to `True` if its operand evaluates to `False`. It evaluates to `False` if its operand evalutes to `True`.

What do you think the following expression evaluates to? Try it out in the Python interpreter.

```py
>>> True and not False or not True and False
```

It is difficult to read complex expressions, like the one above, and understand how a program will behave. Using parentheses can make your code easier to understand. Python interprets that expression in the following way:

```py
>>> (True and (not False)) or ((not True) and False)
```

This is because boolean operators, like arithmetic operators, have an order of operation:

- `not` has the highest priority
- `and`
- `or` has the lowest priority

**Truthy and Falsey Values**: It turns out `and` and `or` work on more than just booleans (`True`, `False`). Python values such as `0`, `None`, `''` (the empty string), and `[]` (the empty list) are considered false values. All other values are considered true values.

#### Short Circuiting

What do you think will happen if we type the following into Python?

```
1 / 0
```

Try it out in Python! You should see a `ZeroDivisionError`. But what about this expression?

```
True or 1 / 0
```

It evaluates to `True` because Python's `and` and `or` operators *short-circuit*. That is, they don't necessarily evaluate every operand.

<table>
<tr>
<th>
Operator
</th>
<th>
Checks if:
</th>
<th>
Evaluates from left to right up to:
</th>
<th>
Example
</th>
</tr>
<tr>
<td>
AND
</td>
<td>
All values are true
</td>
<td>
The first false value
</td>
<td>

`False and 1 / 0` evaluates to `False`

</td>
</tr>
<tr>
<td>
OR
</td>
<td>
At least one value is true
</td>
<td>
The first true value
</td>
<td>

`True or 1 / 0` evaluates to `True`

</td>
</tr>
</table>

Short-circuiting happens when the operator reaches an operand that allows them to make a conclusion about the expression. For example, `and` will short-circuit as soon as it reaches the first false value because it then knows that not all the values are true.

If `and` and `or` do not short-circuit, they just return the last value; another way to remember this is that `and` and `or` always return the last thing they evaluate, whether they short circuit or not. Keep in mind that `and` and `or` don't always return booleans when using values other than `True` and `False`.

### If Statements

You can review the syntax of `if` statements in [Section 1.5.4](http://composingprograms.com/pages/15-control.html#conditional-statements) of Composing Programs.

> *Tip*: We sometimes see code that looks like this:
>
> ```py
> if x > 3:
>     return True
> else:
>     return False
> ```
>
> This can be written more concisely as `return x > 3`. If your code looks like the code above, see if you can rewrite it more clearly!

### While Loops

You can review the syntax of `while` loops in [Section 1.5.5](http://composingprograms.com/pages/15-control.html#iteration) of Composing Programs.

## Error Messages

By now, you've probably seen a couple of error messages. They might look intimidating, but error messages are very helpful for debugging code. The following are some common types of errors:

<table>
<tr>
<th>
Error Types
</th>
<th>
Descriptions
</th>
</tr>
<tr>
<td>
SyntaxError
</td>
<td>

Contained improper syntax (e.g. missing a colon after an `if` statement or forgetting to close parentheses/quotes)

</td>
</tr>
<tr>
<td>
IndentationError
</td>
<td>
Contained improper indentation (e.g. inconsistent indentation of a function body)
</td>
</tr>
<tr>
<td>
TypeError
</td>
<td>
Attempted operation on incompatible types (e.g. trying to add a function and a number) or called function with the wrong number of arguments
</td>
</tr>
<tr>
<td>
ZeroDivisionError
</td>
<td>
Attempted division by zero
</td>
</tr>
</table>

Using these descriptions of error messages, you should be able to get a better idea of what went wrong with your code. **If you run into error messages, try to identify the problem before asking for help.** You can often Google unfamiliar error messages to see if others have made similar mistakes to help you debug.

For example:

```py
>>> square(3, 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: square() takes 1 positional argument but 2 were given
```

Note:

- The last line of an error message tells us the type of the error. In the example above, we have a `TypeError`.
- The error message tells us what we did wrong -- we gave `square` 2 arguments when it can only take in 1 argument. In general, the last line is the most helpful.
- The second to last line of the error message tells us on which line the error occurred. This helps us track down the error. In the example above, `TypeError` occurred at `line 1`.

# Required Questions

> *Reminder*: Please fill out the Lab 0 setup survey (also included at the beginning of this assignment): [here](https://go.cs61a.org/setup-survey).

## What Would Python Display? (WWPD)

### Q1: WWPD: Control

> Use Ok to test your knowledge with the following "What Would Python Display?" questions:
>
> ```
> python3 ok -q control -u
> ```
>
> **Hint**: Make sure your `while` loop conditions eventually evaluate to a false value, or they'll never stop! Typing `Ctrl-C` will stop infinite loops in the interpreter.

```py
>>> def xk(c, d):
...     if c == 4:
...         return 6
...     elif d >= 4:
...         return 6 + 7 + c
...     else:
...         return 25
>>> xk(10, 10)
______

>>> xk(10, 6)
______

>>> xk(4, 6)
______

>>> xk(0, 0)
______
```

```py
>>> def how_big(x):
...     if x > 10:
...         print('huge')
...     elif x > 5:
...         return 'big'
...     elif x > 0:
...         print('small')
...     else:
...         print("nothing")
>>> how_big(7)
______

>>> how_big(12)
______

>>> how_big(1)
______

>>> how_big(-1)
______
```

```py
>>> n = 3
>>> while n >= 0:
...     n -= 1
...     print(n)
______
```

> *Hint*: Make sure your `while` loop conditions eventually evaluate to a false value, or they'll never stop! Typing `Ctrl-C` will stop infinite loops in the interpreter.

```py
>>> positive = 28
>>> while positive:
...    print("positive?")
...    positive -= 3
______
```

```py
>>> positive = -9
>>> negative = -12
>>> while negative:
...    if positive:
...        print(negative)
...    positive += 3
...    negative += 3
______
```

### Q2: WWPD: Veritasiness

> Use Ok to test your knowledge with the following "What Would Python Display?" questions:
>
> ```
> python3 ok -q short-circuit -u
> ```

```py
>>> True and 13
______

>>> False or 0
______

>>> not 10
______

>>> not None
______
```

```py
>>> True and 1 / 0 and False
______

>>> True or 1 / 0 or False
______

>>> True and 0
______

>>> False or 1
______

>>> 1 and 3 and 6 and 10 and 15
______

>>> -1 and 1 > 0
______

>>> 0 or False or 2 or 1 / 0
______
```

```py
>>> not 0
______

>>> (1 + 1) and 1
______

>>> 1/0 or True
______

>>> (True or False) and False
______
```

### Q3: Debugging Quiz

The following is a quick quiz on different debugging techniques that will be helpful for you to use in this class. You can refer to the [debugging article](https://cs61a.org/articles/debugging/) to answer the questions.

Use Ok to test your understanding:

```
python3 ok -q debugging-quiz -u
```

## Parsons Problems

To work on these problems, open the Parsons editor:

```
python3 parsons
```

### Q4: Add in Range

Complete `add_in_range`, which returns the sum of all integers between `start` and `stop` (inclusive).

```py
def add_in_range(start, stop):
    """
    >>> add_in_range(3, 5)  # .Case 1
    12
    >>> add_in_range(1, 10)  # .Case 2
    55
    """
    "*** YOUR CODE HERE ***"
```

### Q5: Digit Position Match

A number has a digit-position match if the `i`th-to-last digit is `i`. For example, `980` has the `0`th-to-last digit as `0`. Or `98276` has the `2`nd-to-last digit as a `2`.

Write a function that determine if a number `n` has a digit-position match at a `k`th-to-last digit `k`.

```py
def digit_pos_match(n, k):
    """
    >>> digit_pos_match(980, 0) # .Case 1
    True
    >>> digit_pos_match(980, 2) # .Case 2
    False
    >>> digit_pos_match(98276, 2) # .Case 3
    True
    >>> digit_pos_match(98276, 3) # .Case 4
    False
    """
    "*** YOUR CODE HERE ***"
```

## Code Writing Questions

### Q6: Falling Factorial

Let's write a function `falling`, which is a "falling" factorial that takes two arguments, `n` and `k`, and returns the product of `k` consecutive numbers, starting from n and working downwards. When `k` is 0, the function should return 1.

```py
def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
```

Use Ok to test your code:

```
python3 ok -q falling
```

### Q7: Sum Digits

Write a function that takes in a nonnegative integer and sums its digits. (Using floor division and modulo might be helpful here!)

```py
def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
```

Use Ok to test your code:

```py
python3 ok -q sum_digits
```

## Submit

Make sure to submit this assignment by running:

```
python3 ok --submit
```

# Extra Practice

These questions are optional and will not affect your score on this assignment. However, they are **great practice** for future assignments, projects, and exams. Attempting these questions can be valuable in helping cement your knowledge of course concepts.

### Q8: WWPD: What If?

> Use Ok to test your knowledge with the following "What Would Python Display?" questions:
>
> ```
> python3 ok -q if-statements -u
> ```
> 
> **Hint**: `print` (unlike `return`) does not cause the function to exit.

```py
>>> def ab(c, d):
...     if c > 5:
...         print(c)
...     elif c > 7:
...         print(d)
...     print('foo')
>>> ab(10, 20)
______
```

```py
>>> def bake(cake, make):
...     if cake == 0:
...         cake = cake + 1
...         print(cake)
...     if cake == 1:
...         print(make)
...     else:
...         return cake
...     return make
>>> bake(0, 29)
______

>>> bake(1, "mashed potatoes")
______
```

### Q9: K-Occurrence

Complete `k_occurrence`, a function which returns the number of times the digit `k` appears in `num`. 0 is considered to have no digits.

```py
def k_occurrence(k, num):
    """
    >>> k_occurrence(5, 10)  # .Case 1
    0
    >>> k_occurrence(5, 5115)  # .Case 2
    2
    >>> k_occurrence(0, 100)  # .Case 3
    2
    >>> k_occurrence(0, 0)  # .Case 4
    0
    """
    "*** YOUR CODE HERE ***"
```

To work on this problem, open the Parsons editor:

```
python3 parsons
```

### Q10: Double Eights

Write a function that takes in a number and determines if the digits contain two adjacent 8s.

```py
def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
```

Use Ok to test your code:

```
python3 ok -q double_eights
```

# Lab 1: Variables & Functions, Control

## 开始

下载 [lab01.zip](https://cs61a.org/lab/lab01/lab01.zip) 。在该压缩包中，你会发现本实验中问题的启动文件，以及 [Ok](https://cs61a.org/lab/lab01/ok) 自动测试的副本。

此外，请填写这份 [调查表](https://go.cs61a.org/setup-survey) ，说明你在 Lab 0 Python 安装中可能遇到的任何问题，或者你是否使用了 Windows 自动安装程序。

为了快速生成 ok ，你现在可以使用 [ok 命令生成器](https://go.cs61a.org/ok-help)。

# 快速回顾

## 使用 Python

当运行一个 Python 文件时，你可以在命令行上使用选项来进一步检查你的代码。这里有几个会派上用场的选项。如果你想了解更多关于其他 Python 命令行选项的信息，请看一下 [文档](https://docs.python.org/3.9/using/cmdline.html) 。

- 不使用命令行选项将运行你提供的文件中的代码并返回到命令行。例如，如果我们想这样运行 `lab00.py` ，我们会在终端中写道。

    ```
    python3 lab00.py
    ```

- `-i`：选项 `-i` 运行你的 Python 脚本，然后打开一个交互式会话。在交互式会话中，你可以逐行运行 Python 代码，并得到即时的反馈，而不是一次性地运行整个文件。要退出，在解释器提示符下输入 `exit()` 。你也可以在 Linux/Mac 机器上使用键盘快捷键 `Ctrl-D` 或在 Windows 上使用 `Ctrl-Z Enter` 。

    如果你在交互式运行时编辑了 Python 文件，你将需要退出并重新启动解释器，以便使这些改变生效。

    下面是我们如何以交互方式运行 `lab00.py` 。

    ```
    python3 -i lab00.py
    ```

- `-m doctest`：运行一个特定文件中的测试。 Doctests 在函数中用三引号（`"""`）包围。

    文件中的每个测试由 `>>>` 组成，后面是一些 Python 代码和预期的输出（尽管在 doctest 命令的输出中看不到 `>>>` ）。

    为了运行 `lab00.py` 的 doctests ，我们可以运行：

    ```
    python3 -m doctest lab00.py
    ```

## 使用 OK

在 61A 课程中，我们使用一个叫 Ok 的程序来自动处理实验室、家庭作业和项目。在本实验开始时下载的启动文件中拥有 Ok 。关于使用 Ok 命令的更多信息，请在 [这里](https://cs61a.org/articles/using-ok/) 了解。

**你可以在 [ok-help](https://ok-help.cs61a.org/) 上快速生成大多数 ok 命令。**

要使用 Ok 来运行指定函数的测试，请运行以下命令：

```
python3 ok -q <specified function>
```

默认情况下，只有未通过的测试会显示出来。你可以使用 `-v` 选项来显示所有的测试，包括你已经通过的测试。

```
python3 ok -v
```

你也可以使用 OK 中的调试打印功能，方法是编写：

```
print("DEBUG:", x)
```

最后，当你完成了 [lab01.py](https://cs61a.org/lab/lab01/lab01.py) 中的所有问题，你必须使用 `--submit` 选项提交作业：

```
python3 ok --submit
```

## 结对编程

你可以把这个实验作为尝试 pair 编程的一种方式。请查看 [pair 编程页面](https://cs61a.org/articles/pair-programming/)。

# 主题

如果你需要复习本实验的材料，请参考本节。可以直接跳到 [问题](https://cs61a.org/lab/lab01/#required-questions) 上，如果卡住了，可以回到这里。

## 除法、 向下整除和取余

让我们比较一下 Python 3 中不同的除法相关运算符：

<table>
<tr>
<th>真除法: / (十进制除法)
</th>
<th>
向下整除: // (整数除法)
</th>
<th>
取余: % (余数)
</th>
</tr>
<tr>
<td>

```py
>>> 1 / 5
0.2

>>> 25 / 4
6.25

>>> 4 / 2
2.0

>>> 5 / 0
ZeroDivisionError
```

</td>
<td>

```py
>>> 1 // 5
0

>>> 25 // 4
6

>>> 4 // 2
2

>>> 5 // 0
ZeroDivisionError
```

</td>
<td>

```py
>>> 1 % 5
1

>>> 25 % 4
1

>>> 4 % 2
0

>>> 5 % 0
ZeroDivisionError
```

</td>
</tr>
</table>

注意， Python 在某些情况下会输出 `ZeroDivisionError` 。我们将在本实验后面的 [错误信息](https://cs61a.org/lab/lab01/#error-messages) 中讨论这个问题。

一个涉及 `%` 运算符的有用技术是检查一个数字 `x` 是否能被另一个数字 `y` 整除。

```
x % y == 0
```

例如，为了检查 `x` 是否是一个偶数：

```
x % 2 == 0
```

## 函数

如果我们想反复执行一系列的语句，我们可以把它们抽象成一个函数，以避免重复的代码。

例如，假设我们想知道数字 1-3 乘以 3 然后再加 2 的结果。这里有一个方法：

```
>>> 1 * 3 + 2
5
>>> 2 * 3 + 2
8
>>> 3 * 3 + 2
11
```

如果我们想对一个更大的数字集做这个操作，那就会有很多重复的代码。让我们写一个函数来捕捉这个操作，给定任何输入数字都会执行这个操作。

```py
def foo(x):
    return x * 3 + 2
```

这个名为 `foo` 的函数接收一个 `参数` ，并 `返回` 该参数乘以 3 并加上 2 的结果。

现在我们可以随时 `调用` 这个函数来完成这个操作：

```py
>>> foo(1)
5
>>> foo(2)
8
>>> foo(1000)
3002
```

将一些参数赋给一个函数是通过 **调用表达式** 完成的。

### 调用表达式

调用表达式应用一个函数，该函数可能接受也可能不接受参数。调用表达式计算获取函数的返回值。

一个函数调用的语法：

```
  add   (    2   ,    3   )
   |         |        |
operator  operand  operand
```

每个调用表达式都需要一组小括号来限定其逗号分隔的操作数。

一个函数调用：

1. 判断运算符，然后是操作数（从左到右）。
2. 将运算符应用于操作数（操作数的值）。

如果一个操作数是一个嵌套的调用表达式，那么这两个步骤将首先应用于该内部操作数，以便返回给外部操作数。

### `return` 和 `print`

你定义的大多数函数将包含一个 `return` 语句。 `return` 语句将把一些计算的结果反馈给函数的调用者，并退出函数。例如，下面的函数 `square` 接收一个数字 `x` 并返回其平方。

```py
def square(x):
    """
    >>> square(4)
    16
    """
    return x * x
```

当 Python 执行一个 `return` 语句时，函数立即终止。如果 Python 到达函数体的末端而没有执行返回语句，它将自动返回 `None` 。

与此相反， `print` 函数用于在终端显示数值。这可能导致 `print` 和 `return` 之间的一些混淆，因为在 Python 解释器中调用一个函数将打印出函数的返回值。

然而，与 `return` 语句不同，当 Python 执行一个 `print` 表达式时，函数不会立即终止。

```py
def what_prints():
    print('Hello World!')
    return 'Exiting this function.'
    print('61A is awesome!')

>>> what_prints()
Hello World!
'Exiting this function.'
```

> 还请注意， `print` 将显示 **没有引号** 的文本，但 `return` 将保留引号。

## 控制

### Boolean 运算

Python 支持三个布尔运算符： `and`、 `or` 和 `not`：

```py
>>> a = 4
>>> a < 2 and a > 0
False
>>> a < 2 or a > 0
True
>>> not (a > 0)
False
```

- 只有当两个操作数都是 `True` 时， `and` 结果才为 `True` 。如果至少有一个操作数是 `False` 的，那么 `and` 的结果是 `False` 。
- 如果至少有一个操作数的值为 `True` ，则 `or` 的结果为 `True` 。如果两个操作数都是 `False` 的，那么 `or` 的结果是 `False` 。
- 如果它的操作数是 `False` 的，则 `not` 的结果为 `True` 。如果它的操作数为 `True` ，`not` 的结果 `False` 。

你认为下面这个表达式的结果是什么？在 Python 解释器中试试吧。

```py
>>> True and not False or not True and False
```

阅读复杂的表达式，如上面的表达式，并理解程序的行为方式是很困难的。使用小括号可以使你的代码更容易理解。Python 以下列方式解释该表达式：

```py
>>> (True and (not False)) or ((not True) and False)
```

这是因为布尔运算符，像算术运算符一样，有一个运算顺序：

- `not` 具有最高的优先权
- `and`
- `or` 优先级最低

**Truthy 和 Falsey 值**：事实证明， `and` 和 `or` 不仅仅是对布尔值（`True`， `False`）起作用。 Python 的值，如 `0`、 `None` 、 `''`（空字符串）和 `[]` （空列表）被认为是假值。所有其他的值都被认为是真值。

#### 短路运算

如果我们在 Python 中键入以下内容，你认为会发生什么？

```
1 / 0
```

在 Python 中试试吧！你应该看到一个 `ZeroDivisionError` 。但是这个表达式呢？

```
True or 1 / 0
```

它的结果为 `True` ，因为 Python 的 `and` 和 `or` 操作符是短路的。也就是说，它们不一定对每个操作数进行计算。

<table>
<tr>
<th>
操作符
</th>
<th>
检查
</th>
<th>
从左到右评估，直至：
</th>
<th>
例子
</th>
</tr>
<tr>
<td>
AND
</td>
<td>
所有值都为真
</td>
<td>
第一个为假的值
</td>
<td>

`False and 1 / 0` 计算结果为 `False`

</td>
</tr>
<tr>
<td>
OR
</td>
<td>
至少一个值为真
</td>
<td>
第一个真值
</td>
<td>

`True or 1 / 0` 计算结果为 `True`

</td>
</tr>
</table>

当运算符到达一个允许它们对表达式作出结论的操作数时，就会发生短路现象。例如， `and` 在到达第一个假值时就会短路，因为它知道不是所有的值都是真的。

如果 `and` 和 `or` 没有短路，它们只是返回最后一个值；记住这一点的另一种方法是 `and` 和 `or` 总是返回它们计算的最后一个东西，不管它们是否短路。请记住，当使用 `True` 和 `False` 以外的值时， `and` 和 `or` 并不总是返回布尔值。

### If 语句

你可以在《Composing Programs》 [第1.5.4节](http://composingprograms.com/pages/15-control.html#conditional-statements) 中回顾 `if` 语句的语法。

> *提示*：我们有时会看到像这样的代码：
>
> ```py
> if x > 3:
>     return True
> else:
>     return False
> ```
>
> 如果你的代码看起来像上面的代码，看看你是否能更清楚地重写它！这可以更简洁地写成 `return x > 3` 。

### While 循环

你可以在《Composing Programs》 [第1.5.5节](http://composingprograms.com/pages/15-control.html#iteration) 中查看 `while` 循环的语法。

## Error 信息

到现在，你可能已经看到了一些错误信息。它们可能看起来很吓人，但错误信息对调试代码非常有帮助。以下是一些常见的错误类型：

<table>
<tr>
<th>
错误类型
</th>
<th>
描述
</th>
</tr>
<tr>
<td>
SyntaxError
</td>
<td>

包含不恰当的语法（例如，在 `if` 语句后缺少一个冒号或忘记右括号或者引号）。

</td>
</tr>
<tr>
<td>
IndentationError
</td>
<td>
包含不适当的缩进（例如，函数体的缩进不一致）。
</td>
</tr>
<tr>
<td>
TypeError
</td>
<td>
试图对不兼容的类型进行操作（例如，试图添加一个函数和一个数字）或以错误的参数数量调用函数
</td>
</tr>
<tr>
<td>
ZeroDivisionError
</td>
<td>
企图除以零
</td>
</tr>
</table>

利用这些错误信息的描述，你应该能够更好地了解你的代码出了什么问题。**如果你遇到了错误信息，在寻求帮助之前，试着找出问题所在。**你通常可以在谷歌上搜索不熟悉的错误信息，看看其他人是否犯过类似的错误，以帮助你进行调试。

比如说：

```py
>>> square(3, 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: square() takes 1 positional argument but 2 were given
```

注意：

- 错误信息的最后一行告诉我们错误的类型。在上面的例子中，我们有一个 `TypeError` 错误提示。
- 错误信息告诉我们我们做错了什么 —— 我们给了 `square` 两个参数，而它只能接受一个参数。一般来说，最后一行是最有帮助的。
- 错误信息的倒数第二行告诉我们错误发生在哪一行。这有助于我们追踪错误。在上面的例子中， `TypeError` 发生在 `第1行` 。

# 必要的问题

> **提醒**：请填写实验室0设置的调查（也包括在本作业的开头）： [这里](https://go.cs61a.org/setup-survey).

## Python会显示什么？ (WWPD)

### Q1: WWPD: Control

> 用 Ok 来测试你的掌握程度，有以下“Python会显示什么？”问题：
>
> ```
> python3 ok -q control -u
> ```
>
> **提示**：确保你的 `while` 循环条件最终计算结果为一个假值，否则他们永远不会停止！键入 `Ctrl-C` 可以停止解释器中的无限循环。

```py
>>> def xk(c, d):
...     if c == 4:
...         return 6
...     elif d >= 4:
...         return 6 + 7 + c
...     else:
...         return 25
>>> xk(10, 10)
______

>>> xk(10, 6)
______

>>> xk(4, 6)
______

>>> xk(0, 0)
______
```

```py
>>> def how_big(x):
...     if x > 10:
...         print('huge')
...     elif x > 5:
...         return 'big'
...     elif x > 0:
...         print('small')
...     else:
...         print("nothing")
>>> how_big(7)
______

>>> how_big(12)
______

>>> how_big(1)
______

>>> how_big(-1)
______
```

```py
>>> n = 3
>>> while n >= 0:
...     n -= 1
...     print(n)
______
```

> **提示**：确保你的 `while` 循环条件最终计算结果为一个假值，否则他们永远不会停止！键入 `Ctrl-C` 可以停止解释器中的无限循环。

```py
>>> positive = 28
>>> while positive:
...    print("positive?")
...    positive -= 3
______
```

```py
>>> positive = -9
>>> negative = -12
>>> while negative:
...    if positive:
...        print(negative)
...    positive += 3
...    negative += 3
______
```

### Q2: WWPD: Veritasiness

> 用 Ok 来测试你的掌握程度，有以下“Python会显示什么？”问题：
>
> ```
> python3 ok -q short-circuit -u
> ```
> 

```py
>>> True and 13
______

>>> False or 0
______

>>> not 10
______

>>> not None
______
```

```py
>>> True and 1 / 0 and False
______

>>> True or 1 / 0 or False
______

>>> True and 0
______

>>> False or 1
______

>>> 1 and 3 and 6 and 10 and 15
______

>>> -1 and 1 > 0
______

>>> 0 or False or 2 or 1 / 0
______
```

```py
>>> not 0
______

>>> (1 + 1) and 1
______

>>> 1/0 or True
______

>>> (True or False) and False
______
```

### Q3: Debugging Quiz

下面是一个关于不同调试技术的快速测试，对你在这门课上的使用会有帮助。你可以参考 [调试文章](https://cs61a.org/articles/debugging/) 来回答这些问题。

用 Ok 来测试你的理解程度：

```
python3 ok -q debugging-quiz -u
```

## Parsons 问题

要解决这些问题，请打开 Parsons 编辑器：

```
python3 parsons
```

### Q4: Add in Range

完成 `add_in_range` ，返回 `start` 和 `stop` （包括）之间所有整数的总和。

```py
def add_in_range(start, stop):
    """
    >>> add_in_range(3, 5)  # .Case 1
    12
    >>> add_in_range(1, 10)  # .Case 2
    55
    """
    "*** YOUR CODE HERE ***"
```

### Q5: Digit Position Match

一个数字有一定的数字位 `i` 。例如， `980` 的有一位是 `0` ，或者 `98276` 有一位是 `2` 。

写一个函数来确定一个数字 `n` ，是否在 `n` 中有一位是 `k` 。

```py
def digit_pos_match(n, k):
    """
    >>> digit_pos_match(980, 0) # .Case 1
    True
    >>> digit_pos_match(980, 2) # .Case 2
    False
    >>> digit_pos_match(98276, 2) # .Case 3
    True
    >>> digit_pos_match(98276, 3) # .Case 4
    False
    """
    "*** YOUR CODE HERE ***"
```

## 代码编写问题

### Q6: Falling Factorial

让我们写一个函数 `falling` ，这是一个“下降”阶乘，它接受两个参数 `n` 和 `k` ，并返回 `k` 个连续数字的乘积，从 `n` 开始，向下进行。当 `k` 为 0 时，该函数应返回 `1` 。

```py
def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
```

用 Ok 来测试你的代码：

```
python3 ok -q falling
```

### Q7: Sum Digits

写一个函数，接收一个非负整数并对其数字进行求和。（使用底层除法和 modulo 在这里可能会有帮助！）

```py
def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
```

用 Ok 来测试你的代码：

```
python3 ok -q sum_digits
```

## 提交

请记得提交这份作业：

```
python3 ok --submit
```

# 额外练习

> 这些问题是可选的，不会影响你在这次作业中的得分。然而，它们是未来作业、项目和考试的 **绝佳练习** 。尝试这些问题对巩固你对课程概念的知识很有价值。

### Q8: WWPD: What If?

> 用 Ok 来测试你的掌握程度，有以下“Python会显示什么？”问题：
>
> ```
> python3 ok -q if-statements -u
> ```
>
> **提示**： `print` （与 `return` 不同）不会导致函数退出。

```py
>>> def ab(c, d):
...     if c > 5:
...         print(c)
...     elif c > 7:
...         print(d)
...     print('foo')
>>> ab(10, 20)
______
```

```py
>>> def bake(cake, make):
...     if cake == 0:
...         cake = cake + 1
...         print(cake)
...     if cake == 1:
...         print(make)
...     else:
...         return cake
...     return make
>>> bake(0, 29)
______

>>> bake(1, "mashed potatoes")
______
```

### Q9: K-Occurrence

完成 `k_occurrence` ，这个函数可以返回数字 `k` 在 `num` 中出现的次数。 `0` 被认为是没有该数字的。

```py
def k_occurrence(k, num):
    """
    >>> k_occurrence(5, 10)  # .Case 1
    0
    >>> k_occurrence(5, 5115)  # .Case 2
    2
    >>> k_occurrence(0, 100)  # .Case 3
    2
    >>> k_occurrence(0, 0)  # .Case 4
    0
    """
    "*** YOUR CODE HERE ***"
```

为了解决这个问题，打开 Parsons 编辑器。

```
python3 parsons
```

### Q10: Double Eights

编写一个函数，输入一个数字并确定数字是否包含两个相邻的 8 。

```py
def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 测试你的代码：

```
python3 ok -q double_eights
```