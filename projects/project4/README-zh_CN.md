# Project 4: Scheme Interpreter

![](./images/money_tree.png)

*Eval 调用 apply，*

*这只是再次调用 eval！*

*这一切何时结束？*

## 说明

> **注意：** 如果你对这个项目的另一个版本感兴趣，它给你提供的支架和指导要少得多，你可以试试 [Scheme 挑战版](https://inst.eecs.berkeley.edu/~cs61a/sp22/proj/scheme_stubbed/) ！为了评分的目的，完成本项目的任何一个版本（本版本或挑战版）都是等效的。

> **重要的提交说明：** 为了获得全部分数，
>
> - 在 **4 月 12 日（星期二）** 之前提交完成的第一部分（分值 1 分）。
> - 在 **4 月 19 日（星期二）** 之前完成第二和第三部分（包括通过 `tests.scm` 中提供的所有测试）（分值 1 分）。
> - 在 **4 月 26 日（星期二）** 之前完成所有阶段的提交。
>
> 尽量按顺序尝试这些问题，因为后面的一些问题在实现时将取决于前面的问题，因此在运行 `ok` 测试时也是如此。
>
> 整个项目可以和一个伙伴一起完成。
>
> 在 **4 月 25 日星期一** 之前提交整个项目，你可以得到 1 分奖励。

在这个项目中，你将为 Scheme 语言的一个子集开发一个解释器。在你进行的过程中，要思考在设计编程语言时出现的问题；语言的许多怪癖是解释器和编译器中实现决定的副产品。本项目中使用的语言子集在 Composing Programs 的 [函数式编程](http://composingprograms.com/pages/32-functional-programming.html) 部分有描述，以及本项目中你要构建的 CS 61A Scheme 子集的 [语言规范](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/scheme-spec/) 和 [内置程序参考](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/scheme-builtins/) 。

观看（或参加）关于计算器和解释器的讲座，了解项目的概况。

此外，还有一个完全可选的开放式艺术竞赛（单独发布），挑战你只用几行 Scheme 来制作递归图像。举个例子，上面的图片抽象地描绘了用美国货币为 0.5 美元找零的所有方法。所有的花都出现在一个长度为 50 的树枝的末端。树枝上的小角表示一个额外的硬币，而大角表示一个新的货币面值。在比赛中，你也将有机会成为你内心的递归艺术家。

## 下载起始文件

你可以下载所有的项目代码 [压缩文件](https://inst.eecs.berkeley.edu/~cs61a/sp22/proj/scheme/scheme.zip) 。

你将编辑的文件：

- `scheme_eval_apply.py`：Scheme 表达式的递归计算器
- `scheme_forms.py`：特殊形式的计算
- `scheme_classes.py`：描述 Scheme 表达式的类
- `questions.scm`：包含第三部分的骨架代码

该项目中的其他文件：

- `scheme.py`：解释器的 REPL
- `pair.py`：定义了 `Pair` 类和 `nil` 对象
- `scheme_builtins.py`：内置的 Scheme 程序
- `scheme_reader.py`：Scheme 输入的阅读器（这个文件被混淆了，所以你可以在实验中实现它）
- `scheme_tokens.py`：Scheme 输入的标记器
- `scheme_utils.py`：用于检查 Scheme 表达式的函数
- `ucb.py`：61A 项目中使用的实用函数
- `tests.scm`：用 Scheme 编写的测试案例集
- `ok`：自动评分器
- `tests`：`ok` 使用的测试目录
- `mytests.rst`：一个可以添加你自己的测试的文件

## 组织

该项目是有分值的。28 分是正确性，其中包括通过 `tests.scm` 的 1 分。 1 分是在第一个检查点日期前提交第一部分， 1 分是在第二个检查点日期前提交第二和第三部分。

此外，还有一些加分的机会。在 **4 月 25 日（星期一）** 之前提交整个项目可以得到 1 个额外分数，提交额外分数问题可以得到 2 个额外分数。

> **重要提示：** 为了获得所有可能的 Scheme 加分，你对整个项目的实施， *包括* EC 问题，必须在提交的截止日期前提交。

你将交出以下文件：

- `scheme_eval_apply.py`
- `scheme_forms.py`
- `scheme_classes.py`
- `questions.scm`

你不需要修改或上交任何其他文件来完成这个项目。要提交该项目，请运行以下命令：

```py
python3 ok --submit
```

你将能够在 [Ok 仪表板](http://ok.cs61a.org/) 上查看你的提交。

对于我们要求你完成的功能，可能有一些我们提供的初始代码。如果你不愿意使用这些代码，可以随时删除它，然后从头开始。你也可以在你认为合适的时候添加新的功能定义。

**但是，请不要修改任何其他函数或编辑任何未列出的文件。** 这样做可能会导致你的代码无法通过我们的自动评分系统测试。此外，请不要改变任何函数的签名（名称、参数顺序或参数数量）。

在整个项目中，你应该测试你的代码的正确性。经常测试是很好的做法，这样就可以很容易地分离出任何问题。然而，你不应该测试得太频繁，以使自己有时间思考问题。

我们提供了一个名为 `ok` 的 **自动评分器** ，以帮助你测试你的代码并跟踪你的进度。在你第一次运行自动评分系统时，你会被要求 **用你的网络浏览器登录你的 Ok 账户** 。请这样做。每次你运行 `ok` 时，它都会在我们的服务器上备份你的工作和进度。

`ok` 的主要目的是为了测试你的实现。

我们建议您在 **完成每个问题后** 提交。只有你的最后一次提交才会被打分。在你遇到提交问题时，多备份你的代码对我们来说也很有用。 **如果你忘记提交，你的最后一份备份将自动转换为提交。**

如果你不希望我们记录你的工作备份或你的进度信息，你可以运行

```py
python3 ok --local
```

有了这个选项，任何信息都不会被发送到我们的课程服务器。如果你想以交互方式测试你的代码，你可以运行

```py
python3 ok -q [question number] -i
```

并插入相应的问题编号（例如 `01` ）。这将运行该问题的测试，直到第一个测试失败为止，然后给你一个机会来交互测试你写的函数。

你也可以使用 OK 中的调试打印功能，写上

```py
print("DEBUG:", x)
```

这将在你的终端产生一个输出，而不会出现额外输出导致 OK 测试失败。

## 解释器的细节

### Scheme 特征

**读取-计算-打印。** 解释器读取 Scheme 表达式，对其进行计算，并显示结果。

```py
scm> 2
2
scm> (+ 2 3)
5
scm> ((lambda (x) (* x x)) 5)
25
```

你的 Scheme 解释器的启动代码可以成功地计算上述第一个表达式，因为它由一个数字组成。第二个（调用一个内置程序）和第三个（计算 5 的平方）还不能工作。

**加载。** 你可以通过传入一个文件名的符号来加载一个文件。例如，要加载 `tests.scm` ，请计算以下调用表达式。

```py
scm> (load 'tests)
```

**符号。** 不同的 Scheme 方言对标识符（作为符号和变量名）都有或多或少的允许性。

我们的规则是：

> 一个标识符是一连串的字母（a-z 和 A-Z）、数字和 `!$%&*/:<=>?@^_~-+.` 中的字符，它们不构成有效的整数或浮点数，也不是现有的特殊形式速记。

我们的 Scheme 版本是不区分大小写的：如果两个标识符只在字母的大小写上有所不同，则被认为是相同的。它们在内部是以小写字母表示和打印的：

```py
scm> 'Hello
hello
```

**龟类图形。** 除了标准的 Scheap 程序外，我们还包括对 Python `turtle` 包的程序调用。这在比赛中会很方便。你 **不需要** 为了参赛而安装这个包。

如果你很好奇，你可以在网上阅读 [turtle 模块的文档](http://docs.python.org/py3k/library/turtle.html) 。

### 运行解释器

要启动一个交互式 Scheme 解释器会话，请键入：

```py
python3 scheme.py
```

目前，你的 Scheme 解释器可以处理一些简单的表达式，如：

```py
scm> 1
1
scm> 42
42
scm> true
#t
```

要退出 Scheme 解释器，请按 `Ctrl-d` 或执行 `exit` 程序（完成问题 3 和 4 后）：

```py
scm> (exit)
```

你可以使用你的 Scheme 解释器来计算输入文件中的表达式，方法是将文件名作为一个命令行参数传递给 `scheme.py`：

```py
python3 scheme.py tests.scm
```

`tests.scm` 文件包含了一长串 Scheme 表达式的例子和它们的预期值。其中许多例子来自 [《计算机程序的结构与解释》](https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-4.html#%_toc_start) 的第 1 章和第 2 章，《Composing Programs》就是根据这本教科书改编的。

## Part 1: The Evaluator

在第一部分中，你将开发解释器的以下功能：

- 符号计算
- 调用内置程序
- 定义

在给你的启动器实现中，计算器只能计算自计算的表达式：数字、布尔和 `nil` 。

首先，阅读相关代码。在 `scheme_eval_apply.py` 的“Eval/Apply”部分：

- `scheme_eval` 在给定的环境中计算一个 Scheme 表达式。这个函数几乎是完整的，但缺少调用表达式的逻辑。
- 当计算一个特殊的形式时， `scheme_eval` 将计算重定向到 `scheme_forms.py` 中找到的适当的 `do_?_form` 函数
- `scheme_apply`  将一个过程应用于一些参数。这个函数为你将要实现的各种类型的过程（内置过程、用户定义的过程等等）提供了案例

在 `scheme_classes.py` 的 “环境” 和 “过程” 部分：

- `Frame` 类实现了一个环境框架。
- `LambdaProcedure` 类（在“程序”部分）表示用户定义的程序。

这些都是解释器的基本组成部分。 `scheme_forms.py` 定义了特殊形式， `scheme_builtins.py` 定义了标准库中内置的各种函数， `scheme.py` 定义了输入/输出行为。

使用 Ok 来测试你的理解：

```py
python3 ok -q eval_apply -u
```

### Problem 1 (1 pt)

实现 `scheme_classes.py` 中 `Frame` 类的 `define` 和 `lookup` 方法。每个 `Frame` 对象都有以下的实例属性：

- `bindings` 是一个代表框架中的绑定的字典。它将 Scheme 符号（用 Python 字符串表示）映射到 Scheme 值。
- `parent` 是父 `Frame` 实例。全局框架的父级是 `None` 。

1. `define` 接收一个符号（用 Python 字符串表示）和一个值。它将符号与 `Frame` 实例中的值绑定。
2. `lookup` 接收一个符号，并返回与该符号绑定的 *环境* 中的第一个框架中的值。一个 `Frame` 实例的环境由该框架、其父框架和所有其祖先框架组成，包括全局框架。这将在下面解释：
    - 如果符号在当前框架中被绑定，返回其值。
    - 如果符号在当前框架中没有被绑定，并且该框架有一个父框架，继续在父框架中查找。
    - 如果在当前框架中没有找到该符号，并且没有父框架，则引发SchemeError 。

使用 Ok 来解锁和测试你的代码：

```py
python3 ok -q 01 -u
python3 ok -q 01
```

完成这个问题后，你可以启动 Scheme 解释器（用 `python3 scheme.py` ）。你应该能够查询到内置程序的名称：

```py
scm> +
#[+]
scm> odd?
#[odd?]
```

然而，你的 Scheme 解释器仍然无法调用这些程序。让我们来解决这个问题。

记住，这时你只能按 `Ctrl-d` 来退出解释器。

### Problem 2 (2 pt)

为了能够调用内置过程，例如 `+` ，你需要在 `scheme_eval_apply.py` 中的 `scheme_apply` 函数中完成 `BuiltinProcedure` 案例。内置过程是通过调用实现该过程的相应 Python 函数来应用的。

> 要查看项目中使用的所有 Scheme 内置过程的列表，请在 `scheme_builtins.py` 文件中查看。任何用 `@builtin` 装饰的函数将被添加到全局定义的 `BUILTINS` 列表中。

一个 `BuiltinProcedure` 有两个实例属性：

- `py_func`：实现内置 Scheme 过程的 Python 函数。
- `expect_env`：一个布尔标志，表示这个内置存储过程是否期望将当前环境作为最后一个参数传入。例如，在实现内置的 `eval` 过程时需要环境。

`scheme_apply` 接收 `procedure` 对象、一个参数值列表和当前环境。 `args` 是一个 Scheme 列表，用 `Pair` 对象或 `nil` 表示。你的应该做以下工作：

- 将 Scheme 列表转换成 Python 的参数列表。 *提示：* `args` 是一个 Pair ，它有一个 `.first` 和 `.rest` ，类似于一个 Linked List 。想一想，你将如何把 Linked List 的值放入一个列表中。
- 如果 `procedure.expect_env` 为 `True` ，那么将当前环境 `env` 作为最后一个参数添加到这个 Python 列表中。
- 使用 `*args` 符号对所有这些参数调用 `procedure.py_func` （ `f(1, 2, 3)` 相当于 `f(*[1, 2, 3])` ）。
- 如果调用该函数的结果是出现 `TypeError` 异常，那么就说明传递的参数数量不对。使用 `try`/`except` 块来拦截该异常，并引发一个 `SchemeError` ，信息为 `'incorrect number of arguments'` 。
- 否则， `scheme_apply` 应该返回通过调用 `procedure.py_func` 得到的值。

使用 Ok 来解锁和测试你的代码：

```py
python3 ok -q 02 -u
python3 ok -q 02
```

👩🏽‍💻👨🏿‍💻 [配对编程？](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/pair-programming) 记住要交替扮演司机和导航员的角色。驾驶员控制键盘；导航员观察，提出问题，并提出想法。

### Problem 3 (2 pt)

`scheme_eval` 函数（在 `scheme_eval_apply.py` 中）在给定的环境中计算一个 Scheme 表达式（用 `Pair` 表示）。所提供的代码已经在当前环境中查找名字，返回自计算表达式（如数字），并计算特殊形式。

实现 `scheme_eval` 中缺少的部分，即计算一个调用表达式。要计算一个调用表达式：

1. 计算操作符（它应该计算为 `Procedure` 的一个实例）
2. 计算所有的操作数
3. 通过调用 `scheme_apply` 将存储过程应用于已计算的操作数，然后返回结果

在前两个步骤中，你必须递归地调用 `scheme_eval` 。下面是一些你应该使用的其他函数/方法：

- `Pair` 的 `map` 方法返回一个新的 Scheme 列表，该列表是通过对 Scheme 列表中的每一个项目应用一个单参数函数而构建的。
- `scheme_apply` 函数将一个 Scheme 过程应用于以 Scheme 列表（一个 `Pair` 实例）表示的参数。

重要的是：不要改变传入的 `expr` 。那会在程序被计算时改变它，产生奇怪和不正确的效果。

使用 Ok 来解锁和测试你的代码：

```py
python3 ok -q 03 -u
python3 ok -q 03
```

> 其中一些测试调用了一个叫做 `print-then-return` 的原始（内置）过程。这个存储过程在 Scheme 中并不存在，只是为了测试这个问题而被添加到这个项目中。 `print-then-return` 需要两个参数。它打印出第一个参数并返回第二个参数。你可以在 `scheme_builtins.py` 的底部找到这个函数。

你的解释器现在应该能够计算内置过程调用，给你提供计算器语言的功能更多。运行 `python3 scheme.py` ，你现在可以进行加法和乘法运算了！

```py
scm> (+ 1 2)
3
scm> (* 3 4 (- 5 2) 1)
36
scm> (odd? 31)
#t
```

### Problem 4 (2 pt)

Scheme 中的 `define` 特殊形式（ [spec](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/scheme-spec/#define) ）既可以用来为给定表达式的值分配一个名称，也可以用来创建一个过程并将其与一个名称绑定：

```py
scm> (define a (+ 2 3))  ; Binds the name a to the value of (+ 2 3)
a
scm> (define (foo x) x)  ; Creates a procedure and binds it to the name foo
foo
```

第一个操作数的类型告诉我们什么是被定义的：

- 如果它是一个符号，例如 `a` ，那么这个表达式就定义了一个名字。
- 如果它是一个列表，例如 `(foo x)` ，那么这个表达式就是在定义一个存储过程。

`scheme_forms.py` 中的 `do_define_form` 函数计算了 `(define ...)` 表达式。这个函数中缺少两个部分。对于这个问题， **只需实现第一部分** ，即对第二个操作数进行求值以获得一个值，并将第一个操作数，即一个符号，与该值绑定。然后， `do_define_form` 返回被绑定的符号。

使用 Ok 来解锁和测试你的代码：

```py
python3 ok -q 04 -u
python3 ok -q 04
```

你现在应该能够给值起名字，并计算产生的符号。例如，这里是本题的 `ok` 测试的一些测试案例。

```py
scm> (define x 15)
x
scm> (define y (* 2 x))
y
scm> y
30
scm> (+ y (* y 2) 1)
91
scm> (define x 20)
x
scm> x
20
```

对于这个测试，目标是强调在引发错误之前，运算符是否被多次计算。预期的，也是有意的行为是，在引发错误之前，运算符只被计算了一次。

```py
(define x 0)
; expect x
((define x (+ x 1)) 2)
; expect Error
x
; expect 1
```

我们希望在这里引发一个错误，因为操作符没有计算到一个过程。然而，如果运算符在引发错误之前被多次计算， x 将被绑定到 2 而不是 1 ，导致测试失败。因此，如果你的解释器不能通过这个测试，你要确保在 `scheme_eval` 中只计算一次运算符。

### Problem 5 (1 pt)

在 Scheme 中，你可以用两种方式来引用表达式：用 `quote` 特殊形式（ [spec](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/scheme-spec/#quote) ）或用符号 ' 。读取器将 `'...` 转换为 `(quote ...)` ，因此你的解释器只需要评估 `(quote ...)` 的语法。 `quote` 特殊形式返回其操作数表达式，而不对其进行评估：

```py
scm> (quote hello)
hello
scm> '(cons 1 2)  ; Equivalent to (quote (cons 1 2))
(cons 1 2)
```

实现 `scheme_forms.py` 中的 `do_quote_form` 函数，使其简单地返回 `(quote ...)` 表达式的未评估的操作数。

使用 Ok 来解锁和测试你的代码：

```py
python3 ok -q 05 -u
python3 ok -q 05
```

在完成这个函数后，你应该能够评估引号表达式。在你的解释器中试试下面的一些方法吧！

```py
scm> (quote a)
a
scm> (quote (1 2))
(1 2)
scm> (quote (1 (2 three (4 5))))
(1 (2 three (4 5)))
scm> (car (quote (a b)))
a
scm> 'hello
hello
scm> '(1 2)
(1 2)
scm> '(1 (2 three (4 5)))
(1 (2 three (4 5)))
scm> (car '(a b))
a
scm> (eval (cons 'car '('(1 2))))
1
scm> (eval (define tau 6.28))
6.28
scm> (eval 'tau)
6.28
scm> tau
6.28
```

> 一旦你完成了问题 5 ，请确保你使用 OK 提交，以获得第一个检查点的全部分数。
>
> ```py
> python3 ok --submit
> ```
>
> 如果你想检查你到目前为止的得分，请使用以下命令：
>
> ```py
> python3 ok --score
> ```

## Part 2: Procedures

在第 2 部分中，你将增加创建和调用用户定义的程序的能力。你将在解释器中添加以下功能：

- Lambda 程序，使用 `(lambda ...)` 的特殊形式
- 使用 `(define (...) ...)` 特殊形式的命名 lambda 程序
- Mu 程序，具有 *动态范围*

### 用户定义的程序

用户定义的 lambda 程序被表示为 `LambdaProcedure` 类的实例。一个 `LambdaProcedure` 实例有三个实例属性：

- `formals` 是一个形式参数（符号）的 Scheme 列表，它命名了程序的参数。
- `body` 是一个表达式的 Scheme 列表；程序的主体。
- `env` 是 **定义** 该过程的环境。

### Problem 6 (1 pt)

改变 `scheme_eval_apply.py` 中的 `eval_all` 函数（该函数由 `scheme_forms.py` 中的 `do_begin_form` 调用）以完成 `begin` 特殊形式（ [spec](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/scheme-spec/#begin) ）的实现。

一个 `begin` 表达式是通过依次评估所有子表达式来进行评估的。 `begin` 表达式的值是最后一个子表达式的值。

为了完成 `begin` 的实现， `eval_all` 将接收 `expressions` （表达式的 Scheme 列表）和 `env` （代表当前环境的 `Frame` ），评估 `expressions` 中的所有表达式，并返回表达式中最后一个 `expressions` 的值。

```py
scm> (begin (+ 2 3) (+ 5 6))
11
scm> (define x (begin (display 3) (newline) (+ 2 3)))
3
x
scm> (+ x 3)
8
scm> (begin (print 3) '(+ 2 3))
3
(+ 2 3)
```

如果 `eval_all` 被传递给一个空的表达式列表（ `nil` ），那么它应该返回 Python 值 `None` ，它代表了 Scheme 值 `undefined` 。

使用 Ok 来解锁和测试你的代码：

```py
python3 ok -q 06 -u
python3 ok -q 06
```

👩🏽‍💻👨🏿‍💻 [结对编程？](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/pair-programming) 这将是一个转换角色的好时机。交换角色可以确保你们都能从每个角色的学习经历中受益。

### Problem 7 (2 pt)

在 `scheme_forms.py` 中实现 `do_lambda_form` 函数（ [spec](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/scheme-spec/#lambda) ），它创建并返回一个 `LambdaProcedure` 实例。虽然你还不能调用用户定义的存储过程，但你可以通过在解释器提示符中输入 lambda 表达式来验证你是否正确地创建了存储过程：

```py
scm> (lambda (x y) (+ x y))
(lambda (x y) (+ x y))
```

在 Scheme 中，在过程的主体中放置一个以上的表达式是合法的。（因此 `LambdaProcedure` 实例的 `body` 属性是一个主体表达式的 Scheme 列表。 `LambdaProcedure` 实例的 `formals` 属性应该是一个正确嵌套的 `Pair` 表达式。像 `begin` 特殊形式一样，评估过程的主体会按顺序评估所有主体表达式。过程的返回值是其最后一个主体表达式的值。

使用 Ok 来解锁和测试你的代码：

```py
python3 ok -q 07 -u
python3 ok -q 07
```

### Problem 8 (2 pt)

实现 `Frame` 类的 `make_child_frame` 方法（在 `scheme_classes.py` 中），当调用用户定义的过程时，它将被用来创建新的框架。这个方法接收两个参数： `formals` ，这是一个符号的 Scheme 列表，和 `vals` ，这是一个值的 Scheme 列表。它应该返回一个新的子框架，将形式参数与值绑定。

要做到这一点：

- 如果参数值的数量与形式参数的数量不匹配，则引发 `SchemeError` 。
- 创建一个新的 `Frame` 实例，它的父级是 `self` 。
- 在新创建的框架中，将每个形式参数绑定到其相应的参数值。 `formals` 中的第一个符号应该被绑定到 `vals` 中的第一个值，以此类推。
- 返回新的框架。

> *提示：* 一个 `Frame` 实例的 `define` 方法在该框架中创建一个绑定。

使用 Ok 来解锁和测试你的代码：

```py
python3 ok -q 08 -u
python3 ok -q 08
```

### Problem 9 (2 pt)

在 `scheme_apply` 函数中实现 `LambdaProcedure` 案例（在 `scheme_eval_apply.py` ）。

你应该首先使用适当的父框架的 `make_child_frame` 方法创建一个新的 `Frame` 实例，将形式参数与参数值绑定。然后，在这个新的框架中使用 `eval_all` 方法评估存储过程主体的每个表达式。

你的新框架应该是定义 lambda 的那个框架的一个子框架。注意，作为参数提供给 `scheme_apply` 的 `env` 是存储过程被调用的框架。请参阅 [用户定义的程序](https://inst.eecs.berkeley.edu/~cs61a/sp22/proj/scheme/#user-defined-procedures) 以提醒自己 `LambdaProcedure` 的属性。

使用 Ok 来解锁和测试你的代码：

```py
python3 ok -q 09 -u
python3 ok -q 09
```

### Problem 10 (1 pt)

目前，你的 Scheme 解释器能够以如下方式将符号绑定到用户定义的过程中：

```py
scm> (define f (lambda (x) (* x 2)))
f
```

然而，我们希望能够使用定义命名过程的速记形式：

```py
scm> (define (f x) (* x 2))
f
```

修改 `scheme_forms.py` 中的 `do_define_form` 函数，使其能够正确处理 `define (...) ...)` 表达式（ [spec](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/scheme-spec/#define) ）。

确保它能够处理多表达式体。比如说，

```py
scm> (define (g y) (print y) (+ y 1))
g
scm> (g 3)
3
4
```

你的应该做以下工作：

- 使用给定的变量 `signature` 和 `expressions` ，找到定义的函数的名称（符号）、格式和主体。
- 使用 formals 和 body 创建一个 `LambdaProcedure` 实例。提示：你可以使用你在问题 8 中所做的，在适当的参数上调用 `do_lambda_form` 。
- 将符号与这个新的 `LambdaProcedure` 实例绑定。

使用 Ok 来解锁和测试你的代码：

```py
python3 ok -q 10 -u
python3 ok -q 10
```

### Problem 11 (1 pt)

到目前为止，我们看到的所有 Scheme 程序都使用了 *词法范围* ：新调用框架的父级是定义程序的环境。另一种范围，在 Scheme 中不是标准的，但在 Lisp 的其他变体中出现，被称为 *动态范围* ：新的调用框架的父级是调用表达式被评估的环境。通过动态范围，在代码的不同部分用相同的参数调用同一个过程可以产生不同的行为（由于父框架不同）。

`mu` 的特殊形式（ [spec](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/scheme-spec/#mu) ；为这个项目发明的）评估到一个动态范围的过程。

```py
scm> (define f (mu () (* a b)))
f
scm> (define g (lambda () (define a 4) (define b 5) (f)))
g
scm> (g)
20
```

上面，过程 `f` 没有 `a` 或 `b` 作为参数；但是，由于 `f` 在过程 `g` 中被调用，它可以访问 `g` 的框架中定义的 `a` 和 `b` 。

在 `scheme_forms.py` 中实现 `do_mu_form` 来评估 `mu` 特殊形式。一个 `mu` 表达式可以评估为一个 `MuProcedure` 。大部分的 `MuProcedure` 类（定义在 `scheme_classes.py` 中）已经为你提供了。

除了实现 `do_mu_form` 之外，在 `scheme_apply` 函数（在 `scheme_eval_apply.py` 中）中完成 `MuProcedure` 案例，这样当一个 mu 过程被调用时，它的主体会在正确的环境中被评估。当一个 `MuProcedure` 被调用时，新的调用框架的父级是该调用表达式被评估的环境。因此，一个 `MuProcedure` 不需要将环境作为实例属性来存储。

使用 Ok 来解锁和测试你的代码：

```py
python3 ok -q 11 -u
python3 ok -q 11
```

在项目的这一点上，你的 Scheme 解释器应该支持以下功能：

- 使用 `lambda` 和 `mu` 表达式创建程序，
- 使用 `define` 表达式来定义命名的程序，以及
- 调用用户定义的程序。

## Part 3: Special Forms

这一部分将在 `scheme_forms.py` 中完成。

逻辑上的特殊形式包括 `if` 、 `and` 、 `or` 和 `cond` 。这些表达式之所以特殊，是因为并非所有的子表达式都可以被评估。

在 Scheme 中，只有 `#f` 是一个假值。所有其他的值（包括 `0` 和 `nil` ）都是真值。你可以使用 `scheme_utils.py` 中定义的 Python 函数 `is_scheme_true` 和 `is_scheme_false` 来测试一个值是真值还是假值。

> Scheme 传统上使用 `#f` 来表示假布尔值。在我们的解释器中，这相当于 `false` 或 `False` 。同样地， `true` 、 `True` 和 `#t` 都是等价的。然而，在解锁测试时，使用 `#t` 和 `#f` 。

为了让你入门，我们在 `do_if_form` 函数中提供了 `if` 特殊形式的实现。在开始做下面的问题之前，请确保你理解这个实现。

### Problem 12 (2 pt)

实现 `do_and_form` 和 `do_or_form` ，使 `and` 和 `or` 表达式（ [spec](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/scheme-spec/#and) ）得到正确的评估。

逻辑形式 `and` 和 `or` 是 *短路的* 。对于 `and` ，你的解释器应该从左到右评估每个子表达式，如果其中任何一个是一个假值，就返回这个值。否则，返回最后一个子表达式的值。如果在 `and` 表达式中没有子表达式，它就会被判定为 `#t` 。

```py
scm> (and)
#t
scm> (and 4 5 6)  ; all operands are true values
6
scm> (and 4 5 (+ 3 3))
6
scm> (and #t #f 42 (/ 1 0))  ; short-circuiting behavior of and
#f
```

> 对于 `and` 和 `or` 的形式，记住要使用我们内部的 Python 表示法 `#t` 和 `#f` 。参见实验 11 的 [内部表示法](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab11/#internal-representations) 。

对于 `or` ，从左到右评估每个子表达式。如果任何一个子表达式被评估为一个真值，返回这个值。否则，返回最后一个子表达式的值。如果在一个 `or` 表达式中没有子表达式，那么它的值是 `#f` 。

```py
scm> (or)
#f
scm> (or 5 2 1)  ; 5 is a true value
5
scm> (or #f (- 1 1) 1)  ; 0 is a true value in Scheme
0
scm> (or 4 #t (/ 1 0))  ; short-circuiting behavior of or
4
```

> **重要提示：** 使用 `scheme_utils.py` 中提供的 Python 函数 `is_scheme_true` 和 `is_scheme_false` 来测试布尔值。

使用 Ok 来解锁和测试你的代码：

```py
python3 ok -q 12 -u
python3 ok -q 12
```

### Problem 13 (2 pt)

填补 `do_cond_form` 的缺失部分，使其正确实现 `cond` （ [spec](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/scheme-spec/#cond) ），返回对应于 true 谓词的第一个结果子表达式的值，或者对应于 `else` 的结果子表达式的值。

一些特殊情况：

- 当真谓词没有相应的结果子表达式时，返回谓词值。
- 当一个 `cond` case 的结果子表达式有多个表达式时，评估它们并返回最后一个表达式的值。（ *提示：* 使用 `eval_all` 。）

你的实现应该符合下面的例子和 `tests.scm` 中的附加测试。

```py
scm> (cond ((= 4 3) 'nope)
           ((= 4 4) 'hi)
           (else 'wait))
hi
scm> (cond ((= 4 3) 'wat)
           ((= 4 4))
           (else 'hm))
#t
scm> (cond ((= 4 4) 'here (+ 40 2))
           (else 'wat 0))
42
```

如果没有真谓语，也没有其他 `else` 情况， `cond` 的值是 `undefined` 。在这种情况下， `do_cond_form` 应该返回 `None` 。如果只有一个 `else` ，返回其子表达式。如果它没有，则返回 `#t` 。

```py
scm> (cond (False 1) (False 2))
scm> (cond (else))
#t
```

使用 Ok 来解锁和测试你的代码：

```py
python3 ok -q 13 -u
python3 ok -q 13
```

### Problem 14 (2 pt)

`let` 的特殊形式（ [spec](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/scheme-spec/#let) ）将符号与数值局部绑定，赋予它们初始值。比如说：

```py
scm> (define x 5)
x
scm> (define y 'bye)
y
scm> (let ((x 42)
           (y (* x 10)))  ; this x refers to the global value of x, not 42
       (list x y))
(42 50)
scm> (list x y)
(5 bye)
```

在 `scheme_forms.py` 中实现 `make_let_frame` ，它返回一个 `env` 的子框架，将 `bindings` 的每个元素中的符号绑定到其对应表达式的值上。 `bindings` Scheme 列表包含了每一个包含一个符号和一个相应表达式的对。

你可能会发现下面的函数和方法很有用：

- `validate_form`：这个函数可以用来验证每个绑定的结构。它接收一个表达式的 Scheme list `expr` 以及 `min` 和 `max` 长度。如果 `expr` 不是一个长度在 `min` 和 `max` 之间的列表，它将引发一个错误。如果没有传入 `max` ，默认为无穷大。
- `validate_formals`：该函数验证其参数是一个 Scheme 符号列表，每个符号都是不同的。

如果你不理解任何测试案例，请记得参考 [规范](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/scheme-spec/#let) ！

使用 Ok 来解锁和测试你的代码：

```py
python3 ok -q 14 -u
python3 ok -q 14
```

### Additional Scheme Tests (1 pt)

本项目第三部分的最后一项任务是确保你的 scheme 解释器通过我们提供的额外测试套件。

要运行这些测试（分值 1 分），请运行命令：

```py
python3 ok -q tests.scm
```

如果你已经通过了所有要求的情况，当你运行 `python ok --score` 时，你应该看到 `tests.scm` 收到了 1/1 的分数。如果你由于在代码中添加了用于调试的 `print` 语句的输出而导致测试失败，请确保将这些语句也删除，以便测试通过。

> 当你完成第三部分后，请确保你使用 OK 提交，以获得检查点的全部分数。
>
> ```py
> python3 ok --submit
> ```
>
> 如果你想检查你到目前为止的分数，请使用以下命令：
>
> ```py
> python3 ok --score
> ```
>
> **查看你在检查点中通过了哪些测试的最好方法是使用 OK 中的分数命令。**

祝贺你！你的 Scheme 解释器实现已经完成了！

## Part IV: Write Some Scheme

不仅你的 Scheme 解释器本身是一个树状递归程序，而且它也足够灵活，可以评估其他递归程序。在 `questions.scm` 文件中实现以下程序。

关于所有内置 Scheme 程序的行为描述，请参见 [内置程序参考](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/scheme-builtins/) 。

当你使用你的解释器时，你可能会在你的解释器实现中发现额外的错误。因此，你可能会发现在工作人员解释器或 [网络编辑器](https://code.cs61a.org/scheme) 中测试你的这些问题的代码是很有用的，一旦你确信你的 Scheme 代码是有效的，再在你自己的解释器中尝试。你也可以使用网络编辑器来可视化你写的方案代码，帮助你进行调试。

### Scheme 编辑器

在你写代码的时候，你可以使用 Scheme Editor 进行调试。在你的 `scheme` 文件夹中，你会发现一个新的编辑器。要运行这个编辑器，请运行 `python3 editor` 。这应该会在你的浏览器中弹出一个窗口；如果没有，请导航到 [localhost:31415](localhost:31415) ，你应该会看到它。

请确保在一个单独的标签或窗口中运行 `python3 ok` ，以便编辑器持续运行。

👩🏽‍💻👨🏿‍💻 [配对编程？](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/pair-programming) 记住要交替扮演司机和导航员的角色。驾驶员控制键盘；导航员观察、提问并提出意见。

### Problem 15 (2 pt)

实现 `enumerate` 过程，该过程接收一个值的列表并返回一个两元素的列表，其中第一个元素是值的索引，第二个元素是值本身。

```py
scm> (enumerate '(3 4 5 6))
((0 3) (1 4) (2 5) (3 6))
scm> (enumerate '())
()
```

使用 Ok 来测试你的代码：

```py
python3 ok -q 15
```

### Problem 16 (2 pt)

实现 `merge` 过程，该过程接收一个比较器函数 `inorder?` 和两个被排序的列表，并将两个列表合并成一个被排序的列表。比较器通过比较两个值来定义排序，当且仅当这两个值是有序的，返回一个真值。这里，排序的意思是根据比较器进行排序。比如说：

```py
scm> (merge < '(1 4 6) '(2 5 8))
(1 2 4 5 6 8)
scm> (merge > '(6 4 1) '(8 5 2))
(8 6 5 4 2 1)
```

在出现平局的情况下，你可以任意选择打破平局。

使用 Ok 来测试你的代码：

```py
python3 ok -q 16
```

## Extra Credit

> 在正常的办公时间和项目聚会期间，工作人员将优先帮助学生解决必要的问题。除非 [队列](https://oh.cs61a.org/) 是空的，否则我们不会对这两个额外的问题提供帮助。

### Problem EC 1 (2 pt)

完成 `scheme_eval_apply.py` 中的函数 `optimize_tail_calls` 。它返回一个替代 `scheme_eval` 的正确的尾部递归。也就是说，解释器将允许在恒定的空间内有不受限制的主动尾调用。它有一个第三个参数 `tail` ，表示要评估的表达式是否在尾部上下文中。

`Unevaluated` 类表示一个需要在环境中被评估的表达式。当 `optimized_eval` 收到一个在尾部上下文中的非原子表达式时，它返回一个 `Unevaluated` 实例。否则，它应该重复调用 `unoptimized_scheme_eval` 直到结果是一个值，而不是一个 `Unevaluated` 。

**一个成功的实现将需要改变其他几个函数，包括我们为你提供的一些函数。** 整个解释器中所有处于尾部上下文中的表达式都应该通过调用 `scheme_eval` 来进行评估，其第三个参数为 `True` （现在称为 `tail` ）。你的目标是确定你的代码中哪些表达式处于尾部上下文中，并根据需要改变对 `scheme_eval` 的调用。

> 尾部调用的优化在 [第 29 讲](https://inst.eecs.berkeley.edu/~cs61a/sp22/assets/slides/29-Scopes_+_Tail_Calls.html) 中讨论过。 Scheme 解释器中的 Unevaluated 类在概念上类似于讲座中讨论的“thunk”，而 optimized_eval 中缺少的代码基本上是讲座中讨论的“蹦床”技术。

完成后，在 `scheme_eval_apply.py` 中取消注释以下一行，以使用你的实现：

```py
scheme_eval = optimize_tail_calls(scheme_eval)
```

使用 Ok 来测试你的代码：

```py
python3 ok -q EC
```

## 可选问题

### Optional Problem 1 (0 pt)

在 Scheme 中，源代码就是数据。每一个非原子表达式都被写成 Scheme 列表，所以我们可以写操纵其他程序的程序，就像我们写操纵列表的程序一样。

重写程序可能很有用：我们可以写一个只处理一小部分核心语言的解释器，然后写一个程序，在程序传递给解释器之前，将其他特殊形式转换为核心语言。

例如， `let` 特殊形式相当于一个以 `lambda` 表达式开头的调用表达式。两者都创建一个新的框架，扩展当前环境，并在该新环境中评估一个主体。

```py
(let ((a 1) (b 2)) (+ a b))
;; Is equivalent to:
((lambda (a b) (+ a b)) 1 2)
```

这些表达式可以用下面的图来表示：

<table>
<tr>
<th>
Let
</th>
<th>
Lambda
</th>
</tr>
<tr>
<td>

![](./images/let.png)

</td>
<td>

![](./images/lambda.png)

</td>
</tr>
</table>

使用这个规则来实现一个叫做 `let-to-lambda` 的过程，它将所有 `let` 的特殊形式改写成 `lambda` 表达式。如果我们引用一个 `let` 表达式并将其传入这个过程，应该会返回一个等价的 `lambda` 表达式：

```py
scm> (let-to-lambda '(let ((a 1) (b 2)) (+ a b)))
((lambda (a b) (+ a b)) 1 2)
scm> (let-to-lambda '(let ((a 1)) (let ((b a)) b)))
((lambda (a) ((lambda (b) b) a)) 1)
scm> (let-to-lambda 1)
1
scm> (let-to-lambda 'a)
a
```

为了处理所有程序， `let-to-lambda` 必须了解 Scheme 语法。由于 Scheme 表达式是递归嵌套的， `let-to-lambda` 也必须是递归的。事实上， `let-to-lambda` 的结构与 `scheme_eval` 的结构有些相似——但都是 Scheme 的结构。作为提醒，原子包括数字、布尔值、 nil 和符号。对于这个问题，你不需要考虑包含准引号的代码。

```py
(define (let-to-lambda expr)
  (cond ((atom?   expr) <rewrite atoms>)
        ((quoted? expr) <rewrite quoted expressions>)
        ((lambda? expr) <rewrite lambda expressions>)
        ((define? expr) <rewrite define expressions>)
        ((let?    expr) <rewrite let expressions>)
        (else           <rewrite other expressions>)))
```

*提示：* 考虑如何使用 `map` 将 list 中每个元素的 `let` 形式转换为等价的 `lambda` 形式。

```py
scm> (zip '((1 2) (3 4) (5 6)))
((1 3 5) (2 4 6))
scm> (zip '((1 2)))
((1) (2))
scm> (zip '())
(() ())
```

*提示 2：* 在这个问题中，建立一个可以求值为特殊形式（例如 `lambda` 表达式）的 scheme 列表可能会有帮助。作为一个相关的例子，下面的代码建立了一个 scheme 列表，它的值是表达式 `(define (f x) (+ x 1))` 。

```py
(let ((name-and-params '(f x))
      (body '(+ x 1)))
  (cons 'define
        (cons name-and-params (cons body nil))))
```

通过运行测试你的实现

使用 Ok 来测试你的代码：

```py
python3 ok -q optional_1
```

> 我们在定义 `let-to-lambda` 的时候使用了 `let` 。如果我们想在一个不认识 `let` 的解释器上运行 `let-to-lambda` 怎么办？我们可以把 `let-to-lambda` 传给它自己，把它改写成一个没有 `let` 的等价程序：
>
> ```py
> ;; The let-to-lambda procedure
> (define (let-to-lambda expr)
>  ...)
> 
> ;; A list representing the let-to-lambda procedure
> (define let-to-lambda-code
>   '(define (let-to-lambda expr)
>      ...))
> 
> ;; A let-to-lambda procedure that does not use 'let'!
> (define let-to-lambda-without-let
>   (let-to-lambda let-to-lambda-code))
> ```

## Optional Problem 2 (0 pt)

宏允许用户对语言本身进行扩展。简单的宏可以用 `define-macro` 的特殊形式提供。这必须像过程定义一样使用，它和 `define` 一样创建一个过程。然而，这个过程有一个特殊的评估规则：它被应用于其参数，而不首先评估它们。然后对这个应用的结果进行评估。

这个最后的评估步骤发生在调用者的框架内，就像宏的返回值真的被粘贴到了代码中，代替了宏的位置。

下面是一个简单的例子：

```py
scm> (define (map f lst) (if (null? lst) nil (cons (f (car lst)) (map f (cdr lst)))))
scm> (define-macro (for formal iterable body)
....     (list 'map (list 'lambda (list formal) body) iterable))
scm> (for i '(1 2 3)
....     (print (* i i)))
1
4
9
(None None None)
```

上面的代码定义了一个 macro `for` ，除了不需要在主体周围设置 lambda 之外，它就像一个 `map` 。

为了实现 `define-macro` ，完成 `do_define_macro` 的实现，它应该创建一个 `MacroProcedure` ，并与 `do_define_form` 中的名称绑定。然后，更新 `scheme_eval` ，以便正确评估对宏程序的调用。

使用 Ok 来测试你的代码：

```py
python3 ok -q optional_2
```

### 结论

**恭喜你！** 你刚刚实现了一个解释器。你刚刚为整个语言实现了一个解释器！如果你喜欢这个项目并想进一步扩展它，你可能会对更多的高级功能感兴趣，比如 [let* 和 letrec](http://schemers.org/Documents/Standards/R5RS/HTML/r5rs-Z-H-7.html#%_sec_4.2.2) 、 [unquote 拼接](http://schemers.org/Documents/Standards/R5RS/HTML/r5rs-Z-H-7.html#%_sec_4.2.6) 、 [error 跟踪](https://en.wikipedia.org/wiki/Stack_trace) 和 [continuations](https://en.wikipedia.org/wiki/Call-with-current-continuation) 。

提交到 Ok 来完成这个项目。

```py
python3 ok --submit
```

如果你有伙伴，请确保将他们加入到 okpy.org 上的提交中。