# Lab 10: Scheme

## 起始文件

下载 [lab10.zip](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab10/lab10.zip) 。在该压缩包中，你将找到本实验中问题的起始文件，以及 [Ok](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab10/ok) 自动评分器的副本。

# 主题

如果你需要复习本实验的材料，请参考本节。可以直接跳到 [问题](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab10/#required-questions) 上，如果卡住了，可以回到这里。

## Scheme

Scheme 是 20 世纪 70 年代的一种著名的函数式编程语言。它是 Lisp （代表 LISt Processing ）的一种方言。大多数人的第一印象是独特的语法，它使用前缀符号和（通常是许多）嵌套括号（见 [http://xkcd.com/297/](http://xkcd.com/297/) ）。Scheme 的特点是一流的函数和优化的尾部递归，这在当时是比较新的功能。

> 我们的课程使用一个自定义版本的 Scheme （你将为项目 4 建立这个版本），包含在启动器 ZIP 压缩包中。要启动解释器，请输入 `python3 scheme` 。要交互式地运行 Scheme 程序，输入 `python3 scheme -i <file.scm>` 。要退出 Scheme 解释器，键入 `(exit)` 。在解决问题时，你可能会发现 [code.cs61a.org/scheme](https://code.cs61a.org/scheme) 很有用，因为它可以画出环境图和框点图，还可以让你一步步地走完你的代码（类似于 Python Tutor ）。不过别忘了通过 Ok 提交你的代码！

### Scheme 编辑器

在你写代码的时候，你可以使用 Scheme 编辑器进行调试。在你的 `scheme` 文件夹中，你会发现一个新的编辑器。要运行这个编辑器，请运行 `python3 editor` 。这应该会在你的浏览器中弹出一个窗口；如果没有，请打开浏览器进入此网站 [localhost:31415](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab10/localhost:31415) ，你应该会看到它。

请确保在一个单独的标签或窗口中运行 `python3 ok` ，以便编辑器持续运行。

如果你发现你的代码在在线编辑器中可以运行，但在你自己的解释器中却不能运行，那就有可能是你在早期的代码中出现了错误，你必须要追查清楚。每隔一段时间就会有一个我们测试没有发现的错误，如果你发现了一个，你应该让我们知道！

## Expressions

### Primitive Expressions

就像在 Python 、原子或基元中一样， Scheme 中的表达式只需要一个步骤就能计算。这包括数字、布尔、符号。

```py
scm> 1234    ; integer
1234
scm> 123.4   ; real number
123.4
```

#### Symbols

在这些类型中，符号类型是我们在 Python 中唯一没有遇到的。 **符号** 的作用很像 Python 的名字，但不完全是。具体来说， Scheme 中的符号也是一种值的类型。另一方面，在 Python 中，名字只能作为表达式；Python 的表达式永远不能称为一个名字。

```py
scm> quotient      ; A name bound to a built-in procedure
#[quotient]
scm> 'quotient     ; An expression that evaluates to a symbol
quotient
scm> 'hello-world!
hello-world!
```

#### Booleans

在 Scheme 中，除了特殊的布尔值 `#f` 之外，所有的值都被解释为真值（不像 Python ，那里有一些像 `0` 这样的假值）。我们特定版本的 Scheme 解释器允许你用 `True` 和 `False` 来代替 `#t` 和 `#f` 。这并不是标准的。

```py
scm> #t
#t
scm> #f
#f
```

### Call Expressions

和 Python 一样， Scheme 调用表达式中的运算符在所有操作数之前。与  Python 不同的是，运算符包含在圆括号内，操作数用空格而不是逗号分开。然而， Scheme 调用表达式遵循与 Python 完全相同的规则。

1. 计算运算符。它应该为一个过程。
2. 计算操作数，从左到右。
3. 将过程应用于被计算的操作数。

下面是一些使用内置过程的例子：

```py
scm> (+ 1 2)
3
scm> (- 10 (/ 6 2))
7
scm> (modulo 35 4)
3
scm> (even? (quotient 45 2))
#t
```

### Special Forms

特殊形式表达式的运算符是一种特殊形式。特殊形式之所以“特殊”，是因为它们不遵循上一节所述的三种计算规则。相反，每个特殊形式都遵循它自己的特殊执行规则，比如在计算所有操作数之前进行短路。

我们今天要研究的一些特殊形式的例子是 `if` 、 `cond` 、 `define` 和 `lambda` 形式。请阅读下面相应的章节，了解它们的计算规则是什么！

## Control Structures

### `if` Expressions

`if` 的特殊形式允许我们根据一个谓词来计算两个表达式中的一个。它接收两个必要的参数和一个可选的第三个参数：

```py
(if <predicate> <if-true> [if-false])
```

第一个操作数是 Scheme 中所谓的 **谓词** 表达式，一个表达式的值被解释为 `#t` 或 `#f` 。

计算 `if` 特殊形式表达式的规则如下：

1. 计算 `<predicate>`。
2. 如果 `<predicate>` 求值为真值，那么计算并返回 if 表达式 `<if-true>` 的值。否则，如果提供了 `[if-false]` 的值，就计算并返回该值。

你能明白为什么这个表达式是一个特殊形式吗？比较正则调用表达式和 `if` 表达式之间的规则。两者有什么不同？

> 计算调用表达式的第 2 步需要按顺序计算所有的操作数。然而， `if` 表达式只会计算它的两个操作数，即条件表达式和 `<true-result>` 或 `<false-result>` 。因为我们不计算 `if` 表达式中的所有操作数，所以它是一种特殊形式。

让我们比较一下 Scheme `if` 表达式和 Python `if` 语句。

<table>
<tr>
<th>
Scheme
</th>
<th>
Python
</th>
</tr>
<tr>
<td>

```py
scm> (if (> x 3)
         1
         2)
```

</td>
<td>

```py
>>> if x > 3:
...     1
... else:
...     2
```

</td>
</tr>
</table>

虽然代码看起来是一样的，但每个代码块被计算时发生的事情实际上是非常不同的。具体来说， Scheme 表达式，鉴于它是一个表达式，会被计算为某个值。然而， Python 的 `if` 语句只是引导了程序的流程。

两者之间的另一个区别是，有可能在 Python `if` 语句的嵌套中加入更多的代码行，而 Scheme `if` 表达式只期望在真结果和假结果中各有一个表达式。

最后一个区别是，在 Scheme 中，你不能写 `elif` 情况。如果你想用多个条件的 `if` 表达式，你需要多个分支的 `if` 表达式。

<table>
<tr>
<th>
Scheme
</th>
<th>
Python
</th>
</tr>
<tr>
<td>

```py
scm> (if (< x 0)
         'negative
         (if (= x 0)
             'zero
             'positive
         )
 )
```

</td>
<td>

```py
>>> if x < 0:
...     'negative'
... else:
...     if x == 0:
...         'zero'
...     else:
...         'positive'
```

</td>
</tr>
</table>

### `cond` Expressions

使用嵌套的 `if` 表达式似乎并不是一个非常实用的方法来处理多种情况。相反，我们可以使用 `cond` 的特殊形式，这是一个类似于 Python 中多语句 if/elif/else 条件表达式的通用条件表达式。 `cond` 接受任意数量的参数，称为子句。一个子句被写成一个包含两个表达式的列表：（`(<p> <e>)`）。

```py
(cond
    (<p1> <e1>)
    (<p2> <e2>)
    ...
    (<pn> <en>)
    [(else <else-expression>)])
```

每个子句中的第一个表达式是一个谓词。子句中的第二个表达式是与它的谓词相对应的返回表达式。可选的 `else` 子句没有谓语。

计算的规则如下：

1. 依次计算谓词 `<p1>`、 `<p2>`、 ...、 `<pn>` ，直到达到一个计算结果为真的值。
2. 如果达到一个计算结果为真的值的谓词，就计算并返回子句中的相应表达式。
3. 如果没有一个谓词结果是真值，并且有一个 `else` 子句，那么计算并返回 `<else-expression>` 。

正如你所看到的， `cond` 是一个特殊的形式，因为它不对其操作数进行整体计算；谓词和其相应的返回表达式是分开计算的。此外，表达式在到达第一个计算结果为真值的谓词时就会短路，剩下的谓词则不被计算。

下面的代码大致上是等价的（见 [if 表达式部分](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab10/#if-expressions) 的解释）。

<table>
<tr>
<th>
Scheme
</th>
<th>
Python
</th>
</tr>
<tr>
<td>

```py
scm> (cond
        ((> x 0) 'positive)
        ((< x 0) 'negative)
        (else 'zero))
```

</td>
<td>

```py
>>> if x > 0:
...     'positive'
... elif x < 0:
...     'negative'
... else:
...     'zero'
```

</td>
</tr>
</table>

## Defining Names

`define` 这个特殊形式是用来定义 Scheme 中的变量和函数。 `define` 的特殊形式有两个版本。为了定义变量，我们使用 `define` 形式，其语法如下：

```py
(define <name> <expression>)
```

计算这个表达式的规则是

1. 计算 `<expression>` 。
2. 将其值与当前帧中的 `<name>` 绑定。
3. 返回 `<name>` 。

`define` 的第二个版本用于定义程序：

```py
(define (<name> <param1> <param2> ...) <body> )
```

为了计算这个表达式：

1. 用给定的参数和 `<body>` 创建一个 lambda 过程。
2. 将该过程与当前框架中的 `<name>` 绑定。
3. 返回 `<name>` 。

下面两个表达式是等价的：

```py
scm> (define foo (lambda (x y) (+ x y)))
foo
scm> (define (foo x y) (+ x y))
foo
```

`define` 是一种特殊的形式，因为它的操作数根本就没有被计算过 例如， `<body>` 在定义过程时不被计算，而是在调用过程时被计算。 `<name>` 和参数名都是在执行这个 `define` 表达式时不应该被计算的名字。

## Lambda Functions

所有的 Scheme 程序都是 lambda 程序。为了创建一个 lambda 过程，我们可以使用 `lambda` 的特殊形式：

```py
(lambda (<param1> <param2> ...) <body>)
```

这个表达式将创建并返回一个具有给定参数和主体的函数，但它不会改变当前环境。这与 Python 中的 `lambda` 表达式非常相似！

```py
scm> (lambda (x y) (+ x y))        ; Returns a lambda function, but doesn't assign it to a name
(lambda (x y) (+ x y))
scm> ((lambda (x y) (+ x y)) 3 4)  ; Create and call a lambda function in one line
7
```

一个过程可以接受任何数量的参数。 `<body>` 可以包含多个表达式。在 Scheme 中没有一个与 Python `return` 语句相当的版本。该函数将简单地返回主体中最后一个表达式的值。

# 必要的问题

## What Would Scheme Display?

### Q1: Combinations

让我们熟悉一下一些内置的 Scheme 程序和特殊形式吧！

> 使用 Ok 来解锁以下“Scheme会打印什么？”的问题：
>
> ```py
> python3 ok -q combinations -u
> ```

```py
scm> (- 10 4)

scm> (* 7 6)

scm> (+ 1 2 3 4)

scm> (/ 8 2 2)

scm> (quotient 29 5)

scm> (modulo 29 5)
```

```py
scm> (= 1 3)                    ; Scheme uses '=' instead of '==' for comparison

scm> (< 1 3)

scm> (or 1 #t)                  ; or special form short circuits

scm> (and #t #f (/ 1 0))

scm> (not #t)
```

```py
scm> (define x 3)

scm> x

scm> (define y (+ x 4))

scm> y

scm> (define x (lambda (y) (* y 2)))

scm> (x y)
```

```py
scm> (if (not (print 1)) (print 2) (print 3))

scm> (* (if (> 3 2) 1 2) (+ 4 5))

scm> (define foo (lambda (x y z) (if x y z)))

scm> (foo 1 2 (print 'hi))

scm> ((lambda (a) (print 'a)) 100)
```

## 代码编写问题

### Q2: Over or Under

定义一个过程 `over-or-under` ，它接收一个数字 `num1` 和一个数字 `num2` 并返回如下结果：

- 如果 `num1` 小于 `num2` ，则返回 -1
- 如果 `num1` 等于 `num2` 则返回 0
- 如果 `num1` 大于 `num2` 则返回 1

> 挑战：使用 `if` 和 `cond` 以两种不同的方式实现这一目标！

```py
(define (over-or-under num1 num2)
  'YOUR-CODE-HERE
)
```

使用 Ok 来测试你的代码：

```py
python3 ok -q over_or_under
```

### Q3: Make Adder

编写程序 `make-adder` ，它接收一个初始数字 `num` ，然后返回一个程序。这个返回过程接收一个数字 `inc` ，并返回 `num + inc` 的结果。

> *提示：* 要返回一个过程，你可以返回一个 `lambda` 表达式或者 `define` 另一个嵌套过程。记住， Scheme 会自动返回过程中的最后一个子句。
>
> 你可以在 [61A 方案规范](https://cs61a.org/articles/scheme-spec/#lambda) 中找到关于 `lambda` 表达式的语法的文档！

```py
(define (make-adder num)
  'YOUR-CODE-HERE
)
```

使用 Ok 来测试你的代码：

```py
python3 ok -q make_adder
```

### Q4: Compose

编写一个程序 `composed` ，它接收程序 `f` 和 `g` 并输出一个新的程序。这个新程序接收一个数字 `x` ，并输出 `f` 调用 `g` 且其参数为 `x` 的结果。

```py
(define (composed f g)
  'YOUR-CODE-HERE
)
```

使用 Ok 来测试你的代码：

```py
python3 ok -q composed
```

### Q5: Pow

实现一个过程 `pow` ，用于将数 `base` 提高到非负整数 `exp` 的幂，对于该过程，操作数是对数增长，而不是线性增长（递归调用的数量应该比输入的 `exp` 小得多）。例如，对于 `(pow 2 32)` 应该采取 5 次递归调用而不是 32 次递归调用。同样地， `(pow 2 64)` 应该采取 6 次递归调用。

> *提示：* 考虑观察以下结果：
>
> 1. $x^{2y} = (x^{y})^{2}$
> 2. $x^{2y+1} = x(x^{y})^{2}$
>
> 例如，我们看到 $2^{32}$ 是 $(2^{16})^{2}$ ， $2^{16}$ 是 $(2^{8})^{2}$ ，等等。你可以使用内置的谓词 `even?` 和 `odd?` 。 Scheme 并不像 Python 那样支持迭代，所以考虑用另一种方式来解决这个问题。

```py
(define (square n) (* n n))

(define (pow base exp)
  'YOUR-CODE-HERE
)
```

使用 Ok 来解锁测试，并测试你的代码：

```py
python3 ok -q pow -u
python3 ok -q pow
```

## 提交

请确保提交本实验：

```py
python3 ok --submit
```