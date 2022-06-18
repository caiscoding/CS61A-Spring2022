# Homework 3: Recursion, Tree Recursion

## Instructions

Download [hw03.zip](https://inst.eecs.berkeley.edu/~cs61a/sp22/hw/hw03/hw03.zip). Inside the archive, you will find a file called [hw03.py](https://inst.eecs.berkeley.edu/~cs61a/sp22/hw/hw03/hw03.py), along with a copy of the `ok` autograder.

**Submission:** When you are done, submit with `python3 ok --submit`. You may submit more than once before the deadline; only the final submission will be scored. Check that you have successfully submitted your code on [okpy.org](https://okpy.org/). See [Lab 0](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab00#submitting-the-assignment) for more instructions on submitting assignments.

**Using Ok:** If you have any questions about using Ok, please refer to [this guide](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/using-ok).

**Readings:** You might find the following references useful:

- [Section 1.7](http://composingprograms.com/pages/17-recursive-functions.html)

**Grading:** Homework is graded based on correctness. Each incorrect problem will decrease the total score by one point. There is a homework recovery policy as stated in the syllabus. **This homework is out of 2 points.**

> **Important:** An update to Homework 3 was released on Sunday. If you downloaded the homework before then, please update your assignment! To do so and save your progress, redownload the homework and copy the `hw03.ok` file from the new folder to your old folder. You can continue working in and submit from your old folder.

# Required Questions

## Getting Started Videos

These videos may provide some helpful direction for tackling the coding problems on this assignment.

> To see these videos, you should be logged into your berkeley.edu email.

[YouTube link](https://youtu.be/watch?v=_F4uNI6qTjA&list=PLx38hZJ5RLZdj4fEiGslUdu3VKoVOqTg3)

## Parsons Problems

To work on these problems, open the Parsons editor:

```
python3 parsons
```

### Q1: Neighbor Digits

Implement the function `neighbor_digits`. `neighbor_digits` takes in a positive integer `num` and an optional argument `prev_digit`. `neighbor_digits` outputs the number of digits in `num` that have the same digit to its right or left.

```py
def neighbor_digits(num, prev_digit=-1):
    """
    Returns the number of digits in num that have the same digit to its right
    or left.
    >>> neighbor_digits(111)
    3
    >>> neighbor_digits(123)
    0
    >>> neighbor_digits(112)
    2
    >>> neighbor_digits(1122)
    4
    """
    "*** YOUR CODE HERE ***"
```

### Q2: Has Subsequence

Implement the function `has_subseq`, which takes in a number `n` and a "sequence" of digits `seq`. The function returns whether `n` contains `seq` as a subsequence, which does not have to be consecutive.

For example, `141` contains the sequence `11` because the first digit of the sequence, 1, is the first digit of `141`, and the next digit of the sequence, 1, is found later in `141`.

```py
def has_subseq(n, seq):
    """
    Complete has_subseq, a function which takes in a number n and a "sequence"
    of digits seq and returns whether n contains seq as a subsequence, which
    does not have to be consecutive.

    >>> has_subseq(123, 12)
    True
    >>> has_subseq(141, 11)
    True
    >>> has_subseq(144, 12)
    False
    >>> has_subseq(144, 1441)
    False
    >>> has_subseq(1343412, 134)
    True
    """
    "*** YOUR CODE HERE ***"
```

## Code Writing Questions

### Q3: Num eights

Write a recursive function `num_eights` that takes a positive integer `pos` and returns the number of times the digit 8 appears in `pos`.

**Important:** Use recursion; the tests will fail if you use any assignment statements. (You can however use function definitions if you so wish.)

```py
def num_eights(pos):
    """Returns the number of times 8 appears as a digit of pos.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    "*** YOUR CODE HERE ***"
```

Use Ok to test your code:

```
python3 ok -q num_eights
```

### Q4: Ping-pong

The ping-pong sequence counts up starting from 1 and is always either counting up or counting down. At element `k`, the direction switches if `k` is a multiple of 8 or contains the digit 8. The first 30 elements of the ping-pong sequence are listed below, with direction swaps marked using brackets at the 8th, 16th, 18th, 24th, and 28th elements:

|Index|1|2|3|4|5|6|7|[8]|9|10|11|12|13|14|15|[16]|17|[18]|19|20|21|22|23|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|PingPong Value|1|2|3|4|5|6|7|[8]|7|6|5|4|3|2|1|[0]|1|[2]|1|0|-1|-2|-3|

|Index (cont.)|[24]|25|26|27|[28]|29|30|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|PingPong Value|[-4]|-3|-2|-1|[0]|-1|-2|

Implement a function `pingpong` that returns the nth element of the ping-pong sequence without using any assignment statements. (You are allowed to use function definitions.)

You may use the function `num_eights`, which you defined in the previous question.

**Important:** Use recursion; the tests will fail if you use any assignment statements. (You can however use function definitions if you so wish.)

> **Hint:** If you're stuck, first try implementing `pingpong` using assignment statements and a `while` statement. Then, to convert this into a recursive solution, write a helper function that has a parameter for each variable that changes values in the body of the while loop.
>
> **Hint:** There are a few pieces of information that we need to keep track of. One of these details is the direction that we're going (either increasing or decreasing). Building off of the hint above, think about how we can keep track of the direction throughout the calls to the helper function.

```py
def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    "*** YOUR CODE HERE ***"
```

Use Ok to test your code:

```
python3 ok -q pingpong
```

### Q5: Count coins

Given a positive integer `change`, a set of coins makes change for `change` if the sum of the values of the coins is `change`. Here we will use standard US Coin values: 1, 5, 10, 25. For example, the following sets make change for `15`:

- 15 1-cent coins
- 10 1-cent, 1 5-cent coins
- 5 1-cent, 2 5-cent coins
- 5 1-cent, 1 10-cent coins
- 3 5-cent coins
- 1 5-cent, 1 10-cent coin

Thus, there are 6 ways to make change for `15`. Write a **recursive** function `count_coins` that takes a positive integer `change` and returns the number of ways to make change for `change` using coins.

You can use either of the functions given to you:

- `get_larger_coin` will return the next larger coin denomination from the input, i.e. `get_larger_coin(5)` is `10`.
- `get_smaller_coin` will return the next smaller coin denomination from the input, i.e. `get_smaller_coin(5)` is `1`.

There are two main ways in which you can approach this problem. One way uses `get_larger_coin`, and another uses `get_smaller_coin`.

**Important:** Use recursion; the tests will fail if you use loops.

> **Hint:** Refer the [implementation](http://composingprograms.com/pages/17-recursive-functions.html#example-partitions) of `count_partitions` for an example of how to count the ways to sum up to a final value with smaller parts. If you need to keep track of more than one value across recursive calls, consider writing a helper function.

```py
def get_larger_coin(coin):
    """Returns the next larger coin in order.
    >>> get_larger_coin(1)
    5
    >>> get_larger_coin(5)
    10
    >>> get_larger_coin(10)
    25
    >>> get_larger_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25

def get_smaller_coin(coin):
    """Returns the next smaller coin in order.
    >>> get_smaller_coin(25)
    10
    >>> get_smaller_coin(10)
    5
    >>> get_smaller_coin(5)
    1
    >>> get_smaller_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1

def count_coins(change):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
```

Use Ok to test your code:

```
python3 ok -q count_coins
```

## Optional Questions

Homework assignments will also contain prior exam-level questions for you to take a look at. These questions have no submission component; feel free to attempt them if you'd like a challenge!

1. Fall 2017 MT1 Q4a: [Digital](https://inst.eecs.berkeley.edu/~cs61a/fa21/exam/fa17/mt1/61a-fa17-mt1.pdf#page=5)
2. Summer 2018 MT1 Q5a: [Won't You Be My Neighbor?](https://inst.eecs.berkeley.edu/~cs61a/su18/assets/pdfs/61a-su18-mt.pdf#page=5)
3. Fall 2019 Final Q6b: [Palindromes](https://inst.eecs.berkeley.edu/~cs61a/sp21/exam/fa19/final/61a-fa19-final.pdf#page=6)