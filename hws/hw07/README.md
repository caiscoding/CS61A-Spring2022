# Homework 7: Scheme Data Abstractions, Programs as Data

## Instructions

Download [hw07.zip](https://inst.eecs.berkeley.edu/~cs61a/sp22/hw/hw07/hw07.zip). Inside the archive, you will find a file called [hw07.scm](https://inst.eecs.berkeley.edu/~cs61a/sp22/hw/hw07/hw07.scm), along with a copy of the `ok` autograder.

**Submission:** When you are done, submit with `python3 ok --submit`. You may submit more than once before the deadline; only the final submission will be scored. Check that you have successfully submitted your code on [okpy.org](https://okpy.org/). See [Lab 0](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab00#submitting-the-assignment) for more instructions on submitting assignments.

**Using Ok:** If you have any questions about using Ok, please refer to [this guide](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/using-ok).

**Readings:** You might find the following references useful:

- [Scheme Specification](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/scheme-spec/)
- [Scheme Built-in Procedure Reference](https://inst.eecs.berkeley.edu/~cs61a/sp22/articles/scheme-builtins/)

**Grading:** Homework is graded based on correctness. Each incorrect problem will decrease the total score by one point. There is a homework recovery policy as stated in the syllabus. **This homework is out of 2 points.**

Scheme is a famous functional programming language from the 1970s. It is a dialect of Lisp (which stands for LISt Processing). The first observation most people make is the unique syntax, which uses a prefix notation and (often many) nested parentheses (see [http://xkcd.com/297/](http://xkcd.com/297/)). Scheme features first-class functions and optimized tail-recursion, which were relatively new features at the time.

You may find it useful to try [code.cs61a.org/scheme](https://code.cs61a.org/scheme) when working through problems, as it can draw environment and box-and-pointer diagrams and it lets you walk your code step-by-step (similar to Python Tutor). Don't forget to submit your code through Ok though!

## Scheme Editor

As you're writing your code, you can debug using the Scheme Editor. In your `scheme` folder you will find a new editor. To run this editor, run `python3 editor`. This should pop up a window in your browser; if it does not, please navigate to [localhost:31415](localhost:31415) and you should see it.

Make sure to run `python3 ok` in a separate tab or window so that the editor keeps running.

If you find that your code works in the online editor but not in your own interpreter, it's possible you have a bug in code from an earlier part that you'll have to track down. Every once in a while there's a bug that our tests don't catch, and if you find one you should let us know!

## Required Questions

## Getting Started Videos

These videos may provide some helpful direction for tackling the coding problems on this assignment.

> To see these videos, you should be logged into your berkeley.edu email.

[YouTube link](https://youtu.be/watch?v=6jM18JXj-Q4&list=PLx38hZJ5RLZea1rWe3s2JtuCIku_blUu_)

## Keyword Lists

In the following problems, you will explore creating two separate implementations for the same abstraction.

A *keyword list* is the Scheme analogue of a `dict` in Python, with a few key differences:

- It allows for repeating keys
- It functions as a list as well, which allows for ordering.

The `kwlist` abstraction keeps a mapping of `keys` and `values`. To create a `kwlist`, call the constructor `(make-kwlist keys values)` where `keys` is a Scheme list of symbols and `values` is a Scheme list of any type. This returns some abstracted item `lst` that we can call the following methods to either retrieve or add items:

```py
scm> (define lst (make-kwlist '(x y z) '(7 8 9)) ; create the keyword list
lst
scm> (get-first-from-kwlist lst 'x) ; get an item
7
scm> (define lst (add-to-kwlist lst 'a 10)) ; add a new item
lst
scm> (get-first-from-kwlist lst 'a) ; get the new item.
10
```

### Q1: Keyword List: Construct

First, implement abstractions for `kwlist` in two ways, with the following example: `(kwlist '(x y z) '(7 8 9))`

1. `kwlist1`, which stores a keyword list in the following manner: `((key1 key2 key3 ...) (value1 value2 value3 ...)`. With the example above, this should look like `((x y z) (7 8 9))`.
2. `kwlist2`, which stores a keyword list in the following manner: `((key1 value1) (key2 value2) ...)`. With the example above, this should look like `((x 7) (y 8) (z 9))`.

Specifically, implement constructors and selectors for `kwlist1` and `kwlist2`.

- The constructors, `make-kwlist1` and `make-kwlist2`, should take in Scheme lists for both `keys` and `values`, and construct the abstraction as above.
- The selectors, `get-keys-kwlist1`, `get-keys-kwlist2`, `get-values-kwlist1`, and `get-values-kwlist1`, should take in a `kwlist1` or `kwlist2` and return their keys and values respectively. Note that because you are currently creating the implementation, you are "under the abstraction barrier;" feel free to refer to specific details of the structure of `kwlist1` and `kwlist2`.

> **Hint:** The `map` function may prove to be useful, but is not required. You may also use the `cadr` function, which is defined for you in the file.

```py
scm> (define ex-lst1 (make-kwlist1 '(a b c) '(1 2 3)))
ex-list
scm> (get-keys-kwlist1 ex-lst1)
(a b c)
scm> (get-values-kwlist1 ex-lst1)
(1 2 3)
scm> (define ex-lst2 (make-kwlist2 '(a b c) '(1 2 3)))
ex-list
scm> (get-keys-kwlist2 ex-lst)
(a b c)
scm> (get-values-kwlist2 ex-lst)
(1 2 3)
```

```py
(define (make-kwlist1 keys values)
  'YOUR-CODE-HERE
)

(define (get-keys-kwlist1 kwlist)
  'YOUR-CODE-HERE
)

(define (get-values-kwlist1 kwlist)
  'YOUR-CODE-HERE
)
(define (make-kwlist2 keys values)
  'YOUR-CODE-HERE
)

(define (get-keys-kwlist2 kwlist)
  'YOUR-CODE-HERE
)

(define (get-values-kwlist2 kwlist)
  'YOUR-CODE-HERE
)
```

Use Ok to test your code:

```py
python3 ok -q kwlist_construct
```

> **Important:** For the following questions, your implementations should be invariant with respect to the abstraction used; that is, it should work regardless of whether `kwlist1` or `kwlist2` is used. Specifically, in the tests, we will define the abstraction `kwlist` as either `kwlist1` or `kwlist2`:
> 
> ```py
> scm> (define make-kwlist make-kwlist1)
> scm> (define get-keys-kwlist get-keys-kwlist1)
> scm> (define get-values-kwlist get-values-kwlist1)
> ; tests here...
> scm> (define make-kwlist make-kwlist2)
> scm> (define get-keys-kwlist get-keys-kwlist2)
> scm> (define get-values-kwlist get-values-kwlist2)
> ; tests here...
> ```
> 
> **You should refer to the above `kwlist` procedures, not `kwlist1` or `kwlist2`'s procedures in your implementation.**

### Q2: Keyword List: Add

Now, implement `add-to-kwlist`, which implements support for adding a new (`key`, `value`) pair to any implementation of a `kwlist`. Specifically, `add-to-kwlist` takes in a `kwlist`, a `key`, and a `value` as input, and returns a *new* `kwlist` with updated keys and values. Note that `kwlist`s are ordered; that is, a pair `p1` that was added to a `kwlist` before a different pair `p2` should appear earlier in the `kwlist`.

> **Hint:** The `append` method may be useful here. To make your implementation work with both abstractions, *be sure to use methods ending in `kwlist`, not `kwlist1` or `kwlist2`.*

```py
scm> (define ex-lst (make-kwlist '(a b c) '(1 2 3)))
ex-lst
scm> (get-keys-kwlist ex-lst)
(a b c)
scm> (get-values-kwlist ex-lst)
(1 2 3)
scm> (define ex-lst (add-to-kwlist ex-lst 'd '4))
ex-lst
scm> (get-keys-kwlist ex-lst) ; note that new items are at the end of the list!
(a b c d)
scm> (get-values-kwlist ex-lst) ; here too!
(1 2 3 4)
```

```py
(define (add-to-kwlist kwlist key value)
  'YOUR-CODE-HERE
)
```

Use Ok to test your code:

```py
python3 ok -q kwlist_add
```

### Q3: (Optional) Keyword List: Get

Now, implement `get-first-from-kwlist`, which implements support for getting the first value bound to a `key` in `kwlist`. If `key` is not present in the list, the function should return `nil` to indicate that there were no valid keys found.

> **Hint:** Consider using `let` to temporarily bind names to values. To make your implementation work with both abstractions, *be sure to use methods ending in `kwlist`, not `kwlist1` or `kwlist2`.*

```py
scm> (define ex-lst (make-kwlist '(a b c) '(1 2 3)))
ex-lst
scm> (get-first-from-kwlist ex-lst 'b)
2
scm> (get-first-from-kwlist ex-lst 'd) ; if not found, return nil
()
scm> (define ex-lst (add-to-kwlist ex-lst 'd '4))
ex-lst
scm> (get-first-from-kwlist ex-lst 'b)
2
scm> (get-first-from-kwlist ex-lst 'd)
4
scm> (define ex-lst (add-to-kwlist ex-lst 'd '5))
ex-lst
scm> (get-first-from-kwlist ex-lst 'b)
2
scm> (get-first-from-kwlist ex-lst 'd) ; return the *first* occurrence
4
```

```py
(define (get-first-from-kwlist kwlist key)
  'YOUR-CODE-HERE
)
```

Use Ok to test your code:

```py
python3 ok -q kwlist_get
```

## Programs as Data

> **Note that** the following question is separate from the previous questions.

### Q4: Prune

Implement `prune-expr`, a procedure that takes in an expression, which is represented as a list, and returns the same expression with every other argument included. The operator should not be modified.

> **Hint:** You may find it helpful to write a helper function that prunes a list.

The behavior of `prune-expr` is specified by the following doctests:

```py
scm> (prune-expr '(+ 10 20))
(+ 10)
scm> (prune-expr '(+ 10 20 30))
(+ 10 30)
scm> (eval (prune-expr '(+ 10 20 30)))
40
```

```py
(define (prune-expr expr)
    (define (prune-helper lst)
      'YOUR-CODE-HERE
    )
    'YOUR-CODE-HERE
)
```

Use Ok to test your code:

```py
python3 ok -q prune-expr
```

## Chef Curry

Recall that `curry`ing transforms a multiple argument function into a series of higher-order, one argument functions. In the next set of questions, you will be creating functions that can automatically curry a function of any length using the notion that programs are data!

### Q5: Cooking Curry

Implement the function `curry-cook`, which takes in a Scheme list `formals` and a quoted expression `body`. `curry-cook` should generate a program as a list which is a curried version of a lambda function. The outputted program should be a curried version of a lambda function with formal arguments equal to `formals`, and a function body equal to `body`. You may assume that all functions passed in will have more than 0 `formals`; otherwise, it would not be curry-able!

For example, if you wanted to curry the function `(lambda (x y) (+ x y))`, you would set `formals` equal to `'(x y)`, the `body` equal to `'(+ x y)`, and make a call to `curry-cook`: `(curry-cook '(x y) '(+ x y))`.

```py
scm> (curry-cook '(a) 'a)
(lambda (a) a)
scm> (curry-cook '(x y) '(+ x y))
(lambda (x) (lambda (y) (+ x y)))
```

```py
(define (curry-cook formals body)
    'YOUR-CODE-HERE
)
```

Use Ok to test your code:

```py
python3 ok -q curry_cook
```

### Q6: Consuming Curry

Now that you have a function that creates lambda programs as lists, create a function which is able to evaluate lambda functions using a series of arguments. Specifically, implement the function `curry-consume`, which takes in a curried lambda *function* `curries` (not a list), and `apply`s the function to a list of arguments `args`. Similarly to the previous question, you may make several assumptions:

1. If `curries` is an `n`-curried function, then there will be at most `n` arguments in `args`.
2. **If there are 0 arguments**, then you may assume that `curries` has been fully `apply`'d with relevant arguments; in this case, `curries` now contains a value representing the output of the lambda function. Return it.

Note that there can be fewer `args` than `formals` for the corresponding lambda function `curries`! In the case that there are fewer arguments, `curry-consume` should return a curried lambda function, which is the result of partially `apply`ing `curries` up to the number of `args` provdied.

```py
scm> (define three-curry (curry-cook '(x y z) '(+ x (* y z))))
three-curry
scm> three-curry
(lambda (x) (lambda (y) (lambda (z) (+ x (* y z)))))
scm> (define three-curry-fn (eval three-curry)) ; three-curry-fn is a lambda function derived from the program
three-curry-fn
scm> (define eat-two (curry-consume three-curry-fn '(1 2))) ; pass in only two arguments, return should be a one-arg lambda function!
eat-two
scm> eat-two
(lambda (z) (+ x (* y z)))
scm> (eat-two 3) ; pass in the last argument; 1 + (2 * 3)
7
scm> (curry-consume three-curry-fn '(1 2 3)) ; all three arguments at once
7
```

```py
(define (curry-consume curries args)
    'YOUR-CODE-HERE
)
```

Use Ok to test your code:

```py
python3 ok -q curry_consume
```

## Optional Questions

Homework assignments will also contain prior exam-level questions for you to take a look at. These questions have no submission component; feel free to attempt them if you'd like a challenge!

1. Fall 2019 Final Q7c: [*-to-mul](https://cs61a.org/exam/fa19/final/61a-fa19-final.pdf#page=9)
2. Fall 2021 Final Q5a: [Spice](https://cs61a.org/exam/fa21/final/61a-fa21-final.pdf#page=18)