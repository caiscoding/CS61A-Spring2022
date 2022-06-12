# Homework 1: Variables & Functions, Control

## Instructions

Download [hw01.zip](https://cs61a.org/hw/hw01/hw01.zip).

<font color="#bd31e9">

下载 hw01.zip 。

</font>

**Submission**: When you are done, submit with `python3 ok --submit`. You may submit more than once before the deadline; only the final submission will be scored. Check that you have successfully submitted your code on [okpy.org](https://okpy.org/). See [Lab 0](https://cs61a.org/lab/lab00/#submitting-the-assignment) for more instructions on submitting assignments.

<font color="#bd31e9">

**提交**：完成后，用 `python3 ok --submit` 提交。你可以在截止日期前多次提交，但只有最后一次提交才会被评分。检查你是否已经在 okpy.org 上成功提交了你的代码。关于提交作业的更多说明，请参见Lab 0 。

</font>

**Using Ok**: If you have any questions about using Ok, please refer to [this guide](https://cs61a.org/articles/using-ok/).

<font color="#bd31e9">

**使用 Ok**：如果你对使用 Ok 有任何疑问，请参考本指南。

</font>

**Readings**: You might find the following references useful:

- [Section 1.1](http://composingprograms.com/pages/11-getting-started.html)
- [Section 1.2](http://composingprograms.com/pages/12-elements-of-programming.html)
- [Section 1.3](http://composingprograms.com/pages/13-defining-new-functions.html)
- [Section 1.4](http://composingprograms.com/pages/14-designing-functions.html)
- [Section 1.5](http://composingprograms.com/pages/15-control.html)

<font color="#bd31e9">

**阅读资料**：你可能会发现以下参考资料很有用：

- 第1.1节
- 第1.2节
- 第1.3节
- 第1.4节
- 第1.5节

</font>

> **Important** : The lecture on Monday 1/24 will cover readings 1.3-1.5, which contain the material required for questions 2 and 5. (Control)

> <font color="#bd31e9"> **重要提示** ：1/24星期一的讲座将涉及阅读 1.3-1.5 ，其中包含问题 2 和 5 所需的材料。
</font>

**Grading**: Homework is graded based on correctness. Each incorrect problem will decrease the total score by one point. There is a homework recovery policy as stated in the syllabus. **This homework is out of 2 points.**

<font color="#bd31e9">

**评分**：家庭作业是根据正确性来评分的。每一个错误的问题将使总分减少一分。如教学大纲中所述，有一个家庭作业政策。这个家庭作业满分为 2 分。

</font>

# Required Questions

## Welcome Forms

### Q1: Welcome Forms

Please fill out both the [Syllabus Quiz](https://go.cs61a.org/syllabus-quiz), which is based off of our policies found on the course [syllabus](https://cs61a.org/articles/about/), as well as the optional [Welcome Survey](https://go.cs61a.org/welcome-survey).

<font color="#bd31e9">

请填写“课程大纲测验”，该测验是根据课程大纲上的政策制定的，同时也是可选的“欢迎调查”。

</font>

## Parsons Problems

To work on these problems, open the Parsons editor:

<font color="#bd31e9">

要解决这些问题，请打开 Parsons 编辑器：

</font>

```
python3 parsons
```

### Q2: k in Num

Write a function `k_in_num` which takes in two integers, `k` and `num`. `k_in_num` returns `True` if `num` has the digit `k` and returns `False` if `num` does not have the digit `k`. `0` is considered to have no digits.

<font color="#bd31e9">

写一个函数 `k_in_num` ，它接收两个整型参数， `k` 和 `num` 。如果 `num` 含有数字 `k` ， `k_in_num` 返回 `True` ，如果 `num` 不含有数字 `k` ，返回 `False` 。

</font>

```py
def k_in_num(k, num):
    """
    Complete k_in_num, a function which returns True if num has the digit k and
    returns False if num does not have the digit k. 0 is considered to have no
    digits.

    >>> k_in_num(3, 123) # .Case 1
    True
    >>> k_in_num(2, 123) # .Case 2
    True
    >>> k_in_num(5, 123) # .Case 3
    False
    >>> k_in_num(0, 0) # .Case 4
    False
    """
    "*** YOUR CODE HERE ***"
```

## Code Writing Problems

### Q3: A Plus Abs B

Python's `operator` module defines binary functions for Python's intrinsic arithmetic operators. For example, calling `operator.add(2,3)` is equivalent to calling the expression `2 + 3` ; both will return `5`.

<font color="#bd31e9">

Python 的 `operator` 模块为 Python 内在的算术运算符定义了二进制函数。例如，调用 `operator.add(2,3)` 等同于调用表达式 `2+3` ；两者都将返回 `5` 。

</font>

Fill in the blanks in the following function for adding `a` to the absolute value of `b`, without calling `abs`. You may **not** modify any of the provided code other than the two blanks.

<font color="#bd31e9">

在下面的函数中填空， `a` 加 `b` 的绝对值，而不调用 `abs` 。除了这两个空格外，你 **不得** 修改所提供的任何代码。

</font>

```py
def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> a_plus_abs_b(-1, 4)
    3
    >>> a_plus_abs_b(-1, -4)
    3
    """
    if b < 0:
        f = _____
    else:
        f = _____
    return f(a, b)
```

Use Ok to test your code:

<font color="#bd31e9">

用 Ok 来测试你的代码：

</font>

```
python3 ok -q a_plus_abs_b
```

### Q4: Two of Three

Write a function that takes three *positive* numbers as arguments and returns the sum of the squares of the two smallest numbers. **Use only a single line for the body of the function.**

<font color="#bd31e9">

编写一个以三个 *正数* 为参数并返回两个最小数的平方之和的函数。**函数的主体只用一行。**

</font>

```py
def two_of_three(i, j, k):
    """Return m*m + n*n, where m and n are the two smallest members of the
    positive numbers i, j, and k.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    """
    return _____
```

> **Hint**: Consider using the `max` or `min` function:
>
> ```py
> >>> max(1, 2, 3)
> 3
> >>> min(-1, -2, -3)
> -3
> ```
>

> <font color="#bd31e9"> **提示** ：考虑使用 `max` 或 `min` 函数：
>
> ```py
> >>> max(1, 2, 3)
> 3
> >>> min(-1, -2, -3)
> -3
> ```
>
</font>

Use Ok to test your code:

<font color="#bd31e9">

用 Ok 来测试你的代码：

</font>

```
python3 ok -q two_of_three
```

### Q5: Largest Factor

Write a function that takes an integer `n` that is **greater than 1** and returns the largest integer that is smaller than `n` and evenly divides `n`.

<font color="#bd31e9">

编写一个函数，接收一个 **大于 1** 的整数 `n` ，并返回小于 `n` 的最大整数，并且该数能整除 `n` 。

</font>

```py
def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
```

> **Hint**: To check if `b` evenly divides `a`, you can use the expression `a % b == 0`, which can be read as, "the remainder of dividing `a` by `b` is 0."

> <font color="#bd31e9"> **提示** ：要检查 `b` 是否整除以 `a` ，可以使用表达式 `a % b == 0` ，可以读作：“a除以b的余数是0”。
</font>

Use Ok to test your code:

<font color="#bd31e9">

用 Ok 来测试你的代码：

</font>

```
python3 ok -q largest_factor
```

## Submit

Make sure to submit this assignment by running:

<font color="#bd31e9">

请记得提交这份作业：

</font>

```
python3 ok --submit
```