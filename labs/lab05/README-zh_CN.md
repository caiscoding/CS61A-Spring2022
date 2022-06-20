# Lab 5: Python Lists, Mutability

## 起始文件

下载 [lab05.zip](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab05/lab05.zip) 。在该压缩包中，你将找到本实验中问题的起始文件，以及 [Ok](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab05/ok) 自动评分器的副本。

# 主题

如果你需要复习本实验的材料，请查阅 [本节](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab05/#required-questions) 。你可以直接跳到问题上，如果卡住了，可以回到这里。

## 列表

列表是一个可以存储多个元素的数据结构。每个元素可以是任何类型，甚至是一个列表本身。我们把列表写成方括号内的逗号分隔的表达式列表：

```py
>>> list_of_ints = [1, 2, 3, 4]
>>> list_of_bools = [True, True, False, False]
>>> nested_lists = [1, [2, 3], [4, [5]]]
```

列表中的每个元素都有一个索引，第一个元素的索引从 `0` 开始。因此我们说，列表是“零索引”。

通过列表索引，我们可以指定我们想要检索的元素的索引。负的索引代表从列表的末尾开始，所以负的索引 `-i` 等于正的索引 `len(lst)-i` 。

```py
>>> lst = [6, 5, 4, 3, 2, 1, 0]
>>> lst[0]
6
>>> lst[3]
3
>>> lst[-1] # Same as lst[6]
0
```

为了创建一个列表的部分或全部的副本，我们可以使用列表切片。切分一个列表 `lst` 的语法是： `lst[<start index>:<end index>:<step size>]` 。

这个表达式被评估为一个包含 `lst` 元素的新列表：

- 从 `<start index>` 处开始并包括该元素。
- 直到但不包括 `<end index>` 处的元素。
- 用 `<step size>` 作为要包括的元素的索引之差。

如果没有明确指定开始、结束或步长， Python 对它们有默认值。负的步长表示在包含元素时，我们在列表中向后退步。

```py
>>> lst[:3]   # Start index defaults to 0
[6, 5, 4]
>>> lst[3:]   # End index defaults to len(lst)
[3, 2, 1, 0]
>>> lst[::-1]   # Make a reversed copy of the entire list
[0, 1, 2, 3, 4, 5, 6]
>>> lst[::2]  # Skip every other; step size defaults to 1 otherwise
[6, 4, 2, 0]
```

## 列表语法

列表语法是一种从序列中创建新列表的紧凑而强大的方法。列表的一般语法如下：

```py
[<expression> for <element> in <sequence> if <conditional>]
```

其中 `if <conditional>` 部分是可选的。

语法被设计成像英语一样的语法。“计算序列中每个元素的表达式（如果条件对该元素为真）。”

```py
>>> [i**2 for i in [1, 2, 3, 4] if i % 2 == 0]
[4, 16]
```

这个列表的语法将：

- 计算表达式 `i**2`
- 对于序列 `[1, 2, 3, 4]` 中的每个元素 `i`
- 其中 `i % 2 == 0` （ `i` 是一个偶数）

然后将表达式的结果值放入一个新的列表。

换句话说，这个列表语法将创建一个新的列表，其中包含原始列表 `[1, 2, 3, 4]` 中每个偶数元素的平方。

我们也可以把列表语法改写成一个等价的 `for` 语句，比如上面的例子：

```py
>>> lst = []
>>> for i in [1, 2, 3, 4]:
...     if i % 2 == 0:
...         lst = lst + [i**2]
>>> lst
[4, 16]
```

## 可变性

如果一个对象的状态可以随着代码的执行而改变，我们就说它是 **可变的** 。改变一个对象的状态的过程被称为 **突变** 。可变对象的例子包括列表和字典。不可变的对象的例子包括图元和函数。

# 必要的问题

## What Would Python Do?

### Q1: WWPD: List-Mutation

> 用 Ok 来测试你对知识的理解，有以下“Python会显示什么？”问题：
>
> ```
> python3 ok -q list-mutation -u
> ```
>
> **重要提示：** 对于所有的 WWPD 问题，如果你认为答案是 `<function...>` ，则输入 `Function` ，如果出错则输入 `Error` ，如果没有显示则输入 `Nothing` 。

```py
>>> lst = [5, 6, 7, 8]
>>> lst.append(6)
______

>>> lst
______

>>> lst.insert(0, 9)
>>> lst
______

>>> x = lst.pop(2)
>>> lst
______

>>> lst.remove(x)
>>> lst
______

>>> a, b = lst, lst[:]
>>> a is lst
______

>>> b == lst
______

>>> b is lst
______

>>> lst = [1, 2, 3]
>>> lst.extend([4,5])
>>> lst
______

>>> lst.extend([lst.append(9), lst.append(10)])
>>> lst
______
```

## Parsons 问题

要解决这些问题，请打开 Parsons 编辑器：

```
python3 parsons
```

### Q2: Replace Elements

完成函数 `replace_elements` ，这个函数接收 `source_list` 和 `dest_list` ，并将 `dest_list` 中的元素改成 `source_list` 中相应索引的元素。

`dest_list` 的长度总是大于或等于 `source_list` 的长度。

```py
def replace_elements(source_list, dest_list):
    """
    Complete the function replace_elements, a function which takes in source_list
    and dest_list and mutates the elements of dest_list to be the elements at the
    corresponding index in source_list.

    dest_list always has a length greater than or equal to the length of
    source_list.

    >>> s1 = [1, 2, 3]
    >>> s2 = [5, 4]
    >>> replace_elements(s2, s1)
    >>> s1
    [5, 4, 3]
    >>> s3 = [0, 0, 0, 0, 0]
    >>> replace_elements(s1, s3)
    >>> s3
    [5, 4, 3, 0, 0]
    """
    "*** YOUR CODE HERE ***"
```

## 代码编写问题

### Q3: Flatten

编写一个函数 `flatten` ，接收一个列表并将其“扁平化”。这个列表可以是一个深层列表，也就是说，在这个列表中可以有多层嵌套。

例如， `flatten` 的一个用例可以是这样的：

```py
>>> lst = [1, [[2], 3], 4, [5, 6]]
>>> flatten(lst)
[1, 2, 3, 4, 5, 6]
```

确保你的解决方案不会改变输入的列表。

> **提示：** 你可以通过使用内置的 `type` 函数来检查某物是否是一个列表。比如说：
>
> ```py
> >>> type(3) == list
> False
> >>> type([1, 2, 3]) == list
> True
> ```

```py
def flatten(s):
    """Returns a flattened version of list s.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]     # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x # Ensure x is not mutated
    [1, [2, 3], 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    >>> x
    [[1, [1, 1]], 1, [1, 1]]
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q flatten
```

### Q4: Couple

实现函数 `couple` ，它接收两个列表并返回一个包含有两个序列的第 i 个元素的列表，并将其耦合在一起。你可以假设两个序列的长度是一样的。尝试使用列表语法。

> *提示：* 你可能会发现内置的 [range](https://www.w3schools.com/python/ref_func_range.asp) 函数很有帮助。

```py
def couple(s, t):
    """Return a list of two-element lists in which the i-th element is [s[i], t[i]].

    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> couple(a, b)
    [[1, 4], [2, 5], [3, 6]]
    >>> c = ['c', 6]
    >>> d = ['s', '1']
    >>> couple(c, d)
    [['c', 's'], [6, '1']]
    """
    assert len(s) == len(t)
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q couple
```

### Q5: Insert Items

写一个函数，它接收一个列表 `lst` ，一个参数 `entry` 和另一个参数 `elem` 。这个函数将检查 `lst` 中的每一项，看它是否与 `entry` 相同。一旦发现一个项等于 `entry` ，该函数应修改列表，将 `elem` 放在该项之后。在函数的最后，应该返回修改后的列表。

请看 doctests 中关于如何使用这个函数的例子。

**重要提示：** 修改原始列表。不应该创建或返回新的列表。

> **注意：** 如果传入 `entry` 和 `elem` 的值是相等的，确保你在迭代时没有创建一个无限长的列表。如果你发现你的代码运行时间超过了几秒钟，函数可能处于插入新值的循环中。

```py
def insert_items(lst, entry, elem):
    """Inserts elem into lst after each occurence of entry and then returns lst.

    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> double_lst = [1, 2, 1, 2, 3, 3]
    >>> double_lst = insert_items(double_lst, 3, 4)
    >>> double_lst
    [1, 2, 1, 2, 3, 4, 3, 4]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    >>> # Ban creating new lists
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'insert_items',
    ...       ['List', 'ListComp', 'Slice'])
    True
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q insert_items
```

## 提交

请确保提交这份作业：

```
python3 ok --submit
```