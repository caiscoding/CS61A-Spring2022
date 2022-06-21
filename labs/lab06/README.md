# Lab 6: Object-Oriented Programming

## Starter Files

Download [lab06.zip](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab06/lab06.zip). Inside the archive, you will find starter files for the questions in this lab, along with a copy of the [Ok](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab06/ok) autograder.

# Topics

Consult this section if you need a refresher on the material for this lab. It's okay to skip directly to [the questions](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab06/#required-questions) and refer back here should you get stuck.

## Object-Oriented Programming

**Object-oriented programming** (OOP) is a style of programming that allows you to think of code in terms of "objects." Here's an example of a `Car` class:

```py
class Car:
    num_wheels = 4

    def __init__(self, color):
        self.wheels = Car.num_wheels
        self.color = color

    def drive(self):
        if self.wheels <= Car.num_wheels:
            return self.color + ' car cannot drive!'
        return self.color + ' car goes vroom!'

    def pop_tire(self):
        if self.wheels > 0:
            self.wheels -= 1
```

Here's some terminology:

- **class:** a blueprint for how to build a certain type of object. The `Car` class (shown above) describes the behavior and data that all `Car` objects have.
- **instance:** a particular occurrence of a class. In Python, we create instances of a class like this:

    ```py
    >>> my_car = Car('red')
    ```

    `my_car` is an instance of the `Car` class.
- **data attributes:** a variable that belongs to the instance (also called instance variables). Think of a data attribute as a quality of the object: cars have wheels and *color*, so we have given our `Car` instance `self.wheels` and `self.color` attributes. We can access attributes using **dot notation**:

    ```py
    >>> my_car.color
    'red'
    >>> my_car.wheels
    4
    ```
- **method:** Methods are just like normal functions, except that they are bound to an instance. Think of a method as a "verb" of the class: cars can drive and also *pop their tires*, so we have given our `Car` instance the methods `drive` and `pop_tire`. We call methods using **dot notation**:

    ```py
    >>> my_car = Car('red')
    >>> my_car.drive()
    'red car goes vroom!'
    ```
- **constructor:** Constructors build an instance of the class. The constructor for car objects is `Car(color)`. When Python calls that constructor, it immediately calls the `__init__` method. That's where we initialize the data attributes:

    ```py
    def __init__(self, color):
        self.wheels = Car.num_wheels
        self.color = color
    ```

    The constructor takes in one argument, `color`. As you can see, this constructor also creates the `self.wheels` and `self.color` attributes.

- **self:** in Python, `self` is the first parameter for many methods (in this class, we will only use methods whose first parameter is `self`). When a method is called, `self` is bound to an instance of the class. For example:

    ```py
    >>> my_car = Car('red')
    >>> car.drive()
    ```

    Notice that the `drive` method takes in `self` as an argument, but it looks like we didn't pass one in! This is because the dot notation implicitly passes in `car` as `self` for us.

## Inheritance

Python classes can implement a useful abstraction technique known as **inheritance**. To illustrate this concept, consider the following `Dog` and `Cat` classes.

```py
class Dog():
    def __init__(self, name, owner):
        self.is_alive = True
        self.name = name
        self.owner = owner
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    def talk(self):
        print(self.name + " says woof!")

class Cat():
    def __init__(self, name, owner, lives=9):
        self.is_alive = True
        self.name = name
        self.owner = owner
        self.lives = lives
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    def talk(self):
        print(self.name + " says meow!")
```

Notice that because dogs and cats share a lot of similar qualities, there is a lot of repeated code! To avoid redefining attributes and methods for similar classes, we can write a single **base class** from which the similar classes **inherit**. For example, we can write a class called **Pet** and redefine **Dog** as a **subclass** of **Pet**:

```py
class Pet():
    def __init__(self, name, owner):
        self.is_alive = True    # It's alive!!!
        self.name = name
        self.owner = owner
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    def talk(self):
        print(self.name)

class Dog(Pet):
    def talk(self):
        print(self.name + ' says woof!')
```

Inheritance represents a hierarchical relationship between two or more classes where one class **is a** (no relation to the Python `is` operator) more specific version of the other, e.g. a dog is a pet. Because `Dog` inherits from `Pet`, we didn't have to redefine `__init__` or `eat`. However, since we want `Dog` to `talk` in a way that is unique to dogs, we did **override** the `talk` method.

We can use the `super()` function to refer to a class's superclass. For example, calling `super()` within the class definition of `Dog` allows us to access the same object but as if it were an instance of its superclass, in this case `Pet`. This is a little bit of a simplification, and if you're interested you can read more at https://docs.python.org/3/library/functions.html#super.

Here's an example of an alternate equivalent definition of `Dog` that uses `super()` to explicitly call the `__init__` method of the parent class:

```py
class Dog(Pet):
    def __init__(self, name, owner):
        super().__init__(name, owner)
        # this is equivalent to calling Pet.__init__(self, name, owner)
    def talk(self):
        print(self.name + ' says woof!')
```

Keep in mind that creating the `__init__` function shown above is actually not necessary, because creating a `Dog` instance will automatically call the `__init__` method of `Pet`. Normally when defining an `__init__` method in a subclass, we take some additional action to calling `super().__init__`. For example, we could add a new instance variable like the following:

```py
def __init__(self, name, owner, has_floppy_ears):
    super().__init__(name, owner)
    self.has_floppy_ears = has_floppy_ears
```

# Required Questions

## What Would Python Do?

These questions use inheritance. For an overview of inheritance, see the [inheritance portion](http://composingprograms.com/pages/25-object-oriented-programming.html#inheritance) of Composing Programs.

### Q1: WWPD: Classy Cars

Below is the definition of a `Car` class that we will be using in the following WWPD questions.

> **Note:** The `Car` class definition can also be found in `car.py`.

```py
class Car:
    num_wheels = 4
    gas = 30
    headlights = 2
    size = 'Tiny'

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.color = 'No color yet. You need to paint me.'
        self.wheels = Car.num_wheels
        self.gas = Car.gas

    def paint(self, color):
        self.color = color
        return self.make + ' ' + self.model + ' is now ' + color

    def drive(self):
        if self.wheels < Car.num_wheels or self.gas <= 0:
            return 'Cannot drive!'
        self.gas -= 10
        return self.make + ' ' + self.model + ' goes vroom!'

    def pop_tire(self):
        if self.wheels > 0:
            self.wheels -= 1

    def fill_gas(self):
        self.gas += 20
        return 'Gas level: ' + str(self.gas)
```

For the later unlocking questions, we will be referencing the `MonsterTruck` class below.

> **Note:** The `MonsterTruck` class definition can also be found in `car.py`.

```py
 class MonsterTruck(Car):
     size = 'Monster'

     def rev(self):
         print('Vroom! This Monster Truck is huge!')

     def drive(self):
         self.rev()
         return super().drive()
```

You can find the unlocking questions below.

> Use Ok to test your knowledge with the following "What Would Python Display?" questions:
>
> ```
> python3 ok -q wwpd-car -u
> ```
>
> **Important:** For all WWPD questions, type `Function` if you believe the answer is `<function...>`, `Error` if it errors, and `Nothing` if nothing is displayed.

```py
>>> deneros_car = Car('Tesla', 'Model S')
>>> deneros_car.model
______

>>> deneros_car.gas = 10
>>> deneros_car.drive()
______

>>> deneros_car.drive()
______

>>> deneros_car.fill_gas()
______

>>> deneros_car.gas
______

>>> Car.gas
______
```

```py
>>> deneros_car = Car('Tesla', 'Model S')
>>> deneros_car.wheels = 2
>>> deneros_car.wheels
______

>>> Car.num_wheels
______

>>> deneros_car.drive()
______

>>> Car.drive()
______

>>> Car.drive(deneros_car)
______
```

```py
>>> deneros_car = MonsterTruck('Monster', 'Batmobile')
>>> deneros_car.drive()
______

>>> Car.drive(deneros_car)
______

>>> MonsterTruck.drive(deneros_car)
______

>>> Car.rev(deneros_car)
______
```

## Parsons Problems

To work on these problems, open the Parsons editor:

```
python3 parsons
```

### Q2: Cool Cats

The `Cat` class models a cat: you can find the implementation below. Now, you will implement `NoisyCat`; `NoisyCats` are very similar to `Cat`s, but `talk`s twice as much. However, in exchange for such great powers, it gives up one of its initial `lives`.

Use superclass methods wherever possible.

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

    def talk(self):
        "*** YOUR CODE HERE ***"
```

## Coding Practice

### Q3: Cat Adoption

So far, you've implemented the `NoisyCat` based off of the `Cat` class. However, you now want to be able to create lots of different `Cat`s!

Build on the `Cat` class from the earlier problem by adding a **class method** called `adopt_a_cat`. This class method allows you to create `Cat`s that can then be adopted.

Specifically, `adopt_a_cat` should return a new instance of a `Cat` whose owner is `owner`.

This `Cat` instance's name and number of lives depends on the `owner`. Its name should be chosen from `cat_names` (provided in the skeleton code), and should correspond to the name at the index `len(owner)` `%` (modulo) the number of possible cat names. Its number of lives should be equal to `len(owner)` + the length of the chosen name.

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
        return cls(____, ____, ____)
```

Use Ok to test your code:

```
python3 ok -q Cat.adopt_a_cat
```

### Accounts

Let's say we'd like to model a bank account that can handle interactions such as depositing funds or gaining interest on current funds. In the following questions, we will be building off of the `Account` class. Here's our current definition of the class:

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
```

### Q4: Retirement

Add a `time_to_retire` method to the `Account` class. This method takes in an `amount` and returns how many years the holder would need to wait in order for the current `balance` to grow to at least `amount`, assuming that the bank adds `balance` times the `interest` rate to the total balance at the end of every year.

```py
def time_to_retire(self, amount):
    """Return the number of years until balance would grow to amount."""
    assert self.balance > 0 and amount > 0 and self.interest > 0
    "*** YOUR CODE HERE ***"
```

Use Ok to test your code:

```
python3 ok -q Account
```

### Q5: FreeChecking

Implement the `FreeChecking` class, which is like the `Account` class from lecture except that it charges a withdraw fee after 2 withdrawals. If a withdrawal is unsuccessful, it still counts towards the number of free withdrawals remaining, but no fee for the withdrawal will be charged.

> **Hint:** Don't forget that `FreeChecking` inherits from `Account`! Check the Inheritance section in Topics for a refresher.

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
```

Use Ok to test your code:

```
python3 ok -q FreeChecking
```

## Submit

Make sure to submit this assignment by running:

```
python3 ok --submit
```