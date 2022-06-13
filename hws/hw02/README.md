# Homework 2: Higher Order Functions

## Instructions

Download [hw02.zip](https://cs61a.org/hw/hw02/hw02.zip). Inside the archive, you will find a file called [hw02.py](https://cs61a.org/hw/hw02/hw02.py), along with a copy of the `ok` autograder.

**Submission**: When you are done, submit with `python3 ok --submit`. You may submit more than once before the deadline; only the final submission will be scored. Check that you have successfully submitted your code on [okpy.org](https://okpy.org/). See [Lab 0](https://cs61a.org/lab/lab00#submitting-the-assignment) for more instructions on submitting assignments.

**Using Ok**: If you have any questions about using Ok, please refer to [this guide](https://cs61a.org/articles/using-ok).

**Readings**: You might find the following references useful:

- [Section 1.6](https://composingprograms.com/pages/16-higher-order-functions.html)

**Grading**: Homework is graded based on correctness. Each incorrect problem will decrease the total score by one point. There is a homework recovery policy as stated in the syllabus. **This homework is out of 2 points.**

# Required questions

Several doctests refer to these functions:

```py
from operator import add, mul

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1
```

## Getting Started Videos

These videos may provide some helpful direction for tackling the coding problems on this assignment.

> To see these videos, you should be logged into your berkeley.edu email.

[YouTube link](https://youtu.be/playlist?list=PLx38hZJ5RLZedViMkGxB-aaVh2M272bHc)

## Parsons Problems

To work on these problems, open the Parsons editor:

```
python3 parsons
```

### Q1: Count Until Larger

Implement the function `count_until_larger`. `count_until_larger` takes in a positive integer `num`. `count_until_larger` counts the distance between the rightmost digit of `num` and the nearest greater digit; to do so, the function counts digits from right to left. Once it encounters a digit larger than the rightmost digit, it returns that count. If no such digit exists, then the function returns `-1`.

For example, `8117` has a rightmost digit of `7` and returns a count of `3`. `9118117` also returns a count of `3`: for both, the count stops at `8`.

`0` should be treated as having no digits and returns a count of `-1`.

Consult the following doctests for specific behaviors of `count_until_larger`.

```py
def count_until_larger(num):
    """
    Complete the function count_until_larger that takes in a positive integer num.
    count_until_larger examines the rightmost digit and counts digits from right to
    left until it encounters a digit larger than the rightmost digit, then returns that count.

    >>> count_until_larger(117) # .Case 1
    -1
    >>> count_until_larger(8117) # .Case 2
    3
    >>> count_until_larger(9118117) # .Case 3
    3
    >>> count_until_larger(8777)  # .Case 4
    3
    >>> count_until_larger(22) # .Case 5
    -1
    >>> count_until_larger(0) # .Case 6
    -1
    """
    "*** YOUR CODE HERE ***"
```

### Q2: Filter Sequence

Write a function `filter_sequence` which takes in two integers, `start` and `stop`, as well as a function `cond`, which takes in a single argument and outputs a boolean value. `filter_sequence` returns the sum of all digits from `start` to `stop` (inclusive) for which `cond` returns `True`.

```py
def filter_sequence(cond, start, stop):
    """
    Returns the sum of numbers from start (inclusive) to stop (inclusive) that satisfy
    the one-argument function cond.

    >>> filter_sequence(lambda x: x % 2 == 0, 0, 10) # .Case 1
    30
    >>> filter_sequence(lambda x: x % 2 == 1, 0, 10) # .Case 2
    25
    """
    "*** YOUR CODE HERE ***"
```

## Code Writing Questions

### Q3: Hailstone

Douglas Hofstadter's Pulitzer-prize-winning book, Gödel, Escher, Bach, poses the following mathematical puzzle.

1. Pick a positive integer `n` as the start.
2. If `n` is even, divide it by 2.
3. If `n` is odd, multiply it by 3 and add 1.
4. Continue this process until `n` is 1.

The number `n` will travel up and down but eventually end at 1 (at least for all numbers that have ever been tried -- nobody has ever proved that the sequence will terminate). Analogously, a hailstone travels up and down in the atmosphere before eventually landing on earth.

This sequence of values of `n` is often called a Hailstone sequence. Write a function that takes a single argument with formal parameter name `n`, prints out the hailstone sequence starting at `n`, and returns the number of steps in the sequence:

```py
def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    "*** YOUR CODE HERE ***"
```

Hailstone sequences can get quite long! Try 27. What's the longest you can find?

> Note that if `n == 1` initially, then the sequence is one step long.

Use Ok to test your code:

```
python3 ok -q hailstone
```

**Curious about hailstones or hailstone sequences? Take a look at these articles:**

- Check out [this article](https://www.nationalgeographic.org/encyclopedia/hail/) to learn more about how hailstones work!
- In 2019, there was a major [development](https://www.quantamagazine.org/mathematician-terence-tao-and-the-collatz-conjecture-20191211/) in understanding how the hailstone conjecture works for most numbers!

### Q4: Product

The `summation(n, term)` function from the higher-order functions lecture adds up `term(1) + ... + term(n)`. Write a similar function called `product` that returns `term(1) * ... * term(n)`.

```py
def product(n, term):
    """Return the product of the first n terms in a sequence.

    n: a positive integer
    term:  a function that takes one argument to produce the term

    >>> product(3, identity)  # 1 * 2 * 3
    6
    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)    # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    162
    """
    "*** YOUR CODE HERE ***"
```

Use Ok to test your code:

```
python3 ok -q product
```

### Q5: Accumulate

Let's take a look at how `summation` and `product` are instances of a more general function called `accumulate`, which we would like to implement:

```py
def accumulate(merger, start, n, term):
    """Return the result of merging the first n terms in a sequence and start.
    The terms to be merged are term(1), term(2), ..., term(n). merger is a
    two-argument commutative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    >>> # 2 + (1^2 + 1) + (2^2 + 1) + (3^2 + 1)
    >>> accumulate(lambda x, y: x + y + 1, 2, 3, square)
    19
    >>> # ((2 * 1^2 * 2) * 2^2 * 2) * 3^2 * 2
    >>> accumulate(lambda x, y: 2 * x * y, 2, 3, square)
    576
    >>> accumulate(lambda x, y: (x + y) % 17, 19, 20, square)
    16
    """
    "*** YOUR CODE HERE ***"
```

`accumulate` has the following parameters:

- `term` and `n`: the same parameters as in `summation` and `product`
- `merger`: a two-argument function that specifies how the current term is merged with the previously accumulated terms.
- `start`: value at which to start the accumulation.

For example, the result of `accumulate(add, 11, 3, square)` is

```
11 + square(1) + square(2) + square(3) = 25
```

> **Note**: You may assume that `merger` is commutative. That is, `merger(a, b) == merger(b, a)` for all `a`, `b`, and `c`. However, you may not assume `merger` is chosen from a fixed function set and hard-code the solution.

After implementing `accumulate`, show how `summation` and `product` can both be defined as function calls to `accumulate`.

**Important**: You should have a single line of code (which should be a `return` statement) in each of your implementations for `summation_using_accumulate` and `product_using_accumulate`, which the syntax check will check for.

Use Ok to test your code:

```
python3 ok -q accumulate
python3 ok -q summation_using_accumulate
python3 ok -q product_using_accumulate
```

## Submit

Make sure to submit this assignment by running:

```
python3 ok --submit
```

## Bonus Questions

Homework assignments will also contain prior exam-level questions for you to take a look at. These questions have no submission component; feel free to attempt them if you'd like a challenge!

> Note that exams from Spring 2020, Fall 2020, and Spring 2021 gave students access to an interpreter, so the question format may be different than other years. Regardless, the questions included remain good exam-level problems doable *without* access to an interpreter.

1. Fall 2019 MT1 Q3: [You Again](https://cs61a.org/exam/fa19/mt1/61a-fa19-mt1.pdf#page=4) [Higher Order Functions]
2. Spring 2021 MT1 Q4: [Domain on the Range](https://cs61a.org/exam/sp21/mt1/61a-sp21-mt1.pdf#page=14) [Higher Order Functions]
3. Fall 2021 MT1 Q1b: [tik](https://cs61a.org/exam/fa21/mt1/61a-fa21-mt1.pdf#page=4) [Functions and Expressions]

<font color="#bd31e9">

# Homework 2: Higher Order Functions

## 说明

下载 [hw02.zip](https://cs61a.org/hw/hw02/hw02.zip) 。在该压缩包内，你会发现一个名为 [hw02.py](https://cs61a.org/hw/hw02/hw02.py) 的文件，以及一份 `ok` 的自动测试副本。

**提交**：完成后，用 `python3 ok --submit` 提交。你可以在截止日期前多次提交；只有最后一次提交才会被评分。检查你是否已经在 [okpy.org](https://okpy.org/) 上成功提交了你的代码。关于提交作业的更多说明，请参见 [Lab 0](https://cs61a.org/lab/lab00#submitting-the-assignment) 。

**使用 Ok**：如果你有任何关于使用 Ok 的问题，请参考 [本指南](https://cs61a.org/articles/using-ok) 。

**阅读资料**：你可能会发现以下参考资料很有用：

- [第1.6节](https://composingprograms.com/pages/16-higher-order-functions.html)

**评分**：家庭作业是根据正确率来评分的。每一个错误的问题将使总分减少一分。如教学大纲中所述，有一个家庭作业政策。**这个家庭作业满分为 2 分。**

# 必要的问题

有几个测试提到了这些函数：

```py
from operator import add, mul

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1
```

## 入门视频

这些视频可以为解决本作业中的编码问题提供一些有用的指导。

> 要看这些视频，你应该登录到你的 berkeley.edu 邮箱。

[视频链接](https://youtu.be/playlist?list=PLx38hZJ5RLZedViMkGxB-aaVh2M272bHc)

## Parsons 问题

要解决这些问题，请打开 Parsons 编辑器：

```
python3 parsons
```

### Q1: Count Until Larger

实现函数 `count_until_larger` 。 `count_until_larger` 接收一个正整数 `num` 。 `count_until_larger` 计算 `num` 的最右边的数字与最近的大数字之间的距离；为此，函数从右到左计算数字。一旦遇到一个比最右边的数字大的数字，它就会两者之间的距离。如果没有比最右边大的数字，那么函数就会返回 `-1` 。

例如， `8117` 的最右边的数字是 `7` ，返回 `3` 。 `9118117` 也返回 `3` ：对于这两个数字，距离停止在 `8` 。

`0` 应该被视为没有数字，并返回一个 `-1` 。

关于 `count_until_larger` 的具体行为，请参考下面的测试：

```py
def count_until_larger(num):
    """
    Complete the function count_until_larger that takes in a positive integer num.
    count_until_larger examines the rightmost digit and counts digits from right to
    left until it encounters a digit larger than the rightmost digit, then returns that count.

    >>> count_until_larger(117) # .Case 1
    -1
    >>> count_until_larger(8117) # .Case 2
    3
    >>> count_until_larger(9118117) # .Case 3
    3
    >>> count_until_larger(8777)  # .Case 4
    3
    >>> count_until_larger(22) # .Case 5
    -1
    >>> count_until_larger(0) # .Case 6
    -1
    """
    "*** YOUR CODE HERE ***"
```

### Q2: Filter Sequence

编写一个函数 `filter_sequence` ，它接收两个整数 `start` 和 `stop` ，以及一个函数 `cond` ， `cond` 接收一个参数并输出一个布尔值。 `filter_sequence` 计算当 `cond` 函数返回 `True` 时，从 `start` 到 `stop` （包括）的所有数字的总和。

```py
def filter_sequence(cond, start, stop):
    """
    Returns the sum of numbers from start (inclusive) to stop (inclusive) that satisfy
    the one-argument function cond.

    >>> filter_sequence(lambda x: x % 2 == 0, 0, 10) # .Case 1
    30
    >>> filter_sequence(lambda x: x % 2 == 1, 0, 10) # .Case 2
    25
    """
    "*** YOUR CODE HERE ***"
```

## 代码编写问题

### Q3: Hailstone

Douglas Hofstadter's 的 Pulitzer-prize-winning 获奖作品《哥德尔、艾舍尔、巴赫》提出了以下数学难题。

1. 选择一个正整数 `n` 作为开始。
2. 如果 `n` 是偶数，就用它除以 2 。
3. 如果 `n` 是奇数，就用它乘以 3 并加上 1 。
4. 继续这个过程直到 `n` 是 1 。

数字 `n` 会向上和向下移动，但最终会在 1 处结束（至少对于所有曾经尝试过的数字而言——没有人证明过这个序列会终止）。类似地，冰雹在大气层中上下游走，最终落在地球上。

这个 `n` 值的序列通常被称为 Hailstone 序列。编写一个函数，接受一个单一参数 `n` ，打印出从 `n` 开始的 Hailstone 序列，并返回该序列的步数：

```py
def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    "*** YOUR CODE HERE ***"
```

Hailstone 序列可以变得相当长！试试 27 。你能找到的最长的序列是什么？

> 注意，如果 `n == 1` ，那么这个序列就是一步长的。

用 Ok 来测试你的代码：

```
python3 ok -q hailstone
```

**对 hailstone 或 hailstone 序列感到好奇？看看这些文章吧：**

- 看看这篇 [文章](https://www.nationalgeographic.org/encyclopedia/hail/) ，了解更多关于 hailstone 的工作原理！
- 2019 年，在理解 hailstone 猜想对大多数数字的作用方面有了重大 [进展](https://www.quantamagazine.org/mathematician-terence-tao-and-the-collatz-conjecture-20191211/) ！

### Q4: Product

高阶函数讲座中的 `summation(n, term)` 函数将 `term(1) + ... + term(n)` 加起来。写一个类似的函数，叫做 `乘积` ，返回 `term(1) * ... * term(n)` 。

```py
def product(n, term):
    """Return the product of the first n terms in a sequence.

    n: a positive integer
    term:  a function that takes one argument to produce the term

    >>> product(3, identity)  # 1 * 2 * 3
    6
    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)    # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    162
    """
    "*** YOUR CODE HERE ***"
```

用 Ok 来测试你的代码：

```
python3 ok -q product
```

### Q5: Accumulate

让我们来看看 `summation` 和 `product` 是如何成为一个叫做 `accumulate` 的更通用的函数的实例，我们想实现这个函数：

```py
def accumulate(merger, start, n, term):
    """Return the result of merging the first n terms in a sequence and start.
    The terms to be merged are term(1), term(2), ..., term(n). merger is a
    two-argument commutative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    >>> # 2 + (1^2 + 1) + (2^2 + 1) + (3^2 + 1)
    >>> accumulate(lambda x, y: x + y + 1, 2, 3, square)
    19
    >>> # ((2 * 1^2 * 2) * 2^2 * 2) * 3^2 * 2
    >>> accumulate(lambda x, y: 2 * x * y, 2, 3, square)
    576
    >>> accumulate(lambda x, y: (x + y) % 17, 19, 20, square)
    16
    """
    "*** YOUR CODE HERE ***"
```

`accumulate` 有以下参数：

- `term` 和 `n`：与 `summation` 和 `product` 中的参数相同
- `merger`：一个双参数函数，用于指定当前项与先前累积项的合并方式
- `start`：开始累加的数值

例如， `accumulate(add, 11, 3, square)` 的结果是

```
11 + square(1) + square(2) + square(3) = 25
```

> **注意**：你可以假设 `merger` 是换元的。也就是说，对于所有的 `a` 、`b` 和 `c` ， `merger(a, b) == merger(b, a)` 。然而，你不能假设 `merger` 是从一个固定的函数集中选择的，并用硬编码解决。

在实现 `accumulate` 之后，说明如何将 `summation` 与 `product` 都定义为对 `accumulate` 的函数调用。

**重要的是**：你应该在每个实现中为 `summation_using_accumulate` 和 `product_using_accumulate` 编写一行代码（应该是一个返回语句），语法检查将对此进行检查。

用 Ok 来测试你的代码：

```
python3 ok -q accumulate
python3 ok -q summation_using_accumulate
python3 ok -q product_using_accumulate
```

## 提交

请确保提交此次作业：

```
python3 ok --submit
```

## 奖励问题

作业中也会包含一些考试级别的问题供你参考。这些问题没有提交的成分；如果你想挑战一下，可以随时尝试一下！

> 请注意，2020 年春季、2020 年秋季和 2021 年春季的考试让学生有机会接触解释器，所以问题的形式可能与其他年份不同。不管怎么说，所包括的问题仍然是很好的考试级问题，不需要使用解释器就可以做。

1. 2019 年秋季 MT1 Q3：[You Again](https://cs61a.org/exam/fa19/mt1/61a-fa19-mt1.pdf#page=4)[高阶函数]
2. 2021 年春季 MT1 Q4：[Domain on the Range](https://cs61a.org/exam/sp21/mt1/61a-sp21-mt1.pdf#page=14)[高阶函数]
3. 2021 年秋季 MT1 Q1b：[tik](https://cs61a.org/exam/fa21/mt1/61a-fa21-mt1.pdf#page=4) [Functions and Expressions][函数和表达式]

</font>