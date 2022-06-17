# Lab 0: Getting Started

## 起始文件

下载 [lab00.zip](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab00/lab00.zip) 。在该压缩包中，你将找到本实验中问题的启动文件，以及 [Ok](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab00/ok) 自动评分的副本。

## 说明

本实验解释了如何使用自己的计算机来完成 CS 61A 的作业，并介绍了 Python 的一些基础知识。

如果你在任何实验需要帮助，请随时在 [办公时间](https://inst.eecs.berkeley.edu/~cs61a/sp22/office-hours) 需求帮助或在 [Piazza](https://piazza.com/berkeley/fall2021/cs61a) 上发帖。

这个实验看起来很长，但它主要是入门介绍和学习如何使用这门课的基本工具；这些现在看来可能有点困难，但随着我们进一步学习课程，学习起来很快就会变得很自然。

## 开始

### 安装一个终端

终端是一个允许你通过输入命令与电脑交互的程序。无论你使用什么操作系统（Windows、macOS、Linux），终端都将是 CS 61A 的一个重要工具。

### macOS/Linux

如果你用的是 Mac 或使用某种形式的 Linux （如 Ubuntu ），你的电脑上已经有一个叫做终端或类似的程序。打开它，就可以了。

### Windows

在 Windows 上获得终端的最简单方法（在撰写本文时）是使用 Windows Subsystem for Linux ，或 WSL 。这可以通过终端程序 Ubuntu 访问，它可以在你的 Windows 电脑上模拟 Ubuntu 操作系统。这使我们的大部分作业能在你的设备上顺利进行。

要为 Windows 安装 Ubuntu ，点击开始并搜索 PowerShell 。右键单击并选择“以管理员身份运行”。然后，在 PowerShell 窗口中，输入 `wsl --install` 并按回车键。该命令必须按照这个顺序输入。这应该会自动完成设置过程（按照屏幕上可能给你的任何指示操作）。

下一步，从 Windows 商店下载 Ubuntu 。

一旦安装完成，在你的开始菜单中搜索 Ubuntu 。第一次启动可能需要几分钟，但随后的启动应该会很快。

## 安装 Python 3

Python 3 是本课程中使用的主要编程语言。使用下面的说明来安装Python 3。（这些说明可能是旧版本的 Python 3 ，但步骤是相似的。）

**重要提示：** 如果你已经安装了旧版本的 Python ，请确保下载并安装 Python 3.9 。你可以用 `python3 --version` 检查你的 Python 版本。

### macOS

下载并安装 [Python 3（64位）](https://www.python.org/ftp/python/3.9.6/python-3.9.6-macosx10.9.pkg) 。你可能需要右击下载图标并选择“打开”。安装完毕后，请关闭并重新打开你的终端。

如果你安装了 Homebrew ，你也可以通过运行 `brew install python3` 来安装 Python 3 。

### Windows

在 Ubuntu 中输入 `sudo apt install python3` ，然后点击回车键来安装 Python 。一旦安装完成，你可以通过输入 `python3 --version` 来测试它是否安装成功。你应该看到一个响应信息，显示你的 python 3 版本： `Python 3.9.6` 。

### Linux

运行 `sudo apt install python3` （Ubuntu）， `sudo pacman -S python3` （Arch），或你的发行版命令。

### Other

[从下载页面下载 Python](https://www.python.org/downloads/) 。

## 安装一个文本编辑器

你刚刚安装的 **Python 解释器** 允许你运行 Python 代码。你还需要一个 **文本编辑器** ，你将在那里编写 Python 代码。

[Visual Studio Code （VS Code）](https://code.visualstudio.com/) 是本课程工作人员中最受欢迎的选择，用于编写 Python 。下面也列举了一些在工作人员中使用的其他编辑器。

如果你使用 Windows 并遵循我们的 Python 设置过程， VS Code 对你来说是最好的（因为它有 WSL 支持）。在安装 VS Code 之后，安装 [远程开发扩展包](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) 。然后，你可以使用 VS Code 文档中 [这一部分](https://code.visualstudio.com/docs/remote/wsl#_open-a-remote-folder-or-workspace) 的说明，在 VS Code 中打开 WSL 文件夹。

我们强烈建议使用 VS Code 来学习这门课。这将有助于我们为你提供最好的支持，因为大多数员工也使用 VS Code 。

> **警告：** 请，请，请不要使用文字处理软件，例如 Microsoft Word 来编辑程序。文字处理程序可以在文件中添加额外的内容，会使解释器感到困惑。

为了供你参考，我们还写了一些关于使用流行文本编辑器的指南。在你做完实验后，如果你有兴趣，可以看一看。

- [Visual Studio Code](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/vscode) ：一个全功能的桌面编辑器，有很多扩展功能，可以支持不同的语言。
- [Atom](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/atom)：一个更轻便的桌面编辑器。
- [Vim](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/vim)：一个命令行编辑器。
- [Emacs](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/emacs)：一个命令行编辑器。

其他几个编辑器：

- [PyCharm](https://www.jetbrains.com/pycharm/)：一个为 Python 设计的桌面编辑器。
- [Sublime Text](https://www.sublimetext.com/)：一个可以处理代码的文本编辑器。

## 结对编程

在整个课程中，你将有很多机会在实验和项目中与他人合作编码。我们建议你现在就下载这些扩展程序，以便在将来使用。

对于分享代码，你可以按照你所选择的编辑器进行：

- [VS Code](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/vscode#pair-programming)
- [Atom](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/atom#pair-programming)

## 备份设置

如果你在安装 Python 解释器、文本编辑器和终端时遇到麻烦，或者你使用的东西不允许你安装软件，如 iPad ，你可以作为临时措施，在你获得更合适的硬件时，使用下面的一些步骤完成作业。

### Soda 实验室电脑

你将需要一个教学账户，这将允许你登录和使用 Soda 实验室计算机。你可以查看你现有的教学账户，也可以为适用的课程建立新的教学账户，请访问：[https://inst.eecs.berkeley.edu/connecting.html](https://inst.eecs.berkeley.edu/connecting.html) 。

你可以通过你的 CalNet ID 登录到该网站。要为这门课程建立一个教学账户，请点击以“cs61a”为目的的那一行的“获得一个新账户”。

一旦你建立了帐户，你就可以用它来登录到 Soda 实验室的计算机，并使用该计算机进行课程作业。

### 作为备份的在线编辑

> **重要提示：** 下面列出的两种替代品都不适合在本课程中使用。我们建议能够使用你自己的本地设置或使用 Soda 实验室计算机（你可以用你的课程教学账户访问）。

**61A Code:**

你可以使用 [61A 代码](https://code.cs61a.org/) ，这个课程的在线环境，你可以在这里编辑、运行、调试、可视化，并与工作人员分享程序。61A 代码的文档可以在这里找到：[61A 代码文档](https://cs61a.org/articles/61a-code-docs/) 。

> **注意：** 你将不能在 61A 代码中运行 ok 命令，你需要做的是解锁测试、运行测试和提交作业。

完成 61A 代码这一任务的步骤：

1. 访问 [61A 代码](https://code.cs61a.org/) 。
2. 打开现有文件：进入你的 cs61a 文件夹，然后是作业文件夹（lab00），在其中你可以找到这个作业的文件。
3. 你会被提示授权给编辑器。你可以点击 "确认"。回到编辑器本身，然后你可以打开你想编辑的文件。
4. 要打开终端，点击“控制台”。
5. 你可以用编辑器来写你的代码，用控制台来运行你的代码。

**Datahub:**

在本地工作的另一个选择是使用加州大学伯克利分校的 Datahub 。

在 [Datahub](https://datahub.berkeley.edu/) 上完成这项任务的步骤：

1. 访问 Datahub 。
2. 将作业的压缩文件上传到 Datahub 。
3. 按左上角的“新建”并选择终端，打开一个终端。
4. 导航到压缩文件所在的位置，运行 `unzip lab00.zip` 。
5. 打开代码文件（`lab00.py`），输入代码，然后保存。
6. 现在你可以提交这个实验了。

## 使用终端

让我们检查一下所有的东西是否都安装好了！

首先，打开一个终端窗口。

![](./images/terminal.png)

当你第一次打开你的终端时，你将位于“主目录”中。 **主目录** 由 `~` 符号表示，你可能会在提示符下看到这个符号。

> 如果你的终端窗口看起来不完全一样也不用担心。重要的是，提示符显示 `$` （表示Bash）或 `%` （表示zsh）。

尝试运行 `echo "$HOME"` 。该命令应该显示你的主目录的完整路径。它应该看起来像这样：

`/Users/OskiBear`

路径就像一个地址：它告诉你和计算机通往某个文件夹的完整路径（或路线）。请记住，你可以通过两种不同的方式访问计算机上的文件和目录（文件夹）。你可以使用终端（这是一个命令行界面又称 CLI ），或者你可以使用 Finder （在Mac上）或资源管理器（在Windows上）。Finder 和资源管理器都是图形用户界面（又称 GUI ）的一个例子。导航的技术是不同的，但文件是相同的。例如，下面是我的 cs61a 实验文件夹在我的 GUI 中的样子。

![](./images/finder-path-example.png)

下面是完全相同的文件夹在终端中的样子：

![](./images/terminal-path-example.png)

请注意，在这两种情况下，黄色方框显示的是路径，紫色椭圆显示的是 “实验”文件夹的内容。

**Python 解释器**

我们可以用终端来检查你的 Python 3 解释器是否安装正确。试试下面的命令：

```
python3
```

如果安装成功，你应该看到一些关于解释器的信息被打印出来，后面是 `>>>` 。这就是你可以输入 Python 代码的地方。试着输入你在课堂上看到的一些表达式，或者只是玩玩看会发生什么 你可以输入 `exit()` 或 `Ctrl-D` 来返回你的命令行。

> 如果你遇到困难被卡住了，可以寻求帮助！

## 终端 vs Python 解释器

让我们暂停一下，想想终端和 Python 解释器之间的区别。

![](./images/terminal-vs-interpreter.png)

1. 在A、B、C和D中，哪个是“终端”？
2. 哪一个是 Python 解释器？
3. 哪一个是我的代码编辑器？
4. 你又是如何分辨的呢？

A 和 D 都是我的终端。在这里你可以运行 `cd` 和 `ls` 等 bash 命令。D 是 VS Code 内置的终端。

B 是 Python 解释器。你可以从 >>> 的提示中看出，这意味着你已经启动了一个 Python 解释器。你还可以知道，启动它的命令是可见的： `python3` 。 `python3` 命令启动了一个 Python 解释器。如果你在 python 解释器中输入一条 bash 命令，你可能会得到一个语法错误。下面是一个例子：

![](./images/interpreter-syntax-error.png)

如果你需要退出 Python 解释器，只需输入 `exit()`

C 是我的代码编辑器。在这里，我可以写 Python 代码，通过我的终端执行。

## 组织你的文件

在本节中，你将学习如何使用终端命令来管理文件。

> 确保你的提示符在某处包含一个 `$` ，并且不是以 `>>>` 开始。如果它以 `>>>` 开头，你仍然在一个 Python shell 中，你需要退出。具体方法见上文。

### 目录

你要使用的第一个命令是 `ls` 。试着在你的终端输入它。

```
ls
```

`ls` 命令列出了当前目录下的所有文件和文件夹。 **目录** 是一个文件夹的另一个名称（如 `Documents` 文件夹）。

#### macOS/Linux

由于你现在是在主目录中，在你输入 `ls` 后，你应该看到你的主目录的内容。

#### Windows

在 Ubuntu 中，当你输入 `ls` 时，你不会看到 `~` 中的任何文件。相反，你首先需要改变目录（见下文）。

### 改变目录

要移动到另一个目录，使用 `cd` 命令（改变目录）。

#### macOS/Linux

让我们试着移动到你的 `桌面` 目录。首先，确保你在你的主目录中（检查你的命令行上的 `~` ），并使用 `ls` 来查看 `桌面` 目录是否存在。

尝试在你的终端输入以下命令，这应该会使你进入该目录。

```
cd Desktop
```

如果你还没有进入你的主目录，试试 `cd ~/Desktop` 。这就是告诉终端你想去的路径位置。

#### Windows

在 Windows 上，首先进入你的主目录。

```
cd /mnt/c/Users/
```

现在试试前面的 `ls` 命令。你应该看到有几个文件夹。这些文件夹中的一个应该与你的用户名相符。例如，假设你的用户名是 `OskiBear` ，你应该看到一个名为 `OskiBear` 的文件夹。（注意，你的 Windows 用户名可能与你的 Ubuntu 用户名不同）让我们换到那个文件夹。

```
cd /mnt/c/Users/OskiBear/Desktop
```

如果你仍然找不到你的桌面目录，请在 Piazza 上或在办公时间寻求帮助。

### 创建新目录

下一个命令叫做 `mkdir` ，它可以建立一个新的目录。让我们在你的桌面目录中建立一个名为 `cs61a` 的目录，以存储本课的所有作业。

```
mkdir cs61a
```

一个名为 `cs61a` 的文件夹将出现在你的桌面上。你可以通过再次使用 `ls` 命令或使用资源管理器（Windows）或 Finder （Mac）检查你的桌面来验证这一点。

在这一点上，让我们再创建一些目录。首先，确保你在 `cs61a` 目录下（Mac：`~/Desktop/cs61a`，Windows：`/mnt/c/Users/Desktop/cs61a`）。然后，创建两个新的文件夹，一个叫 `projects` ，另一个叫 `lab` 。这两个文件夹都应该在你的 `cs61a` 文件夹中。

#### macOS/Linux

```
cd ~/Desktop/cs61a
mkdir projects
mkdir lab
```

#### Windows

```
cd /mnt/c/Users/OskiBear/Desktop/cs61a
mkdir projects
mkdir lab
```

现在，如果你列出该目录的内容（使用 `ls` ），你会看到两个文件夹， `projects` 和 `lab` 。

![](./images/terminal_commands.png)

### 更多目录变化

有几种方法可以返回到主目录：

- `cd ..`（两个点）。`..` 的意思是“父目录”，或比你的当前目录高一个目录。
- `cd ~` （斜体字）。记住，`~` 意味着主目录，所以这个命令将总是改变到你的主目录。
- `cd` （只是输入 `cd` ），只输入 `cd` 是输入 `cd ~` 的一个快捷方式。

> 如果你不愿意，你不一定要把文件放在你的桌面上。你在本地保存文件不会影响你的成绩。做任何对你来说最简单和最方便的事情吧！

### 下载作业

如果你还没有下载，请下载压缩文件 [lab00.zip](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab00/lab00.zip) ，它包含了你在这个实验中需要的所有文件。一旦你完成了下载，让我们找到下载的文件。在大多数计算机上，`lab00.zip` 可能位于你的主目录下一个叫做 `下载` 的目录中。使用 `ls` 命令来检查。

```
ls ~/Downloads
```

如果你没有看到 `lab00.zip` ，请在 Piazza 或办公时间寻求帮助。在某些版本的 Safari 浏览器中，该文件可能会被解压缩，在这种情况下，你只会看到一个名为 `lab00` 的新目录。

### 提取启动文件

在处理实验文件之前，你必须解压缩文件。不同的操作系统和不同的浏览器有不同的解压方式。在 Mac 中点击 .zip 文件会自动解压。在 Windows 中，你需要先点击 .zip 文件，然后选择“全部提取”。如果你遇到了麻烦，你可以在网上搜索如何解压缩文件。

这里有一个使用终端解压的方法：

> 使用终端，你可以从命令行解压缩压缩文件。首先， `cd` 到包含该压缩文件的目录。
> 
> ```
> cd ~/Downloads
> ```
> 
> 现在，用压缩文件的名称运行 `unzip` 命令。
> 
> ```
> unzip lab00.zip
> ```
> 

你只需要解压一次文件。

一旦你解压缩 `lab00.zip` ，你会有一个名为 `lab00` 的新文件夹，其中包含以下文件（用 `cd lab00` 和 `ls` 检查）：

- `lab00.py`：你要加入你的代码的模板文件
- `ok`：一个用于测试和提交作业的程序
- `lab00.ok`： `ok` 的配置文件

### 移动文件

将实验文件移到你之前创建的实验文件夹中。

#### macOS/Linux

```
mv ~/Downloads/lab00 ~/Desktop/cs61a/lab
```

#### Windows

```
mv /mnt/c/Users/Desktop/lab00 /mnt/c/Users/Desktop/cs61a/lab
```

`mv` 命令将把 `~/Downloads/lab00` 文件夹移到 `~/Desktop/cs61a/lab` 文件夹中。

现在，进入你刚刚移动的 `lab00` 文件夹。试着用 `cd` 来浏览你自己的路径！如果你被难住了，你可以使用下面的命令：

#### macOS/Linux

```
cd ~/Desktop/cs61a/lab/lab00
```

#### Windows

```
cd /mnt/c/Users/Desktop/cs61a/lab/lab00
```

## 总结

下面是对我们刚才所讲的命令的总结，供你参考：

- `ls`：列出当前目录下的所有文件
- `cd <目录路径>`：切换到指定目录
- `mkdir <目录名称>`：用给定的名称创建一个新目录
- `mv <来源路径> <目的地路径>`：将指定来源的文件移动到指定目的地

最后，你已经准备好开始编辑实验文件了！如果这看起来很复杂，不要担心，随着时间的推移会越来越容易。只要继续练习就可以了！你也可以看看我们的 [UNIX 教程](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/unix) ，了解更详细的终端命令的解释。

## Python 基础

### 表达式和声明

程序是由表达式和语句组成的。表达式是一段确定为某种值的代码，而语句是在程序中使某些事情发生的一行或多行代码。

当你在交互式 Python 解释器中输入一个 Python 表达式时，它的值就会显示出来。当你阅读下面的例子时，在你自己的 Python 解释器上尝试一些类似的表达式，你可以通过在终端键入这个来启动它：

```
python3
```

> 记住，如果你使用的是 Windows ，而 `python3` 命令不起作用，请尝试使用 `python` 或 `py` 。更多信息请参见 [安装 Python 3](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab00/#install-python-3) 部分，如果你遇到困难，请寻求帮助！

你将在本课程中学习各种类型的表达式和语句。现在，让我们来看看你在完成本实验时需要哪些表达式。

### 原始表达方式

原始表达式只需要一个计算步骤。这些表达式包括数字类型和布尔类型，它们只对自己进行求值。

```py
>>> 3
3
>>> 12.5
12.5
>>> True
True
```

### 算术表达式

数字可以与数学运算符相结合，形成复合表达式。除了 `+` 运算符（加法）、 `-` 运算符（减法）、 `*` 运算符（乘法）和 `**` 运算符（指数）之外，还有三个类似除法的运算符需要记住：

- 浮点除法（`/`）：用第一个数字除以第二个数字，即使两个数字平分，也会计算出一个带小数点的数字。
- 底限除法（`//`）：用第一个数字除以第二个数字，然后向下舍入，结果为一个整数。
- 取余（`%`）：结果为除法后留下的正余数。

括号可以用来将子表达式组合在一起；整个表达式以 PEMDAS （括号、指数、乘/除、加/减）的顺序进行计算。

```py
>>> 7 / 4
1.75
>>> (2 + 6) / 4
2.0
>>> 7 // 4        # Floor division (rounding down)
1
>>> 7 % 4         # Modulus (remainder of 7 // 4)
3
```

### 字符串

字符串由一个或多个被单引号（`''`）或双引号（`""`）包裹的字符组成。字符串实际上与原始表达式略有不同，但就本作业而言，可以类似于对自身进行求值的表达式来对待。在本课程的未来几周，你将会学到更多关于字符串的复杂知识。

```py
>>> "hello"       # Both single and double quotes work!
'hello'
>>> 'world!'
'world'
```

### 作业声明

一个赋值语句由一个变量名和一个表达式组成。它通过计算 `=` 符号右边的表达式并将其值绑定到左边的变量名上来改变程序的状态。

```py
>>> a = (100 + 50) // 2
```

现在，如果我们对 `a` 进行计算，解释器将显示 75 这个值。

```py
>>> a
75
```

## 做好作业

> 在做作业时，确保你的终端工作目录是正确的（这很可能是你解压作业的地方）。

### What Would Python Do? (WWPD)

实验作业的一个组成部分是预测 Python 解释器将如何表现。

> 在你的终端输入以下内容：
>
> ```
> python3 ok -q python-basics -u
> ```
>
> 你会被提示输入各种语句/表达式。你必须正确输入才能继续前进，但错误的答案不会受到惩罚。
>
> 第一次运行 Ok 时，系统会提示你输入 bCourses 电子邮件。请遵循 [这些提示](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/using-ok/#signing-in-with-ok) 。在评分时，我们会使用这些信息将你的代码与你联系起来。

```py
>>> 10 + 2
______

>>> 7 / 2
______

>>> 7 // 2
______

>>> 7 % 2  # 7 modulo 2, the remainder when dividing 7 by 2.
______
```

```py
>>> x = 20
>>> x + 2
______

>>> x
______

>>> y = 5
>>> y = y + 3
>>> y * 2
______

>>> y = y // 4
>>> y + x
______
```

### Parsons 问题

实验和作业的一个组成部分是 Parsons 问题。一个 Parsons 问题由一组部分完整的代码行组成。为了完成这个问题，你必须用有效的表达式填满代码行中的空白，并重新排列代码行以构建一个有效的程序。

#### 启动 Parsons 编辑器

在 `lab00` 目录下，你应该看到以下文件夹，用于布置 Parsons 问题的作业。

- `parsons`：Parsons 网络应用的文件
- `parsons_probs`：每个 Parsons 问题的文件。每个问题应该包括一个源文件（`.py`）和一个配置文件（`.yaml`）

一旦你确认了上述内容，在你的终端运行以下命令：

```
python3 parsons
```

该命令将在您的浏览器中启动一个应用程序。当第一次启动这个应用程序时，如果有提示，您可能需要登录您的 okpy 账户。在这里，你应该能够进入作业所需的问题。

与代码编写问题类似， Parsons 编辑器将为每个问题提供问题描述和测试。为了完成这些问题，在 Parsons 编辑器中你可以：

- 缩进代码的行数，把它们对准正确的标尺。
- 使用 `# ______` 块在代码上留下注释。
- 使用 `print('DEBUG:', ______)` 块打印调试语句。

![](./images/parsons_interface.png)

现在，导航并完成所需的问题 `ilove61a` ：

```py
def ilove61a():
    """
    Write a function that returns the string "I love CS 61A!".
    >>> ilove61a() # .Case 1
    'I love CS 61A!'
    """
    "*** YOUR CODE HERE ***"
```

#### 测试你的代码

要测试你的代码，请使用页面右下方的 `运行测试` 按钮。在主页上，问题完成后会有适当的标记。

> 你的进度会自动保存在 Parsons 网络应用上，所以不需要保存。

### 代码编写问题

#### 理解问题

实验也将包括函数编写问题。在你的文本编辑器中打开 `lab00.py` 。你可以在 MacOS 上输入 `open .` 或者在 Windows 上输入 `start .` 来打开 Finder/File Explorer 中的当前目录。然后双击或右击，在文本编辑器中打开该文件。你应该看到类似这样的东西：

![](./images/text-editor.png)

三引号 `"""` 中的几行被称为 **docstring** ，它是对该函数应该做什么的描述。在 61A 中编写代码时，你应该始终阅读文档！

以 `>>>` 开头的行被称为 **doctests** 。回顾一下，当使用 Python 解释器时，你在 `>>>` 旁边写 Python 表达式，输出被打印在该行下面。Doctests 通过显示实际的 Python 代码来解释函数的作用。它回答了这个问题。“如果我们输入这段 Python 代码，预期输出应该是什么？”

在这里，我们圈出了文档字符串和测试，以使它们更容易看到：

![](./images/text-editor-annotated.png)

在 `wenty_twenty_two` 中：

- docstring 告诉你“想出一个最有创意的表达式，其值为2022”，但你只能使用数字和算术运算符 `+` （加）、 `*` （乘）和 `-` （减）。
- 该测试检查函数调用 `twenty_twenty_two()` 应该返回数字 2022 。

> 你不应该修改文档串，除非你想添加你自己的测试！你唯一需要编辑的作业部分是代码，除非另有规定。

#### 编写代码

一旦你理解了这个问题的要求，你就可以开始写代码了！你应该用一个计算结果为 2022 的表达式来替换 `return ______` 中的下划线。你能想出的最有创意的表达式是什么？

> 编辑完作业后，别忘了保存作业！在大多数文本编辑器中，你可以通过导航到“文件”>“保存”或按 MacOS 的 Command-S 或 Windows 的 Ctrl-S 来保存。

### 运行测试

在 CS 61A 中，我们将使用一个名为 `ok` 的程序来测试我们的代码。 `ok` 将包含在本课的每一次作业中。

> 为了快速生成 `ok` 命令，你现在可以使用 [ok 命令生成器](https://ok-help.cs61a.org/)。

回到终端——确保你在我们先前创建的 `lab00` 目录下（记住， `cd` 命令让你 [改变目录](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab00/#changing-directories) ）。

在该目录中，你可以输入 `ls` 来验证是否有以下三个文件：

- `lab00.py`：你刚刚编辑的启动文件
- `ok`：我们的测试程序
- `lab00.ok`： Ok 的一个配置文件

现在，让我们测试一下我们的代码，以确保它的工作。你可以用这个命令运行 `ok` ：

```
python3 ok
```

> 记住，如果你使用的是 Windows ，并且 `python3` 命令不起作用，试着只使用 `python` 或 `py` 。更多信息请参见 [安装 Python 3](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab00/#install-python-3) 部分，如果你遇到困难，请寻求帮助。

如果你的代码写得正确，并且完成了测试，你应该看到一个成功的测试信息：

```
=====================================================================
Assignment: Lab 0
Ok, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    3 test cases passed! No cases failed.
```

如果你没有通过测试， `ok` 反而会给你看这样的东西：

```
---------------------------------------------------------------------
Doctests for twenty_twenty_two

>>> from lab00 import *
>>> twenty_twenty_two()
2013

# Error: expected
#     2022
# but got
#     2013

---------------------------------------------------------------------
Test summary
    0 test cases passed before encountering first failed test case
```

在你的文本编辑器中修正你的代码，直到测试通过。

> 每次你运行 Ok ， Ok 都会尝试备份你的工作。如果它说“连接超时”，请不要担心。我们不会用你的备份来评分的。
>
> 虽然 `Ok` 是 CS 61A 的主要作业“自动生成器”，但你可能会发现，有时以 [doctests](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab00/#understanding-problems) 的形式编写一些自己的测试是很有用的。然后，你可以使用 Python 的 `-m doctest` [选项](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab00/#appendix-useful-python-command-line-options) 对它们进行尝试）。
>
> 你在 Parsons 网络应用中的进展也应该通过 `python3 ok` 命令反映在你的终端上。你可以通过检查 `ok` 来确认这一点： `python3 ok -q ilove61a` 。

## 提交作业

现在你已经完成了你的第一个 CS 61A 作业，是时候交作业了。您可以按照以下步骤提交您的作业并获得分数。

### 步骤 1: 以 `ok` 提交

在你的终端中，确保你是在包含 `ok` 的目录中。如果你还没有到，你可以使用这个命令：

```
cd ~/Desktop/cs61a/lab/lab00
```

接下来，使用 `ok` 和 `-submit` 选项：

```
python3 ok --submit
```

如果你以前没有运行过 Ok ，这将提示你输入一个电子邮件地址。请遵循这些 [指示](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/using-ok/#signing-in-with-ok) ，如果你遇到问题，请参考该页的故障排除步骤。之后， Ok 会打印出一个类似下面的信息：

```
Submitting... 100% complete
Submission successful for user: ...
URL: https://okpy.org/...
```

### 步骤 2: 验证您的提交

您可以按照 Ok 打印出来的链接来查看您的最终提交材料，或者您也可以登录 [okpy.org](https://okpy.org/) 。登录后，您就可以看到您提交的材料了。

> 确保你用你在终端运行 `ok` 时提供相同的电子邮件进行登录。

你应该看到实验 0 的提交成功。

恭喜你，你刚刚提交了你的第一个 CS 61A 作业。

> 关于 Ok 的更多信息可以在 [这里](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/using-ok/) 找到。你也可以使用 `--help` 标志。
>
> ```
> python3 ok --help
> ```
>
> 这个标志的作用就像我们前面使用的 UNIX 命令一样。

## 附录：有用的Python命令行选项

当运行一个 Python 文件时，你可以在命令行上使用选项来进一步检查你的代码。这里有几个会派上用场的。如果你想进一步了解其他的 Python 命令行选项，请看一下 [文档](https://docs.python.org/3.9/using/cmdline.html) 。

- 不使用命令行选项将运行你提供的文件中的代码并返回到命令行。例如，如果我们想这样运行 `lab00.py` ，我们会在终端中写道：

    ```
    python3 lab00.py
    ```

- `-i`: 选项 `-i` 运行你的 Python 脚本，然后打开一个交互式会话。在交互式会话中，你可以逐行运行 Python 代码，并立即得到反馈，而不是一次性运行整个文件。要退出，在解释器的提示符下输入 `exit()` 。你也可以在 Linux/Mac 机器上使用键盘快捷键 `Ctrl-D` 或在 Windows 上使用 `Ctrl-Z Enter` 。

    如果你在交互式运行时编辑了 Python 文件，你将需要退出并重新启动解释器，以便使这些改变生效。

    下面是我们如何以交互方式运行 `lab00.py` 。

    ```
    python3 -i lab00.py
    ```

- `-m doctest`：在一个特定的文件中运行测试。 Doctest 在函数中用三引号 (`"""`) 围绕。

    文件中的每个测试由 `>>>` 组成，后面是一些 Python 代码和预期的输出（尽管在 doctest 命令的输出中看不到 `>>>` ）。

    为了运行 `lab00.py` 的 doctests，我们可以运行：

    ```
    python3 -m doctest lab00.py
    ```