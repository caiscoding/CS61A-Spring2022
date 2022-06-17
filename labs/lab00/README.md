# Lab 0: Getting Started

## Starter Files

Download [lab00.zip](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab00/lab00.zip). Inside the archive, you will find starter files for the questions in this lab, along with a copy of the [Ok](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab00/ok) autograder.

## Introduction

This lab explains how to use your own computer to complete assignments for CS 61A and introduces some of the basics of Python.

If you need any help at any time through the lab, please feel free to come to [office hours](https://inst.eecs.berkeley.edu/~cs61a/sp22/office-hours) or post on [Piazza](https://piazza.com/berkeley/fall2021/cs61a).

This lab looks really long, but it's mostly setup and learning how to use the essential tools for this class; these may seem a bit difficult now, but will quickly become second nature as we move further into the course.

## Setup

### Install a terminal

The terminal is a program that allows you to interact with your computer by entering commands. No matter what operating system you use (Windows, macOS, Linux), the terminal will be an essential tool for CS 61A.

### macOS/Linux

If you're on a Mac or are using a form of Linux (such as Ubuntu), you already have a program called `Terminal` or something similar on your computer. Open that up and you should be good to go.

### Windows

The easiest way to get a terminal on Windows (at the time of writing) is using the Windows Subsystem for Linux, or WSL. This can be accessed through the terminal program `Ubuntu` , which emulates the Ubuntu Operating System (OS) on your Windows computer. This will make most of our assignments work smoothly on your device.

To install Ubuntu for Windows, click on Start and search for PowerShell. Right-click and select "Run as Administrator." Then, in the PowerShell window, type `wsl --install` and press Enter. The command must be typed in that exact order. This should automatically complete the setup process (follow any instructions that you may be given on the screen).

Next, download Ubuntu from the Windows store.

Once the installation completes, search for Ubuntu in your Start menu. The first launch may take a few minutes, but subsequent launches should be quick.

## Install Python 3

Python 3 is the primary programming language used in this course. Use the instructions below to install Python 3. (The instructions may feature older versions of Python 3, but the steps are similar.)

**Important:** If you already have an older version of Python installed, please make sure to download and install Python 3.9. You can check your Python version with `python3 ––version` .

### macOS

Download and install [Python 3 (64-bit)](https://www.python.org/ftp/python/3.9.6/python-3.9.6-macosx10.9.pkg). You may need to right-click the download icon and select "Open". After installing, please close and reopen your Terminal.

If you have Homebrew installed, you can also install Python3 by running `brew install python3` .

### Windows

Install Python by typing `sudo apt install python3` into Ubuntu, and hitting `enter` . Once it's finished installing, you can test that it installed correctly by typing `python3 --version`. You should see a message in response that shows you your python3 version: `Python 3.9.6`.

### Linux

Run `sudo apt install python3` (Ubuntu), `sudo pacman -S python3` (Arch), or the command for your distro.

### Other

[Download Python from the download page](https://www.python.org/downloads/).

## Install a text editor

The **Python interpreter** that you just installed allows you to *run* Python code. You will also need a **text editor**, where you will write Python code.

[Visual Studio Code (VS Code)](https://code.visualstudio.com/) is the most popular choice among the staff for this course for writing Python. Some other editors that are used among staff are listed below as well.

**If you're using Windows** and followed our Python setup process, VS Code will work best for you (since it has WSL support). After installing VS Code, install the [Remote Development extension pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack). Then, you can use the instructions in [this section](https://code.visualstudio.com/docs/remote/wsl#_open-a-remote-folder-or-workspace) of the VS Code docs to open WSL folders in VS Code.

**We highly recommend using VS Code for this class.** This will help us support you best, as most of staff uses VS Code as well.

> **Warning** : Please, please, please do not use word processors such as Microsoft Word to edit programs. Word processors can add extra content to documents that will confuse the interpreter.

For your reference, we've also written some guides on using popular text editors. After you're done with lab, you can take a look if you're interested:

- [Visual Studio Code](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/vscode): A full-featured desktop editor with many extensions available to support different languages.
- [Atom](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/atom): A more lightweight desktop editor.
- [Vim](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/vim): A command-line editor.
- [Emacs](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/emacs): A command-line editor.

A few other editors:

- [PyCharm](https://www.jetbrains.com/pycharm/): A desktop editor designed for Python.
- [Sublime Text](https://www.sublimetext.com/): A text editor that works with code.

## Pair Programming

Throughout this course, you will have many chances to collaboratively code with others in labs and projects. We recommend you download these pair programming extensions now to use in the future.

For sharing code, you can follow the instructions for your editor of choice:

- [VS Code](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/vscode#pair-programming)
- [Atom](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/atom#pair-programming)

## Backup setups

In case you had troubles installing a Python interpreter, text editor, and terminal, or if you are using something that does not allow you to install software, like an iPad, you can as a temporary measure do the assignments in using some of the following steps while you acquire more appropriate hardware.

### Soda lab computers

You will need an instructional account which will allow you to log into and use any of the lab computers in Soda. You can see your existing instructional accounts as well as make new instructional accounts for applicable classes by going to: [https://inst.eecs.berkeley.edu/connecting.html](https://inst.eecs.berkeley.edu/connecting.html).

You can login via your CalNet ID to the site. To make an instructional account for this course, click "Get a new account" for the row that has "cs61a" as its purpose.

Once you've made your account, you can then use it to log into a Soda lab computer, and work on course assignments using that computer.

### Online editors as a backup

> **Important** : Both of the alternatives listed below are not ideal for use in this course. We recommend being able to use your own local setup or using the lab computers in Soda (which you can access with your course instructional account).

**61A Code:**

You can use [61A Code](https://code.cs61a.org/), the course online environment where you can edit, run, debug, visualize, and share programs with staff. The documentation for 61A Code can be found here: [61A Code docs](https://cs61a.org/articles/61a-code-docs/).

> **Note** : You will not be able to run `ok` commands in 61A Code, which you will need to do for unlocking tests, running tests, and submitting assignments.

Steps to complete this assignment on 61A Code:

1. Visit [61A Code](https://code.cs61a.org/).
2. Open an existing file: go into your `cs61a` folder, then the assignment folder (`lab00`), in which you can find the files for this assignment.
3. You will be prompted to authorize the editor. You can click on "Confirm". Back to the editor itself, you can then open the files you would like to edit.
4. To open the terminal, click on "Console".
5. You can use the editor to write your code and the console to run your code.

**Datahub:**

Another alternative to working locally is to use Datahub at UC Berkeley.

Steps to complete this assignment on Datahub:

1. Visit [Datahub](https://datahub.berkeley.edu/).
2. Upload the assignment zip file to datahub.
3. Open a terminal by pressing "New" in the top left corner and selecting the terminal.
4. Navigating to where the zip file is and running `unzip lab00.zip`.
5. Opening up the code file (`lab00.py`) and typing in it, then saving.
6. Now you can submit the lab.

## Using the terminal

Let's check if everything was installed properly!

First, open a terminal window.

![](./images/terminal.png)

When you first open your terminal, you will start in the "home directory". The **home directory** is represented by the `~` symbol, which you might see at the prompt.

> Don't worry if your terminal window doesn't look exactly the same. The important part is that the prompt shows `$` (indicating Bash) or `%` (indicating zsh).

Try running `echo "$HOME"` . That command should display the full PATH to your home directory. It should look something like this:

`/Users/OskiBear`

A PATH is like an address: it tells both you and the computer the full path (or route) to a certain folder. Remember that you can access the files and directories (folders) on your computer in two different ways. You can either use the terminal (which is a **c**ommand **l**ine **i**nterface or CLI), or you can use Finder (on Mac) or Explorer (on Windows). Both Finder and Explorer are an example of a **g**raphics **u**ser **i**nterface (or GUI). The techniques for navigating are different, but the files are the same. For example, here's how my lab folder for cs61a looks in my GUI:

![](./images/finder-path-example.png)

And here's how the exact same folder looks in terminal:

![](./images/terminal-path-example.png)

Notice the yellow box shows you the PATH in both cases, and the purple ellipse shows you the contents of the "labs" folder.

**Python Interpreter**

We can use the terminal to check if your Python 3 interpreter was installed correctly. Try the following command:

```
python3
```

If the installation worked, you should see some text printed out about the interpreter followed by `>>>` on its own line. This is where you can type in Python code. Try typing some expressions you saw in lecture, or just play around to see what happens! You can type `exit()` or `Ctrl-D` to return to your command line.

>Ask for help if you get stuck!

## Terminal vs Python Interpreter

Let's pause and think about the difference between the terminal, and the python interpreter.

![](./images/terminal-vs-interpreter.png)

1. Which out of A, B, C or D is "the terminal"?
2. Which one is the python interpreter?
3. Which one is my code editor?
4. And how can you tell?

Both A and D are my terminal. This is where you can run bash commands like cd and ls. D is the terminal that is built-in to VS Code.

B is the python interpreter. You can tell because of the >>> prompt that means you've started a python interpreter. You can also tell because the command that started it is visible: `python3`. The `python3` command launches a python interpreter. If you type a bash command into the python interpreter, you'll probably get a syntax error! Here's an example:

![](./images/interpreter-syntax-error.png)

If you need to exit the python interpreter, just type `exit()`

C is my code editor. This is where I can write python code to be executed via my terminal.

## Organizing your files

In this section, you will learn how to manage files using terminal commands.

>Make sure your prompt contains a `$` somewhere in it and does not begin with `>>>`. If it begins with `>>>` you are still in a Python shell, and you need to exit. See above for how.

### Directories

The first command you'll use is `ls`. Try typing it in your terminal:

```
ls
```

The `ls` command **l**i**s**ts all the files and folders in the current directory. A **directory** is another name for a folder (such as the `Documents` folder).

#### macOS/Linux

Since you're in the home directory right now, after you type `ls` you should see the contents of your home directory.

#### Windows

In Ubuntu, you won't see any files in `~` when you type `ls`. Instead, you'll first need to change directories (see below).

### Changing directories

To move into another directory, use the `cd` command (change directory).

#### macOS/Linux

Let's try moving into your `Desktop` directory. First, make sure you're in your home directory (check for the `~` on your command line) and use `ls` to see if the `Desktop` directory is present.

Try typing the following command into your terminal, which should move you into that directory:

```
cd Desktop
```

If you're *not* already in your home directory, try `cd ~/Desktop`. This is telling the terminal the PATH where you want to go.

#### Windows

On Windows, first change into your main home directory.

```
cd /mnt/c/Users/
```

Now try the `ls` command from earlier. You should see a few folders. One of those folders should match your username. For example, assuming your username is `OskiBear`, you should see a folder named `OskiBear`. (Note that your Windows username might be different from your Ubuntu username) Let's change into that folder:

```
cd /mnt/c/Users/OskiBear/Desktop
```

If you still can't find your Desktop directory, ask for help on Piazza or in office hours.

### Making new directories

The next command is called `mkdir`, which **m**a**k**es a new **dir**ectory. Let's make a directory called `cs61a` in your `Desktop` directory to store all of the assignments for this class:

```
mkdir cs61a
```

A folder named `cs61a` will appear on your Desktop. You can verify this by using the `ls` command again or by checking your Desktop using Explorer (Windows) or Finder (Mac).

At this point, let's create some more directories. First, make sure you are in the cs61a directory (mac: `~/Desktop/cs61a`, Windows: `/mnt/c/Users/Desktop/cs61a`). Then, create two new folders, one called `projects` and the other called `lab`. Both should be inside of your `cs61a` folder:

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

Now if you list the contents of the directory (using `ls`), you'll see two folders, `projects` and `lab`.

![](./images/terminal_commands.png)

### More directory changing

There are a few ways to return to the home directory:

- `cd ..` (two dots). The `..` means "the parent directory", or one directory above your current directory.
- `cd ~` (the tilde). Remember that `~` means home directory, so this command will always change to your home directory.
- `cd` (`cd` on its own). Typing just `cd` is a shortcut for typing `cd ~`.

> You do not have to keep your files on your Desktop if you prefer otherwise. Where you keep your files locally will not affect your grade. Do whatever is easiest and most convenient for you!

### Downloading the assignment

If you haven't already, download the zip archive, [lab00.zip](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab00/lab00.zip) , which contains all the files that you'll need for this lab. Once you've done that, let's find the downloaded file. On most computers, `lab00.zip` is probably located in a directory called `Downloads` in your home directory. Use the `ls` command to check:

```
ls ~/Downloads
```

If you don't see `lab00.zip`, ask for help on Piazza or in office hours. On some versions of Safari the file may get unzipped for you, in which case you would just see a new directory named `lab00`.

### Extracting starter files

You must expand the zip archive before you can work on the lab files. Different operating systems and different browsers have different ways of unzipping. Clicking on a .zip file in Mac will automatically unzip. On Windows, you need to first click on the .zip file, then choose "Extract all". If you run into trouble, you can search online for how to unzip a file.

Here's a way to unzip using the terminal:

>Using a terminal, you can unzip the zip file from the command line. First, `cd` into the directory that contains the zip file:
>
> ```
> cd ~/Downloads
> ```
>
> Now, run the `unzip` command with the name of the zip file:
>
> ```
> unzip lab00.zip
> ```
>

You only need to unzip the files once.

Once you unzip `lab00.zip`, you'll have a new folder called `lab00` which contains the following files (check it out with `cd lab00` and `ls`):

- `lab00.py`: The template file you'll be adding your code to
- `ok`: A program used to test and submit assignments
- `lab00.ok`: A configuration file for `ok`

### Moving files

Move the lab files to the lab folder you created earlier:

#### macOS/Linux

```
mv ~/Downloads/lab00 ~/Desktop/cs61a/lab
```

#### Windows

```
mv /mnt/c/Users/Desktop/lab00 /mnt/c/Users/Desktop/cs61a/lab
```

The `mv` command will **m**o**v**e the `~/Downloads/lab00` folder into the `~/Desktop/cs61a/lab` folder.

Now, go to the `lab00` folder that you just moved. Try using `cd` to navigate your own way! If you get stuck, you can use the following command:

#### macOS/Linux

```
cd ~/Desktop/cs61a/lab/lab00
```

#### Windows

```
cd /mnt/c/Users/Desktop/cs61a/lab/lab00
```

## Summary

Here is a summary of the commands we just went over for your reference:

- `ls`: **l**i**s**ts all files in the current directory
- `cd <path to directory>`: **c**hange into the specified **d**irectory
- `mkdir <directory name>`: **m**a**k**e a new **dir**ectory with the given name
- `mv <source path> <destination path>`: **m**o**v**e the file at the given source to the given destination

Finally, you're ready to start editing the lab files! Don't worry if this seems complicated—it will get much easier over time. Just keep practicing! You can also take a look at our [UNIX tutorial](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/unix) for a more detailed explanation of terminal commands.

## Python Basics

### Expressions and statements

Programs are made up of expressions and statements. An expression is a piece of code that evaluates to some value and a statement is one or more lines of code that make something happen in a program.

When you enter a Python expression into the interactive Python interpreter, its value will be displayed. As you read through the following examples, try out some similar expressions on your own Python interpreter, which you can start up by typing this in your terminal:

```
python3
```

> Remember, if you are using Windows and the `python3` command doesn't work, try using `python` or `py`. See the [install Python 3](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab00/#install-python-3) section for more info and ask for help if you get stuck!

You'll be learning various types of expressions and statements in this course. For now, let's take a look at the ones you'll need to complete this lab.

### Primitive expressions

Primitive expressions only take one step to evaluate. These include numbers and booleans, which just evaluate to themselves.

```py
>>> 3
3
>>> 12.5
12.5
>>> True
True
```

### Arithmetic expressions

Numbers may be combined with mathematical operators to form compound expressions. In addition to the `+` operator (addition), the `-` operator (subtraction), the `*` operator (multiplication) and the `**` operator (exponentiation), there are three division-like operators to remember:

- Floating point division (`/`): divides the first number number by the second, evaluating to a number with a decimal point even if the numbers divide evenly.
- Floor division (`//`): divides the first number by the second and then rounds down, evaluating to an integer.
- Modulo (`%`): evaluates to the positive remainder left over from division.

Parentheses may be used to group subexpressions together; the entire expression is evaluated in PEMDAS (Parentheses, Exponentiation, Multiplication / Division, Addition / Subtraction) order.

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

### Strings

A string consists of one or more characters wrapped in either single quotes (`''`) or double quotes (`""`). Strings actually differ slightly from primitive expressions, but for the purposes of this assignment can be treated similarly as expressions which evaluate to themselves. You'll learn more about the intricacies of strings in the coming weeks in this course!

```py
>>> "hello"       # Both single and double quotes work!
'hello'
>>> 'world!'
'world'
```

### Assignment statements

An assignment statement consists of a name and an expression. It changes the state of the program by evaluating the expression to the right of the `=` sign and binding its value to the name on the left.

```py
>>> a = (100 + 50) // 2
```

Now, if we evaluate `a`, the interpreter will display the value 75.

```py
>>> a
75
```

## Doing the assignment

> When working on assignments, ensure that your terminal's working directory is correct (which is likely where you unzipped the assignment).

### What Would Python Do? (WWPD)

One component of lab assignments is to predict how the Python interpreter will behave.

> Enter the following in your terminal to begin this section:
>
> ```
> python3 ok -q python-basics -u
> ```
>
> You will be prompted to enter the output of various statements/expressions. You must enter them correctly to move on, but there is no penalty for incorrect answers.
>
> The first time you run Ok, you will be prompted for your bCourses email. Please follow [these directions](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/using-ok/#signing-in-with-ok). We use this information to associate your code with you when grading.

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

### Parsons problems

One component of lab and homework assignments are Parsons Problems. A Parsons Problem will consist of a set of partially complete lines of code. To complete the problem, you must fll in blanks in the lines of code with valid expressions as well as rearrange the lines of code to construct a valid program.

#### Launching the Parsons editor

Within the `lab00` directory, you should see the following folders for assignments with Parsons Problems:

- `parsons`: the files for the Parsons web app
- `parsons_probs`: the files for each Parsons Problem. Each problem should consist of a source file (`.py`) and a configuration file (`.yaml`)

Once you've confirmed the above, run the following command in your terminal:

```
python3 parsons
```

This command should launch an app within your browser. When launching the app for the first time, you may be required to log into your okpy account if prompted. From here, you should be able to access the required questions for the assignment.

Similarly to code writing questions, the Parsons editor will provide each problem with a problem description and doctests. To complete the questions, within the Parsons editor you can:

- indent lines of code by aligning them to the correct ruling.
- leave comments on code using the `# ______` blocks.
- print debug statements using `print('DEBUG:', ______)` blocks.

![](./images/parsons_interface.png)

Now, navigate to and complete the required question `ilove61a`:

```py
def ilove61a():
    """
    Write a function that returns the string "I love CS 61A!".
    >>> ilove61a() # .Case 1
    'I love CS 61A!'
    """
    "*** YOUR CODE HERE ***"
```

#### Testing your code

To test your code, use the `Run Tests` button in the bottom right of the page. On the home page, problems will be marked appropriately when completed.

> Your progress is automatically saved on the Parsons web app, so there is no need to save.

### Code writing questions

#### Understanding problems

Labs will also consist of function writing problems. Open up `lab00.py` in your text editor. You can type `open .` on MacOS or `start .` on Windows to open the current directory in your Finder/File Explorer. Then double click or right click to open the file in your text editor. You should see something like this:

![](./images/text-editor.png)

The lines in the triple-quotes `"""` are called a **docstring**, which is a description of what the function is supposed to do. When writing code in 61A, you should always read the docstring!

The lines that begin with `>>>` are called **doctests**. Recall that when using the Python interpreter, you write Python expressions next to `>>>` and the output is printed below that line. Doctests explain what the function does by showing actual Python code. It answers the question: "If we input this Python code, what should the expected output be?"

Here, we've circled the docstrings and the doctests to make them easier to see:

![](./images/text-editor-annotated.png)

In `twenty_twenty_two`,

- The docstring tells you to "come up with the most creative expression that evaluates to 2022," but that you can only use numbers and arithmetic operators `+` (add), `*` (multiply), and `-` (subtract).
- The doctest checks that the function call `twenty_twenty_two()` should return the number 2022.

> You should not modify the docstring, unless you want to add your own tests! The only part of your assignments that you'll need to edit is the code unless otherwise specified.

#### Writing code

Once you understand what the question is asking, you're ready to start writing code! You should replace the underscores in `return ______` with an expression that evaluates to 2022. What's the most creative expression you can come up with?

> Don't forget to save your assignment after you edit it! In most text editors, you can save by navigating to File > Save or by pressing Command-S on MacOS or Ctrl-S on Windows.

### Running tests

In CS 61A, we will use a program called `ok` to test our code. `ok` will be included in every assignment in this class.

> For quickly generating ok commands, you can now use the [ok command generator](https://ok-help.cs61a.org/).

Back to the terminal—make sure you are in the `lab00` directory we created earlier (remember, the `cd` command lets you [change directories](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab00/#changing-directories)).

In that directory, you can type `ls` to verify that there are the following three files:

- `lab00.py`: the starter file you just edited
- `ok`: our testing program
- `lab00.ok`: a configuration file for Ok

Now, let's test our code to make sure it works. You can run `ok` with this command:

```
python3 ok
```

> Remember, if you are using Windows and the `python3` command doesn't work, try using just `python` or `py`. See the the [install Python 3](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab00/#install-python-3) section for more info and ask for help if you get stuck!

If you wrote your code correctly and you finished unlocking your tests, you should see a successful test:

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

If you didn't pass the tests, `ok` will instead show you something like this:

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

Fix your code in your text editor until the test passes.

> Every time you run Ok, Ok will try to back up your work. Don't worry if it says that the "Connection timed out." We won't use your backups for grading.
>
> While `ok` is the primary assignment "autograder" in CS 61A, you may find it useful at times to write some of your own tests in the form of [doctests](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab00/#understanding-problems). Then, you can try them out using the `-m doctest` [option for Python](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab00/#appendix-useful-python-command-line-options)).
>
> Your progress in the Parsons web app should also be reflected on your terminal using the `python3 ok` commands. You can confirm this by checking on `ok`: `python3 ok -q ilove61a`.

## Submitting the assignment

Now that you have completed your first CS 61A assignment, it's time to turn it in. You can follow these next steps to submit your work and get points.

### Step 1: Submit with `ok`

In your terminal, make sure you are in the directory that contains `ok`. If you aren't there yet, you can use this command:

```
cd ~/Desktop/cs61a/lab/lab00
```

Next, use `ok` with the `--submit` option:

```
python3 ok --submit
```

This will prompt you for an email address if you haven't run Ok before. Please follow [these directions](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/using-ok/#signing-in-with-ok), and refer to the troubleshooting steps on that page if you encounter issues. After that, Ok will print out a message like the following:

```
Submitting... 100% complete
Submission successful for user: ...
URL: https://okpy.org/...
```

### Step 2: Verify your submission

You can follow the link that Ok printed out to see your final submission, or you can go to [okpy.org](https://okpy.org/). You will be able to view your submission after you log in.

> Make sure you log in with the same email you provided when running `ok` from your terminal!

You should see a successful submission for Lab 0.

**Congratulations**, you just submitted your first CS 61A assignment!

> More information on Ok is available [here](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/using-ok/). You can also use the `--help` flag:
>
> ```
> python3 ok --help
> ```
>
> This flag works just like it does for UNIX commands we used earlier.

## Appendix: Useful Python command line options

When running a Python file, you can use options on the command line to inspect your code further. Here are a few that will come in handy. If you want to learn more about other Python command-line options, take a look at the [documentation](https://docs.python.org/3.9/using/cmdline.html).

- Using no command-line options will run the code in the file you provide and return you to the command line. For example, if we want to run `lab00.py` this way, we would write in the terminal:

    ```
    python3 lab00.py
    ```

- `-i`: The `-i` option runs your Python script, then opens an interactive session. In an interactive session, you run Python code line by line and get immediate feedback instead of running an entire file all at once. To exit, type `exit()` into the interpreter prompt. You can also use the keyboard shortcut `Ctrl-D` on Linux/Mac machines or `Ctrl-Z Enter` on Windows.

    If you edit the Python file while running it interactively, you will need to exit and restart the interpreter in order for those changes to take effect.

    Here's how we can run `lab00.py` interactively:

    ```
    python3 -i lab00.py
    ```

- `-m doctest`: Runs doctests in a particular file. Doctests are surrounded by triple quotes (`"""`) within functions.

    Each test in the file consists of `>>>` followed by some Python code and the expected output (though the `>>>` are not seen in the output of the doctest command).

    To run doctests for `lab00.py`, we can run:

    ```
    python3 -m doctest lab00.py
    ```