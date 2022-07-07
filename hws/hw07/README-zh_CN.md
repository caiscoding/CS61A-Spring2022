# Homework 7: Scheme Data Abstractions, Programs as Data

## 说明

下载 [hw07.zip](https://inst.eecs.berkeley.edu/~cs61a/sp22/hw/hw07/hw07.zip) 。在压缩包内，你会发现一个名为 [hw07.scm](https://inst.eecs.berkeley.edu/~cs61a/sp22/hw/hw07/hw07.scm) 的文件，以及一份 `ok` 自动评分器的副本。

**提交：** 完成后，用 `python3 ok --submit` 提交。你可以在截止日期前多次提交，但只有最后一次提交才会被打分。检查你是否已经在 [okpy.org](https://okpy.org/) 上成功提交了你的代码。关于提交作业的更多说明，请参见 [Lab 0](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab00#submitting-the-assignment) 。

**使用Ok：** 如果你有任何关于使用 Ok 的问题，请参考 [本指南](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/using-ok) 。

**阅读资料：** 你可能会发现以下参考资料很有用：

- [Scheme 规范](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/scheme-spec/)
- [Scheme 内置程序参考](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/scheme-builtins/)

**评分：** 家庭作业是根据正确性来评分的。每一个错误的问题将使总分减少一分。如教学大纲中所述，有一个家庭作业政策。 **本作业满分为 2 分。**

Scheme 是 20 世纪 70 年代的一种著名的函数式编程语言。它是 Lisp（代表 LISt Processing ）的一种方言。大多数人的第一个观察是它独特的语法，它使用前缀符号和（通常是许多）嵌套的小括号（见 [http://xkcd.com/297/](http://xkcd.com/297/) ）。Scheme 的特点是一流的函数和优化的尾部递归，这在当时是比较新的特点。

在解决问题时，你可能会发现尝试一下 [code.cs61a.org/scheme](https://code.cs61a.org/scheme) 是很有用的，因为它可以画出环境图和框点图，它可以让你一步步地走完你的代码（类似于 Python Tutor ）。不过别忘了通过 Ok 提交你的代码！

## Scheme 编辑器

在你写代码的时候，你可以使用 Scheme 编辑器进行调试。在你的 `scheme` 文件夹中，你会发现一个新的编辑器。要运行这个编辑器，请运行 `python3 editor` 。这应该会在你的浏览器中弹出一个窗口；如果没有，请导航到 [localhost:31415](localhost:31415) ，你应该会看到它。

请确保在一个单独的标签或窗口中运行 `python3 ok` ，以便编辑器持续运行。

如果你发现你的代码在在线编辑器中可以运行，但在你自己的解释器中却不能运行，那就有可能是你在早期的代码中出现了错误，你必须要追查清楚。每隔一段时间就会有一个我们的测试没有捕捉到的错误，如果你发现一个，你应该让我们知道！

## 必要的问题

## 入门视频

这些视频可以为解决本作业中的编码问题提供一些有用的指导。

> 要看这些视频，你应该登录到你的 berkeley.edu 邮箱。

[YouTube link](https://youtu.be/watch?v=6jM18JXj-Q4&list=PLx38hZJ5RLZea1rWe3s2JtuCIku_blUu_)

## Keyword Lists

在下面的问题中，你将探索为同一个抽象创建两个独立的实现。

*关键词列表* 是 Python 中 `dict` 的 Scheme 类似物，但有几个关键的区别：

- 它允许重复的键
- 它的功能也是一个列表，可以进行排序。

`kwlist` 抽象保留了一个 `keys` 和 `values` 的映射。要创建一个 `kwlist` ，请调用构造函数 `(make-kwlist keys values)` ，其中 `keys` 是一个符号的 Scheme 列表，而 `values` 是一个任意类型的 Scheme 列表。这将返回一些抽象的项目 `lst` ，我们可以调用以下方法来检索或添加项目：

```py
scm> (define lst (make-kwlist '(x y z) '(7 8 9)) ; create the keyword list
lst
scm> (get-first-from-kwlist lst 'x) ; get an item
7
scm> (define lst (add-to-kwlist lst 'a 10)) ; add a new item
lst
scm> (get-first-from-kwlist lst 'a) ; get the new item.
10
```

### Q1: Keyword List: Construct

首先，以两种方式实现 `kwlist` 的抽象，例子如下： `(kwlist '(x y z) '(7 8 9))`

1. `kwlist1` ，它以如下方式存储一个关键词列表： `((key1 key2 key3 ...) (value1 value2 value3 ...)` 。通过上面的例子，这应该看起来像 `((x y z) (7 8 9))` 。
2. `kwlist2` ，它以如下方式存储关键字列表： `((key1 value1) (key2 value2) ...)` 。通过上面的例子，这应该看起来像 `((x 7) (y 8) (z 9))` 。

具体来说，实现 `kwlist1` 和 `kwlist2` 的构造函数和选择器。

- 构造函数 `make-kwlist1` 和 `make-kwlist2` 应该接收 Scheme list 的 `keys` 和 `values` ，并构造上述的抽象。
- 选择器 `get-keys-kwlist1`、 `get-keys-kwlist2`、 `get-values-kwlist1` 和 `get-values-kwlist1` 应该接收 `kwlist1` 或 `kwlist2` 并分别返回其键和值。请注意，由于你目前正在创建实现，你是在“抽象障碍之下”；请随意参考 `kwlist1` 和 `kwlist2` 的具体结构细节。

> **提示：** `map` 函数可能被证明是有用的，但不是必须的。你也可以使用 `cadr` 函数，它在文件中为你定义。

```py
scm> (define ex-lst1 (make-kwlist1 '(a b c) '(1 2 3)))
ex-list
scm> (get-keys-kwlist1 ex-lst1)
(a b c)
scm> (get-values-kwlist1 ex-lst1)
(1 2 3)
scm> (define ex-lst2 (make-kwlist2 '(a b c) '(1 2 3)))
ex-list
scm> (get-keys-kwlist2 ex-lst)
(a b c)
scm> (get-values-kwlist2 ex-lst)
(1 2 3)
```

```py
(define (make-kwlist1 keys values)
  'YOUR-CODE-HERE
)

(define (get-keys-kwlist1 kwlist)
  'YOUR-CODE-HERE
)

(define (get-values-kwlist1 kwlist)
  'YOUR-CODE-HERE
)
(define (make-kwlist2 keys values)
  'YOUR-CODE-HERE
)

(define (get-keys-kwlist2 kwlist)
  'YOUR-CODE-HERE
)

(define (get-values-kwlist2 kwlist)
  'YOUR-CODE-HERE
)
```

使用 Ok 来测试你的代码：

```py
python3 ok -q kwlist_construct
```

> **重要的是：** 对于下面的问题，你的实现应该与所使用的抽象概念无关；也就是说，不管是使用 `kwlist1` 还是 `kwlist2` ，它都应该工作。具体来说，在测试中，我们将把抽象的 `kwlist` 定义为 `kwlist1` 或 `kwlist2` ：
> 
> ```py
> scm> (define make-kwlist make-kwlist1)
> scm> (define get-keys-kwlist get-keys-kwlist1)
> scm> (define get-values-kwlist get-values-kwlist1)
> ; tests here...
> scm> (define make-kwlist make-kwlist2)
> scm> (define get-keys-kwlist get-keys-kwlist2)
> scm> (define get-values-kwlist get-values-kwlist2)
> ; tests here...
> ```
> 
> **你应该参考上面的 `kwlist` 程序，而不是 `kwlist1` 或 `kwlist2` 的程序来实现。**

### Q2: Keyword List: Add

现在，实现 `add-to-kwlist` ，它支持向任何 `kwlist` 的实现添加新的（ `key` ， `value` ）对。具体来说， `add-to-kwlist` 接收一个 `kwlist` 、一个 `key` 和一个 `value` 作为输入，并返回一个带有最新键和值的 *新* `kwlist` 。注意， `kwlist` 是有顺序的；也就是说，在不同的配对 `p2` 之前被添加到 `kwlist` 中的配对 `p1` 应该出现在 `kwlist` 的前面。

> **提示：** `append` 方法在这里可能是有用的。为了使你的实现与这两个抽象概念一起工作， *一定要使用以 `kwlist` 结尾的方法，而不是 `kwlist1` 或 `kwlist2` 。*

```py
scm> (define ex-lst (make-kwlist '(a b c) '(1 2 3)))
ex-lst
scm> (get-keys-kwlist ex-lst)
(a b c)
scm> (get-values-kwlist ex-lst)
(1 2 3)
scm> (define ex-lst (add-to-kwlist ex-lst 'd '4))
ex-lst
scm> (get-keys-kwlist ex-lst) ; note that new items are at the end of the list!
(a b c d)
scm> (get-values-kwlist ex-lst) ; here too!
(1 2 3 4)
```

```py
(define (add-to-kwlist kwlist key value)
  'YOUR-CODE-HERE
)
```

使用 Ok 来测试你的代码：

```py
python3 ok -q kwlist_add
```

### Q3: (Optional) Keyword List: Get

现在，实现 `get-first-from-kwlist` ，它获取 `kwlist` 中某个 `key` 绑定的第一个值。如果 `key` 不在列表中，该函数应该返回 `nil` 以表示没有找到有效的键。

> **提示：** 考虑使用 `let` 来临时性地将名字与值绑定。为了使你的实现与这两个抽象概念一起工作， *一定要使用以 `kwlist` 结尾的方法，而不是 `kwlist1` 或 `kwlist2` 。*

```py
scm> (define ex-lst (make-kwlist '(a b c) '(1 2 3)))
ex-lst
scm> (get-first-from-kwlist ex-lst 'b)
2
scm> (get-first-from-kwlist ex-lst 'd) ; if not found, return nil
()
scm> (define ex-lst (add-to-kwlist ex-lst 'd '4))
ex-lst
scm> (get-first-from-kwlist ex-lst 'b)
2
scm> (get-first-from-kwlist ex-lst 'd)
4
scm> (define ex-lst (add-to-kwlist ex-lst 'd '5))
ex-lst
scm> (get-first-from-kwlist ex-lst 'b)
2
scm> (get-first-from-kwlist ex-lst 'd) ; return the *first* occurrence
4
```

```py
(define (get-first-from-kwlist kwlist key)
  'YOUR-CODE-HERE
)
```

使用 Ok 来测试你的代码：

```py
python3 ok -q kwlist_get
```

## Programs as Data

> **注意：** 下面的问题与前面的问题是分开的。

### Q4: Prune

实现 `prune-expr` ，这个过程接收一个以列表形式表示的表达式，并返回包含其他所有参数的相同表达式。操作符不应该被修改。

> **提示：** 你可能会发现编写一个修剪列表的辅助函数是有帮助的。

`prune-expr` 的行为由下面的测试来说明：

```py
scm> (prune-expr '(+ 10 20))
(+ 10)
scm> (prune-expr '(+ 10 20 30))
(+ 10 30)
scm> (eval (prune-expr '(+ 10 20 30)))
40
```

```py
(define (prune-expr expr)
    (define (prune-helper lst)
      'YOUR-CODE-HERE
    )
    'YOUR-CODE-HERE
)
```

使用 Ok 来测试你的代码：

```py
python3 ok -q prune-expr
```

## Chef Curry

回顾一下， `curry` 将一个多参数函数转化为一系列高阶的单参数函数。在下一组问题中，你将利用“程序就是数据”这一概念，创建能够自动 `curry` 任何长度的函数的函数！

### Q5: Cooking Curry

实现函数 `curry-cook` ，它接收一个 Scheme list `formals` 和一个带引号的表达式 `body` 。 `curry-cook` 应该生成一个列表形式的程序，它是一个 lambda 函数的 curried 版本。输出的程序应该是一个 curried 版本的 lambda 函数，形式参数等于 `formals` ，函数体等于 `body` 。你可以假设所有传入的函数都会有超过 0 个 `formals` ；否则，它就不能被 curry 了。

例如，如果你想对函数 `(lambda (x y) (+ x y))` 进行 curry 处理，你将设置 `formals` 等于 `'(x y)` ， `body` 等于 `'(+ x y)` ，并调用 `curry-cook` ： `(curry-cook '(x y) '(+ x y))` 。

```py
scm> (curry-cook '(a) 'a)
(lambda (a) a)
scm> (curry-cook '(x y) '(+ x y))
(lambda (x) (lambda (y) (+ x y)))
```

```py
(define (curry-cook formals body)
    'YOUR-CODE-HERE
)
```

使用 Ok 来测试你的代码：

```py
python3 ok -q curry_cook
```

### Q6: Consuming Curry

现在你有了一个将 lambda 程序创建为列表的函数，创建一个能够使用一系列参数计算 lambda 函数的函数。具体来说，实现函数 `curry-consume` ，它接收一个 curried 的 lambda *函数* `curries` （不是一个列表），并将该函数 `apply` 于一个参数 `args` 的列表。与前面的问题类似，你可以做几个假设：

1. 如果 `curries` 是一个 `n` curried 函数，那么 `args` 中最多有 `n` 个参数。
2. **如果有 0 个参数** ，那么你可以假设 `curries` 已经完全 `apply` 了相关的参数；在这种情况下， `curries` 现在包含一个代表 lambda 函数输出的值。返回它。

注意，对于相应的 lambda 函数 `curries` 来说， `args` 的数量可以少于 `formals` ！在参数较少的情况下， `curry-consume` 应该返回一个 curried lambda 函数，它是部分 `apply` `curries` 的结果，最多到所提供的 `args` 数量。

```py
scm> (define three-curry (curry-cook '(x y z) '(+ x (* y z))))
three-curry
scm> three-curry
(lambda (x) (lambda (y) (lambda (z) (+ x (* y z)))))
scm> (define three-curry-fn (eval three-curry)) ; three-curry-fn is a lambda function derived from the program
three-curry-fn
scm> (define eat-two (curry-consume three-curry-fn '(1 2))) ; pass in only two arguments, return should be a one-arg lambda function!
eat-two
scm> eat-two
(lambda (z) (+ x (* y z)))
scm> (eat-two 3) ; pass in the last argument; 1 + (2 * 3)
7
scm> (curry-consume three-curry-fn '(1 2 3)) ; all three arguments at once
7
```

```py
(define (curry-consume curries args)
    'YOUR-CODE-HERE
)
```

使用 Ok 来测试你的代码：

```py
python3 ok -q curry_consume
```

## 可选的问题

作业中也会包含一些考试级别的问题供你参考。这些问题没有提交的成分；如果你想挑战一下，可以随时尝试一下！

1. Fall 2019 Final Q7c: [*-to-mul](https://cs61a.org/exam/fa19/final/61a-fa19-final.pdf#page=9)
2. Fall 2021 Final Q5a: [Spice](https://cs61a.org/exam/fa21/final/61a-fa21-final.pdf#page=18)