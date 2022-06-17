# Project 1: The Game of Hog

<center>

![](./images/icon.gif)

I know! I'll use my Higher-order functions to Order higher rolls.

</center>

## Introduction

> **Update**: A new version of the project was recently released, which fixes a problem with the point totals for Question 5. If you are running into submission issues, please redownload the project and copy the file `tests/05.py` from your new project folder to your old project folder. This will update the tests for the question.

> **Important submission note:** For full credit:
>
> - Submit with Phase 1 complete by **Thursday, February 3**, worth 1 pt.
> - Submit with all phases complete by **Thursday, February 10**.
>
> Try to attempt the problems in order, as some later problems will depend on earlier problems in their implementation and therefore also when running `ok` tests.
>
> The entire project can be completed with a partner.
>
> You can get 1 bonus point by submitting the entire project by **Wednesday, February 9**.

In this project, you will develop a simulator and multiple strategies for the dice game Hog. You will need to use *control statements* and *higher-order functions* together, as described in Sections 1.2 through 1.6 of [Composing Programs](http://composingprograms.com/), the online textbook.

> When students in the past have tried to implement the functions without thoroughly reading the problem description, they’ve often run into issues. 😱 **Read each description thoroughly before starting to code.**

## Rules

In Hog, two players alternate turns trying to be the first to end a turn with at least 100 total points. On each turn, the current player chooses some number of dice to roll, up to 10. That player's score for the turn is the sum of the dice outcomes. However, a player who rolls too many dice risks:

- **Sow Sad**. If any of the dice outcomes is a 1, the current player's score for the turn is `1`.

- *Example 1*: The current player rolls 7 dice, 5 of which are 1's. They score `1` point for the turn.
- *Example 2*: The current player rolls 4 dice, all of which are 3's. Since Sow Sad did not occur, they score `12` points for the turn.

In a normal game of Hog, those are all the rules. To spice up the game, we'll include some special rules:

- **Hefty Hogs. If the opponent's score is 0** and the player chooses to roll zero dice, the player will get 1 point. However, **if the opponent's score is not 0**, a player who chooses to roll zero dice will gain points according to the following:
    - The opponent's score will be mapped to a series of functions to be applied to the player's score, starting from the rightmost digit (the one's place) and ending on the leftmost digit.
    - Each digit from `0` to `9` corresponds to a pre-defined function, `f0` through `f9`.
    - The result of this series of calls **modulo 30** is the amount of points the player receives for the turn.

- *Example 1*: The current player has 10 points. The opponent player has 32 points. The functions are applied in this order:
    - The rightmost digit of the opponent's score is `2`.
    - The corresponding function, `f2`, is applied to `10`.
    - The next digit of the opponent's score is `3`.
    - The corresponding function, `f3`, is applied to the result of `f2(10)`.
    - The points the current player gains is the result of that call, modulo 30: `f3(f2(10)) % 30`.

- *Example 2*: The current player has 33 points. The opponent player has 5439 points. The functions are applied in this order:
    - The rightmost digit of the opponent's score is `9`.
    - The corresponding function,`f9`, is applied to `33`.
    - And so on:
    - Function `f3` is applied to the result of `f9(33)`.
    - Function `f4` is applied to the result of `f3(f9(33))`.
    - Function `f5` is applied to the result of `f4(f3(f9(33)))`.
    - The points the current player gains is the result of that call, modulo 30: `f5(f4(f3(f9(33)))) % 30`.

- **Hog Pile**. After points for the turn are added to the current player's score, if the one's digit (`ones_digit`) of the current player's score is the same as the one's digit of the opponent player's score, the current player gains an additional `ones_digit` points.

- Example:
    - Both players start out at 0. (0, 0)
    - Player 0 rolls 2 dice and gets `5` points. (5, 0)
    - Player 1 rolls 1 dice and gets `5` points. (5, 5) Player 1 gets `5` more points. (5, 10)
    - Player 0 rolls 2 dice and gets `6` points. (11, 10)
    - Player 1 rolls 8 dice and gets `1` point. (11, 11) Player 1 gets `1` more point. (11, 12)

## Final product

You can try out the online Hog GUI with the staff solution to the project at [hog.cs61a.org](https://hog.cs61a.org/). When you finish the project, you'll have implemented a significant part of this game yourself.

## Download starter files

To get started, download all of the project code as a [zip archive](https://cs61a.org/proj/hog/hog.zip). Below is a list of all the files you will see in the archive once unzipped. For the project, you'll only be making changes to `hog.py`.

- `hog.py`: A starter implementation of Hog
- `dice.py`: Functions for rolling dice
- `hog_gui.py`: A graphical user interface (GUI) for Hog (updated)
- `ucb.py`: Utility functions for CS 61A
- `ok`: CS 61A autograder
- `tests`: A directory of tests used by `ok`
- `gui_files`: A directory of various things used by the web GUI
- `calc.py`: A file you can use to approximately test your final strategy (in progress)

You may notice some files other than the ones listed above too—those are needed for making the autograder and portions of the GUI work. Please do not modify any files other than `hog.py`.

## Logistics

The project is worth 25 points. 24 points are for correctness and 1 point is for submitting Phase 1 by the checkpoint date.

You will turn in the following files:

- `hog.py`

You do not need to modify or turn in any other files to complete the project. To submit the project, run the following command:

```
python3 ok --submit`
```

You will be able to view your submissions on the [Ok dashboard](http://ok.cs61a.org/).

For the functions that we ask you to complete, there may be some initial code that we provide. If you would rather not use that code, feel free to delete it and start from scratch. You may also add new function definitions as you see fit.

**However, please do not modify any other functions or edit any files not listed above.** Doing so may result in your code failing our autograder tests. Also, please do not change any function signatures (names, argument order, or number of arguments).

Throughout this project, you should be testing the correctness of your code. It is good practice to test often, so that it is easy to isolate any problems. However, you should not be testing too often, to allow yourself time to think through problems.

We have provided an **autograder** called `ok` to help you with testing your code and tracking your progress. The first time you run the autograder, you will be asked to **log in with your Ok account using your web browser**. Please do so. Each time you run `ok`, it will back up your work and progress on our servers.

The primary purpose of `ok` is to test your implementations.

We recommend that you submit **after you finish each problem**. Only your last submission will be graded. It is also useful for us to have more backups of your code in case you run into a submission issue. **If you forget to submit, your last backup will be automatically converted to a submission.**

If you do not want us to record a backup of your work or information about your progress, you can run

```
python3 ok --local
```

With this option, no information will be sent to our course servers. If you want to test your code interactively, you can run

```
python3 ok -q [question number] -i
```

with the appropriate question number (e.g. `01`) inserted. This will run the tests for that question until the first one you failed, then give you a chance to test the functions you wrote interactively.

You can also use the debugging print feature in OK by writing

```
print("DEBUG:", x)
```

which will produce an output in your terminal without causing OK tests to fail with extra output.

## Graphical User Interface

A **graphical user interface** (GUI, for short) is provided for you. At the moment, it doesn't work because you haven't implemented the game logic. Once you complete the `play` function, you will be able to play a fully interactive version of Hog!

Once you've done that, you can run the GUI from your terminal:

```
python3 hog_gui.py
```

## Phase 1: Rules of the Game

In the first phase, you will develop the rules for the game of Hog.

### Problem 0 (0 pt)

The `dice.py` file represents dice using non-pure zero-argument functions. These functions are non-pure because they may have different return values each time they are called. The documentation of `dice.py` describes the two different types of dice used in the project:

- A **fair** dice produces each possible outcome with equal probability. Two fair dice are already defined, `four_sided` and `six_sided`, and are generated by the `make_fair_dice` function.
- A **test** dice is deterministic: it always cycles through a fixed sequence of values that are passed as arguments. Test dice are generated by the `make_test_dice` function.

Before writing any code, read over the `dice.py` file and check your understanding by unlocking the following tests.

```
python3 ok -q 00 -u
```

This should display a prompt that looks like this:

```
=====================================================================
Assignment: Project 1: Hog
Ok, version v1.18.2
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 0 > Suite 1 > Case 1
(cases remaining: 1)

>>> test_dice = make_test_dice(4, 1, 2)
>>> test_dice()
?
```

You should type in what you expect the output to be. To do so, you need to first figure out what `test_dice` will do, based on the description above.

You can exit the unlocker by typing `exit()`.

**Typing Ctrl-C on Windows to exit out of the unlocker has been known to cause problems, so avoid doing so.**

In general, for each of the unlocking tests, you might find it helpful to read through the provided skeleton for that problem before attempting the unlocking test.

### Problem 1 (2 pt)

Implement the `roll_dice` function in `hog.py`. It takes two arguments: a positive integer called `num_rolls` giving the number of dice to roll and a `dice` function. It returns the number of points scored by rolling the dice that number of times in a turn: either the sum of the outcomes or 1 (*Sow Sad*).

- **Sow Sad**. If any of the dice outcomes is a 1, the current player's score for the turn is `1`.

- *Example 1*: The current player rolls 7 dice, 5 of which are 1's. They score `1` point for the turn.
- *Example 2*: The current player rolls 4 dice, all of which are 3's. Since Sow Sad did not occur, they score `12` points for the turn.

To obtain a single outcome of a dice roll, call `dice()`. You should call `dice()` **exactly** `num_rolls` **times** in the body of `roll_dice`.

Remember to call `dice()` exactly `num_rolls` times **even if Sow Sad happens in the middle of rolling**. By doing so, you will correctly simulate rolling all the dice together.

**Understand the problem:**

Before writing any code, unlock the tests to verify your understanding of the question:

```
python3 ok -q 01 -u
```

> **Note**: You will not be able to test your code using `ok` until you unlock the test cases for the corresponding question.

**Write code and check your work:**

Once you are done unlocking, begin implementing your solution. You can check your correctness with:

```
python3 ok -q 01
```

Debugging Tips

If the tests don't pass, it's time to debug. You can observe the behavior of your function using Python directly. First, start the Python interpreter and load the `hog.py` file.

```
python3 -i hog.py
```

Then, you can call your `roll_dice` function on any number of dice you want. The `roll_dice` function has a [default argument value](http://composingprograms.com/pages/14-designing-functions.html#default-argument-values) for `dice` that is a random six-sided dice function. Therefore, the following call to `roll_dice` simulates rolling four fair six-sided dice.

```py
>>> roll_dice(4)
```

You will find that the previous expression may have a different result each time you call it, since it is simulating random dice rolls. You can also use test dice that fix the outcomes of the dice in advance. For example, rolling twice when you know that the dice will come up 3 and 4 should give a total outcome of 7.

```py
>>> fixed_dice = make_test_dice(3, 4)
>>> roll_dice(2, fixed_dice)
7
```

> On most systems, you can evaluate the same expression again by pressing the up arrow, then pressing enter or return. To evaluate earlier commands, press the up arrow repeatedly.
>
> If you find a problem, you need to change your `hog.py` file, save it, quit Python, start Python again, and then start evaluating expressions. Pressing the up arrow should give you access to your previous expressions, even after restarting Python.

Continue debugging your code and running the `ok` tests until they all pass. You should follow this same procedure of understanding the problem, implementing a solution, testing, and debugging for all the problems in this project.

> One more debugging tip: to start the interactive interpreter automatically upon failing an `ok` test, use `-i`. For example, `python3 ok -q 01 -i` will run the tests for question 1, then start an interactive interpreter with `hog.py` loaded if a test fails.

### Problem 2 (4 pt)

Implement `hefty_hogs`, which takes the player's current score `player_score` and the opponent's current score `opponent_score`, and returns the number of points scored by Hefty Hogs when the player rolls 0 dice.

- **Hefty Hogs. If the opponent's score is 0** and the player chooses to roll zero dice, the player will get 1 point. However, **if the opponent's score is not 0**, a player who chooses to roll zero dice will gain points according to the following:
    - The opponent's score will be mapped to a series of functions to be applied to the player's score, starting from the rightmost digit (the one's place) and ending on the leftmost digit.
    - Each digit from `0` to `9` corresponds to a pre-defined function, `f0` through `f9`.
    - The result of this series of calls **modulo 30** is the amount of points the player receives for the turn.

- *Example 1*: The current player has 10 points. The opponent player has 32 points. The functions are applied in this order:
    - The rightmost digit of the opponent's score is `2`.
    - The corresponding function, `f2`, is applied to `10`.
    - The next digit of the opponent's score is `3`.
    - The corresponding function, `f3`, is applied to the result of `f2(10)`.
    - The points the current player gains is the result of that call, modulo 30: `f3(f2(10)) % 30`.

- *Example 2*: The current player has 33 points. The opponent player has 5439 points. The functions are applied in this order:
    - The rightmost digit of the opponent's score is `9`.
    - The corresponding function,`f9`, is applied to `33`.
    - And so on:
    - Function `f3` is applied to the result of `f9(33)`.
    - Function `f4` is applied to the result of `f3(f9(33))`.
    - Function `f5` is applied to the result of `f4(f3(f9(33)))`.
    - The points the current player gains is the result of that call, modulo 30: `f5(f4(f3(f9(33)))) % 30`.

> **Important Note on Test Cases:** The test cases for this question do not explicitly test for the case where the opponent's score is 0. However, you should make sure you implement what happens for this rule in the case that the opponent's score is 0. Otherwise, you will fail tests for later questions without implementing this.

> **Important:** Your implementation should **not** use `str`, lists, or contain square brackets `[ ]`. The test cases will check if those have been used. To make sure you're not getting an incorrect `str` error from the test cases, please **remove** the `"*** YOUR CODE HERE ***"` string.
>
> If the syntax check isn't passing on the docstring, try upgrading your Python version to `3.8` or `3.9`. Running into further issues regarding this check? Please post on Piazza.
>
> **Hint:** You may find `digit_fn` useful. This function maps a digit to the function corresponding to that digit.

Before writing any code, unlock the tests to verify your understanding of the question:

```
python3 ok -q 02 -u
```

Once you are done unlocking, begin implementing your solution. You can check your correctness with:

```
python3 ok -q 02
```

You can also test `hefty_hogs` interactively by entering `python3 -i hog.py` in the terminal and then calling `hefty_hogs` with various inputs.

### Problem 3 (2 pt)

Implement the `take_turn` function, which returns the number of points scored for a turn by rolling the given `dice` `num_rolls` times.

Your implementation of `take_turn` should call both `roll_dice` and `hefty_hogs` when possible.

Before writing any code, unlock the tests to verify your understanding of the question:

```
python3 ok -q 03 -u
```

Once you are done unlocking, begin implementing your solution. You can check your correctness with:

```
python3 ok -q 03
```

👩🏽‍💻👨🏿‍💻 [Pair programming?](https://cs61a.org/articles/pair-programming) Remember to alternate between driver and navigator roles. The driver controls the keyboard; the navigator watches, asks questions, and suggests ideas.

### Problem 4 (1 pt)

Implement `hog_pile`, which takes the current player and opponent scores and returns the points that the current player will receive due to Hog Pile. If Hog Pile is not applicable, the current player could also receive 0 additional points.

- **Hog Pile**. After points for the turn are added to the current player's score, if the one's digit (`ones_digit`) of the current player's score is the same as the one's digit of the opponent player's score, the current player gains an additional `ones_digit` points.

- Example:
    - Both players start out at 0. (0, 0)
    - Player 0 rolls 2 dice and gets `5` points. (5, 0)
    - Player 1 rolls 1 dice and gets `5` points. (5, 5) Player 1 gets `5` more points. (5, 10)
    - Player 0 rolls 2 dice and gets `6` points. (11, 10)
    - Player 1 rolls 8 dice and gets `1` point. (11, 11) Player 1 gets `1` more point. (11, 12)

Before writing any code, unlock the tests to verify your understanding of the question:

```
python3 ok -q 04 -u
```

Once you are done unlocking, begin implementing your solution. You can check your correctness with:

```
python3 ok -q 04
```

Make sure to submit your work so far before the checkpoint deadline:

```
python3 ok --submit
```

Check to make sure that you did all the problems in Phase 1:

```
python3 ok --score
```

**Congratulations! You have finished Phase 1 of this project!**

👩🏽‍💻👨🏿‍💻 [Pair programming?](https://cs61a.org/articles/pair-programming) This would be a good time to switch roles. Switching roles makes sure that you both benefit from the learning experience of being in each role.

## Phase 2: Playing the Game

### Problem 5 (5 pt)

Implement the `play` function, which simulates a full game of Hog. Players take turns rolling dice until one of the players reaches the `goal` score. A turn is defined as one roll of the dice.

To determine how many dice are rolled each turn, each player uses their respective strategy (Player 0 uses `strategy0` and Player 1 uses `strategy1`). A strategy is a function that, given a player's score and their opponent's score, returns the number of dice that the current player will roll in the turn. Don't worry about implementing strategies yet; you'll do that in Phase 3.

> **Important:** Your implementation should only need to use a single loop; you don't need multiple loops. This might not affect passing the test cases if your logic is correct overall, but this could affect your [composition](https://cs61a.org/articles/composition/) grade for the project. Here's the section of the syllabus on composition for [projects](https://cs61a.org/articles/about#projects).
>
> Additionally, each strategy function should be called only once per turn. This means you only want to call `strategy0` when it is Player 0's turn and only call `strategy1` when it is Player 1's turn. Otherwise, the GUI and some `ok` tests may get confused.

If a player achieves the goal score by the end of their turn, i.e. after all applicable rules have been applied, the game ends. `play` will then return the final total scores of both players, with Player 0's score first and Player 1's score second.

> **Hints:**
>
> - You should call the functions you have implemented already.
> - Call `take_turn` with five arguments (don't forget to pass in the `goal`). Only call `take_turn` once per turn.
> - Call `hog_pile` to determine if the current player will gain additional points due to Hog Pile, and if so, how many points.
> - You can get the number of the next player (either 0 or 1) by calling the provided function `next_player`.
> - You can ignore the `leader` variable and the `say` argument to the `play` function for now. You will use them in Problem 7.
> - For the unlocking tests, `hog.always_roll` refers to the `always_roll` function defined in `hog.py`.

Before writing any code, unlock the tests to verify your understanding of the question:

```
python3 ok -q 05 -u
```

Once you are done unlocking, begin implementing your solution. You can check your correctness with:

```
python3 ok -q 05
```

Once you are finished, you will be able to play a graphical version of the game. We have provided a file called `hog_gui.py` that you can run from the terminal:

```
python3 hog_gui.py
```

The GUI relies on your implementation, so if you have any bugs in your code, they will be reflected in the GUI. This means you can also use the GUI as a debugging tool; however, it's better to run the tests first.

### Commentary functions

In the next few problems, you will implement a commentary function that prints remarks about the game, such as: `"Player 0 takes the lead by 5"`.

A commentary function takes three arguments:

- Player 0's current score, `score0`
- Player 1's current score, `score1`
- The previous leading player (if applicable), `leader`

And returns two values:

- The current leading player (if applicable)
- The message to be printed, or `None` if no message is to be printed

A commentary function should have no side effects; you'll later update `play` to call the commentary function and print out the current turn's message when applicable.

### Problem 6 (2 pt)

Implement `announce_lead_changes`, a commentary function that tracks lead changes. When the leading player changes, `announce_lead_changes` should return a message. If there is no leading player (i.e. the two player's scores are the same) or if there has been no change from the previous leading player, then `announce_lead_changes` should return `None` for its message.

At the end of `announce_lead_changes`, you should return two values:

1. The player (either 0 or 1) with the higher score (or `None` if the player's score and the opponent's scores are equal)
2. The message to be printed (or `None` if no message should be printed)

When there has been a change in the leading player, `announce_lead_changes` should return a message. The format of this message is very specific, and your implementation should match the doctest provided.

Before writing any code, unlock the tests to verify your understanding of the question:

```
python3 ok -q 06 -u
```

Once you are done unlocking, begin implementing your solution. You can check your correctness with:

```
python3 ok -q 06
```

When you are done, you will see commentary in the GUI:

```
python3 hog_gui.py
```

The commentary in the GUI is generated by passing the following function as the say argument to `play`.

```
announce_lead_changes
```

### Problem 7 (2 pt)

Update your `play` function so that the commentary function `say` is called at the end of each turn. Whenever `say` is called, two things are returned: a new `leader` and a `message`. The `leader` should be passed into `say` on the next turn as its third argument. If the `message` is not `None` and is not the empty string `""`, it should be `print`ed.

On the first turn, you can pass in the provided `leader` as the third argument to `say`. Each consecutive call to `say` will then rely on the return value of `say` from the previous call.

For example, the function `say_scores` in `hog.py` is a commentary function that simply announces both players' scores. In this function, the `leader` argument is not used, but it is still returned.

```py
def say_scores(score0, score1, player=None):
    """A commentary function that announces the score for each player."""
    message = f"Player 0 now has {score0} and now Player 1 has {score1}"
    return player, message
```

> **Hint:** For the unlocking tests for this problem, remember that when calling `print` with multiple arguments, Python will put a space between each of the arguments. For example:
>
> ```py
> >>> print(9, 12)
> 9 12
> ```
>

Before writing any code, unlock the tests to verify your understanding of the question:

```
python3 ok -q 07 -u
```

Once you are done unlocking, begin implementing your solution. You can check your correctness with:

```
python3 ok -q 07
```

Great work! You just finished Phase 2 of the project!


👩🏽‍💻👨🏿‍💻 [Pair programming?](https://cs61a.org/articles/pair-programming) Celebrate, take a break, and switch roles!

## Phase 3: Strategies of the Game

In the third phase, you will experiment with ways to improve upon the basic strategy of always rolling a fixed number of dice. First, you need to develop some tools to evaluate strategies.

### Problem 8 (2 pt)

Implement the `make_averaged` function, which is a higher-order function that takes a function `original_function` as an argument.

The return value of `make_averaged` is a function that takes in the same number of arguments as `original_function`. When we call this returned function on arguments, it will return the average value of repeatedly calling `original_function` on the arguments passed in.

Specifically, this function should call `original_function` a total of `total_samples` times and return the average of the results of these calls.

> **Important:** To implement this function, you will need to use a new piece of Python syntax. We would like to write a function that accepts an arbitrary number of arguments, and then calls another function using exactly those arguments. Here's how it works.
>
> Instead of listing formal parameters for a function, you can write `*args`, which represents all of the **arg**ument**s** that get passed into the function. We can then call another function with these same arguments by passing these `*args` into this other function. For example:
>
> ```py
> >>> def printed(f):
> ...     def print_and_return(*args):
> ...         result = f(*args)
> ...         print('Result:', result)
> ...         return result
> ...     return print_and_return
> >>> printed_pow = printed(pow)
> >>> printed_pow(2, 8)
> Result: 256
> 256
> >>> printed_abs = printed(abs)
> >>> printed_abs(-10)
> Result: 10
> 10
> ```
>
> Here, we can pass any number of arguments into `print_and_return` via the `*args` syntax. We can also use `*args` inside our `print_and_return` function to make another function call with the same arguments.

Read the docstring for `make_averaged` carefully to understand how it is meant to work.

Before writing any code, unlock the tests to verify your understanding of the question:

```
python3 ok -q 08 -u
```

Once you are done unlocking, begin implementing your solution. You can check your correctness with:

```
python3 ok -q 08
```

### Problem 9 (2 pt)

Implement the `max_scoring_num_rolls` function, which runs an experiment to determine the number of rolls (from 1 to 10) that gives the maximum average score for a turn. Your implementation should use `make_averaged` and `roll_dice`.

If two numbers of rolls are tied for the maximum average score, return the lower number. For example, if both 3 and 6 achieve a maximum average score, return 3.

You might find it useful to read the doctest and the example shown in the doctest for this problem before doing the unlocking test.

> **Important:** In order to pass all of our tests, please make sure that you are testing dice rolls starting from 1 going up to 10, rather than starting from 10 to 1.

Before writing any code, unlock the tests to verify your understanding of the question:

```
python3 ok -q 09 -u
```

Once you are done unlocking, begin implementing your solution. You can check your correctness with:

```
python3 ok -q 09
```

**Running experiments:**

To run this experiment on randomized dice, call `run_experiments` using the `-r` option:

```
python3 hog.py -r
```

For the remainder of this project, you can change the implementation of `run_experiments` as you wish. The function includes calls to `average_win_rate` for evaluating various Hog strategies, but most of the calls are currently commented out. You can un-comment the calls to try out strategies, like to compare the win rate for `always_roll(8)` to the win rate for `always_roll(6)`.

Some of the experiments may take up to a minute to run. You can always reduce the number of trials in your call to `make_averaged` to speed up experiments.

Running experiments won't affect your score on the project.

👩🏽‍💻👨🏿‍💻 [Pair programming?](https://cs61a.org/articles/pair-programming) We suggest switching roles now, if you haven't recently. Almost done!

### Problem 10 (1 pt)

A strategy can try to take advantage of the Hefty Hogs rule by rolling 0 when it is most beneficial to do so. Implement `hefty_hogs_strategy`, which returns 0 whenever rolling 0 would give **at least** `threshold` points and returns `num_rolls` otherwise.

> **Hint:** You can use the function `hefty_hogs` you defined in Problem 2.

Before writing any code, unlock the tests to verify your understanding of the question:

```
python3 ok -q 10 -u
```

Once you are done unlocking, begin implementing your solution. You can check your correctness with:

```
python3 ok -q 10
```

Once you have implemented this strategy, change `run_experiments` to evaluate your new strategy against the baseline. Is this strategy an improvement over the baseline?

### Problem 11 (1 pt)

A strategy can also take advantage of the Hog Pile rules. The Hog Pile strategy always rolls 0 if doing so triggers the rule and earns a nonzero amount of points. In other cases, it rolls 0 if rolling 0 would give **at least** `threshold` points. Otherwise, the strategy rolls `num_rolls`.

> **Hint:** You can use the function `hefty_hogs_strategy` you defined in Problem 10.
>
> **Hint:** Remember that the `hog_pile` check should be done after the points from `hefty_hogs` have been added to the score.

Before writing any code, unlock the tests to verify your understanding of the question:

```
python3 ok -q 11 -u
```

Once you are done unlocking, begin implementing your solution. You can check your correctness with:

```
python3 ok -q 11
```

Once you have implemented this strategy, update `run_experiments` to evaluate your new strategy against the baseline.

### Optional: Problem 12 (0 pt)

Implement `final_strategy`, which combines these ideas and any other ideas you have to achieve a high win rate against the baseline strategy. Some suggestions:

- `hefty_hogs_strategy` or `hog_pile_strategy` are default strategies you can start with.
- If you know the goal score (by default it is 100), there's no point in scoring more than the goal. Check whether you can win by rolling 0, 1 or 2 dice. If you are in the lead, you might decide to take fewer risks.
- Choose the `num_rolls` and `threshold` arguments carefully.
- Take the action that is most likely to win the game.

You can check that your final strategy is valid by running `ok`.

```
python3 ok -q 12
```

You can also play against your final strategy with the graphical user interface:

```
python3 hog_gui.py
```

> Note: The GUI has been updated. See the announcement at the top of the page for instructions.

The GUI will alternate which player is controlled by you.

## Project submission

At this point, run the entire autograder to see if there are any tests that don't pass:

```
python3 ok
```

You can also check your score on each part of the project:

```
python3 ok --score
```

Once you are satisfied, submit to complete the project.

```
python3 ok --submit
```

**If you have a partner, make sure to add them to the project submission on** [okpy](https://okpy.org/).

**Congratulations, you have reached the end of your first CS 61A project!** If you haven't already, relax and enjoy a few games of Hog with a friend.