# Homework 4 Solution

## Q1: Remove Odd Indices

**hw04/parsons_probs/remove_odd_indices.py**

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
    i = 0
    new_list = []
    if not odd:
        i += 1
    while i < len(lst):
        new_list.append(lst[i])
        i = i + 2
    return new_list
```

## Q2: Smart Fridge

**hw04/parsons_probs/smartfridge.py**

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
        if item in self.items.keys():
            self.items[item] +=  quantity
        else:
            self.items[item] = quantity
        return 'I now have {0} {1}'.format(self.items[item], item)

    def use_item(self, item, quantity):
        "*** YOUR CODE HERE ***"
        if self.items[item] <= quantity:
            self.items[item] = 0
            return 'Uh oh, buy more {0}!'.format(item)
        else:
            self.items[item] -= quantity
            return 'I have {0} {1} left'.format(self.items[item], item)
```

## Q3: Merge

**hw04/hw04.py**

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
    if len(lst1) == 0:
        return lst2
    elif len(lst2) == 0:
        return lst1
    new_list = []
    if lst1[0] <= lst2[0]:
        new_list = new_list + [lst1[0]] + merge(lst1[1:], lst2)
    else:
        new_list = new_list + [lst2[0]] + merge(lst1, lst2[1:])
    return new_list
```

## Q4: Mint

**hw04/hw04.py**

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
        return coin(self.year)

    def update(self):
        "*** YOUR CODE HERE ***"
        self.year = Mint.present_year


class Coin:
    cents = None  # will be provided by subclasses, but not by Coin itself

    def __init__(self, year):
        self.year = year

    def worth(self):
        "*** YOUR CODE HERE ***"
        return self.cents + max(0, Mint.present_year - self.year - 50)


class Nickel(Coin):
    cents = 5


class Dime(Coin):
    cents = 10
```

## Q5: Vending Machine

**hw04/hw04.py**

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
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.stock = 0
        self.balance = 0

    def vend(self):
        if self.stock == 0:
            return 'Nothing left to vend. Please restock.'
        else:
            if self.balance < self.price:
                return 'You must add ${0} more funds.'.format(self.price - self.balance)
            else:
                change = self.balance - self.price
                self.balance = 0
                self.stock -= 1
                if change == 0:
                    return 'Here is your {0}.'.format(self.name)
                else:
                    return 'Here is your {0} and ${1} change.'.format(self.name, change)

    def add_funds(self, funds):
        if self.stock != 0:
            self.balance += funds
            return 'Current balance: ${0}'.format(self.balance)
        else:
            return 'Nothing left to vend. Please restock. Here is your ${0}.'.format(funds)

    def restock(self, stock):
        self.stock += stock
        return 'Current {0} stock: {1}'.format(self.name, self.stock)
```

## Running tests

```py
$ python3 ok
=====================================================================
Assignment: Homework 4
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    5 test cases passed! No cases failed.
```