# Homework 5: Trees, Linked Lists

## 说明

下载 [hw05.zip](https://inst.eecs.berkeley.edu/~cs61a/sp22/hw/hw05/hw05.zip) 。在压缩包内，你会发现一个名为 [hw05.py](https://inst.eecs.berkeley.edu/~cs61a/sp22/hw/hw05/hw05.py) 的文件，以及一份 `ok` 的自动评分器的副本。

**提交：** 完成后，用 `python3 ok --submit` 提交。你可以在截止日期前多次提交；只有最后一次提交才会被评分。检查你是否已经在 [okpy.org](https://okpy.org/) 上成功提交了你的代码。关于提交作业的更多说明，请参见 [Lab 0](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab00#submitting-the-assignment) 。

**使用 Ok：** 如果你有任何关于使用 Ok 的问题，请参考 [本指南](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/using-ok) 。

**阅读资料：** 你可能会发现以下参考资料很有用：

- [第 4.2 节](http://composingprograms.com/pages/42-implicit-sequences.html)

**评分：** 家庭作业是根据正确率来评分的。每一个错误的问题将使总分减少一分。如教学大纲中所述，有一个家庭作业政策。 **该家庭作业满分为 2 分。**

# 必要的问题

> **注意：** 本作业应在 3 月 15 日（星期二）完成，而不是 3 月 10 日（星期四）的标准期限。

## 入门视频

这些视频可以为解决本作业中的编码问题提供一些有用的指导。

> 要看这些视频，你应该登录到你的 berkeley.edu 邮箱。

[YouTube link](https://youtu.be/watch?v=WuR5ZPYuyZw&list=PLx38hZJ5RLZc9d722rT5jOAR_S6fWovdN)

## Mid-Semester Feedback

### Q1: Mid-Semester Feedback

作为本周家庭作业的一部分，请填写 [学期中反馈](https://go.cs61a.org/midsem-survey) 表。

这项调查是为了帮助我们对课程进行短期调整，使其更适合你。我们感谢您的反馈。我们可能无法做出你要求的每一项改变，但我们会阅读所有的反馈并加以考虑。

> **保密性：** 对调查的回答是保密的，只有老师（Pamela）和首席助教（Vanshaj）能看到这些数据，而不是匿名的。关于保密性的更多细节可以在调查表上找到。

一旦你完成调查，你会收到一个口令（如果你错过了，它也应该在你收到的确认邮件的底部）。把这个口令，作为一个字符串，放在这个作业的 Python 文件中的 `passphrase = '*** PASSPHRASE HERE ***'` 一行。

用 Ok 来测试你的代码：

```
python3 ok -q midsem_survey
```

## Parsons 问题

### Q2: Chain

对于这个问题，我们将把链定义为从树 `t` 的根到任何叶子结点的路径，而且这路径上的所有结点都有相同的 `label` 。实现函数 `chain` ，给定一棵树 `t` ，如果树中存在任何 `chain` ，则返回 `True` ，否则返回 `False` 。

```py
def chain(t):
    """
    Returns whether there exists a path in t where all nodes
    share the same label.
    >>> all_fives = Tree(5, [Tree(5), Tree(5, [Tree(5)])])
    >>> chain(all_fives)
    True
    >>> t1 = Tree(1, [Tree(3, [Tree(4)]), Tree(1)])
    >>> chain(t1)
    True
    >>> t2 = Tree(1, [Tree(3, [Tree(4)]), Tree(5)])
    >>> chain(t2)
    False
    """
    "*** YOUR CODE HERE ***"
```

### Q3: Flatten Link

编写一个函数 `flatten_link` ，它接收一个链表 `lnk` 并将该序列作为一个 Python 列表返回。如果 `lnk` 有嵌套的链表， `flatten_link` 应该使 `lnk` 平坦。

```py
def flatten_link(lnk):
    """Takes a linked list and returns a flattened Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> flatten_link(link)
    [1, 2, 3, 4]
    >>> flatten_link(Link.empty)
    []
    >>> deep_link = Link(Link(1, Link(2, Link(3, Link(4)))), Link(Link(5), Link(6)))
    >>> flatten_link(deep_link)
    [1, 2, 3, 4, 5, 6]
    """
    "*** YOUR CODE HERE ***"
```

## 代码编写问题

### Q4: Has Path

写一个函数 `has_path` ，它接收树 `t` 和一个字符串 `term` 。如果有一条从根部开始的路径，并且路径上的 `label` 拼出了该 `term` ，则返回 `True` ，否则返回 `False` 。你可以假设每个节点的 `label` 正好是一个字符。

> 这种数据结构被称为 trie ，它有很多很酷的应用，比如自动化。

```py
def has_path(t, term):
    """Return whether there is a path in a Tree where the entries along the path
    spell out a particular term.

    >>> greetings = Tree('h', [Tree('i'),
    ...                        Tree('e', [Tree('l', [Tree('l', [Tree('o')])]),
    ...                                   Tree('y')])])
    >>> print(greetings)
    h
      i
      e
        l
          l
            o
        y
    >>> has_path(greetings, 'h')
    True
    >>> has_path(greetings, 'i')
    False
    >>> has_path(greetings, 'hi')
    True
    >>> has_path(greetings, 'hello')
    True
    >>> has_path(greetings, 'hey')
    True
    >>> has_path(greetings, 'bye')
    False
    >>> has_path(greetings, 'hint')
    False
    """
    assert len(term) > 0, 'no path for empty term.'
    "*** YOUR CODE HERE ***"
```

用 Ok 来测试你的代码：

```
python3 ok -q has_path
```

### Q5: Duplicate Link

编写一个函数 `duplicate_link` ，它接收一个链表 `lnk` 和一个值 `value` 。 `duplicate_link` 将突变 `lnk` ，这样，如果有一个链表节点的第一个值 `first` 等于值 `value` ，该节点将被复制。**注意**，你应该突变原始链表 `lnk` ；你将需要创建新的 `Link` ，但你不应该返回一个新的链表。

> **注意：** 为了在链表中插入一个链表，你需要修改链表的 `.rest` 部分。我们鼓励你画出一个测试样例来进行可视化！

```py
def duplicate_link(lnk, val):
    """Mutates `lnk` such that if there is a linked list
    node that has a first equal to value, that node will
    be duplicated. Note that you should be mutating the
    original link list.

    >>> x = Link(5, Link(4, Link(3)))
    >>> duplicate_link(x, 5)
    >>> x
    Link(5, Link(5, Link(4, Link(3))))
    >>> y = Link(2, Link(4, Link(6, Link(8))))
    >>> duplicate_link(y, 10)
    >>> y
    Link(2, Link(4, Link(6, Link(8))))
    """
    "*** YOUR CODE HERE ***"
```

用 Ok 来测试你的代码：

```
python3 ok -q duplicate_link
```

### Q6: Mutable Mapping

实现 `deep_map_mut(fn, link)` ，它将一个函数 `fn` 应用于给定的链表 `lnk` 中的所有元素。如果一个元素本身是一个链表，将 `fn` 应用于它的每个元素，以此类推。

你的实现应该对原始链表进行改变。不要创建任何新的链表。

> **提示：** 内置的 `isinstance` 函数可能是有用的。
>
> ```py
> >>> s = Link(1, Link(2, Link(3, Link(4))))
> >>> isinstance(s, Link)
> True
> >>> isinstance(s, int)
> False
> ```

> **构造检查：** 本题的最后一个测试确保你不创建新的链表。如果你没有通过这个测试，请确保你没有通过调用构造函数来创建链接列表，即：
>
> ```
> s = Link(1)
> ```

```py
def deep_map_mut(fn, lnk):
    """Mutates a deep link lnk by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor).

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> # Disallow the use of making new Links before calling deep_map_mut
    >>> Link.__init__, hold = lambda *args: print("Do not create any new Links."), Link.__init__
    >>> try:
    ...     deep_map_mut(lambda x: x * x, link1)
    ... finally:
    ...     Link.__init__ = hold
    >>> print(link1)
    <9 <16> 25 36>
    """
    "*** YOUR CODE HERE ***"
```

用 Ok 来测试你的代码：

```
python3 ok -q deep_map_mut
```

## 提交

请确保前提交这份作业：

```
python3 ok --submit
```

# 可选的问题

家庭作业也将包含先前的考试级问题供你参考。这些问题没有提交的成分；如果你想挑战的话，可以随时尝试！

1. Spring 2018 MT2 Q5ab: [Trees](https://cs61a.org/exam/sp18/mt2/61a-sp18-mt2.pdf#page=7)
2. Spring 2019 MT2 Q6a: [Trie this](https://cs61a.org/exam/sp19/mt2/61a-sp19-mt2.pdf#page=7)
3. Fall 2017 Final Q4a: [O! Pascal](https://inst.eecs.berkeley.edu/~cs61a/fa17/assets/pdfs/61a-fa17-final.pdf#page=5)