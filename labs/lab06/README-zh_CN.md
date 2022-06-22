# Lab 6: Object-Oriented Programming

## 起始文件

下载 [lab06.zip](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab06/lab06.zip) 。在该压缩包中，你将找到本实验室中问题的起始文件，以及 [Ok](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab06/ok) 自动评分器的副本。

# 主题

如果你需要复习本实验的材料，请查阅本节。你可以直接跳到 [问题](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab06/#required-questions) 上，如果卡住了，可以回到这里。

## 面向对象的编程

**面向对象编程** （OOP）是一种编程风格，它允许你用“对象”来思考。下面是一个 `Car` 类的例子：

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

这里有一些术语：

- **class:** 关于如何构建某种类型的对象的蓝图。 `Car` 类（如上所示）描述了所有 `Car` 对象的行为和数据。
- **instance:** 一个类的特定实现。在 Python 中，我们像这样创建一个类的实例：
    ```py
    >>> my_car = Car('red')
    ```

    `my_car` 是 `Car` 类的一个实例。

- **data attributes:** 属于该实例的变量（也叫实例变量）。把数据属性看作是对象的一部分：汽车有车轮和颜色，所以我们给我们的 `Car` 实例赋予了 `self.wheels` 和 `self.color` 属性。我们可以使用 **点符号** 来访问属性：

    ```py
    >>> my_car.color
    'red'
    >>> my_car.wheels
    4
    ```

- **method:** 方法就像普通的函数，只是它们被绑定到一个实例上。可以把方法看作是类的一个“动词”：汽车可以开，也可以爆胎，所以我们给我们的汽车实例提供了 `drive` 和 `pop_tire` 方法。我们使用 **点符号** 来调用方法：

    ```py
    >>> my_car = Car('red')
    >>> my_car.drive()
    'red car goes vroom!'
    ```

- **constructor:** 构造函数建立一个类的实例。汽车对象的构造函数是 `Car(color)` 。当 Python 调用这个构造函数时，它立即调用 `__init__` 方法。这就是我们初始化数据属性的地方：

    ```py
    def __init__(self, color):
        self.wheels = Car.num_wheels
        self.color = color
    ```

    这个构造函数只接受一个参数，即 `color` 。正如你所看到的，这个构造函数也创建了 `self.wheels` 和 `self.color` 属性。

- **self:** 在 Python 中， `self` 是许多方法的第一个参数（在这个类中，我们将只使用第一个参数是 `self` 的方法）。当一个方法被调用时， `self` 被绑定到该类的一个实例。比如说：

    ```py
    >>> my_car = Car('red')
    >>> car.drive()
    ```

    请注意， `drive` 方法将 `self` 作为一个参数，但看起来我们并没有传入一个参数。这是因为点符号隐含地将 `car` 作为 `self` 传入。

## 继承

Python 类可以实现一种有用的抽象技术，即 **继承** 。为了说明这个概念，请看下面的 `Dog` 和 `Cat` 类。

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

请注意，因为狗和猫有很多相似的属性，所以有很多重复的代码！为了避免为类似的类重新定义属性和方法，我们可以写一个 **基类** ，类似的类从基类 **继承** 。例如，我们可以写一个叫 **Pet** 的类，并把 **Dog** 重新定义为 **Pet** 的子类：

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

继承表示两个或多个类之间的层次关系，其中一个类 **是** 另一个类的（与 Python is 操作符无关）更具体的说，例如，狗是宠物。因为 `Dog` 继承于 `Pet` ，我们不必重新定义 `__init__` 或 `eat` 。然而，由于我们希望 `Dog` 能以狗特有的方式 `talk` ，我们确实 **覆盖** 了 `talk` 方法。

我们可以使用 `super()` 函数来指代一个类的超类。例如，在 `Dog` 类定义中调用 `super()` 允许我们访问同一个对象，但就像它是其超类的一个实例一样，在这个例子中是 `Pet` 。这是一个小小的简化，如果你有兴趣，你可以查看 https://docs.python.org/3/library/functions.html#super 。

这里有一个 `Dog` 的另一个等价定义的例子，它使用 `super()` 来明确地调用父类的 `__init__` 方法：

```py
class Dog(Pet):
    def __init__(self, name, owner):
        super().__init__(name, owner)
        # this is equivalent to calling Pet.__init__(self, name, owner)
    def talk(self):
        print(self.name + ' says woof!')
```

请记住，创建上面所示的 `__init__` 函数实际上是没有必要的，因为创建一个 `Dog` 实例将自动调用 `Pet` 的 `__init__` 方法。通常在子类中定义一个 `__init__` 方法时，我们会采取一些额外的动作来调用 `super().__init__` 。例如，我们可以添加一个新的实例变量，如下所示：

```py
def __init__(self, name, owner, has_floppy_ears):
    super().__init__(name, owner)
    self.has_floppy_ears = has_floppy_ears
```

# 必要的问题

## What Would Python Do?

These questions use inheritance. For an overview of inheritance, see the [inheritance portion](http://composingprograms.com/pages/25-object-oriented-programming.html#inheritance) of Composing Programs.

### Q1: WWPD: Classy Cars

我们将在以下 WWPD 问题中使用的 `Car` 类的定义。

> **注意：** `Car` 类的定义也可以在 `car.py` 中找到。

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

对于后面的解锁问题，我们将参考下面的 `MonsterTruck` 类。

> **注意：** `MonsterTruck` 类的定义也可以在 `car.py` 中找到。

```py
 class MonsterTruck(Car):
     size = 'Monster'

     def rev(self):
         print('Vroom! This Monster Truck is huge!')

     def drive(self):
         self.rev()
         return super().drive()
```

你可以在下面找到解锁的问题。

> 使用 Ok 来测试你对以下“Python会显示什么？”问题的认识：
>
> ```
> python3 ok -q wwpd-car -u
> ```
>
> **重要提示：** 对于所有的 WWPD 问题，如果你认为答案是 `<function...>` ，请输入 `Function` ，如果出错，请输入 `Error` ，如果没有显示，请输入 `Nothing` 。

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

## Parsons 问题

要解决这些问题，请打开 Parsons 编辑器：

```
python3 parsons
```

### Q2: Cool Cats

`Cat` 类为一只猫建模：你可以找到下面的实现。现在，你将实现 `NoisyCat` ； `NoisyCats` 与 `Cat` 非常相似，但 `talk` 的次数是其两倍。然而，为了换取此的能力，它会牺牲 `lives` 属性。

尽可能地使用超类方法。

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

## 代码编写问题

### Q3: Cat Adoption

到目前为止，你已经实现了基于 `Cat` 类的 `NoisyCat` 。然而，你现在希望能够创建很多不同的 `Cat` ！

在前面的问题中，通过添加一个名为 `adopt_a_cat` 的 **类方法** 来建立 `Cat` 类。这个类方法允许你创建可以被收养的 `Cat` 。

具体来说， `adopt_a_cat` 应该返回一个新的 `Cat` 的实例，它的主人就是 `owner` 。

这个 `Cat` 的实例的名字和生命值取决于 `owner` 。它的名字应该从 `cat_names` （在骨架代码中提供）中选择，并且应该对应于索引 `len(owner)` `%` 可能取到的猫名字的数量 。它的生命值应该等于 `len(owner)` + 所选名字的长度。

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

使用 Ok 来测试你的代码：

```
python3 ok -q Cat.adopt_a_cat
```

### Account

假设我们想建立一个银行账户的模型，该账户可以处理诸如存入资金或从当前资金中获得利息等交互行为。在下面的问题中，我们将以 `Account` 类为基础。下面是我们目前对该类的定义：

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

在 `Account` 类中增加一个 `time_to_retire` 方法。这个方法接收一个 `amount` ，并返回持有人需要等待多少年才能使当前的 `balance` 增长到 `amount` ，假设银行在每年年底将 `balance` 乘以 `interest` 加入总余额。

```py
def time_to_retire(self, amount):
    """Return the number of years until balance would grow to amount."""
    assert self.balance > 0 and amount > 0 and self.interest > 0
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q Account
```

### Q5: FreeChecking

实现 `FreeChecking` 类，它和讲座中的 `Account` 类一样，只是在两次取款后会收取取款费用。如果取款不成功，它仍然计入剩余的免费取款次数，但不会收取取款费用。

> **提示：** 不要忘记 `FreeChecking` 是继承自 `Account` ！请查看主题中的继承部分进行复习。

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

使用 Ok 来测试你的代码：

```
python3 ok -q FreeChecking
```

## 提交

请确保在做完实验后提交：

```
python3 ok --submit
```