# Lab 1 Solution

## Q1: WWPD: Control

```py
$ python3 ok -q control -u
=====================================================================
Assignment: Lab 1
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Control > Suite 1 > Case 1
(cases remaining: 5)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> def xk(c, d):
...     if c == 4:
...         return 6
...     elif d >= 4:
...         return 6 + 7 + c
...     else:
...         return 25
>>> xk(10, 10)
? 23
-- OK! --

>>> xk(10, 6)
? 23
-- OK! --

>>> xk(4, 6)
? 6
-- OK! --

>>> xk(0, 0)
? 25
-- OK! --

---------------------------------------------------------------------
Control > Suite 1 > Case 2
(cases remaining: 4)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> def how_big(x):
...     if x > 10:
...         print('huge')
...     elif x > 5:
...         return 'big'
...     elif x > 0:
...         print('small')
...     else:
...         print("nothing")
>>> how_big(7)
? 'big'
-- OK! --

>>> how_big(12)
? huge
-- OK! --

>>> how_big(1)
? small
-- OK! --

>>> how_big(-1)
? nothing
-- OK! --

---------------------------------------------------------------------
Control > Suite 2 > Case 1
(cases remaining: 3)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> n = 3
>>> while n >= 0:  # If this loops forever, just type Infinite Loop
...     n -= 1
...     print(n)
(line 1)? 2
(line 2)? 1
(line 3)? 0
(line 4)? -1
-- OK! --

---------------------------------------------------------------------
Control > Suite 2 > Case 2
(cases remaining: 2)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> positive = 28
>>> while positive: # If this loops forever, just type Infinite Loop
...    print("positive?")
...    positive -= 3
(line 1)? Infinite Loop
-- OK! --

---------------------------------------------------------------------
Control > Suite 2 > Case 3
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> positive = -9
>>> negative = -12
>>> while negative: # If this loops forever, just type Infinite Loop
...    if positive:
...        print(negative)
...    positive += 3
...    negative += 3
(line 1)? -12
(line 2)? -9
(line 3)? -6
-- OK! --

---------------------------------------------------------------------
OK! All cases for Control unlocked.
```

## Q2: WWPD: Veritasiness

```py
$ python3 ok -q short-circuit -u
=====================================================================
Assignment: Lab 1
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Veritasiness > Suite 1 > Case 1
(cases remaining: 3)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> True and 13
? 13
-- OK! --

>>> False or 0
? 0
-- OK! --

>>> not 10
? False
-- OK! --

>>> not None
? True
-- OK! --

---------------------------------------------------------------------
Veritasiness > Suite 1 > Case 2
(cases remaining: 2)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> True and 1 / 0 and False  # If this errors, just type Error.
? Error
-- OK! --

>>> True or 1 / 0 or False  # If this errors, just type Error.
? True
-- OK! --

>>> True and 0  # If this errors, just type Error.
? 0
-- OK! --

>>> False or 1  # If this errors, just type Error.
? 1
-- OK! --

>>> 1 and 3 and 6 and 10 and 15  # If this errors, just type Error.
? 15
-- OK! --

>>> -1 and 1 > 0 # If this errors, just type Error.
? True
-- OK! --

>>> 0 or False or 2 or 1 / 0  # If this errors, just type Error.
? 2
-- OK! --

---------------------------------------------------------------------
Veritasiness > Suite 2 > Case 1
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> not 0
? True
-- OK! --

>>> (1 + 1) and 1  # If this errors, just type Error. If this is blank, just type Nothing.
? 1
-- OK! --

>>> 1/0 or True  # If this errors, just type Error. If this is blank, just type Nothing.
? Error
-- OK! --

>>> (True or False) and False  # If this errors, just type Error. If this is blank, just type Nothing.
? False
-- OK! --

---------------------------------------------------------------------
OK! All cases for Veritasiness unlocked.
```

## Q3: Debugging Quiz

```py
$ python3 ok -q debugging-quiz -u
=====================================================================
Assignment: Lab 1
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 1
(cases remaining: 8)

Q: In the following traceback, what is the most recent function call?
Traceback (most recent call last):
    File "temp.py", line 10, in <module>
      f("hi")
    File "temp.py", line 2, in f
      return g(x + x, x)
    File "temp.py", line 5, in g
      return h(x + y * 5)
    File "temp.py", line 8, in h
      return x + 0
  TypeError: must be str, not int
Choose the number of the correct choice:
0) g(x + x, x)
1) h(x + y * 5)
2) f("hi")
? 1
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 2
(cases remaining: 7)

Q: In the following traceback, what is the cause of this error?
Traceback (most recent call last):
    File "temp.py", line 10, in <module>
      f("hi")
    File "temp.py", line 2, in f
      return g(x + x, x)
    File "temp.py", line 5, in g
      return h(x + y * 5)
    File "temp.py", line 8, in h
      return x + 0
  TypeError: must be str, not int
Choose the number of the correct choice:
0) the code looped infinitely
1) there was a missing return statement
2) the code attempted to add a string to an integer
? 2
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 3
(cases remaining: 6)

Q: How do you write a doctest asserting that square(2) == 4?
Choose the number of the correct choice:
0) def square(x):
       '''
       square(2)
       4
       '''
       return x * x
1) def square(x):
       '''
       input: 2
       output: 4
       '''
       return x * x
2) def square(x):
       '''
       >>> square(2)
       4
       '''
       return x * x
3) def square(x):
       '''
       doctest: (2, 4)
       '''
       return x * x
? 2
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 4
(cases remaining: 5)

Q: When should you use print statements?
Choose the number of the correct choice:
0) To investigate the values of variables at certain points in your code
1) For permanant debugging so you can have long term confidence in your code
2) To ensure that certain conditions are true at certain points in your code
? 0
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 5
(cases remaining: 4)

Q: How do you prevent the ok autograder from interpreting print statements as output?
Choose the number of the correct choice:
0) You don't need to do anything, ok only looks at returned values, not printed values
1) Print with # at the front of the outputted line
2) Print with 'DEBUG:' at the front of the outputted line
? 2
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 6
(cases remaining: 3)

Q: What is the best way to open an interactive terminal to investigate a failing test for question sum_digits in assignment lab01?
Choose the number of the correct choice:
0) python3 ok -q sum_digits --trace
1) python3 -i lab01.py
2) python3 ok -q sum_digits -i
3) python3 ok -q sum_digits
? 2
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 7
(cases remaining: 2)

Q: What is the best way to look at an environment diagram to investigate a failing test for question sum_digits in assignment lab01?
Choose the number of the correct choice:
0) python3 ok -q sum_digits
1) python3 ok -q sum_digits --trace
2) python3 ok -q sum_digits -i
3) python3 -i lab01.py
? 1
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 8
(cases remaining: 1)

Q: Which of the following is NOT true?
Choose the number of the correct choice:
0) It is generally bad practice to release code with debugging print statements left in
1) Debugging is not a substitute for testing
2) It is generally good practice to release code with assertion statements left in
3) Code that returns a wrong answer instead of crashing is generally better as it at least works fine
4) Testing is very important to ensure robust code
? 3
-- OK! --

---------------------------------------------------------------------
OK! All cases for debugging-quiz unlocked.
```

## Q4: Add in Range

**lab01/parsons_probs/add_in_range.py**

```py
def add_in_range(start, stop):
    """
    >>> add_in_range(3, 5)  # .Case 1
    12
    >>> add_in_range(1, 10)  # .Case 2
    55
    """
    "*** YOUR CODE HERE ***"
    sum = 0
    for i in range(start, stop + 1):
        sum += i
    return sum
```

## Q5: Digit Position Match

**lab01/parsons_probs/digit_pos_match.py**

```py
def digit_pos_match(n, k):
    """
    >>> digit_pos_match(980, 0) # .Case 1
    True
    >>> digit_pos_match(980, 2) # .Case 2
    False
    >>> digit_pos_match(98276, 2) # .Case 3
    True
    >>> digit_pos_match(98276, 3) # .Case 4
    False
    """
    "*** YOUR CODE HERE ***"
    while n > 0:
        x = n % 10
        if x == k:
            return True
        else:
            n = n // 10
    return False
```

## Q6: Falling Factorial

**lab01/lab01.py**

```py
def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    if k == 0:
        return 1
    res = 1
    while k > 0:
        res *= n
        n -= 1
        k -= 1
    return res
```

## Q7: Sum Digits

**lab01/lab01.py**

```py
def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    sum = 0
    while y > 0:
        sum, y = sum + y % 10, y // 10
    return sum
```

## Q8: WWPD: What If?

```py
$ python3 ok -q if-statements -u
=====================================================================
Assignment: Lab 1
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
What If? > Suite 1 > Case 1
(cases remaining: 2)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> def ab(c, d):
...     if c > 5:
...         print(c)
...     elif c > 7:
...         print(d)
...     print('foo')
>>> ab(10, 20)
(line 1)? 10
(line 2)? foo
-- OK! --

---------------------------------------------------------------------
What If? > Suite 1 > Case 2
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> def bake(cake, make):
...    if cake == 0:
...        cake = cake + 1
...        print(cake)
...    if cake == 1:
...        print(make)
...    else:
...        return cake
...    return make
>>> bake(0, 29)
(line 1)? 1
(line 2)? 29
(line 3)? 29
-- OK! --

>>> bake(1, "mashed potatoes")
(line 1)? mashed potatoes
(line 2)? "mashed potatoes"
-- OK! --

---------------------------------------------------------------------
OK! All cases for What If? unlocked.
```

## Q9: K-Occurrence

**lab01/parsons_probs/k_occurrence.py**

```py
def k_occurrence(k, num):
    """
    >>> k_occurrence(5, 10)  # .Case 1
    0
    >>> k_occurrence(5, 5115)  # .Case 2
    2
    >>> k_occurrence(0, 100)  # .Case 3
    2
    >>> k_occurrence(0, 0)  # .Case 4
    0
    """
    "*** YOUR CODE HERE ***"
    if num == 0:
        return 0
    count = 0
    while num:
        if num % 10 == k:
            count += 1
        num = num // 10
    return count
```

## Q10: Double Eights

**lab01/lab01.py**

```py
def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    while n > 0:
        temp = n % 100
        if temp == 88:
            return True
        n = n // 10
    return False
```

## Running tests

```py
$ python3 ok
=====================================================================
Assignment: Lab 1
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    20 test cases passed! No cases failed.
```
