# Lab 10 Solution

## Q1: Combinations

```py
$ python3 ok -q combinations -u
=====================================================================
Assignment: Lab 10
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
What Would Scheme Display? > Suite 1 > Case 1
(cases remaining: 4)


scm> (- 10 4)
? 6
-- OK! --

scm> (* 7 6)
? 42
-- OK! --

scm> (+ 1 2 3 4)
? 10
-- OK! --

scm> (/ 8 2 2)
? 2
-- OK! --

scm> (quotient 29 5)
? 5
-- OK! --

scm> (modulo 29 5)
? 4
-- OK! --

---------------------------------------------------------------------
What Would Scheme Display? > Suite 1 > Case 2
(cases remaining: 3)


scm> (= 1 3)                    ; Scheme uses '=' instead of '==' for comparison
? #f
-- OK! --

scm> (< 1 3)
? #t
-- OK! --

scm> (or 1 #t)                  ; or special form short circuits
? 1
-- OK! --

scm> (and #t #f (/ 1 0))
? #f
-- OK! --

scm> (not #t)
? #f
-- OK! --

---------------------------------------------------------------------
What Would Scheme Display? > Suite 1 > Case 3
(cases remaining: 2)


scm> (define x 3)
? x
-- OK! --

scm> x
? 3
-- OK! --

scm> (define y (+ x 4))
? y
-- OK! --

scm> y
? 7
-- OK! --

scm> (define x (lambda (y) (* y 2)))
? x
-- OK! --

scm> (x y)
? 14
-- OK! --

---------------------------------------------------------------------
What Would Scheme Display? > Suite 1 > Case 4
(cases remaining: 1)


scm> (if (not (print 1)) (print 2) (print 3))
(line 1)? 1
(line 2)? 3
-- OK! --

scm> (* (if (> 3 2) 1 2) (+ 4 5))
? 9
-- OK! --

scm> (define foo (lambda (x y z) (if x y z)))
? foo
-- OK! --

scm> (foo 1 2 (print 'hi))
(line 1)? hi
(line 2)? 2
-- OK! --

scm> ((lambda (a) (print 'a)) 100)
? a
-- OK! --

---------------------------------------------------------------------
OK! All cases for What Would Scheme Display? unlocked.
```

## Q2: Over or Under

**lab10/lab10.scm**

use `if`:

```py
(define (over-or-under num1 num2)
  (if (< num1 num2)
    -1
    (if (= num1 num2)
        0
        1
    )
  )
)
```

use `cond`:

```py
(define (over-or-under num1 num2)
  (cond
    ((< num1 num2) -1)
    ((= num1 num2) 0)
    ((> num1 num2) 1))
)
```

## Q3: Make Adder

**lab10/lab10.scm**

```py
(define (make-adder num)
    (lambda (inc) (+ num inc))
)
```

## Q4: Compose

**lab10/lab10.scm**

```py
(define (composed f g)
    (lambda (x) (f (g x)))
)
```

## Q5: Pow

```py
$ python3 ok -q pow -u
=====================================================================
Assignment: Lab 10
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
pow > Suite 1 > Case 1
(cases remaining: 4)

scm> (load-all ".")
scm> (pow 2 5)
? 32
-- OK! --

---------------------------------------------------------------------
pow > Suite 1 > Case 2
(cases remaining: 3)

scm> (load-all ".")
scm> (pow 10 3)
? 1000
-- OK! --

---------------------------------------------------------------------
pow > Suite 1 > Case 3
(cases remaining: 2)

scm> (load-all ".")
scm> (pow 3 3)
? 27
-- OK! --

---------------------------------------------------------------------
pow > Suite 1 > Case 4
(cases remaining: 1)

scm> (load-all ".")
scm> (pow 1 100000000000000) ; make sure this doesn't run forever!
? 1
-- OK! --

---------------------------------------------------------------------
OK! All cases for pow unlocked.
```

**lab10/lab10.scm**

```py
(define (square n) (* n n))

(define (pow base exp)
    (cond
        ((zero? exp) 1)
        ((even? exp) (square (pow base (/ exp 2))))
        ((odd? exp) (* base (pow base (- exp 1)))))
)
```

## Running tests

```py
$ python3 ok
=====================================================================
Assignment: Lab 10
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    22 test cases passed! No cases failed.
```