# Lab 10: Scheme

## Starter Files

Download [lab10.zip](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab10/lab10.zip). Inside the archive, you will find starter files for the questions in this lab, along with a copy of the [Ok](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab10/ok) autograder.

# Topics

Consult this section if you need a refresher on the material for this lab. It's okay to skip directly to [the questions](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab10/#required-questions) and refer back here should you get stuck.

## Scheme

Scheme is a famous functional programming language from the 1970s. It is a dialect of Lisp (which stands for LISt Processing). The first observation most people make is the unique syntax, which uses a prefix notation and (often many) nested parentheses (see [http://xkcd.com/297/](http://xkcd.com/297/)). Scheme features first-class functions and optimized tail-recursion, which were relatively new features at the time.

> Our course uses a custom version of Scheme (which you will build for Project 4) included in the starter ZIP archive. To start the interpreter, type `python3 scheme`. To run a Scheme program interactively, type `python3 scheme -i <file.scm>`. To exit the Scheme interpreter, type `(exit)`. You may find it useful to try [code.cs61a.org/scheme](https://code.cs61a.org/scheme) when working through problems, as it can draw environment and box-and-pointer diagrams and it lets you walk your code step-by-step (similar to Python Tutor). Don't forget to submit your code through Ok though!

### Scheme Editor

As you're writing your code, you can debug using the Scheme Editor. In your `scheme` folder you will find a new editor. To run this editor, run `python3 editor`. This should pop up a window in your browser; if it does not, please navigate to [localhost:31415](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab10/localhost:31415) and you should see it.

Make sure to run `python3 ok` in a separate tab or window so that the editor keeps running.

If you find that your code works in the online editor but not in your own interpreter, it's possible you have a bug in code from an earlier part that you'll have to track down. Every once in a while there's a bug that our tests don't catch, and if you find one you should let us know!

## Expressions

### Primitive Expressions

Just like in Python, atomic, or primitive, expressions in Scheme take a single step to evaluate. These include numbers, booleans, symbols.

```py
scm> 1234    ; integer
1234
scm> 123.4   ; real number
123.4
```

#### Symbols

Out of these, the symbol type is the only one we didn't encounter in Python. A **symbol** acts a lot like a Python name, but not exactly. Specifically, a symbol in Scheme is also a type of value. On the other hand, in Python, names only serve as expressions; a Python expression can never evaluate to a name.

```py
scm> quotient      ; A name bound to a built-in procedure
#[quotient]
scm> 'quotient     ; An expression that evaluates to a symbol
quotient
scm> 'hello-world!
hello-world!
```

#### Booleans

In Scheme, *all* values except the special boolean value `#f` are interpreted as true values (unlike Python, where there are some false-y values like `0`). Our particular version of the Scheme interpreter allows you to write `True` and `False` in place of `#t` and `#f`. This is not standard.

```py
scm> #t
#t
scm> #f
#f
```

### Call Expressions

Like Python, the operator in a Scheme call expression comes before all the operands. Unlike Python, the operator is included within the parentheses and the operands are separated by spaces rather than with commas. However, evaluation of a Scheme call expression follows the exact same rules as in Python:

1. Evaluate the operator. It should evaluate to a procedure.
2. Evaluate the operands, left to right.
3. Apply the procedure to the evaluated operands.

Here are some examples using built-in procedures:

```py
scm> (+ 1 2)
3
scm> (- 10 (/ 6 2))
7
scm> (modulo 35 4)
3
scm> (even? (quotient 45 2))
#t
```

### Special Forms

The operator of a special form expression is a special form. What makes a special form "special" is that they do not follow the three rules of evaluation stated in the previous section. Instead, each special form follows its own special rules for execution, such as short-circuiting before evaluating all the operands.

Some examples of special forms that we'll study today are the `if`, `cond`, `define`, and `lambda` forms. Read their corresponding sections below to find out what their rules of evaluation are!

## Control Structures

### `if` Expressions

The `if` special form allows us to evaluate one of two expressions based on a predicate. It takes in two required arguments and an optional third argument:

```py
(if <predicate> <if-true> [if-false])
```

The first operand is what's known as a **predicate** expression in Scheme, an expression whose value is interpreted as either `#t` or `#f`.

The rules for evaluating an `if` special form expression are as follows:

1. Evaluate `<predicate>`.
2. If `<predicate>` evaluates to a truth-y value, evaluate and return the value if the expression `<if-true>`. Otherwise, evaluate and return the value of `[if-false]` if it is provided.

Can you see why this expression is a special form? Compare the rules between a regular call expression and an `if` expression. What is the difference?

> Step 2 of evaluating call expressions requires evaluating all of the operands in order. However, an `if` expression will only evaluate two of its operands, the conditional expression and either `<true-result>` or `<false-result>`. Because we don't evaluate all the operands in an `if` expression, it is a special form.

Let's compare a Scheme `if` expression with a Python `if` statement:

<table>
<tr>
<th>
Scheme
</th>
<th>
Python
</th>
</tr>
<tr>
<td>

```py
scm> (if (> x 3)
         1
         2)
```

</td>
<td>

```py
>>> if x > 3:
...     1
... else:
...     2
```

</td>
</tr>
</table>

Although the code may look the same, what happens when each block of code is evaluated is actually very different. Specifically, the Scheme expression, given that it is an expression, evaluates to some value. However, the Python `if` statement simply directs the flow of the program.

Another difference between the two is that it's possible to add more lines of code into the suites of the Python `if` statement, while a Scheme `if` expression expects just a single expression for each of the true result and the false result.

One final difference is that in Scheme, you cannot write `elif` cases. If you want to have multiple cases using the `if` expression, you would need multiple branched `if` expressions:

<table>
<tr>
<th>
Scheme
</th>
<th>
Python
</th>
</tr>
<tr>
<td>

```py
scm> (if (< x 0)
         'negative
         (if (= x 0)
             'zero
             'positive
         )
 )
```

</td>
<td>

```py
>>> if x < 0:
...     'negative'
... else:
...     if x == 0:
...         'zero'
...     else:
...         'positive'
```

</td>
</tr>
</table>

### `cond` Expressions

Using nested `if` expressions doesn't seem like a very practical way to take care of multiple cases. Instead, we can use the `cond` special form, a general conditional expression similar to a multi-clause if/elif/else conditional expression in Python. `cond` takes in an arbitrary number of arguments known as clauses. A clause is written as a list containing two expressions: `(<p> <e>)`.

```py
(cond
    (<p1> <e1>)
    (<p2> <e2>)
    ...
    (<pn> <en>)
    [(else <else-expression>)])
```

The first expression in each clause is a predicate. The second expression in the clause is the return expression corresponding to its predicate. The optional `else` clause has no predicate.

The rules of evaluation are as follows:

1. Evaluate the predicates `<p1>`, `<p2>`, ..., `<pn>` in order until you reach one that evaluates to a truth-y value.
2. If you reach a predicate that evaluates to a truth-y value, evaluate and return the corresponding expression in the clause.
3. If none of the predicates are truth-y and there is an `else` clause, evaluate and return `<else-expression>`.

As you can see, `cond` is a special form because it does not evaluate its operands in their entirety; the predicates are evaluated separately from their corresponding return expression. In addition, the expression short circuits upon reaching the first predicate that evaluates to a truth-y value, leaving the remaining predicates unevaluated.

The following code is roughly equivalent (see the explanation in the [if expression section](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab10/#if-expressions)):

<table>
<tr>
<th>
Scheme
</th>
<th>
Python
</th>
</tr>
<tr>
<td>

```py
scm> (cond
        ((> x 0) 'positive)
        ((< x 0) 'negative)
        (else 'zero))
```

</td>
<td>

```py
>>> if x > 0:
...     'positive'
... elif x < 0:
...     'negative'
... else:
...     'zero'
```

</td>
</tr>
</table>

## Defining Names

The special form `define` is used to define variables and functions in Scheme. There are two versions of the `define` special form. To define variables, we use the `define` form with the following syntax:

```py
(define <name> <expression>)
```

The rules to evaluate this expression are

1. Evaluate the `<expression>`.
2. Bind its value to the `<name>` in the current frame.
3. Return `<name>`.

The second version of `define` is used to define procedures:

```py
(define (<name> <param1> <param2> ...) <body> )
```

To evaluate this expression:

1. Create a lambda procedure with the given parameters and `<body>`.
2. Bind the procedure to the `<name>` in the current frame.
3. Return `<name>`.

The following two expressions are equivalent:

```py
scm> (define foo (lambda (x y) (+ x y)))
foo
scm> (define (foo x y) (+ x y))
foo
```

`define` is a special form because its operands are not evaluated at all! For example, `<body>` is not evaluated when a procedure is defined, but rather when it is called. `<name>` and the parameter names are all names that should not be evaluated when executing this `define` expression.

## Lambda Functions

All Scheme procedures are lambda procedures. To create a lambda procedure, we can use the `lambda` special form:

```py
(lambda (<param1> <param2> ...) <body>)
```

This expression will create and return a function with the given parameters and body, but it will not alter the current environment. This is very similar to a `lambda` expression in Python!

```py
scm> (lambda (x y) (+ x y))        ; Returns a lambda function, but doesn't assign it to a name
(lambda (x y) (+ x y))
scm> ((lambda (x y) (+ x y)) 3 4)  ; Create and call a lambda function in one line
7
```

A procedure may take in any number of parameters. The `<body>` may contain multiple expressions. There is not an equivalent version of a Python `return` statement in Scheme. The function will simply return the value of the last expression in the body.

# Required Questions

## What Would Scheme Display?

### Q1: Combinations

Let's familiarize ourselves with some built-in Scheme procedures and special forms!

> Use Ok to unlock the following "What would Scheme print?" questions:
>
> ```py
> python3 ok -q combinations -u
> ```

```py
scm> (- 10 4)

scm> (* 7 6)

scm> (+ 1 2 3 4)

scm> (/ 8 2 2)

scm> (quotient 29 5)

scm> (modulo 29 5)
```

```py
scm> (= 1 3)                    ; Scheme uses '=' instead of '==' for comparison

scm> (< 1 3)

scm> (or 1 #t)                  ; or special form short circuits

scm> (and #t #f (/ 1 0))

scm> (not #t)
```

```py
scm> (define x 3)

scm> x

scm> (define y (+ x 4))

scm> y

scm> (define x (lambda (y) (* y 2)))

scm> (x y)
```

```py
scm> (if (not (print 1)) (print 2) (print 3))

scm> (* (if (> 3 2) 1 2) (+ 4 5))

scm> (define foo (lambda (x y z) (if x y z)))

scm> (foo 1 2 (print 'hi))

scm> ((lambda (a) (print 'a)) 100)
```

## Coding Questions

### Q2: Over or Under

Define a procedure `over-or-under` which takes in a number `num1` and a number `num2` and returns the following:

- -1 if `num1` is less than `num2`
- 0 if `num1` is equal to `num2`
- 1 if `num1` is greater than `num2`

> Challenge: Implement this in 2 different ways using `if` and `cond`!

```py
(define (over-or-under num1 num2)
  'YOUR-CODE-HERE
)
```

Use Ok to test your code:

```py
python3 ok -q over_or_under
```

### Q3: Make Adder

Write the procedure `make-adder` which takes in an initial number, `num`, and then returns a procedure. This returned procedure takes in a number `inc` and returns the result of `num + inc`.

> *Hint:* To return a procedure, you can either return a `lambda` expression or `define` another nested procedure. Remember that Scheme will automatically return the last clause in your procedure.
>
> You can find documentation on the syntax of `lambda` expressions in [the 61A scheme specification](https://cs61a.org/articles/scheme-spec/#lambda)!

```py
(define (make-adder num)
  'YOUR-CODE-HERE
)
```

Use Ok to test your code:

```py
python3 ok -q make_adder
```

### Q4: Compose

Write the procedure `composed`, which takes in procedures `f` and `g` and outputs a new procedure. This new procedure takes in a number `x` and outputs the result of calling `f` on `g` of `x`.

```py
(define (composed f g)
  'YOUR-CODE-HERE
)
```

Use Ok to test your code:

```py
python3 ok -q composed
```

### Q5: Pow

Implement a procedure `pow` for raising the number `base` to the power of a nonnegative integer `exp` for which the number of operations grows logarithmically, rather than linearly (the number of recursive calls should be much smaller than the input `exp`). For example, for `(pow 2 32)` should take 5 recursive calls rather than 32 recursive calls. Similarly, `(pow 2 64)` should take 6 recursive calls.

> *Hint:* Consider the following observations:
>
> 1. $x^{2y} = (x^{y})^{2}$
> 2. $x^{2y+1} = x(x^{y})^{2}$
>
> For example we see that $2^{32}$ is $(2^{16})^{2}$, $2^{16}$ is $(2^{8})^{2}$, etc. You may use the built-in predicates `even?` and `odd?`. Scheme doesn't support iteration in the same manner as Python, so consider another way to solve this problem.

```py
(define (square n) (* n n))

(define (pow base exp)
  'YOUR-CODE-HERE
)
```

Use Ok to unlock and test your code:

```py
python3 ok -q pow -u
python3 ok -q pow
```

## Submit

Make sure to submit this assignment by running:

```py
python3 ok --submit
```