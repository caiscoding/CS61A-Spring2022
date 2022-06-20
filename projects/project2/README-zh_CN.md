# Project 2: CS 61A Autocorrected Typing Software

![](./images/cats_typing.gif)

程序员的梦想是抽象、递归和打字快。

## 说明

> **重要的提交说明：** 为了获得全部分数：
>
> - 在 **2 月 17 日（星期四）** 之前完成第一阶段的提交，获得 1 分。
> - 在 **2 月 24 日（星期四）** 之前完成所有阶段的提交。
>
> 尽量按顺序回答这些问题，因为后面的一些问题会依赖于前面的问题，因此在运行 `ok` 测试时也是如此。
>
> 整个项目可以和另一个伙伴一起完成。
>
> 在 **2 月 23 日（星期三）** 之前提交整个项目，你可以得到 1 分奖励。

在这个项目中，你将编写一个程序来测量打字速度。此外，你将实现打字自动更正，这是一个在用户输入一个单词后试图纠正其拼写的功能。这个项目的灵感来自 [typeracer](https://play.typeracer.com/) 。

> 过去，当学生在没有彻底阅读问题描述的情况下试图实现这些功能时，他们经常会遇到问题。😱 **在开始编码之前，彻底阅读每个描述。**

## 最终成果

我们的工作人员对这个项目的解决方案可以在 [cats.cs61a.org](https://cats.cs61a.org/) 查看。如果你愿意，现在就可以随意尝试。当你完成这个项目时，你将会自己实现这个项目的一个重要部分！

## 下载起始文件

你可以下载所有的项目代码作为一个 [压缩文件](https://inst.eecs.berkeley.edu/~cs61a/sp22/proj/cats/cats.zip) 。这个项目包括几个文件，但你的修改将只对 `cats.py` 进行。以下是压缩包中包含的文件：

- `cats.py`：打字测试逻辑。
- `utils.py`：用于与文件和字符串交互的实用函数。
- `ucb.py`：用于 CS 61A 项目的实用函数。
- `data/sample_paragraphs.txt`：一个包含要输入的文本样本的文件。这些是 [搜刮来的](https://github.com/kavigupta/wikivideos/blob/626de521e04ca643751ed85d549faca6ea528b1d/get_corpus.py) 关于各种主题的维基百科文章。
- `data/common_words.txt`：一个包含常见英语单词的文件，[按频率排序](https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-usa-no-swears.txt) 。
- `data/words.txt`：一个包含更多英语单词的文件， [按频率顺序排列](https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-usa-no-swears.txt) 。
- `cats_gui.py`：一个基于网络的图形用户界面（GUI）的网络服务器。
- `gui_files`：一个包含图形用户界面（GUI）所需文件的目录。
- `multiplayer`：一个支持多人游戏模式所需的文件目录。
- `favicons`：一个图标的目录。
- `images`：一个图片目录。
- `ok`, `proj02.ok`, `tests`：测试文件。

## 组织工作

该项目总分 20 分。 19 分按正确性给分， 1 分是按是否在检查点日期前提交第一阶段给分。

你将提交以下文件：

- `cats.py`

你不需要修改或上交任何其他文件。要提交该项目，请运行以下命令：

```
python3 ok --submit
```

你将能够在 [Ok 页面](http://ok.cs61a.org/) 上查看你的提交。

对于我们要求你完成的功能，可能有一些我们提供的初始代码。如果你不愿意使用这些代码，可以随时删除它，然后从头开始。你也可以在你认为合适的时候添加新的功能定义。

**然而，请不要修改任何其他功能或编辑任何未列出的文件。**这样做可能会导致你的代码无法通过我们的自动测试。另外，请不要改变任何函数的签名（名称、参数顺序或参数数量）。

在整个项目中，你应该测试你代码的正确性。经常测试是很好的做法，这样就可以很容易地区分出问题。然而，你不应该测试得太频繁，以使自己有时间思考问题。

我们提供了一个名为 `ok` 的 **自动评分器** ，以帮助你测试你的代码并跟踪你的进度。在你第一次运行自动评分器时，你会被要求用你的网络浏览器 **登录你的 ok 账户** 。请这样做。每次你运行 `ok` 时，它都会在我们的服务器上备份你的工作和进度。

`ok` 的主要目的是为了测试你的代码实现。

我们建议您 **在完成每个问题后** 提交。只有你的最后一次提交才会被打分。在你遇到提交问题时，多备份你的代码对我们来说也很有用。**如果你忘记提交，你的最后一份备份将自动转换为提交。**

如果你不希望我们记录你的工作备份或你的进度信息，你可以运行

```
python3 ok --local
```

有了这个选项，任何信息都不会被发送到我们的课程服务器。如果你想以交互方式测试你的代码，你可以运行

```
python3 ok -q [question number] -i 
```

并插入适当的问题编号（如 `01` ）。这将运行该问题的测试，直到你失败的第一个测试，然后给你一个机会来交互测试你写的函数。

你也可以在 OK 中使用调试打印功能，写上

```
print("DEBUG:", x)
```

这将在你的终端产生一个输出，而不会导致 OK 测试因额外输出而失败。

# 入门视频

> 要看这些视频，你应该登录到你的 berkeley 邮箱。

[YouTube link](https://youtu.be/watch?v=X-PKsEzyQks&list=PLx38hZJ5RLZdak103Ecx7CZyz1tZHr5I2)

# Phase 1: Typing

> 过去，当学生在没有彻底阅读问题描述的情况下试图实现这些功能时，他们经常会遇到问题。😱 **在开始编码之前，彻底阅读每个描述。**

## Problem 1 (1 pt)

在整个项目中，我们将对 `cats.py` 中的函数进行修改。

实现 `choose` 。这个函数选择用户要输入的段落。它需要三个参数：

- 一个 `paragraphs` 的列表（字符串）
- 一个 `select` 函数，对于可以选择的段落，它返回 `True`
- 一个非负的索引 `k`

`choose` 函数返回第 `k` 个段落，对于该段落， `select` 函数返回 `True` 。如果没有这样的段落存在（因为 `k` 太大），那么 `choose` 函数返回空字符串。

在编写任何代码之前，请解锁测试以验证你对问题的理解：

```
python3 ok -q 01 -u
```

一旦你完成了解锁，就开始实施你的解决方案。你可以用以下方法检查你解决方案的正确性：

```
python3 ok -q 01
```

## Problem 2 (1 pt)

实现 `about` ，它接收一个 `topic` 词的列表。它返回一个函数，该函数接收一个段落，并返回一个布尔值，表明该段落是否包含 `topic` 中的任何单词。

一旦我们实现了 `about` ，我们就可以将返回的函数作为 `select` 参数传递给 `choose` ，这在我们继续实现打字测试时将会很有用。

为了能够准确地进行这种比较，你将需要忽略大小写（也就是说，假设大写和小写字母不会改变它是什么词）和段落中的标点符号。此外，只检查段落中的主题词是否完全匹配，而不是子串。例如，“dogs”不是与“dog”这个词匹配的。

> **提示：** 你可以使用 `utils.py` 中的字符串实用函数。你可以参考实用函数的文档说明，看看它们是如何使用的。

在编写任何代码之前，请解锁测试以验证你对问题的理解：

```
python3 ok -q 02 -u
```

一旦你完成了解锁，就开始实施你的解决方案。你可以用以下方法检查你解决方案的正确性：

```
python3 ok -q 02
```

## Problem 3 (2 pts)

实现 `accuracy` ，它需要一个 `typed` 段落和一个 `reference` 段落。它返回 `typed` 中与 `reference` 中的相应单词完全匹配的单词的百分比。大小写和标点符号也必须匹配。这里的“对应”是指两个词必须出现在 `typed` 和 `reference` 相同索引上——两个词的第一个词必须匹配，两个词的第二个词必须匹配，以此类推。

在这种情况下，一个 *词* 是指用空格与其他词分开的任何字符序列，所以把“dog;”当作一个词。

如果 `typed` 比 `reference` 长，那么 `typed` 中没有对应词的额外词在 `reference` 中都是不正确的。

如果 `typed` 和 `reference` 都是空的，那么准确性是 100.0 。如果 `typed` 是空的，但 `reference` 不是空的，那么准确率为 0 。如果 `typed` 不是空的，但是 `reference` 是空的，那么准确率是 0 。

在编写任何代码之前，请解锁测试以验证你对问题的理解：

```
python3 ok -q 03 -u
```

一旦你完成了解锁，就开始实施你的解决方案。你可以用以下方法检查你解决方案的正确性：

```
python3 ok -q 03
```

👩🏽‍💻👨🏿‍💻 [结对编程？](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/pair-programming) 记住要在驱动者和导航者的角色之间交替进行。驾驶员控制键盘；导航员观察，提问，并提出建议。

## Problem 4 (1 pt)

实现 `wpm` ，计算出 *每分钟的词数* ，这是衡量打字速度的一个标准，给定一个打字的字符串和以 **秒** 为单位的耗时 `elapsed` 。尽管它的名字叫“每分钟词数”，但它不是基于打出的词数，而是基于 5 个字符的组数，这样打字测试就不会因字数的长短而产生偏差。每分钟打字数的公式是打出的字符数（包括空格）除以 5 （典型的字长）与经过的时间（**分钟**）的比率。

例如，`"I am glad!"` 这个字符串包含三个单词和十个字符（不包括引号）。每分钟的字数计算使用 2 作为输入的字数（因为 10 / 5 = 2 ）。如果有人在 30 秒（半分钟）内打完这个字符串，他们的速度将是每分钟 4 个字。

在编写任何代码之前，请解锁测试以验证你对问题的理解：

```
python3 ok -q 04 -u
```

一旦你完成了解锁，就开始实施你的解决方案。你可以用以下方法检查你解决方案的正确性：

```
python3 ok -q 04
```

**是时候测试一下你的打字速度了！**你可以使用命令行来测试你在关于某个特定主题的段落上的打字速度。例如，下面的命令将加载关于猫或小猫的段落。如果你感到好奇，请看 `run_typing_test` 函数的实现（但它是为你定义的）。

```
python3 cats.py -t cats kittens
```

你可以使用以下命令试用基于网络的图形用户界面（GUI）。（你可能需要在你的终端上使用 `Ctrl+C` 或 `Cmd+C` ，在你关闭浏览器的标签后退出 GUI）。

```
python3 cats_gui.py
```

**要提交你的第一阶段检查点** 运行以下命令：

```
python3 ok --submit
```

你可以在完成整个项目后再次提交，我们将只对你最近的提交进行评分，但请在检查点截止日期前至少提交一次（至少完成第一阶段的问题后），以获得检查点的分数。

👩🏽‍💻👨🏿‍💻 [结对编程？](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/pair-programming) 这将是一个转换角色的好时机。交换角色可以确保你们都能从在每个角色中的学习经历中受益。

# Phase 2: Autocorrect

> 过去，当学生在没有彻底阅读问题描述的情况下试图实现这些功能时，他们经常会遇到问题。😱 **在开始编码之前，请彻底阅读每个描述。**

在基于网络的 GUI 中，有一个自动更正按钮，但现在它没有任何作用。让我们来实现对错字的自动纠正。每当用户按下空格键时，如果他们输入的最后一个词与字典中的一个词不匹配，但与之接近，那么这个类似的词将被替换。

## Problem 5 (2 pts)

实现 `autocorrect` ，它需要一个 `typed_word` 、一个 `word_list` 、一个 `diff_function` 和一个 `limit` 。

如果 `typed_word` 包含在 `word_list` 中，那么 `autocorrect` 将返回该单词。

*否则* ， `autocorrect` 会基于 `diff_function` 从 `word_list` 中返回与所提供的 `typed_word` 有最低差异的单词。然而，如果 `typed_word` 和 `word_list` 中任何一个词的最低差值大于 `limit` ，那么就会返回 `typed_word` 。

> **重要提示：** 如果 `typed_word` 不包含在 `word_list` 中，并且根据 `diff_function` ，多个字符串与 `typed_word` 有相同的最低差异，那么 `autocorrect` 应该返回在 `word_list` 中出现的第一个字符串。

一个 diff 函数接收三个参数。前两个参数是要比较的两个字符串（ `typed_word` 和 `word_list` 中的一个词），第三个参数是 `limit` 。diff 函数的输出是一个数字，代表两个字符串之间的差异量。

下面是一个 diff 函数的例子，它计算了 `1 + limit` 和两个输入字符串之间的长度差的最小值：

```py
>>> def length_diff(w1, w2, limit):
...     return min(limit + 1, abs(len(w2) - len(w1)))
>>> length_diff('mellow', 'cello', 10)
1
>>> length_diff('hippo', 'hippopotamus', 5)
6
```

假设 `typed_word` 和 `word_list` 的所有元素都是小写的，没有标点符号。

> **提示：** 尝试使用 `max` 或 `min` 与可选的 `key` 参数。关于使用这个参数的一些例子，请查看 2 月 16 日星期三的讲课幻灯片。

在编写任何代码之前，请解锁测试以验证你对问题的理解：

```
python3 ok -q 05 -u
```

一旦你完成了解锁，就开始实施你的解决方案。你可以用以下方法检查你解决方案的正确性：

```
python3 ok -q 05
```

## Problem 6 (3 pts)

实现 `sphinx_swaps` ，它是一个接受两个字符串的 diff 函数。它返回在 `start` 词中必须改变的最小字符数，以便将其转化为 `goal` 词。如果两个字符串的长度不相等，则长度的差异将被添加到总数中。

> **重要提示：** 你不能在你的实现中使用 `while` 、 `for` 或 `list` 语法。使用递归。

这里有一些例子：

```py
>>> big_limit = 10
>>> sphinx_swaps("nice", "rice", big_limit)    # Substitute: n -> r
1
>>> sphinx_swaps("range", "rungs", big_limit)  # Substitute: a -> u, e -> s
2
>>> sphinx_swaps("pill", "pillage", big_limit) # Don't substitute anything, length difference of 3.
3
>>> sphinx_swaps("roses", "arose", big_limit)  # Substitute: r -> a, o -> r, s -> o, e -> s, s -> e
5
>>> sphinx_swaps("rose", "hello", big_limit)   # Substitute: r->h, o->e, s->l, e->l, length difference of 1.
5
```

> **重要提示：** 如果必须改变的字符数大于 `limit` ，那么 `sphinx_swaps` 应该返回大于 `limit` 的任何数字，并且应该尽量减少这样做所需的计算量。
>
> 这两个对 `sphinx_swaps` 的调用应该花费差不多的时间：
>
> ```py
> >>> limit = 4
> >>> sphinx_swaps("roses", "arose", limit) > limit
> True
> >>> sphinx_swaps("rosesabcdefghijklm", "arosenopqrstuvwxyz", limit) > limit
> True
> ```

在编写任何代码之前，解开测试，以验证你对问题的理解：

```
python3 ok -q 06 -u
```

一旦你完成了解锁，就开始实施你的解决方案。你可以用以下方法检查你解决方案的正确性：

```
python3 ok -q 06
```

试着在 GUI 中打开自动更正功能。它是否能帮助你更快地打字？纠正的结果是否准确？你应该注意到，在一个词的开头附近插入一个字母或漏掉一个字母，这个差异功能处理得不好。让我们来解决这个问题！

## Problem 7 (3 pts)

实现 `minimum_mewtations` ，这是一个 diff 函数，返回将 `start` 词转化为 `goal` 词所需的最小编辑操作数。

有三种编辑操作，有一些例子：

1. 在 `start` 里添加一个字母。
    - 在 `"itten"` 上加上 `"k"` ，就得到了 `"kitten"` 。
2. 从 `start` 中删除一个字母。
    - 从 `"scat"` 中去掉 `"s"` ，就得到了 `"cat"` 。
3. 用一个字母代替 `start` 的另一个字母。
    - 将 `"zaguar"` 中的 `"z"` 替换成 `"j"` ，得到 `"jaguar"` 。

每个编辑操作对两个词之间的差异有 1 的贡献。

```py
>>> big_limit = 10
>>> minimum_mewtations("cats", "scat", big_limit)       # cats -> scats -> scat
2
>>> minimum_mewtations("purng", "purring", big_limit)   # purng -> purrng -> purring
2
>>> minimum_mewtations("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
3
```

我们在 `cats.py` 中提供了一个实现的模板。

> **提示：** 这是一个有三个递归调用的递归函数。其中一个递归调用将类似于 `sphinx_swaps` 中的递归调用。

你可以随心所欲地修改模板或完全删除它。

> **重要提示：** 如果需要的编辑数量大于 `limit` ，那么 `minimum_mewtations` 应该返回大于 `limit` 的任何数字，并且应该尽量减少所需的计算量。
>
> 这两个对 `minimum_mewtations` 的调用应该花费差不多的时间：
>
> ```py
> >>> limit = 2
> >>> minimum_mewtations("ckiteus", "kittens", limit) > limit
> True
> >>> minimum_mewtations("ckiteusabcdefghijklm", "kittensnopqrstuvwxyz", limit) > limit
> True
> ```

在编写任何代码之前，解开测试，以验证你对问题的理解：

```
python3 ok -q 07 -u
```

一旦你完成了解锁，就开始实施你的解决方案。你可以用以下方法检查你解决方案的正确性：

```
python3 ok -q 07
```

再试着打一遍。纠正的结果是否更准确？

```
python3 cats_gui.py
```

👩🏽‍💻👨🏿‍💻 [结对编程？](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/pair-programming) 庆祝一下，休息一下，然后转换一下角色。

## (Optional) Extension: final diff (0pt)

你可以选择设计你自己的 diff 函数，称为 `final_diff` 。这里有一些做出更精确修正的想法：

- 考虑到哪些添加和删除的可能性比其他的更大。例如，如果一个字母连续出现两次，你就更有可能不小心漏掉它。
- 将两个相邻的字母互换位置视为一个变化，而不是两个。
- 尽量把常见的拼写错误纳入其中。

你也可以通过改变 `cats.py` 中的变量 `FINAL_DIFF_LIMIT` 的值来设置你希望你的 diff 函数使用的限制。

你可以通过运行以下命令来检查你的 `final_diff` 的成功率。

```
python3 score.py
```

如果你不知道从哪里开始，可以试着把你的 `sphinx_swaps` 和 `minimum_mewtations` 的代码复制到 `final_diff` 中，然后给它们评分。看看他们不小心修正的错别字，也许能给你一些启发！

# Phase 3: Multiplayer

> 过去，当学生在没有彻底阅读问题描述的情况下试图实现这些功能时，他们经常会遇到问题。😱 **在开始编码之前，请彻底阅读每一个描述。**

和朋友一起打字更有趣！你现在要实现多人游戏功能，这样当你在电脑上运行 `cats_gui.py` 时，它就会连接到 [cats.cs61a.org](https://cats.cs61a.org/) 的课程服务器，并寻找其他人来比赛。

为了和朋友比赛，将有 5 个不同的程序在运行：

- 你的 GUI ，它是一个处理所有文本着色和在你的网络浏览器中显示的程序。
- 你的 `cats_gui.py` ，它是一个网络服务器，使用你在 `cats.py` 中写的代码与你的 GUI 进行通信。
- 你的对手的 `cats_gui.py` 。
- 你的对手的 GUI 。
- CS 61A 的多人游戏服务器，它将玩家匹配在一起并传递信息。

当你打字时，你的 GUI 将你所打的字上传到你的 `cats_gui.py` 服务器，它计算你所取得的进展并返回一个进度更新。它还将进度更新上传到多人游戏服务器，以便你的对手的 GUI 可以显示它。

同时，你的 GUI 显示总是试图通过向 `cats_gui.py` 请求进度更新来保持最新，而 `cats_gui.py` 又从多人游戏服务器上请求该信息。

每个玩家都有一个 `id` 号码，服务器用它来跟踪打字的进度。

## Problem 8 (2 pts)

实现 `report_progress` ，每当用户打完一个单词时就会调用它。它需要一个 `sofar` 的单词列表，一个 `prompt` 中的单词列表，用户的 `user_id` ，以及一个 `upload` 函数，用来上传进度报告到多人游戏服务器。 `sofar` 中的单词永远不会多于 `prompt` 中的单词。

你的进度是你在 `prompt` 中正确输入的单词的比率，直到第一个错误的单词为止，除以 `prompt` 单词的数量。例如，这个例子的进度是 `0.25` ：

```
report_progress(["Hello", "ths", "is"], ["Hello", "this", "is", "wrong"], ...)
```

你的 `report_progress` 函数应该做两件事：向多人游戏服务器上传一条消息，并返回带有 `user_id` 的玩家的进度。

你可以通过对一个包含键 `'id'` 和 `'progress'` 的双元素字典调用 `upload` 函数来向多人游戏服务器上传一条消息。然后你应该返回玩家的进度，也就是你计算出来的比例。

> **提示：** 请看下面的字典，它是一个可能输入到 `upload` 函数的例子。这个字典代表一个 `user_id` 为 1 ， `progress` 为 0.6 的玩家。
>
> `{'id': 1, 'progress': 0.6}`

在编写任何代码之前，请解锁测试以验证你对问题的理解：

```
python3 ok -q 08 -u
```

一旦你完成了解锁，就开始实施你的解决方案。你可以用以下方法检查你解决方案的正确性：

```
python3 ok -q 08
```

## Problem 9 (2 pts)

实现 `time_per_word` ，它接收一个列表 `words` 和 `times_per_player` ，这是一个每个玩家的列表，其中的时间戳表明每个玩家在 `words` 中完成每个单独单词的时间。它返回一个具有给定信息的 `match` 。

`match` 是一个存储 `words` 和 `times` 的字典。 `times` 被存储为每个玩家打完每一个单词的 `words` 列表，花了多长时间。具体来说， `times[i][j]` 表示玩家 `i` 花了多长时间输入 `words[j]` 。

例如，假设 `words = ['Hello', 'world']` ， `times = [[5, 1], [4, 2]]` ，那么 `[5, 1]` 对应于玩家 0 的次数列表，而 `[4, 2]` 对应于玩家 1 的次数列表。因此，玩家 0 花了 5 个单位的时间来写 `'Hello'` 这个词。

> **重要提示：** 当返回一个 `match` 时，一定要使用 `match` 构造函数。测试将检查你是否使用了 `match` 字典，而不是假设一个特定的数据格式。
>
> 阅读 `cats.py` 中 `match` 构造函数的定义，了解更多关于字典的实现方式。

时间戳是累积的，并且总是增加的，而 `times` 的值是 **每个玩家的连续时间戳之间的差异** 。

这里有一个例子。如果 `times_per_player = [[1, 3, 5], [2, 5, 6]]` ， `match` 的相应 `times` 属性将是 `[[2,2], [3, 1]]` 。这是因为第一个选手的时间戳差异是 `(3-1)` 、 `(5-3)` ，第二个选手的时间戳差异是 `(5-2)` 、 `(6-5)` 。 `times_per_player` 内每个列表的第一个值代表每个玩家的初始开始时间。

在编写任何代码之前，请解锁测试以验证你对问题的理解：

```
python3 ok -q 09 -u
```

一旦你完成了解锁，就开始实施你的解决方案。你可以用以下方法检查你解决方案的正确性：

```
python3 ok -q 09
```

👩🏽‍💻👨🏿‍💻 [结对编程？](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/pair-programming) 我们建议现在就转换角色，如果你最近没有的话。几乎完成了！

## Problem 10 (2 pts)

实现 `fastest_words` ，返回每个玩家打的最快的单词。一旦双方打完字，就调用这个函数。它接收了一个 `match` 。

具体来说， `fastest_words` 函数返回一个单词列表，每个玩家有一个列表，在每个列表中，他们输入的单词是最快的（针对所有其他玩家）。在平局的情况下，认为列表中最早的选手（最小的选手索引）是打得最快的选手。

例如，考虑下面的比赛，有“Just”，“have”和“fun”这几个词。玩家 0 输入“fun”最快（3秒），玩家 1 输入“Just”最快（4秒），他们在“have”这个词上打成平手（都花了 1 秒），所以我们认为玩家 0 是最快的，因为他们是列表中最早的玩家。

```py
>>> player_0 = [5, 1, 3]
>>> player_1 = [4, 1, 6]
>>> fastest_words(match(['Just', 'have', 'fun'], [player_0, player_1]))
[['have', 'fun'], ['Just']]
```

`match` 参数是一个 `match` 字典，就像问题 9 中返回的那个。你可以用选择器 `word_at` 来访问 `match` 中的词，它接收一个 `match` 和 `word_index` （一个整数）。通过 `word_at` ，你可以使用时间访问任何玩家输入任何单词所需的 `time` 。

> **重要提示：** 当返回一个 `match` 时，请确保使用 `match` 构造函数。测试将检查你是否使用了 `match` 字典，而不是假设一个特定的数据格式。
>
> 确保你的实现不会突变给定的玩家输入列表。对于上面的例子，在 `[player_0, player_1]` 上调用 `fastest_words` 应该 **不会** 使 `player_0` 或 `player_1` 发生变化。

在编写任何代码之前，请解开测试以验证你对问题的理解：

```
python3 ok -q 10 -u
```

一旦你完成了解锁，就开始实施你的解决方案。你可以用以下方法检查你解决方案的正确性：

```
python3 ok -q 10
```

祝贺你！现在你可以和课程中的其他学生比赛了。在 `cats.py` 的底部附近将 `enable_multiplayer` 设置为 `True` ，然后迅速输入！

```
python3 cats_gui.py
```

这时，运行整个自动测试器，看看是否有任何测试没有通过。

```
python3 ok
```

满意后，提交 Ok ，完成项目。

```
python3 ok --submit
```

如果你有伙伴，请确保将他们加入到 [okpy](https://okpy.org/) 的提交中。

通过运行检查以确保你做了所有的问题：

```
python3 ok --score
```