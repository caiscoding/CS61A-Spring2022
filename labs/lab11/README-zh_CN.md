# Lab 11: Interpreters

## 起始文件

下载 [lab11.zip](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab11/lab11.zip) 。在该压缩包中，你将找到本实验中问题的起始文件，以及 [Ok](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab11/ok) 自动评分器的副本。

# 说明

在 [Scheme 项目](https://cs61a.org/proj/scheme/) 中，你将为 Scheme 实现一个 Python 解释器。

解释 Scheme 表达式的过程的一部分是能够将一串 Scheme 代码作为我们的输入解析到我们的解释器对 Scheme 表达式的内部 Python 表示中。由于所有的 Scheme 表达式都是 Scheme 列表（因此也是链表），我们使用 `Pair` 类来表示所有的 Scheme 表达式，它的行为就像一个链表。 **这个类在** `pair.py` **中定义。**

当给定一个诸如 `(+ 1 2)` 的输入时，有两个主要步骤是我们要做的。

解释表达式的第一部分是采取输入并将其分解为每个组成部分。在我们的例子中，我们想把 `(` 、 `+` 、 `1` 、 `2` 和 `)` 中的每一个都当作一个单独的标记，然后我们可以找出如何表示。这被称为 **词法分析** ，在 `scheme_tokens.py` 的 `tokenize_lines` 函数中已经为你实现。

现在我们已经把输入的内容分解成了它的组成部分，我们想把这些 Scheme tokens 变成我们的解释器对它们的内部表示。这就是所谓的 **语法分析** ，在 `scheme_reader.py` 的 `scheme_read` 和 `read_tail` 函数中进行。

- `(` 告诉我们正在开始一个调用表达式。
- `+` 是运算符，因为它是调用表达式中的第一个元素。
- `1` 是我们的第一个操作数。
- `2` 是我们的第二个操作数。
- `)` 告诉我们，我们正在结束这个调用表达式。

主要的想法是，在我们进行任何计算或在操作数上调用运算符之前，我们首先要认识到输入代表什么，等等。

这个实验的目标是研究解析的各个部分；虽然在这个实验和这个项目中，我们关注的是 Scheme 语言，但我们如何设置 Scheme 解释器的一般想法也可以适用于其他语言 —— 比如 Python 本身！

# 必要的问题

> 请看 [介绍](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab11/#introduction) ，了解本实验的背景。

## Part 1

### Context

我们在 `Buffer` 实例中存储准备被解析的标记。例如，一个包含输入 `(+ (2 3))` 的缓冲区会有 `'('`、 `'+'`、 `'('`、 `2`、 `3`、 `')'` 和 `')'` 的标记。

在这一部分，我们将实现 `Buffer` 类。

`Buffer` 提供了一种访问跨行标记序列的方法。

它的构造函数需要一个迭代器，称为“`source`”，每次查询都会返回下一行标记的列表，直到它的行数用尽。

例如， `source` 可以被定义如下：

```py
line1 = ['(', '+', 6, 1, ')']      # (+ 6 1)
line2 = ['(', 'quote', 'A', ')']  # (quote A)
line3 = [2, 1, 0]                 # 2 1 0
input_lines = [line1, line2, line3]
source = iter(input_lines)
```

实际上， `Buffer` 结合了从其源头返回的序列，然后通过其 `pop_first` 方法一次提供其中的项目，只有在需要时才调用 `source` 的更多项目序列。

此外， `Buffer` 提供了一个 `current` 实例属性，可以查看下一个要供应的项目，而不需要移过它。

### Problem 1

> **重要提示：** 这部分的代码应该放在 `buffer.py` 中。

你在这部分的工作是实现 `Buffer` 类的 `create_generator` 、 `__init__` 和 `pop_first` 方法。

> **注意：** 对于这个问题，你可能想使用内置的函数 `next` 及其默认参数。这里有一个例子：
>
> ```py
> >>> iterator = iter([1, 2])
> >>> next(iterator) # Here, there is no default arg given.
> 1
> >>> next(iterator, 5) # Here, there is a default arg given, but not used.
> 2
> >>> next(iterator, 5) # The iterator is exhausted, so next returns default.
> 5
> ```
>
> 关于 `next` 的更多信息，请随时阅读 `next` [Python 文档](https://docs.python.org/3/library/functions.html#next)。

#### `create_generator`

实现 `create_generator` ，这是一个生成器函数，它接收 `source` ，是一个行的迭代器，每个行是一个包含标记的列表。

这个函数应该每次从 source 的某一行产生一个标记。如果某行没有更多的标记，那么它应该产生 `EOL_TOKEN` （一个代表行末标记的对象）。

如果整个 source 中没有更多的标记，它就不应该有更多的 yields 。在这种情况下，如果你在这个函数的生成器上调用 `next` ，就会产生一个 `StopIteration` ，因为不再有适用的 yield 了。

你可以在你实现的 `__init__` 和 `pop_first` 中引用这个函数。

> 记住，生成器函数可以如下使用：
> 
> ```py
> >>> gen = some_generator_function()
> >>> next(gen)
> # Returns the first yield from some_generator_function
> >>> next(gen)
> # Returns the next yield from some_generator_function
> ```

#### `__init__`

`__init__` 接收输入源 `source` 。你应该定义以下实例属性：

- 一个实例属性，持有一个由 `create_generator` 基于 `source` 创建的生成器，以及
- `self.current` 代表 `Buffer` 实例所处的生成器的当前标记。在 `__init__` 中，当前 token 应该是生成器产生的第一个 token 。

如果你愿意，你可以定义更多你认为合适的实例属性。

#### `pop_first`

实现 `pop_first` ，其作用如下：

- 保存 `Buffer` 实例的当前 token ，以便以后返回。
- 将 `Buffer` 实例的当前 token 更新为其生成器实例的下一个 token 。
- 如果在初始的当前 token 之后没有更多的 token ，那么就将当前 token 更新为 `None` 。（提示：见本问题开头关于 `next` 的默认参数的说明）。
- 返回初始的当前 token （而不是更新的当前 token ！）。

#### 测试你的代码

使用 Ok 来测试你的代码：

```py
python3 ok -q buffer
```

## Part 2

### Internal Representations

阅读器将把 Scheme 代码解析成 Python 值，其表示方法如下：

<table>
<tr>
<th>
输入示例
</th>
<th>
Scheme 表达式类型
</th>
<th>
我们的内部表述
</th>
</tr>
<tr>
<td>

`scm> 1`

</td>
<td>
Numbers
</td>
<td>

Python 的内置 `int` 和 `float` 值

</td>
</tr>
<tr>
<td>

`scm> x`

</td>
<td>
Symbols
</td>
<td>

Python 的内置 `string` 值

</td>
</tr>
<tr>
<td>

`scm> #t`

</td>
<td>

Booleans (`#t`, `#f`)

</td>
<td>

Python 内置的 `True`、 `False` 值

</td>
</tr>
<tr>
<td>

`scm> (+ 2 3)`

</td>
<td>
Combinations
</td>
<td>

`Pair` 类的实例，定义在 `scheme_reader.py` 中。这个例子被表示为： `Pair('+', Pair(2, Pair(3, nil)))` 。

</td>
</tr>
<tr>
<td>

`scm> nil`

</td>
<td>

`nil`

</td>
<td>

`nil` 对象，定义在 `scheme_reader.py` 中。

</td>
</tr>
</table>

当我们在这里提到组合时，我们指的是调用表达和特殊形式。

### Problem 2

> **重要提示：** 你这部分的代码应该放在 `scheme_reader.py` 中。

> **重要提示：** 在解锁这个问题时，如果从 `Buffer` 实例中产生的 token 是 `EOL_TOKEN` ，它将根据 `EOL_TOKEN` 类的 `__repr__` 函数来显示。具体来说，你会得到：
>
> ```py
> >>> EOL_TOKEN
> This is a token representing the end of a line.
> ```

你在这一部分的工作是编写解析功能，它由两个相互递归的函数组成： `scheme_read` 和 `read_tail` 。每个函数都接收一个 `src` 参数，它是一个 `Buffer` 实例。

- `scheme_read` 从 `src` 中删除足够多的标记以形成一个表达式，并以正确的 [内部表示法](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab11/#internal-representations) 返回该表达式。
- `read_tail` 希望读取 list 或 `Pair` 的其余部分，前提是该 list 或 `Pair` 的开放括号已经被 `scheme_read` 删除。它将读取表达式（并因此移除标记），直到看到匹配的结束括号 `)` 。这个表达式的列表被作为一个 `Pair` 实例的链表返回。

简而言之， `scheme_read` 返回缓冲区中下一个完整的表达式， `read_tail` 返回缓冲区中剩余的列表或 `Pair` 。这两个函数都会改变缓冲区，删除已经处理过的标记。

两个函数的行为都取决于当前在 `src` 中的第一个标记。它们应该按如下方式实现：

`scheme_read`:

- 如果当前 token 是字符串 `"nil"` ，返回 `nil` 对象。
- 如果当前 token 是 `(` ，则表达式是一个对或列表。对 `src` 的其余部分调用 `read_tail` 并返回其结果。
- 如果当前 token 是 `'` ，则缓冲区的其余部分应作为一个引号 `quote` 表达式来处理。你将在下一个问题中实现这一部分。
- 如果下一个 token 不是分隔符，那么它必须是一个原始表达式（即数字、布尔值）。返回它。 **已提供**
- 如果上述情况都不适用，则引发一个错误。 **已提供**

`read_tail`:

- 如果没有更多的 token ，那么这个列表就缺少一个封闭的小括号，我们应该引发一个错误。 **已提供**
- 如果 token 是 `)` ，那么我们已经到达了列表或配对的末端。 **从缓冲区中删除这个 token** ，并返回 `nil` 对象。
- 如果上述情况都不适用，那么下一个 token 就是组合中的运算符。例如， `src` 可能包含 `+ 2 3)` 。要解析这个：
    1. `scheme_read` 缓冲区中的下一个完整表达式。
    2. 调用 `read_tail` 来读取组合的其余部分，直到匹配的结束括号。
    3. 将结果作为一个 `Pair` 实例返回，其中第一个元素是来自 (1) 的下一个完整表达式，第二个元素是来自 (2) 的其余组合。

使用 Ok 来解锁和测试你的代码：

```py
python3 ok -q scheme_read -u
python3 ok -q scheme_read
```

### Problem 3

> **重要提示：** 这一部分的代码应该放在 `scheme_reader.py` 中。

在这个问题上，你的任务是完成 `scheme_read` 的实现，让这个函数现在能够处理带引号的表达式。

在 Scheme 中，像 `'<expr>` 这样的带引号的表达式等同于 `(quote <expr>)` 。这意味着我们需要将 `'` 后面的表达式（你可以通过递归调用 `scheme_read` 得到）包装成 `quote` 的特殊形式，它是一个 Scheme 列表（和所有的特殊形式一样）。

在我们的表述中，一个 `Pair` 代表一个 Scheme 列表。因此，你应该把 `'` 后面的表达式包在 `Pair` 中。

例如， `'bagel` ，或者说 `["'", "bagel"]` 在被标记后，应该表示为 `Pair('quote', Pair('bagel', nil))` 。 `'(1 2)` 或 `["'", "(", 1, 2, ")"]` 应该表示为 `Pair('quote', Pair(Pair(1, Pair(2, nil)), nil))` 。

使用 Ok 来解锁和测试你的代码：

```py
python3 ok -q quote -u
python3 ok -q quote
```

## 运行你的解析器

现在你的解析器已经完成了，你可以通过运行 读取-计算-打印 循环来测试：

```py
python3 scheme_reader.py --repl
```

每次你在提示符中输入一个值，解析后的表达式的 `str` 和 `repr` 值都会被打印出来。你可以尝试以下输入方式：

```py
read> 42
str : 42
repr: 42
read> nil
str : ()
repr: nil
read> (1 (2 3) (4 (5)))
str : (1 (2 3) (4 (5)))
repr: Pair(1, Pair(Pair(2, Pair(3, nil)), Pair(Pair(4, Pair(Pair(5, nil), nil)), nil)))
```

要退出解释器，你可以输入 `exit` 。

## 提交

请确保提交这项作业：

```py
python3 ok --submit
```