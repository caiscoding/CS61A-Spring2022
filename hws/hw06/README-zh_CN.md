# Homework 6: Scheme, Scheme Lists

## 说明

下载 [hw06.zip](https://inst.eecs.berkeley.edu/~cs61a/sp22/hw/hw06/hw06.zip) 。在压缩包内，你会发现一个名为 [hw06.scm](https://inst.eecs.berkeley.edu/~cs61a/sp22/hw/hw06/hw06.scm) 的文件，以及一份 `ok` 自动评分器的副本。

**提交：** 完成后，用 `python3 ok --submit` 提交。你可以在截止日期前多次提交，但只有最后一次提交才会被打分。检查你是否已经在 [okpy.org](https://okpy.org/) 上成功提交了你的代码。关于提交作业的更多说明，请参见 [Lab 0](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab00#submitting-the-assignment) 。

**使用 Ok：** 如果你有任何关于使用 Ok 的问题，请参考 [本指南](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/using-ok) 。

**阅读资料：** 你可能会发现以下参考资料很有用：

- [Scheme 规范](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/scheme-spec/)
- [Scheme 内置程序参考](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/scheme-builtins/)

**评分：** 家庭作业是根据正确性来评分的。每一个错误的问题将使总分减少一分。如教学大纲中所述，有一个家庭作业政策。 **这个家庭作业满分为 2 分。**

# 必要的问题

## 入门视频

这些视频可以为解决本作业中的编码问题提供一些有用的指导。

> 要看这些视频，你应该登录到你的 berkeley.edu 邮箱。

[YouTube link](https://youtu.be/watch?v=yoGzKE1j3Eg&list=PLx38hZJ5RLZfnXDXftRu5P0mn_crGWaWd)

## 代码编写问题

### Q1: Thane of Cadr

定义程序 `cadr` 和 `caddr` ，它们分别返回列表的第二和第三个元素。如果你想快速复习一下 scheme 语法，可以考虑看一下 [Lab 10 Scheme](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab10/#scheme)。

```py
(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  'YOUR-CODE-HERE
)

(define (caddr s)
  'YOUR-CODE-HERE
)
```

使用 Ok 来解锁和测试你的代码：

```py
python3 ok -q cadr-caddr -u
python3 ok -q cadr-caddr
```

### Q2: Ascending

实现一个名为 `ascending?` 的过程，该过程接收一个数字列表 `lst` ，如果这些数字是按非降序排列的，则返回 `True` ，否则返回 `False` 。如果后面的每个数字都大于或等于前面的数字，则认为是非降序排列的，也就是说：

```py
1 2 3 3 4
```

是非降序排列的，但是：

```py
1 2 3 3 2
```

这个不是非降序排列的。

> *提示：* 内置的 `null?` 函数返回其参数是否为 `nil` 。

```py
(define (ascending? lst)
  'YOUR-CODE-HERE
)
```

使用 Ok 来解锁和测试你的代码：

```py
python3 ok -q ascending -u
python3 ok -q ascending
```

### Q3: Interleave

实现函数 `interleave` ，它以两个列表 `lst1` 和 `lst2` 为参数。 `interleave` 应该返回一个新的列表，该列表将两个列表的元素交错排列。（换句话说，返回的列表应该包含 `lst1` 和 `lst2` 之间交替出现的元素）。

如果要 `interleave` 的输入列表之一比另一个短，那么 `interleave` 应该交替使用两个列表中的元素，直到一个列表中没有更多的元素，然后将较长列表中的剩余元素添加到新列表的末端。

```py
(define (interleave lst1 lst2)
  'YOUR-CODE-HERE
)
```

使用 Ok 来解锁和测试你的代码：

```py
python3 ok -q interleave -u
python3 ok -q interleave
```

### Q4: My Filter

编写一个过程 `my-filter` ，它接收一个谓词 `func` 和一个列表 `lst` ，并返回一个新的列表，其中只包含列表中满足谓词的元素。输出的元素应该与它们在原始列表中出现的顺序相同。

**注意：** 请确保你不是在调用 Scheme 中的内置 `filter` 函数——我们要求你重新实现这个函数！

```py
(define (my-filter func lst)
  'YOUR-CODE-HERE
)
```

使用 Ok 来解锁和测试你的代码：

```py
python3 ok -q filter -u
python3 ok -q filter
```

### Q5: No Repeats

实现 `no-repeats` ，它接收一个数字列表 `lst` 作为输入，并返回一个列表，该列表按照第一次出现的顺序拥有 `lst` 的所有独一无二的元素，且没有重复。例如， `(no-repeats (list 5 4 5 4 2 2))` 结果为 `(5 4 2)` 。

> **提示：** 如何使你在输入列表中第一次看到的元素成为你在返回的结果列表中第一次也是唯一一次看到该元素？

你可能会发现在使用 `my-filter` 过程时，用一个辅助的 `lambda` 函数来作为过滤器是很有帮助的。要测试两个数字是否相等，使用 `=` 过程。要测试两个数字是否相等，请使用 `not` 过程与 `=` 结合使用。

```py
(define (no-repeats lst)
  'YOUR-CODE-HERE
)
```

使用 Ok 来解锁和测试你的代码：

```py
python3 ok -q no_repeats -u
python3 ok -q no_repeats
```