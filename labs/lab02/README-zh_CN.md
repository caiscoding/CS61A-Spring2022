# Lab 2: Higher-Order Functions, Lambda Expressions

## 起始文件

下载 [lab02.zip](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab02/lab02.zip) 。在该压缩包中，你将找到本实验中问题的起始文件，以及 [Ok](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab02/ok) 自动评分器的副本。

# 主题

如果你需要复习本实验的材料，请查阅本节。你可以直接跳到 [问题](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab02/#required-questions) 上，如果遇到困难，可以回到这里。

## Lambda 表达式

Lambda 表达式是通过指定两件事来确定的函数：参数和一个返回表达式。

```
lambda <parameters>: <return expression>
```

虽然 `lambda` 表达式和 `def` 语句都创建了函数，但有一些明显的区别。 `lambda` 表达式的工作方式与其他表达式类似；就像数学表达式只是计算为一个数字，并不改变当前环境一样， `lambda` 表达式计算结果为一个函数而不改变当前环境。让我们仔细看一下。

<table>
<tr>
<th>
</th>
<th>
lambda
</th>
<th>
def
</th>
</tr>
<tr>
<td>
类型
</td>
<td>
计算结果为值的表达式
</td>
<td>
改变环境的声明
</td>
</tr>
<tr>
<td>
执行结果
</td>
<td>
创建一个没有内在名称的匿名 lambda 函数。
</td>
<td>
创建一个具有内在名称的函数并将其绑定到当前环境中的该名称。
</td>
</tr>
<tr>
<td>
对环境的影响
</td>
<td>

计算 `lambda` 表达式不会创建或修改任何变量。

</td>
<td>

执行 `def` 语句会创建一个新的函数对象并将其绑定到当前环境中的名称。

</td>
</tr>
<tr>
<td>
用法
</td>
<td>

`lambda` 表达式可以在任何需要表达式的地方使用，例如在赋值语句中或作为调用表达式的运算符或操作数。

</td>
<td>

执行 `def` 语句后，创建的函数会绑定一个名称。您应该使用此名称来引用任何需要表达式的函数。

</td>
</tr>
<tr>
<td>
例子
</td>
<td>

```py
# A lambda expression by itself does not alter
# the environment
lambda x: x * x

# We can assign lambda functions to a name
# with an assignment statement
square = lambda x: x * x
square(3)

# Lambda expressions can be used as an operator
# or operand
negate = lambda f, x: -f(x)
negate(lambda x: x * x, 3)
```

</td>
<td>

```py
def square(x):
    return x * x

# A function created by a def statement
# can be referred to by its intrinsic name
square(3)
```

</td>
</tr>
</table>

[YouTube link](https://youtu.be/vCeNq_P3akI?list=PLx38hZJ5RLZcUPWZ1-3HYsRPgZ8OCrvqz)

## Currying

我们可以将多参数函数转化为一连串的单参数高阶函数。例如，我们可以把一个函数 `f(x, y)` 写成一个不同的函数 `g(x)(y)` 。这就是所谓的 **currying** 。

例如，将函数 `add(x, y)` 转换为其 **currying** 形式。

```py
def curry_add(x):
    def add2(y):
        return x + y
    return add2
```

调用 `curry_add(1)` 会返回一个新的函数，该函数只在返回的函数被调用时执行加法，并带有第二个加数。

```py
>>> add_one = curry_add(1)
>>> add_one(2)
3
>>> add_one(4)
5
```

> 关于 currying 的更多细节，请参考 [教科书](http://composingprograms.com/pages/16-higher-order-functions.html#currying) 。

# 必要的问题

## What Would Python Display?

> **重要提示：** 对于所有的 WWPD 问题，如果你认为答案是 `<function...>` ，则输入 `Function` ，如果出错则输入 `Error` ，如果没有显示则输入 `Nothing` 。

### Q1: WWPD: Lambda the Free

> 用 Ok 来测试你对知识的理解，有以下“Python会显示什么？”问题：
>
> ```
> python3 ok -q lambda -u
> ```
>
> 作为提醒，以下两行代码在执行时不会在 Python 解释器中显示任何东西：
>
> ```py
> >>> x = None
> >>> x
> ```

```py
>>> lambda x: x  # A lambda expression with one parameter x
______

>>> a = lambda x: x  # Assigning the lambda function to the name a
>>> a(5)
______

>>> (lambda: 3)()  # Using a lambda expression as an operator in a call exp.
______

>>> b = lambda x: lambda: x  # Lambdas can return other lambdas!
>>> c = b(88)
>>> c
______

>>> c()
______

>>> d = lambda f: f(4)  # They can have functions as arguments as well.
>>> def square(x):
...     return x * x
>>> d(square)
______
```

```py
>>> x = None # remember to review the rules of WWPD given above!
>>> x
>>> lambda x: x
______
```

```py
>>> z = 3
>>> e = lambda x: lambda y: lambda: x + y + z
>>> e(0)(1)()
______

>>> f = lambda z: x + z
>>> f(3)
______
```

```py
>>> higher_order_lambda = lambda f: lambda x: f(x)
>>> g = lambda x: x * x
>>> higher_order_lambda(2)(g)  # Which argument belongs to which function call?
______

>>> higher_order_lambda(g)(2)
______

>>> call_thrice = lambda f: lambda x: f(f(f(x)))
>>> call_thrice(lambda y: y + 1)(0)
______

>>> print_lambda = lambda z: print(z)  # When is the return expression of a lambda expression executed?
>>> print_lambda
______

>>> one_thousand = print_lambda(1000)
______

>>> one_thousand
______
```

### Q2: WWPD: Higher Order Functions

> 用 Ok 来测试你对知识的理解，有以下“Python会显示什么？”问题：
>
> ```
> python3 ok -q hof-wwpd -u
> ```

```py
>>> def even(f):
...     def odd(x):
...         if x < 0:
...             return f(-x)
...         return f(x)
...     return odd
>>> steven = lambda x: x
>>> stewart = even(steven)
>>> stewart
______

>>> stewart(61)
______

>>> stewart(-4)
______
```

```py
>>> def cake():
...    print('beets')
...    def pie():
...        print('sweets')
...        return 'cake'
...    return pie
>>> chocolate = cake()
______

>>> chocolate
______

>>> chocolate()
______

>>> more_chocolate, more_cake = chocolate(), cake
______

>>> more_chocolate
______

>>> def snake(x, y):
...    if cake == more_cake:
...        return chocolate
...    else:
...        return x + y
>>> snake(10, 20)
______

>>> snake(10, 20)()
______

>>> cake = 'cake'
>>> snake(10, 20)
______
```

## Parsons 问题

要解决这些问题，请打开 Parsons 编辑器：

```
python3 parsons
```

### Q3: A Hop, a Skip, and a Jump

实现 `hop` 函数，实现 `f(x, y) = y` 的 curried 版本。

```py
def hop():
    """
    Calling hop returns a curried version of the function f(x, y) = y.
    >>> hop()(3)(2) # .Case 1
    2
    >>> hop()(3)(7) # .Case 2
    7
    >>> hop()(4)(7) # .Case 3
    7
    """
    "*** YOUR CODE HERE ***"
```

### Q4: Digit Index Factory

实现函数 `digit_index_factory` ，它接收两个整数 `k` 和 `num` 作为输入并返回一个函数。返回的函数不需要参数，输出 `k` 和 `num` 的最右边的数字之间的偏移量。两个数字之间的偏移量被定义为这两个数字之间的步数。例如，在 `25` 中， `2` 和 `5` 之间有一个 `1` 的偏移。

注意， `0` 被认为是没有存在这个数字的（甚至没有 `0` ）。

```py
def digit_index_factory(num, k):
    """
    Returns a function that takes no arguments, and outputs the offset
    between k and the rightmost digit of num. If k is not in num, then
    the returned function returns -1. Note that 0 is considered to
    contain no digits (not even 0).
    >>> digit_index_factory(34567, 4)() # .Case 1
    3
    >>> digit_index_factory(30001, 0)() # .Case 2
    1
    >>> digit_index_factory(999, 1)() # .Case 3
    -1
    >>> digit_index_factory(1234, 0)() # .Case 4
    -1
    """
    "*** YOUR CODE HERE ***"
```

## 代码编写问题

### Q5: Lambdas and Currying

编写一个函数 `lambda_curry2` ，它将使用 lambdas 任何两个参数的函数。

**你对这个问题的解决方案应该完全适合在返回行中。** 你可以尝试先写一个没有限制的解决方案，然后再改写成一行。

> **如果语法检查没有通过：** 确保你已经删除了包含 `"***YOUR CODE HERE***"` 的那一行，这样它就不会在语法检查中被当作函数的一部分。

```py
def lambda_curry2(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add, mul, mod
    >>> curried_add = lambda_curry2(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    >>> curried_mul = lambda_curry2(mul)
    >>> mul_5 = curried_mul(5)
    >>> mul_5(42)
    210
    >>> lambda_curry2(mod)(123)(10)
    3
    """
    "*** YOUR CODE HERE ***"
    return ______
```

使用 Ok 来测试你的代码：

```
python3 ok -q lambda_curry2
```

### Q6: Count van Count

请考虑以下 `count_factors` 和 `count_primes` 的实现：

```py
def count_factors(n):
    """Return the number of positive factors that n has.
    >>> count_factors(6)
    4   # 1, 2, 3, 6
    >>> count_factors(4)
    3   # 1, 2, 4
    """
    i = 1
    count = 0
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    return count

def count_primes(n):
    """Return the number of prime numbers up to and including n.
    >>> count_primes(6)
    3   # 2, 3, 5
    >>> count_primes(13)
    6   # 2, 3, 5, 7, 11, 13
    """
    i = 1
    count = 0
    while i <= n:
        if is_prime(i):
            count += 1
        i += 1
    return count

def is_prime(n):
    return count_factors(n) == 2 # only factors are 1 and n
```

这些实现方式看起来非常相似 通过编写一个函数 `count_cond` 来概括这个逻辑，该函数接收一个双参数的谓词函数 `condition(n, i)` 。 `count_cond` 返回一个单参数函数，该函数接收 `n` ，在调用时计算从 1 到 `n` 中所有满足 `condition` 的数字。

```py
def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function Condition, where
    the first argument for Condition is N and the second argument is the
    number from 1 to N.

    >>> count_factors = count_cond(lambda n, i: n % i == 0)
    >>> count_factors(2)   # 1, 2
    2
    >>> count_factors(4)   # 1, 2, 4
    3
    >>> count_factors(12)  # 1, 2, 3, 4, 6, 12
    6

    >>> is_prime = lambda n, i: count_factors(i) == 2
    >>> count_primes = count_cond(is_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q count_cond
```

## 提交

请确保在完成后提交：

```
python3 ok --submit
```

# 可选问题

### Q7: Composite Identity Function

编写一个函数，接收两个单参数函数 `f` 和 `g` ，并返回另一个有单参数 `x` 的 **函数** 。如果 `f(g(x))` 等于 `g(f(x))` ，返回的结果应该是 `True` 。你可以假设 `g(x)` 的输出是 `f` 的有效输入，反之亦然。尝试使用下面定义的 `composer` 函数来进行更多的 HOF 练习。

```py
def composer(f, g):
    """Return the composition function which given x, computes f(g(x)).

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2
    >>> a1 = composer(square, add_one)   # (x + 1)^2
    >>> a1(4)
    25
    >>> mul_three = lambda x: x * 3      # multiplies 3 to x
    >>> a2 = composer(mul_three, a1)    # ((x + 1)^2) * 3
    >>> a2(4)
    75
    >>> a2(5)
    108
    """
    return lambda x: f(g(x))

def composite_identity(f, g):
    """
    Return a function with one parameter x that returns True if f(g(x)) is
    equal to g(f(x)). You can assume the result of g(x) is a valid input for f
    and vice versa.

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2
    >>> b1 = composite_identity(square, add_one)
    >>> b1(0)                            # (0 + 1)^2 == 0^2 + 1
    True
    >>> b1(4)                            # (4 + 1)^2 != 4^2 + 1
    False
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q composite_identity
```

### Q8: I Heard You Liked Functions...

定义一个函数 `cycle` ，它接收三个函数 `f1`、 `f2`、 `f3` 作为参数。 `cycle` 将返回另一个函数，该函数应接收一个整数参数 `n` 并返回另一个函数。最后一个函数应该接收一个参数 `x` ，并根据 `n` 的大小，循环应用 `f1`、 `f2` 和 `f3` 于 `x` 。下面是在 `n` 的几个值中，最终函数应该对 `x` 做什么：

- `n = 0`，返回 `x`
- `n = 1`，对 `x` 应用 `f1` ，或返回 `f1(x)`
- `n = 2`，对 `x` 应用 `f1` ，然后对其结果应用 `f2` ，或者返回 `f2(f1(x))`
- `n = 3`，对 `x` 应用 `f1` ，对 `f1` 返回的结果应用 `f2` ，然后对应用 `f2` 的结果应用 `f3` ，或者 `f3(f2(f1(x)))`
- `n = 4`，再次开始循环，应用 `f1` ，然后是 `f2` ，然后是 `f3` ，然后又是 `f1` ，或者 `f1(f3(f2(f1(x))))`
- 以此类推。

*提示：* 大部分工作是嵌套最底层的函数中进行的。

```py
def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q cycle
```