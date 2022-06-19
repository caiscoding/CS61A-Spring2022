# Lab 4 Solution

## Q1: Squared Virahanka Fibonacci

```py
$ python3 ok -q squared-virfib-wwpd -u
=====================================================================
Assignment: Lab 4
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Squared Virahanka Fibonacci > Suite 1 > Case 1
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> def virfib_sq(n):
...     print(n)
...     if n <= 1:
...         return n
...     return (virfib_sq(n - 1) + virfib_sq(n - 2)) ** 2
>>> r0 = virfib_sq(0)
? 0
-- OK! --

>>> r1 = virfib_sq(1)
? 1
-- OK! --

>>> r2 = virfib_sq(2)
(line 1)? 2
(line 2)? 1
(line 3)? 0
-- OK! --

>>> r3 = virfib_sq(3)
(line 1)? 3
(line 2)? 2
(line 3)? 1
(line 4)? 0
(line 5)? 1
-- OK! --

>>> r3
? 4
-- OK! --

>>> (r1 + r2) ** 2
? 4
-- OK! --

>>> r4 = virfib_sq(4)
(line 1)? 4
(line 2)? 3
(line 3)? 2
(line 4)? 1
(line 5)? 0
(line 6)? 1
(line 7)? 2
(line 8)? 1
(line 9)? 0
-- OK! --

>>> r4
? 25
-- OK! --

---------------------------------------------------------------------
OK! All cases for Squared Virahanka Fibonacci unlocked.
```

## Q2: Line Stepper

**lab04/parsons_probs/line_stepper.py**

```py
def line_stepper(start, k):
    """
    Complete the function line_stepper, which returns the number of ways there are to go from
    start to 0 on the number line by taking exactly k steps along the number line.

    >>> line_stepper(1, 1)
    1
    >>> line_stepper(0, 2)
    2
    >>> line_stepper(-3, 3)
    1
    >>> line_stepper(3, 5)
    5
    """
    "*** YOUR CODE HERE ***"
    if k == 0:
        if start == 0:
            return 1
        else:
            return 0
    return line_stepper(start - 1, k - 1) + line_stepper(start + 1, k - 1)
```

## Q3: Summation

**lab04/lab04.py**

```py
def summation(n, term):
    """Return the sum of numbers 1 through n (including n) wíth term applied to each number.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    "*** YOUR CODE HERE ***"
    if n == 1:
        return term(1)
    return term(n) + summation(n - 1, term)
```

## Q4: Insect Combinatorics

**lab04/lab04.py**

```py
def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    if m == 1 and n == 1:
        return 1
    elif m < 1 or n < 1:
        return 0
    return paths(m - 1, n) + paths(m, n - 1)
```

## Q5: Pascal's Triangle

**lab04/lab04.py**

```py
def pascal(row, column):
    """Returns the value of the item in Pascal's Triangle
    whose position is specified by row and column.
    >>> pascal(0, 0)
    1
    >>> pascal(0, 5)    # Empty entry; outside of Pascal's Triangle
    0
    >>> pascal(3, 2)    # Row 3 (1 3 3 1), Column 2
    3
    >>> pascal(4, 2)     # Row 4 (1 4 6 4 1), Column 2
    6
    """
    "*** YOUR CODE HERE ***"
    if row == 0 and column == 0:
        return 1
    elif column > row or column < 0:
        return 0
    return pascal(row - 1, column) + pascal(row - 1, column - 1)
```

## Running tests

```py
$  python3 ok
=====================================================================
Assignment: Lab 4
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    4 test cases passed! No cases failed.
```