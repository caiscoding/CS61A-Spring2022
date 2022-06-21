# Homework 4: Python Lists, Object-Oriented Programming

## 说明

下载 [hw04.zip](https://inst.eecs.berkeley.edu/~cs61a/sp22/hw/hw04/hw04.zip) 。在该压缩包中，你会发现一个名为 [hw04.py](https://inst.eecs.berkeley.edu/~cs61a/sp22/hw/hw04/hw04.py) 的文件，以及一份 `ok` 的自动评分器的副本。

**提交：** 完成后，用 `python3 ok --submit` 提交。你可以在截止日期前多次提交，但只有最后一次提交才会被计分。检查你是否已经在 [okpy.org](https://okpy.org/) 上成功提交了你的代码。关于提交作业的更多说明，请参见 [Lab 0](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab00#submitting-the-assignment) 。

**使用 Ok：** 如果你有任何关于使用 Ok 的问题，请参考 [本指南](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/using-ok) 。

**阅读资料：** 你可能会发现以下参考资料很有用：

- [第 2.3 节](http://composingprograms.com/pages/23-sequences.html)
- [第 2.5 节](http://composingprograms.com/pages/25-object-oriented-programming.html)

**评分：** 家庭作业是根据正确性来评分的。每一个错误的问题将使总分减少一分。如教学大纲中所述，有一个家庭作业政策。 **该家庭作业满分为 2 分。**

# 必要的问题

## Parsons 问题

要解决这些问题，请打开 Parsons 编辑器：

```
python3 parsons
```

### Q1: Remove Odd Indices

完成函数 `remove_odd_indices` ，该函数接收一个列表 `lst` 和一个布尔值 `odd` ，并返回一个新的列表，其中的元素在某些索引处被移除。如果 `odd` 为 `True` ，那么该函数应该删除奇数索引的元素；否则如果 `odd` 为 `False` ，那么该函数应该删除偶数索引的项目。

注意，列表是零索引的；因此，第一个元素的索引是 0 ，第二个元素的索引是 1 ，依此类推。

```py
def remove_odd_indices(lst, odd):
    """ 
    Remove elements of lst that have odd indices.
    >>> s = [1, 2, 3, 4]
    >>> t = remove_odd_indices(s, True)
    >>> s
    [1, 2, 3, 4]
    >>> t
    [1, 3]
    >>> l = [5, 6, 7, 8]
    >>> m = remove_odd_indices(l, False)
    >>> m
    [6, 8]
    """
    "*** YOUR CODE HERE ***"
```

### Q2: Smart Fridge

`SmartFridge` 类被智能冰箱用来追踪冰箱中的物品，并让主人知道某个物品何时用完。

该类内部使用一个字典来存储物品，每个键是物品名称，值是当前数量。 `add_item` 方法应该添加给定数量的物品并报告当前数量。你可以假设 `use_item` 方法只对已经在冰箱中的物品进行调用，它应该用完给定数量的物品。如果数量下降到或低于零，它应该只使用到剩余的数量，并提醒主人购买更多的物品。

完成 `SmartFridge` 类定义的实现，使其 `add_item` 和 `use_item` 方法按预期工作。

```py
class SmartFridge:
    """"
    >>> fridgey = SmartFridge()
    >>> fridgey.add_item('Mayo', 1)
    'I now have 1 Mayo'
    >>> fridgey.add_item('Mayo', 2)
    'I now have 3 Mayo'
    >>> fridgey.use_item('Mayo', 2.5)
    'I have 0.5 Mayo left'
    >>> fridgey.use_item('Mayo', 0.5)
    'Uh oh, buy more Mayo!'
    """
    def __init__(self):
        self.items = {}
    def add_item(self, item, quantity):
        "*** YOUR CODE HERE ***"
    def use_item(self, item, quantity):
        "*** YOUR CODE HERE ***"
```

## 代码编写问题

### Q3: Merge

编写一个函数 `merge` ，它接收 2 个 *已排序* 的列表 `lst1` 和 `lst2` ，并返回一个新的列表，该列表包含两个列表中按排序的所有元素。注意：尝试用递归而不是迭代来解决这个问题。

```py
def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q merge
```

### Q4: Mint

造币厂是制造硬币的地方。在这个问题中，你将实现一个 `Mint` 类，该类可以输出具有正确年份和价值的 `Coin` 。

- 每个 `Mint` 都有一个 `year` 。 `update` 方法将 `year` 设置为 `Mint` 类的 `present_year` 属性。
- `create` 方法接受 `Coin` 的一个子类，并返回该类的一个实例，该实例上印有 `mint` 的年份（如果未更新，则可能与 `Mint.present_year` 不同）
- `Coin` 价值方法返回硬币的 `cents` ，超过 50 年的每一年再加 1 美分。硬币的年龄可以通过从 `Mint` 类的 `present_year` 属性中减去硬币的年份来确定。

```py
class Mint:
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.present_year.

    >>> mint = Mint()
    >>> mint.year
    2021
    >>> dime = mint.create(Dime)
    >>> dime.year
    2021
    >>> Mint.present_year = 2101  # Time passes
    >>> nickel = mint.create(Nickel)
    >>> nickel.year     # The mint has not updated its stamp yet
    2021
    >>> nickel.worth()  # 5 cents + (80 - 50 years)
    35
    >>> mint.update()   # The mint's year is updated to 2101
    >>> Mint.present_year = 2176     # More time passes
    >>> mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
    35
    >>> Mint().create(Dime).worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (155 - 50 years)
    115
    >>> Dime.cents = 20  # Upgrade all dimes!
    >>> dime.worth()     # 20 cents + (155 - 50 years)
    125
    """
    present_year = 2021

    def __init__(self):
        self.update()

    def create(self, coin):
        "*** YOUR CODE HERE ***"

    def update(self):
        "*** YOUR CODE HERE ***"

class Coin:
    cents = None # will be provided by subclasses, but not by Coin itself

    def __init__(self, year):
        self.year = year

    def worth(self):
        "*** YOUR CODE HERE ***"

class Nickel(Coin):
    cents = 5

class Dime(Coin):
    cents = 10
```

使用 Ok 来测试你的代码：

```
python3 ok -q Mint
```

### Q5: Vending Machine

在这个问题中，你将创建一个只输出单一产品的 [自动售货机](https://en.wikipedia.org/wiki/Vending_machine) ，并在需要时提供零钱。

创建一个叫做 `VendingMachine` 的类，代表某种产品的自动售货机。一个 `VendingMachine` 对象返回描述其交互的字符串。记住要与测试中的字符串 **完全** 匹配——包括标点符号和间距！

填写 `VendingMachine` 类，适当地添加属性和方法，使其行为与下列测试相符：

```py
class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Nothing left to vend. Please restock.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'You must add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
```

> 你可能会发现 Python 的格式化字符串 [f-strings](https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting) 很有用。这有一个简单的例子：
>
> ```py
> >>> feeling = 'love'
> >>> course = '61A!'
> >>> f'I {feeling} {course}'
> 'I love 61A!'
> ```

使用 Ok 来测试你的代码：

```
python3 ok -q VendingMachine
```

> 如果你对字符串格式化的其他方法感到好奇，你也可以看看 [Python 字符串格式化的方法](https://docs.python.org/2/library/stdtypes.html#str.format) 。这有一个简单的例子：
>
> ```py
> >>> ten, twenty, thirty = 10, 'twenty', [30]
> >>> '{0} plus {1} is {2}'.format(ten, twenty, thirty)
> '10 plus twenty is [30]'
> ```

## 提交

请确保在作业完成后提交：

```
python3 ok --submit
```