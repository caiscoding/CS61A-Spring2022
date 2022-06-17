# Homework 1: Variables & Functions, Control

## Instructions

Download [hw01.zip](https://inst.eecs.berkeley.edu/~cs61a/sp22/hw/hw01/hw01.zip).

**Submission**: When you are done, submit with `python3 ok --submit`. You may submit more than once before the deadline; only the final submission will be scored. Check that you have successfully submitted your code on [okpy.org](https://okpy.org/). See [Lab 0](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab00#submitting-the-assignment) for more instructions on submitting assignments.

**Using Ok**: If you have any questions about using Ok, please refer to [this guide](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/using-ok).

**Readings**: You might find the following references useful:

- [Section 1.1](http://composingprograms.com/pages/11-getting-started.html)
- [Section 1.2](http://composingprograms.com/pages/12-elements-of-programming.html)
- [Section 1.3](http://composingprograms.com/pages/13-defining-new-functions.html)
- [Section 1.4](http://composingprograms.com/pages/14-designing-functions.html)
- [Section 1.5](http://composingprograms.com/pages/15-control.html)

> **Important** : The lecture on Monday 1/24 will cover readings 1.3-1.5, which contain the material required for questions 2 and 5. (Control)

**Grading**: Homework is graded based on correctness. Each incorrect problem will decrease the total score by one point. There is a homework recovery policy as stated in the syllabus. **This homework is out of 2 points.**

# Required Questions

## Welcome Forms

### Q1: Welcome Forms

Please fill out both the [Syllabus Quiz](https://go.cs61a.org/syllabus-quiz), which is based off of our policies found on the course [syllabus](https://cs61a.org/articles/about/), as well as the optional [Welcome Survey](https://go.cs61a.org/welcome-survey).

## Parsons Problems

To work on these problems, open the Parsons editor:

```
python3 parsons
```

### Q2: k in Num

Write a function `k_in_num` which takes in two integers, `k` and `num`. `k_in_num` returns `True` if `num` has the digit `k` and returns `False` if `num` does not have the digit `k`. `0` is considered to have no digits.

```py
def k_in_num(k, num):
    """
    Complete k_in_num, a function which returns True if num has the digit k and
    returns False if num does not have the digit k. 0 is considered to have no
    digits.

    >>> k_in_num(3, 123) # .Case 1
    True
    >>> k_in_num(2, 123) # .Case 2
    True
    >>> k_in_num(5, 123) # .Case 3
    False
    >>> k_in_num(0, 0) # .Case 4
    False
    """
    "*** YOUR CODE HERE ***"
```

## Code Writing Problems

### Q3: A Plus Abs B

Python's `operator` module defines binary functions for Python's intrinsic arithmetic operators. For example, calling `operator.add(2,3)` is equivalent to calling the expression `2 + 3` ; both will return `5`.

Fill in the blanks in the following function for adding `a` to the absolute value of `b`, without calling `abs`. You may **not** modify any of the provided code other than the two blanks.

```py
def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> a_plus_abs_b(-1, 4)
    3
    >>> a_plus_abs_b(-1, -4)
    3
    """
    if b < 0:
        f = _____
    else:
        f = _____
    return f(a, b)
```

Use Ok to test your code:

```
python3 ok -q a_plus_abs_b
```

### Q4: Two of Three

Write a function that takes three *positive* numbers as arguments and returns the sum of the squares of the two smallest numbers. **Use only a single line for the body of the function.**

```py
def two_of_three(i, j, k):
    """Return m*m + n*n, where m and n are the two smallest members of the
    positive numbers i, j, and k.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    """
    return _____
```

> **Hint**: Consider using the `max` or `min` function:
>
> ```py
> >>> max(1, 2, 3)
> 3
> >>> min(-1, -2, -3)
> -3
> ```
>

Use Ok to test your code:

```
python3 ok -q two_of_three
```

### Q5: Largest Factor

Write a function that takes an integer `n` that is **greater than 1** and returns the largest integer that is smaller than `n` and evenly divides `n`.

```py
def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
```

> **Hint**: To check if `b` evenly divides `a`, you can use the expression `a % b == 0`, which can be read as, "the remainder of dividing `a` by `b` is 0."

Use Ok to test your code:

```
python3 ok -q largest_factor
```

## Submit

Make sure to submit this assignment by running:

```
python3 ok --submit
```