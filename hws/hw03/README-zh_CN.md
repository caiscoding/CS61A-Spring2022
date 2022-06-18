# Homework 3: Recursion, Tree Recursion

## 说明

下载 [hw03.zip](https://inst.eecs.berkeley.edu/~cs61a/sp22/hw/hw03/hw03.zip) 。在压缩包内，你会发现一个名为 [hw03.py](https://inst.eecs.berkeley.edu/~cs61a/sp22/hw/hw03/hw03.py) 的文件，以及一份 `ok` 的自动测试的副本。

**提交：**完成后，用 `python3 ok --submit` 提交。你可以在截止日期前多次提交，但只有最后一次提交才会被打分。检查你是否已经在 [okpy.org](https://okpy.org/) 上成功提交了你的代码。关于提交作业的更多说明，请参见[Lab 0](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab00#submitting-the-assignment)  。

**使用 Ok ：**如果你有任何关于使用 Ok 的问题，请参考 [本指南](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/using-ok) 。

**阅读资料：**你可能会发现以下参考资料很有用：

- [第1.7节](http://composingprograms.com/pages/17-recursive-functions.html)

**评分：**家庭作业是根据正确率来评分的。每一个错误的问题将使总分减少一分。如教学大纲中所述，有一个家庭作业政策。**这个家庭作业满分是 2 分。**

> **重要提示：**家庭作业 3 的更新已于周日发布。如果你在那之前下载了该作业，请更新你的作业！要做到这一点并保存你的进度，请重新下载家庭作业，并将新文件夹中的 `hw03.ok` 文件复制到你的旧文件夹。你可以在你的旧文件夹中继续工作并提交。

# 必要的问题

## 入门视频

这些视频可以为解决本作业中的编码问题提供一些有用的指导。

> 要看到这些视频，你应该登录你的 berkeley.edu 电子邮件。

[YouTube link](https://youtu.be/watch?v=_F4uNI6qTjA&list=PLx38hZJ5RLZdj4fEiGslUdu3VKoVOqTg3)

## Parsons 问题

要解决这些问题，请打开 Parsons 编辑器：

```
python3 parsons
```

### Q1: Neighbor Digits

实现函数 `neighbor_digits` ， `neighbor_digits` 接收一个正整数 `num` 和一个可选的参数 `prev_digit` ， `neighbor_digits` 输出 `num` 中在其右边或左边有相同数字的数字数量。

```py
def neighbor_digits(num, prev_digit=-1):
    """
    Returns the number of digits in num that have the same digit to its right
    or left.
    >>> neighbor_digits(111)
    3
    >>> neighbor_digits(123)
    0
    >>> neighbor_digits(112)
    2
    >>> neighbor_digits(1122)
    4
    """
    "*** YOUR CODE HERE ***"
```

### Q2: Has Subsequence

实现函数 `has_subseq` ，它接收一个数字 `n` 和一个数字 `seq` 的 “序列”。该函数返回 `n` 是否包含 `seq` 这个子序列，这个子序列不一定是连续的。

例如， `141` 包含序列 `11` ，因为该序列的第一个数字 1 是 `141` 的第一个数字，该序列的下一个数字 1 在 `141` 的后面。

```py
def has_subseq(n, seq):
    """
    Complete has_subseq, a function which takes in a number n and a "sequence"
    of digits seq and returns whether n contains seq as a subsequence, which
    does not have to be consecutive.

    >>> has_subseq(123, 12)
    True
    >>> has_subseq(141, 11)
    True
    >>> has_subseq(144, 12)
    False
    >>> has_subseq(144, 1441)
    False
    >>> has_subseq(1343412, 134)
    True
    """
    "*** YOUR CODE HERE ***"
```

## 代码编写问题

### Q3: Num eights

编写一个递归函数 `num_eights` ，接收一个正整数 `pos` ，并返回数字 8 在 `pos` 中出现的次数。

**重要提示：**使用递归；如果你使用任何赋值语句，测试将失败。（然而，如果你愿意，你可以使用函数定义）。

```py
def num_eights(pos):
    """Returns the number of times 8 appears as a digit of pos.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    "*** YOUR CODE HERE ***"
```

用 Ok 来测试你的代码：

```
python3 ok -q num_eights
```

### Q4: Ping-pong

ping-pong 序列从 1 开始向上计数，并且总是向上或向下计数。在 `k` 位置处，如果 `k` 是 8 的倍数或包含数字 8 ，则计数方向会进行转换。下面列出了 ping-pong 序列的前 30 个元素，在第 8、16、18、24 和 28 个元素处用括号标记了计数方向的转换：

|索引|1|2|3|4|5|6|7|[8]|9|10|11|12|13|14|15|[16]|17|[18]|19|20|21|22|23|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|PingPong 值|1|2|3|4|5|6|7|[8]|7|6|5|4|3|2|1|[0]|1|[2]|1|0|-1|-2|-3|

|索引 (cont.)|[24]|25|26|27|[28]|29|30|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|PingPong 值|[-4]|-3|-2|-1|[0]|-1|-2|

实现一个函数 `pingpong` ，返回 ping-pong 序列的第 n 个元素，而不使用任何赋值语句。（你可以使用函数定义）

你可以使用你在前一个问题中定义的函数 `num_eights` 。

**重要提示：**使用递归；如果你使用任何赋值语句，测试将失败。（然而，如果你愿意，你可以使用函数定义）。

> **提示：**如果你被难住了，首先尝试用赋值语句和 `while` 语句实现 `pingpong` 。然后，为了将其转换为递归解决方案，编写一个辅助函数，为 `while` 循环主体中改变数值的每个变量设置一个参数。
>
> **提示：**有几个信息是我们需要跟踪的。其中一个细节是计数的方向（增加或减少）。根据上面的提示，想一想我们如何在调用辅助函数的过程中保持对方向的跟踪。

```py
def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    "*** YOUR CODE HERE ***"
```

用 Ok 来测试你的代码：

```
python3 ok -q pingpong
```

### Q5: Count coins

给定一个正整数 `change` ，如果一组硬币的价值之和是 `change` ，那么这组硬币就能换成对应总价值为 `change` 的硬币。这里我们将使用标准的美国硬币价值。1、 5、 10、 25。例如，以下几组硬币可以换取总价值为 `15` 的零钱。

- 15 枚 1 美分硬币
- 10 枚 1 美分硬币和 1 枚 5 美分硬币
- 5 枚 1 美分硬币和 2 枚 5 美分硬币
- 5 枚 1 美分硬币和 1 枚 10 美分硬币
- 3 枚 5 美分硬币
- 1 枚 5 美分硬币和 1 枚 10 美分硬币

因此，有 6 种方法可以找回总价值为 `15` 的零钱。编写一个 **递归** 函数 `count_coins` ，它接收一个正整数的 `change` ，并返回用硬币找零的方法的数量。

你可以使用提供给你的任何一个函数：

- `get_larger_coin` 将返回输入的下一个较大的硬币面值，例如 `get_larger_coin(5)` 返回 `10` 。
- `get_smaller_coin` 将返回输入的下一个较小面值的硬币，例如  `get_smaller_coin(5)`返回 `1` 。

有两种主要方式可以处理这个问题。一种是使用 `get_larger_coin` ，另一种是使用 `get_smaller_coin` 。

**重要提示：**使用递归；如果你使用循环，测试将失败。

> **提示：**参考 `count_partitions` 的 [实现](http://composingprograms.com/pages/17-recursive-functions.html#example-partitions) ，了解如何用较小的部分来计算加起来的最终值的方法。如果你需要跨递归调用来跟踪一个以上的值，可以考虑写一个辅助函数。

```py
def get_larger_coin(coin):
    """Returns the next larger coin in order.
    >>> get_larger_coin(1)
    5
    >>> get_larger_coin(5)
    10
    >>> get_larger_coin(10)
    25
    >>> get_larger_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25

def get_smaller_coin(coin):
    """Returns the next smaller coin in order.
    >>> get_smaller_coin(25)
    10
    >>> get_smaller_coin(10)
    5
    >>> get_smaller_coin(5)
    1
    >>> get_smaller_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1

def count_coins(change):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
```

用 Ok 来测试你的代码：

```
python3 ok -q count_coins
```

## 可选问题

家庭作业也将包含先前的考试级问题供你参考。这些问题没有提交的成分；如果你想挑战的话，可以随时尝试！

1. Fall 2017 MT1 Q4a: [Digital](https://inst.eecs.berkeley.edu/~cs61a/fa21/exam/fa17/mt1/61a-fa17-mt1.pdf#page=5)
2. Summer 2018 MT1 Q5a: [Won't You Be My Neighbor?](https://inst.eecs.berkeley.edu/~cs61a/su18/assets/pdfs/61a-su18-mt.pdf#page=5)
3. Fall 2019 Final Q6b: [Palindromes](https://inst.eecs.berkeley.edu/~cs61a/sp21/exam/fa19/final/61a-fa19-final.pdf#page=6)