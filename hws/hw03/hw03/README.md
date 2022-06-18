# Homework 3 Solution

## Q1: Neighbor Digits

**hw03/parsons_probs/neighbor_digits.py**

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
    if num < 10: 
        if num == prev_digit:
            return 1
        else:
            return 0    lastDigit = num % 10
    currDigit = num // 10
    return int(lastDigit == prev_digit or lastDigit == currDigit % 10) + neighbor_digits(currDigit, lastDigit)
```

## Q2: Has Subsequence

**hw03/parsons_probs/has_subseq.py**

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
    while n > 0:
        if n % 10 == seq % 10:
            seq //= 10
            if seq == 0:
                return True
        n //= 10
    return False
```

## Q3: Num eights

**hw03/hw03.py**

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
    if pos < 10:
        if pos == 8:
            return 1
        else:
            return 0
    elif pos % 10 == 8:
        return 1 + num_eights(pos // 10)
    else:
        return 0 + num_eights(pos // 10)
```

## Q4: Ping-pong

**hw03/hw03.py**

```py
def changtimes(n):
    sum = 0
    for i in range(1, n + 1):
        if i % 8 == 0 or num_eights(i):
            sum += 1
    return sum


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
    if n == 1:
        return 1
    if changtimes(n) % 2 == 0:
        if num_eights(n) or n % 8 == 0:
            return pingpong(n - 1) - 1
        else:
            return pingpong(n - 1) + 1
    else:
        if num_eights(n) or n % 8 == 0:
            return pingpong(n - 1) + 1
        else:
            return pingpong(n - 1) - 1
```

## Q5: Count coins

**hw03/hw03.py**

```py
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
    def count(change, smallestCoin):
        if change == 0:
            return 1
        elif change < 0 or smallestCoin is None:
            return 0
        withoutCoin = count(change, get_larger_coin(smallestCoin))
        withCoin = count(change - smallestCoin, smallestCoin)
        return withoutCoin + withCoin
    return count(change, 1)
```

## Running tests

```py
$ python3 ok
=====================================================================
Assignment: Homework 3
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    5 test cases passed! No cases failed.
```