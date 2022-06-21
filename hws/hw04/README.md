# Homework 4: Python Lists, Object-Oriented Programming

## Instructions

Download [hw04.zip](https://inst.eecs.berkeley.edu/~cs61a/sp22/hw/hw04/hw04.zip). Inside the archive, you will find a file called [hw04.py](https://inst.eecs.berkeley.edu/~cs61a/sp22/hw/hw04/hw04.py), along with a copy of the `ok` autograder.

**Submission:** When you are done, submit with `python3 ok --submit`. You may submit more than once before the deadline; only the final submission will be scored. Check that you have successfully submitted your code on [okpy.org](https://okpy.org/). See [Lab 0](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab00#submitting-the-assignment) for more instructions on submitting assignments.

**Using Ok:** If you have any questions about using Ok, please refer to [this guide](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/using-ok).

**Readings:** You might find the following references useful:

- [Section 2.3](http://composingprograms.com/pages/23-sequences.html)
- [Section 2.5](http://composingprograms.com/pages/25-object-oriented-programming.html)

**Grading:** Homework is graded based on correctness. Each incorrect problem will decrease the total score by one point. There is a homework recovery policy as stated in the syllabus. **This homework is out of 2 points.**

# Required questions

## Parsons Problems

To work on these problems, open the Parsons editor:

```
python3 parsons
```

### Q1: Remove Odd Indices

Complete the function `remove_odd_indices`, which takes in a list `lst` and a boolean `odd`, and returns a new list with elements removed at certain indices. If `odd` is `True`, then the function should remove elements at odd indices; otherwise if `odd` is False, then the function should remove even indexed items.

Note that lists are zero-indexed; thus, the first element is at index 0, the second element is at index 1, etc.

```py
def remove_odd_indices(lst, odd):
    """ 
    Remove elements of lst that have odd indices.
    >>> s = [1, 2, 3, 4]
    >>> t = remove_odd_indices(s, True)
    >>> s
    [1, 2, 3, 4]
    >>> t
    [1, 3]
    >>> l = [5, 6, 7, 8]
    >>> m = remove_odd_indices(l, False)
    >>> m
    [6, 8]
    """
    "*** YOUR CODE HERE ***"
```

### Q2: Smart Fridge

The `SmartFridge` class is used by smart refrigerators to track which items are in the fridge and let owners know when an item has run out.

The class internally uses a dictionary to store items, where each key is the item name and the value is the current quantity. The `add_item` method should add the given quantity of the given item and report the current quantity. You can assume that the `use_item` method will only be called on items that are already in the fridge, and it should use up the given quantity of the given item. If the quantity would fall to or below zero, it should only use up to the remaining quantity, and remind the owner to buy more of that item.

Finish implementing the `SmartFridge` class definition so that its `add_item` and `use_item` methods work as expected.

```py
class SmartFridge:
    """"
    >>> fridgey = SmartFridge()
    >>> fridgey.add_item('Mayo', 1)
    'I now have 1 Mayo'
    >>> fridgey.add_item('Mayo', 2)
    'I now have 3 Mayo'
    >>> fridgey.use_item('Mayo', 2.5)
    'I have 0.5 Mayo left'
    >>> fridgey.use_item('Mayo', 0.5)
    'Uh oh, buy more Mayo!'
    """
    def __init__(self):
        self.items = {}
    def add_item(self, item, quantity):
        "*** YOUR CODE HERE ***"
    def use_item(self, item, quantity):
        "*** YOUR CODE HERE ***"
```

## Code Writing Questions

### Q3: Merge

Write a function `merge` that takes 2 *sorted* lists `lst1` and `lst2`, and returns a new list that contains all the elements in the two lists in sorted order. Note: Try to solve this question using recursion instead of iteration.

```py
def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    "*** YOUR CODE HERE ***"
```

Use Ok to test your code:

```
python3 ok -q merge
```

### Q4: Mint

A mint is a place where coins are made. In this question, you'll implement a `Mint` class that can output a `Coin` with the correct year and worth.

- Each `Mint` instance has a `year` stamp. The `update` method sets the `year` stamp to the `present_year` class attribute of the `Mint` class.
- The `create` method takes a subclass of `Coin` and returns an instance of that class stamped with the `mint`'s year (which may be different from `Mint.present_year` if it has not been updated.)
- A `Coin`'s worth method returns the `cents` value of the coin plus one extra cent for each year of age beyond 50. A coin's age can be determined by subtracting the coin's year from the `present_year` class attribute of the `Mint` class.

```py
class Mint:
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.present_year.

    >>> mint = Mint()
    >>> mint.year
    2021
    >>> dime = mint.create(Dime)
    >>> dime.year
    2021
    >>> Mint.present_year = 2101  # Time passes
    >>> nickel = mint.create(Nickel)
    >>> nickel.year     # The mint has not updated its stamp yet
    2021
    >>> nickel.worth()  # 5 cents + (80 - 50 years)
    35
    >>> mint.update()   # The mint's year is updated to 2101
    >>> Mint.present_year = 2176     # More time passes
    >>> mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
    35
    >>> Mint().create(Dime).worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (155 - 50 years)
    115
    >>> Dime.cents = 20  # Upgrade all dimes!
    >>> dime.worth()     # 20 cents + (155 - 50 years)
    125
    """
    present_year = 2021

    def __init__(self):
        self.update()

    def create(self, coin):
        "*** YOUR CODE HERE ***"

    def update(self):
        "*** YOUR CODE HERE ***"

class Coin:
    cents = None # will be provided by subclasses, but not by Coin itself

    def __init__(self, year):
        self.year = year

    def worth(self):
        "*** YOUR CODE HERE ***"

class Nickel(Coin):
    cents = 5

class Dime(Coin):
    cents = 10
```

Use Ok to test your code:

```
python3 ok -q Mint
```

### Q5: Vending Machine

In this question you'll create a [vending machine](https://en.wikipedia.org/wiki/Vending_machine) that only outputs a single product and provides change when needed.

Create a class called `VendingMachine` that represents a vending machine for some product. A `VendingMachine` object returns strings describing its interactions. Remember to match **exactly** the strings in the doctests -- including punctuation and spacing!

Fill in the `VendingMachine` class, adding attributes and methods as appropriate, such that its behavior matches the following doctests:

```py
class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Nothing left to vend. Please restock.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'You must add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
```

> You may find Python's formatted string literals, or [f-strings](https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting) useful. A quick example:
>
> ```py
> >>> feeling = 'love'
> >>> course = '61A!'
> >>> f'I {feeling} {course}'
> 'I love 61A!'
> ```

Use Ok to test your code:

```
python3 ok -q VendingMachine
```

> If you're curious about alternate methods of string formatting, you can also check out an older method of [Python string formatting](https://docs.python.org/2/library/stdtypes.html#str.format). A quick example:
>
> ```py
> >>> ten, twenty, thirty = 10, 'twenty', [30]
> >>> '{0} plus {1} is {2}'.format(ten, twenty, thirty)
> '10 plus twenty is [30]'
> ```

## Submit

Make sure to submit this assignment by running:

```
python3 ok --submit
```