# Lab 13 Solution

## Q1: What Would RegEx Match?

```py
$ python3 ok -q wwrm -u
=====================================================================
Assignment: Lab 13
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
wwrm > Suite 1 > Case 1
(cases remaining: 4)

Q: #[a-f0-9]{6}
Choose the number of the correct choice:
0) A hexadecimal color code with 3 letters and 3 numbers
1) A hexadecimal color code that starts with letters and ends with numbers, like #gg1234
2) Any 6-digit hexadecimal color code, like #fdb515
3) Any hexadecimal color code with 0-6 digits
? 2
-- OK! --

---------------------------------------------------------------------
wwrm > Suite 1 > Case 2
(cases remaining: 3)

Q: (fizz(buzz|)|buzz)
Choose the number of the correct choice:
0) Only fizzbuzz or buzz
1) Only fizzbuzzbuzz
2) Only fizz
3) Only fizzbuzz, fizz, and buzz
4) Only fizzbuzz
? 3
-- OK! --

---------------------------------------------------------------------
wwrm > Suite 1 > Case 3
(cases remaining: 2)

Q: [-+]?\d*\.?\d+
Choose the number of the correct choice:
0) Only signed numbers like +1000, -1.5
1) Only signed or unsigned integers like +1000, -33
2) Signed or unsigned numbers like +1000, -1.5, .051
3) Only unsigned numbers like 0.051
? 2
-- OK! --

---------------------------------------------------------------------
wwrm > Suite 1 > Case 4
(cases remaining: 1)

Q: [1-9]+[05]+
Choose the number of the correct choice:
0) Any positive number
1) Numbers that are both greater than 5 and divisible by 5 like 10, 25, 800
2) Numbers that are divisible by 5 but do not have the digits 0 and 5 adjacent to each other as the last 2 digits
3) Numbers that are divisible by 5 like 5, 20, 6325
? 1
-- OK! --

---------------------------------------------------------------------
OK! All cases for wwrm unlocked.
```

## Q2: Scientific Name

**lab13/lab13.py**

```py
def scientific_name(name):
    """
    Returns True for strings that are in the correct notation for scientific names;
    i.e. contains a capital letter followed by a period or lowercase letters, 
    followed by a space, followed by more lowercase letters. Returns False for 
    invalid strings.

    >>> scientific_name("T. rex")
    True
    >>> scientific_name("t. rex")
    False
    >>> scientific_name("tyrannosurus rex")
    False
    >>> scientific_name("t rex")
    False
    >>> scientific_name("Falco peregrinus")
    True
    >>> scientific_name("F peregrinus")
    False
    >>> scientific_name("Annie the F. peregrinus")
    False
    >>> scientific_name("I want a pet T. rex right now")
    False
    """
    return bool(re.search(r"^[A-Z]([.]|[a-z]+)\s[a-z]+$", name))
```

## Q3: Calculator Ops

**lab13/lab13.py**

```py
def calculator_ops(calc_str):
    """
    Returns True if an expression from the Calculator language that has two
    numeric operands exists in calc_str, False otherwise.

    >>> calculator_ops("(* 2 4)")
    True
    >>> calculator_ops("(+ (* 3 (+ (* 2 4) (+ 3 5))) (+ (- 10 7) 6))")
    True
    >>> calculator_ops("(* 2)")
    False
    >>> calculator_ops("(/ 8 4 2)")
    False
    >>> calculator_ops("(- 8 3)")
    True
    >>> calculator_ops("+ 3 23")
    False
    """
    return bool(re.search(r"\(([+\-/*]\s+\d+\s+\d+)\)", calc_str))
```

## Q4: Roman Numerals

**lab13/lab13.py**

```py
def roman_numerals(text):
    """
    Returns True if any string of letters that could be a Roman numeral
    (made up of the letters I, V, X, L, C, D, M) is found. Returns False otherwise.

    >>> roman_numerals("Sir Richard IIV, can you tell Richard VI that Richard IV is on the phone?")
    True
    >>> roman_numerals("My TODOs: I. Groceries II. Learn how to count in Roman IV. Profit")
    True
    >>> roman_numerals("I. Act 1 II. Act 2 III. Act 3 IV. Act 4 V. Act 5")
    True
    >>> roman_numerals("Let's play Civ VII")
    True
    >>> roman_numerals("i love vi so much more than emacs.")
    False
    >>> roman_numerals("she loves ALL editors equally.")
    False
    """
    return bool(re.search(r"\b([IVXLCDM]+)\b", text))
```

## Running tests

```py
$ python3 ok
=====================================================================
Assignment: Lab 13
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    7 test cases passed! No cases failed.
```