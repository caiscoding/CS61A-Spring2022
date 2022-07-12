# Optional Contest: Scheme Art

*输出是艺术。*

*但它的源代码呢？*

*它同样是抽象的。*

## 说明

> 这个比赛是完全可以选择的！

参赛作品的截止时间是 **4 月 27 日（星期三）晚上 11:59** 。

以下是参加比赛的步骤：

1. 下载 [scheme_contest.zip](https://inst.eecs.berkeley.edu/~cs61a/sp22/proj/scheme_contest/scheme_contest.zip) 。
2. 从 [这个链接](https://inst.eecs.berkeley.edu/~cs61a/sp22/assets/interpreter/abstract_turtle.zip) 下载 `abstract_turtle.zip` 文件。然后，将该文件解压到你的 `scheme_contest` 目录中。解压后的文件夹应该包含 `canvas.py` 和 `color_names.py` 等文件。另外，如果你喜欢用 `pip` 命令来安装，你可以运行 `pip3 install abstract-turtle` ，而不是下载这个 zip 文件。
3. 完成 `contest.scm` 文件（你可以用 `python3 scheme contest.scm --pillow-turtle --turtle-save-path output` 输出来渲染你的绘图）。关于绘图程序的描述，请参见 [Scheme 内置参考资料中的图形](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/scheme-builtins/#turtle-graphics) 。
    - 如果这个命令不起作用，可以尝试运行 `python3 scheme contest.scm --turtle-save-path output` 来代替。主要的区别是这个命令使用的是 `tkinter` 库，而前一个命令使用的是 `pillow` 库。两者应该产生相同的输出。
4. 上传由前一个命令创建的 `output.png` 。

在 `contest.scm` 中， `draw` 程序应该绘制你的作品，然后在点击时退出。

所有参赛作品，包括它们的源代码，都将分发给你的同学进行投票。 **请不要在你提交的作品中包含个人信息。**

在这次比赛中，你可以和另外一个伙伴一起工作。你应该在 Ok 上添加你的伙伴，并进行一次提交。


> **重要提示：** 当你准备提交时， **请遵循以下两个步骤** ：
>
> - 运行 `python3 ok --submit` 将你的 `contest.scm` 文件提交给 Ok 。
> - 填写 [竞赛表格](http://go.cs61a.org/scheme-contest) 。确保这里的信息是正确的，因为我们将用它来生成你在 Scheme 艺术画廊的作品。
>
> **故障排除：** 当你试图渲染你的作品时，你是否遇到了错误 `name 'builtins' is not defined` ？如果是，请在 `scheme_builtins.py` 的顶部添加以下一行： `import builtins` 。当你试图渲染你的图片时，你可能还会被要求安装一些依赖项，如果你这样做了，它应该能正确地创建你的可视化。如果你没有看到这个错误（通常是对部分 Windows 用户弹出），你不需要添加额外的导入。

## 比赛描述

使用海龟图形创建一个你选择的迭代或递归过程的可视化。你的实现必须完全用 Scheme 编写，并使用你所建立的解释器。所有的计算都必须在 Scheme 中完成。

我们将有两类参赛作品：

- *轻量级：* 少于 512 个Scheme tokens（包括括号）。
- *重量级：* 少于 4096 个Scheme tokens（包括括号）。

**任何一个 token 都不得包含超过 50 个字符。** 如果您的作品需要比重量级类别所允许的更多代价，请联系课程工作人员，以获得提交更长作品的特别许可。 **较长的作品，如果得到批准，将在画廊中展示，但没有资格在艺术竞赛中获得额外分数。**

额外分数将按以下方式授予：

- 每个类别的第一名得 3 分
- 每个类别的第二名得 2 分
- 每个类别的第三名得 1 分

你可以通过运行以下命令来检查名为 `contest.scm` 的 Scheme 文件中的代价数量：

```py
python3 scheme_tokens.py contest.scm
```

参赛作品（代码和图片）将被张贴在网上，获奖者将由大众投票选出。投票结束后，每个类别的前三名作品将在 Piazza 上公布。

为了提高你的成功机会，我们欢迎你在作品的评论中加入标题和描述性的 [俳句](http://en.wikipedia.org/wiki/Haiku) ，这将包括在投票中。

## 比赛规则

在提交之前，请确保你的作品遵守这些准则：

- 参赛作品不得包含超过 50 个字符的代价，并且必须在正确的类别（羽量级/重量级）下提交。
- 参赛作品不得包含任何政治内容。
- 参赛作品不得包含任何攻击性、性暗示或道德上令人反感的内容。
- 参赛作品不得包含任何个人信息。
- 参赛作品必须符合你的代码。也就是说，你提交的 Scheme 代码必须能够准确地生成你提交的输出图形文件。
- 参赛作品必须是静态图像（没有动画）。我们鼓励你自己尝试制作动画，但你不能为本次比赛提交动画作品。

我们保留取消任何不遵守这些准则的作品的资格的权利。

## 过去的参赛作品

为了获得灵感，你可以浏览一下这些过去的参赛作品的画廊。请注意，某些作品可能不符合当前的准则。

- [Fall 2021](http://inst.eecs.berkeley.edu/~cs61a/fa21/proj/scheme_gallery/)
- [Summer 2021](http://inst.eecs.berkeley.edu/~cs61a/su21/proj/scheme_gallery/)
- [Spring 2021](http://inst.eecs.berkeley.edu/~cs61a/sp21/proj/scheme_gallery/)
- [Fall 2020](http://inst.eecs.berkeley.edu/~cs61a/fa20/proj/scheme_gallery/)
- [Summer 2020](http://inst.eecs.berkeley.edu/~cs61a/su20/proj/scheme_gallery/)
- [Spring 2020](http://inst.eecs.berkeley.edu/~cs61a/sp20/proj/scheme_gallery/)
- [Fall 2019](http://inst.eecs.berkeley.edu/~cs61a/fa19/proj/scheme_gallery/)
- [Summer 2019](http://inst.eecs.berkeley.edu/~cs61a/su19/proj/scheme_gallery/)
- [Spring 2019](http://inst.eecs.berkeley.edu/~cs61a/sp19/proj/scheme_gallery/)
- [Fall 2018](http://inst.eecs.berkeley.edu/~cs61a/fa18/proj/scheme_gallery/)
- [Summer 2018](http://inst.eecs.berkeley.edu/~cs61a/su18/proj/scheme_gallery/)
- [Spring 2018](http://inst.eecs.berkeley.edu/~cs61a/sp18/proj/scheme_gallery/)
- [Fall 2017](http://inst.eecs.berkeley.edu/~cs61a/fa17/proj/scheme_gallery/)
- [Summer 2017](http://inst.eecs.berkeley.edu/~cs61a/su17/proj/scheme_gallery/)
- [Spring 2017](http://inst.eecs.berkeley.edu/~cs61a/sp17/proj/scheme_gallery/)
- [Fall 2016](http://inst.eecs.berkeley.edu/~cs61a/fa16/proj/scheme_gallery/)
- [Summer 2016](http://inst.eecs.berkeley.edu/~cs61a/su16/proj/scheme_gallery/)
- [Spring 2016](http://inst.eecs.berkeley.edu/~cs61a/sp16/proj/scheme_gallery/)
- [Fall 2015](http://inst.eecs.berkeley.edu/~cs61a/fa15/proj/scheme_gallery/)
- [Spring 2015](http://inst.eecs.berkeley.edu/~cs61a/sp15/proj/scheme-gallery/)
- [Fall 2014](http://inst.eecs.berkeley.edu/~cs61a/fa14/proj/scheme_gallery/)
- [Spring 2014](http://inst.eecs.berkeley.edu/~cs61a/sp14/proj/scheme_contest/scheme_contest.html)
- [Fall 2013](http://inst.eecs.berkeley.edu/~cs61a/fa13/proj/scheme_contest_gallery/scheme_contest_gallery.html)
- [Spring 2013](http://inst.eecs.berkeley.edu/~cs61a/sp13/projects/scheme_contest_gallery/scheme_contest.html)
- [Fall 2012](http://inst.eecs.berkeley.edu/~cs61a/fa12/projects/scheme_contest.html)