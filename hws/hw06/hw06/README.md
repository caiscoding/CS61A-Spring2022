# Homework 6 Solution

## Q1: Thane of Cadr

```py
$ python3 ok -q cadr-caddr -u
=====================================================================
Assignment: Homework 6
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
cadr-caddr > Suite 1 > Case 1
(cases remaining: 3)

scm> (load-all ".")
scm> (cddr '(1 2 3 4))
? (3 4)
-- OK! --

---------------------------------------------------------------------
cadr-caddr > Suite 1 > Case 2
(cases remaining: 2)

scm> (load-all ".")
scm> (cadr '(1 2 3 4))
? 2
-- OK! --

---------------------------------------------------------------------
cadr-caddr > Suite 1 > Case 3
(cases remaining: 1)

scm> (load-all ".")
scm> (caddr '(1 2 3 4))
? 3
-- OK! --

---------------------------------------------------------------------
OK! All cases for cadr-caddr unlocked.
```

**hw06/hw06.scm**

```py
(define (cddr s) (cdr (cdr s)))
  
(define (cadr s)
    'YOUR-CODE-HERE
    (car (cdr s))
)

(define (caddr s)
    'YOUR-CODE-HERE
    (car (cddr s))
)
```

## Q2: Ascending

```py
$ python3 ok -q ascending -u
=====================================================================
Assignment: Homework 6
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
ascending? > Suite 1 > Case 1
(cases remaining: 4)

scm> (load-all ".")
scm> (ascending? '(1 2 3 4 5))  ; #t or #f
? #t
-- OK! --

---------------------------------------------------------------------
ascending? > Suite 1 > Case 2
(cases remaining: 3)

scm> (load-all ".")
scm> (ascending? '(1 5 2 4 3))  ; #t or #f
? #f
-- OK! --

---------------------------------------------------------------------
ascending? > Suite 1 > Case 3
(cases remaining: 2)

scm> (load-all ".")
scm> (ascending? '(2 2))  ; #t or #f
? #t
-- OK! --

---------------------------------------------------------------------
ascending? > Suite 1 > Case 4
(cases remaining: 1)

scm> (load-all ".")
scm> (ascending? '(1 2 2 4 3))  ; #t or #f
? #f
-- OK! --

---------------------------------------------------------------------
OK! All cases for ascending? unlocked.
```

**hw06/hw06.scm**

```py
(define (ascending? lst)
    'YOUR-CODE-HERE
    (cond
        ((null? lst) #t)
        ((null? (cdr lst)) #t)
        ((> (car lst) (cadr lst)) #f)
        (else (ascending? (cdr lst)))
    )
)
```

## Q3: Interleave

```py
$ python3 ok -q interleave -u
=====================================================================
Assignment: Homework 6
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
interleave > Suite 1 > Case 1
(cases remaining: 6)

scm> (load-all ".")
scm> (interleave (list 1 3 5) (list 2 4))
? (1 2 3 4 5)
-- OK! --

---------------------------------------------------------------------
interleave > Suite 1 > Case 2
(cases remaining: 5)

scm> (load-all ".")
scm> (interleave (list 2 4) (list 1 3 5))
? (2 1 4 3 5)
-- OK! --

---------------------------------------------------------------------
interleave > Suite 1 > Case 3
(cases remaining: 4)

scm> (load-all ".")
scm> (interleave (list 1 2) (list 1 2))
? (1 1 2 2)
-- OK! --

---------------------------------------------------------------------
interleave > Suite 1 > Case 4
(cases remaining: 3)

scm> (load-all ".")
scm> (interleave '(1 2 3 4 5 6) '(7 8))
? (1 7 2 8 3 4 5 6)
-- OK! --

---------------------------------------------------------------------
interleave > Suite 2 > Case 1
(cases remaining: 2)

scm> (load-all ".")
scm> (interleave (list 1 3 5) (list 2 4 6))
? (1 2 3 4 5 6)
-- OK! --

---------------------------------------------------------------------
interleave > Suite 2 > Case 2
(cases remaining: 1)

scm> (load-all ".")
scm> (interleave (list 1 3 5) nil)
? (1 3 5)
-- OK! --

scm> (interleave nil (list 1 3 5))
? (1 3 5)
-- OK! --

scm> (interleave nil nil)
? ()
-- OK! --

---------------------------------------------------------------------
OK! All cases for interleave unlocked.
```

**hw06/hw06.scm**

```py
(define (interleave lst1 lst2)
    'YOUR-CODE-HERE
    (if (null? lst1) lst2
        (if (null? lst2) lst1
            (cons   (car lst1)
                    (cons   (car lst2)
                            (interleave (cdr lst1) (cdr lst2))
                    )
            )
        )
    )
)
```

## Q4: My Filter

```py
$ python3 ok -q filter -u
=====================================================================
Assignment: Homework 6
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
my-filter > Suite 1 > Case 1
(cases remaining: 6)

scm> (load-all ".")
scm> (my-filter even? '(1 2 3 4))
? (2 4)
-- OK! --

---------------------------------------------------------------------
my-filter > Suite 1 > Case 2
(cases remaining: 5)

scm> (load-all ".")
scm> (my-filter odd? '(1 3 5))
? (1 3 5)
-- OK! --

---------------------------------------------------------------------
my-filter > Suite 1 > Case 3
(cases remaining: 4)

scm> (load-all ".")
scm> (my-filter odd? '(2 4 6 1))
? (1)
-- OK! --

---------------------------------------------------------------------
my-filter > Suite 1 > Case 4
(cases remaining: 3)

scm> (load-all ".")
scm> (my-filter even? '(3))
? ()
-- OK! --

---------------------------------------------------------------------
my-filter > Suite 1 > Case 5
(cases remaining: 2)

scm> (load-all ".")
scm> (my-filter odd? nil)
? ()
-- OK! --

---------------------------------------------------------------------
my-filter > Suite 2 > Case 1
(cases remaining: 1)

scm> (define filter nil)
scm> (load-all ".")
scm> (my-filter even? '(1 2 3 4)) ; checks you dont use builtin filter
? (2 4)
-- OK! --

---------------------------------------------------------------------
OK! All cases for my-filter unlocked.
```

**hw06/hw06.scm**

```py
(define (my-filter func lst)
    'YOUR-CODE-HERE
    (cond   ((null? lst) '())
                ((func  (car lst))
                        (cons (car lst) (my-filter func (cdr lst))))
                        (else (my-filter func (cdr lst)))
    )
)
```

## Q5: No Repeats

```py
$ python3 ok -q no_repeats -u
=====================================================================
Assignment: Homework 6
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
no-repeats > Suite 1 > Case 1
(cases remaining: 7)

scm> (load-all ".")
scm> (no-repeats '(5 4 3 2 1))
? (5 4 3 2 1)
-- OK! --

---------------------------------------------------------------------
no-repeats > Suite 1 > Case 2
(cases remaining: 6)

scm> (load-all ".")
scm> (no-repeats '(5 4 3 2 1 1))
? (5 4 3 2 1)
-- OK! --

---------------------------------------------------------------------
no-repeats > Suite 1 > Case 3
(cases remaining: 5)

scm> (load-all ".")
scm> (no-repeats '(5 5 4 3 2 1))
? (5 4 3 2 1)
-- OK! --

---------------------------------------------------------------------
no-repeats > Suite 1 > Case 4
(cases remaining: 4)

scm> (load-all ".")
scm> (no-repeats '(12))
? (12)
-- OK! --

---------------------------------------------------------------------
no-repeats > Suite 1 > Case 5
(cases remaining: 3)

scm> (load-all ".")
scm> (no-repeats '(1 1 1 1 1 1))
? (1)
-- OK! --

---------------------------------------------------------------------
no-repeats > Suite 2 > Case 1
(cases remaining: 2)

scm> (load-all ".")
scm> (no-repeats (list 5 4 2))
? (5 4 2)
-- OK! --

---------------------------------------------------------------------
no-repeats > Suite 2 > Case 2
(cases remaining: 1)

scm> (load-all ".")
scm> (no-repeats (list 5 4 5 4 2 2))
? (5 4 2)
-- OK! --

scm> (no-repeats (list 5 5 5 5 5))
? (5)
-- OK! --

scm> (no-repeats ())
? ()
-- OK! --

---------------------------------------------------------------------
OK! All cases for no-repeats unlocked.
```

**hw06/hw06.scm**

```py
(define (no-repeats lst)
    'YOUR-CODE-HERE
    (cond   ((null? lst) lst)
            (else (cons (car lst) (no-repeats (filter (lambda (x) (not (= x (car lst)))) (cdr lst)))))
    )
)
```

## Running tests

```py
$ python3 ok
=====================================================================
Assignment: Homework 6
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    26 test cases passed! No cases failed.
```