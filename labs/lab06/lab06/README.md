# Lab 6 Solution

## Q1: WWPD: Classy Cars

```py
$  python3 ok -q wwpd-car -u
=====================================================================
Assignment: Lab 6
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Car > Suite 1 > Case 1
(cases remaining: 3)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> from car import *
>>> deneros_car = Car('Tesla', 'Model S')
>>> deneros_car.model
? 'Model S'
-- OK! --

>>> deneros_car.gas = 10
>>> deneros_car.drive()
? 'Tesla Model S goes vroom!'
-- OK! --

>>> deneros_car.drive()
? 'Cannot drive!'
-- OK! --

>>> deneros_car.fill_gas()
? 'Gas level: 20'
-- OK! --

>>> deneros_car.gas
? 20
-- OK! --

>>> Car.gas
? 30
-- OK! --

---------------------------------------------------------------------
Car > Suite 1 > Case 2
(cases remaining: 2)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> from car import *
>>> deneros_car = Car('Tesla', 'Model S')
>>> deneros_car.wheels = 2
>>> deneros_car.wheels
? 2
-- OK! --

>>> Car.num_wheels
? 4
-- OK! --

>>> deneros_car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
? 'Cannot drive!'
-- OK! --

>>> Car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
? Error
-- OK! --

>>> Car.drive(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed
? 'Cannot drive!'
-- OK! --

---------------------------------------------------------------------
Car > Suite 1 > Case 3
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> from car import *
>>> deneros_car = MonsterTruck('Monster', 'Batmobile')
>>> deneros_car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
(line 1)? Vroom! This Monster Truck is huge!
(line 2)? 'Monster Batmobile goes vroom!'
-- OK! --

>>> Car.drive(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed
? 'Monster Batmobile goes vroom!'
-- OK! --

>>> MonsterTruck.drive(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed
(line 1)? Vroom! This Monster Truck is huge!
(line 2)? 'Monster Batmobile goes vroom!'
-- OK! --

>>> Car.rev(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed
? Error
-- OK! --

---------------------------------------------------------------------
OK! All cases for Car unlocked.
```

## Q2: Cool Cats

**lab06/parsons_probs/noisycat.py**

```py
class Cat:
    def __init__(self, name, owner, lives=9):
        self.is_alive = True
        self.name = name
        self.owner = owner
        self.lives = lives

    def talk(self):
        return self.name + ' says meow!'


class NoisyCat(Cat):
    """
    >>> my_cat = NoisyCat("Furball", "James")
    >>> my_cat.name
    'Furball'
    >>> my_cat.is_alive
    True
    >>> my_cat.lives
    8
    >>> my_cat.talk()
    'Furball says meow! Furball says meow!'
    >>> friend_cat = NoisyCat("Tabby", "James", 2)
    >>> friend_cat.talk()
    'Tabby says meow! Tabby says meow!'
    >>> friend_cat.lives
    1
    """

    def __init__(self, name, owner, lives=9):
        "*** YOUR CODE HERE ***"
        Cat.__init__(self, name, owner, lives)
        self.lives -= 1

    def talk(self):
        "*** YOUR CODE HERE ***"
        return Cat.talk(self) + " " + Cat.talk(self)
```

## Q3: Cat Adoption

**lab06/lab06.py**

```py
class Cat:
    def __init__(self, name, owner, lives=9):
        self.is_alive = True
        self.name = name
        self.owner = owner
        self.lives = lives

    def talk(self):
        return self.name + ' says meow!'

    @classmethod
    def adopt_a_cat(cls, owner):
        """
        Returns a new instance of a Cat.

        This instance's owner is the given owner.
        Its name and its number of lives is chosen programatically
        based on the spec's noted behavior.

        >>> cat1 = Cat.adopt_a_cat("Ifeoma")
        >>> isinstance(cat1, Cat)
        True
        >>> cat1.owner
        'Ifeoma'
        >>> cat1.name
        'Felix'
        >>> cat1.lives
        11
        >>> cat2 = Cat.adopt_a_cat("Ay")
        >>> cat2.owner
        'Ay'
        >>> cat2.name
        'Grumpy'
        >>> cat2.lives
        8
        """
        cat_names = ["Felix", "Bugs", "Grumpy"]
        "*** YOUR CODE HERE ***"
        return cls(cat_names[len(owner) % len(cat_names)], owner, len(owner) + len(cat_names[len(owner) % len(cat_names)]))
```

## Q4: Retirement

**lab06/lab06.py**

```py
class Account:
    """An account has a balance and a holder.
    >>> a = Account('John')
    >>> a.deposit(10)
    10
    >>> a.balance
    10
    >>> a.interest
    0.02
    >>> a.time_to_retire(10.25) # 10 -> 10.2 -> 10.404
    2
    >>> a.balance               # balance should not change
    10
    >>> a.time_to_retire(11)    # 10 -> 10.2 -> ... -> 11.040808032
    5
    >>> a.time_to_retire(100)
    117
    """
    max_withdrawal = 10
    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        if amount > self.max_withdrawal:
            return "Can't withdraw that amount"
        self.balance = self.balance - amount
        return self.balance

    def time_to_retire(self, amount):
        """Return the number of years until balance would grow to amount."""
        assert self.balance > 0 and amount > 0 and self.interest > 0
        "*** YOUR CODE HERE ***"
        sum = 0
        curr_balance = self.balance
        while curr_balance < amount:
            curr_balance += curr_balance * self.interest
            sum += 1
        return sum
```

## Q5: FreeChecking

**lab06/lab06.py**

```py
class FreeChecking(Account):
    """A bank account that charges for withdrawals, but the first two are free!
    >>> ch = FreeChecking('Jack')
    >>> ch.balance = 20
    >>> ch.withdraw(100)  # First one's free
    'Insufficient funds'
    >>> ch.withdraw(3)    # And the second
    17
    >>> ch.balance
    17
    >>> ch.withdraw(3)    # Ok, two free withdrawals is enough
    13
    >>> ch.withdraw(3)
    9
    >>> ch2 = FreeChecking('John')
    >>> ch2.balance = 10
    >>> ch2.withdraw(3) # No fee
    7
    >>> ch.withdraw(3)  # ch still charges a fee
    5
    >>> ch.withdraw(5)  # Not enough to cover fee + withdraw
    'Insufficient funds'
    """
    withdraw_fee = 1
    free_withdrawals = 2

    "*** YOUR CODE HERE ***"
    def __init__(self, account_holder):
        super().__init__(account_holder)

    def withdraw(self, amount):
        if self.free_withdrawals > 0:
            self.free_withdrawals -= 1
            if amount > self.balance:
                return "Insufficient funds"
            self.balance = self.balance - amount
            return self.balance
        else:
            self.free_withdrawals -= 1
            if amount > self.balance - self.withdraw_fee:
                return "Insufficient funds"
            self.balance = self.balance - amount - self.withdraw_fee
            return self.balance
```

## Running tests

```py
$ python3 ok
=====================================================================
Assignment: Lab 6
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    7 test cases passed! No cases failed.
```