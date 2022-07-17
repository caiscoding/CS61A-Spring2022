# Homework 1: Variables & Functions, Control

## 说明

下载 [hw01.zip](https://inst.eecs.berkeley.edu/~cs61a/sp22/hw/hw01/hw01.zip) 。

**提交**：完成后，用 `python3 ok --submit` 提交。你可以在截止日期前多次提交，但只有最后一次提交才会被评分。检查你是否已经在 [okpy.org](https://okpy.org/) 上成功提交了你的代码。关于提交作业的更多说明，请参见 [Lab 0](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab00#submitting-the-assignment) 。

**使用 Ok**：如果你对使用 Ok 有任何疑问，请参考 [本指南](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/using-ok) 。

**阅读资料**：你可能会发现以下参考资料很有用：

- [第1.1节](http://composingprograms.com/pages/11-getting-started.html)
- [第1.2节](http://composingprograms.com/pages/12-elements-of-programming.html)
- [第1.3节](http://composingprograms.com/pages/13-defining-new-functions.html)
- [第1.4节](http://composingprograms.com/pages/14-designing-functions.html)
- [第1.5节](http://composingprograms.com/pages/15-control.html)

> **重要提示** ：1/24星期一的讲座将涉及阅读 1.3-1.5 ，其中包含问题 2 和 5 所需的材料。

**评分**：家庭作业是根据正确性来评分的。每一个错误的问题将使总分减少一分。如教学大纲中所述，有一个家庭作业政策。这个家庭作业满分为 2 分。

# 必要的问题

## Welcome Forms

### Q1: Welcome Forms

请填写 [“课程大纲测验”](https://go.cs61a.org/syllabus-quiz) ，该测验是根据课程大纲上的 [政策](https://cs61a.org/articles/about/) 制定的，同时也是可选的 [“欢迎调查”](https://go.cs61a.org/welcome-survey) 。

## Parsons 问题

要解决这些问题，请打开 Parsons 编辑器：

```
python3 parsons
```

### Q2: k in Num

写一个函数 `k_in_num` ，它接收两个整型参数， `k` 和 `num` 。如果 `num` 含有数字 `k` ， `k_in_num` 返回 `True` ，如果 `num` 不含有数字 `k` ，返回 `False` 。

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

## 代码编写问题

### Q3: A Plus Abs B

Python 的 `operator` 模块为 Python 内在的算术运算符定义了二进制函数。例如，调用 `operator.add(2,3)` 等同于调用表达式 `2+3` ；两者都将返回 `5` 。

在下面的函数中填空， `a` 加 `b` 的绝对值，而不调用 `abs` 。除了这两个空格外，你 **不得** 修改所提供的任何代码。

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

用 Ok 来测试你的代码：

```
python3 ok -q a_plus_abs_b
```

### Q4: Two of Three

编写一个以三个 *正数* 为参数并返回两个最小数的平方之和的函数。**函数的主体只用一行。**

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

> **提示** ：考虑使用 `max` 或 `min` 函数：
>
> ```py
> >>> max(1, 2, 3)
> 3
> >>> min(-1, -2, -3)
> -3
> ```
>

用 Ok 来测试你的代码：

```
python3 ok -q two_of_three
```

### Q5: Largest Factor

编写一个函数，接收一个 **大于 1** 的整数 `n` ，并返回小于 `n` 的最大整数，并且该数能被 `n` 整除。

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

> **提示** ：要检查 `b` 是否被 `a` 整除，可以使用表达式 `a % b == 0` ，可以读作：“a除以b的余数是0”。

用 Ok 来测试你的代码：

```
python3 ok -q largest_factor
```

## 提交

请记得提交这份作业：

```
python3 ok --submit
```