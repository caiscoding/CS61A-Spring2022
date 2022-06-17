# Lab 2: Higher-Order Functions, Lambda Expressions

## Starter Files

Download [lab02.zip](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab02/lab02.zip). Inside the archive, you will find starter files for the questions in this lab, along with a copy of the [Ok](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab02/ok) autograder.

# Topics

Consult this section if you need a refresher on the material for this lab. It's okay to skip directly to [the questions](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab02/#required-questions) and refer back here should you get stuck.

## Lambda Expressions

Lambda expressions are expressions that evaluate to functions by specifying two things: the parameters and a return expression.

```
lambda <parameters>: <return expression>
```

While both `lambda` expressions and `def` statements create function objects, there are some notable differences. `lambda` expressions work like other expressions; much like a mathematical expression just evaluates to a number and does not alter the current environment, a `lambda` expression evaluates to a function without changing the current environment. Let's take a closer look.

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
Type
</td>
<td>

*Expression* that evaluates to a value

</td>
<td>

*Statement* that alters the environment

</td>
</tr>
<tr>
<td>
Result of execution
</td>
<td>
Creates an anonymous lambda function with no intrinsic name.
</td>
<td>
Creates a function with an intrinsic name and binds it to that name in the current environment.
</td>
</tr>
<tr>
<td>
Effect on the environment
</td>
<td>

Evaluating a `lambda` expression does not create or modify any variables.

</td>
<td>

Executing a `def` statement both creates a new function object and binds it to a name in the current environment.

</td>
</tr>
<tr>
<td>
Usage
</td>
<td>

A `lambda` expression can be used anywhere that expects an expression, such as in an assignment statement or as the operator or operand to a call expression.

</td>
<td>

After executing a `def` statement, the created function is bound to a name. You should use this name to refer to the function anywhere that expects an expression.

</td>
</tr>
<tr>
<td>
Example
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

We can transform multiple-argument functions into a chain of single-argument, higher order functions. For example, we can write a function `f(x, y)` as a different function `g(x)(y)`. This is known as **currying**.

For example, to convert the function `add(x, y)` into its curried form:

```py
def curry_add(x):
    def add2(y):
        return x + y
    return add2
```

Calling `curry_add(1)` returns a new function which only performs the addition once the returned function is called with the second addend.

```py
>>> add_one = curry_add(1)
>>> add_one(2)
3
>>> add_one(4)
5
```

> Refer to the [textbook](http://composingprograms.com/pages/16-higher-order-functions.html#currying) for more details about currying.

# Required Questions

## What Would Python Display?

> **Important**: For all WWPD questions, type `Function` if you believe the answer is `<function...>`, `Error` if it errors, and `Nothing` if nothing is displayed.

### Q1: WWPD: Lambda the Free

> Use Ok to test your knowledge with the following "What Would Python Display?" questions:
>
> ```
> python3 ok -q lambda -u
> ```
>
> As a reminder, the following two lines of code will not display anything in the Python interpreter when executed:
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

> Use Ok to test your knowledge with the following "What Would Python Display?" questions:
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

## Parsons Problems

To work on these problems, open the Parsons editor:

```
python3 parsons
```

### Q3: A Hop, a Skip, and a Jump

Complete `hop`, which implements a curried version of the function `f(x, y) = y`.

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

Complete the function `digit_index_factory`, which takes in two integers `k` and `num` as input and returns a function. The returned function takes no arguments, and outputs the offset between `k` and the rightmost digit of `num`. The offset between two numbers is defined to be the number of steps between the two numbers. For example, in `25`, there is an offset of `1` between `2` and `5`.

Note that `0` is considered to have no digits (not even `0`).

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

## Coding Practice

### Q5: Lambdas and Currying

Write a function `lambda_curry2` that will curry any two argument function using lambdas.

**Your solution to this problem should fit entirely on the return line.** You can try first writing a solution without the restriction, and then rewriting it into one line after.

> **If the syntax check isn't passing**: Make sure you've removed the line containing `"***YOUR CODE HERE***"` so that it doesn't get treated as part of the function for the syntax check.

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

Use Ok to test your code:

```
python3 ok -q lambda_curry2
```

### Q6: Count van Count

Consider the following implementations of `count_factors` and `count_primes`:

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

The implementations look quite similar! Generalize this logic by writing a function `count_cond`, which takes in a two-argument predicate function `condition(n, i)`. `count_cond` returns a one-argument function that takes in `n`, which counts all the numbers from 1 to `n` that satisfy `condition` when called.

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

Use Ok to test your code:

```
python3 ok -q count_cond
```

## Submit

Make sure to submit this assignment by running:

```
python3 ok --submit
```

# Optional Questions

### Q7: Composite Identity Function

Write a function that takes in two single-argument functions, `f` and `g`, and returns another **function** that has a single parameter `x`. The returned function should return `True` if `f(g(x))` is equal to `g(f(x))`. You can assume the output of `g(x)` is a valid input for `f` and vice versa. Try to use the `composer` function defined below for more HOF practice.

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

Use Ok to test your code:

```
python3 ok -q composite_identity
```

### Q8: I Heard You Liked Functions...

Define a function `cycle` that takes in three functions `f1`, `f2`, `f3`, as arguments. `cycle` will return another function that should take in an integer argument `n` and return another function. That final function should take in an argument `x` and cycle through applying `f1`, `f2`, and `f3` to `x`, depending on what `n` was. Here's what the final function should do to `x` for a few values of `n`:

- `n = 0`, return `x`
- `n = 1`, apply `f1` to `x`, or return `f1(x)`
- `n = 2`, apply `f1` to `x` and then `f2` to the result of that, or return `f2(f1(x))`
- `n = 3`, apply `f1` to `x`, `f2` to the result of applying `f1`, and then `f3` to the result of applying `f2`, or `f3(f2(f1(x)))`
- `n = 4`, start the cycle again applying `f1`, then `f2`, then `f3`, then `f1` again, or `f1(f3(f2(f1(x))))`
- And so forth.

*Hint*: most of the work goes inside the most nested function.

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

Use Ok to test your code:

```
python3 ok -q cycle
```