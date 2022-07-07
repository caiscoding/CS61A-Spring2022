# Lab 12 Solution

## Q1: WWSD: Data Abstractions

```py
$ python3 ok -q abstractions -u
=====================================================================
Assignment: Lab 12
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
What Would Scheme Display? > Suite 1 > Case 1
(cases remaining: 3)

scm> (load "./lab12.scm")
scm> (define x (rational 2 5))
? x
-- OK! --

scm> (numer x)
? 2
-- OK! --

scm> (denom x)
? 5
-- OK! --

scm> (define y (rational 1 4))
? y
-- OK! --

scm> (define z1 (add-rational x y))
? z1
-- OK! --

scm> (numer z1)
? 13
-- OK! --

scm> (denom z1)
? 20
-- OK! --

scm> (define z2 (mul-rational x y))
? z2
-- OK! --

scm> (numer z2)
? 1
-- OK! --

scm> (denom z2)
? 10
-- OK! --

---------------------------------------------------------------------
What Would Scheme Display? > Suite 1 > Case 2
(cases remaining: 2)

scm> (load "./lab12.scm")
scm> (define t (tree 1 (list (tree 2 nil))))
? t
-- OK! --

scm> (label t)
? 1
-- OK! --

scm> (length (branches t))
? 1
-- OK! --

scm> (define child (car (branches t)))
? child
-- OK! --

scm> (label child)
? 2
-- OK! --

scm> (is-leaf child)
? #t
-- OK! --

scm> (branches child)
? ()
-- OK! --

---------------------------------------------------------------------
What Would Scheme Display? > Suite 1 > Case 3
(cases remaining: 1)

scm> (load "./lab12.scm")
scm> (define b1 (tree 5 (list (tree 6 nil) (tree 7 nil)) )) 
? b1
-- OK! --

scm> (map is-leaf (branches b1))  ; draw the tree if you get stuck!
? (#t #t)
-- OK! --

scm> (define b2 (tree 8 (list (tree 9 (list (tree 10 nil)) )) )) 
? b2
-- OK! --

scm> (map is-leaf (branches b2))  ; draw the tree if you get stuck!
? (#f)
-- OK! --

scm> (define t (tree 11 (list b1 b2)))
? t
-- OK! --

scm> (label t)
? 11
-- OK! --

scm> (map (lambda (b) (label b)) (branches t))
? (5 8)
-- OK! --

---------------------------------------------------------------------
OK! All cases for What Would Scheme Display? unlocked.
```

## Q2: Distance

**lab12/lab12.scm**

```py
(define (distance city-a city-b)
    'YOUR-CODE-HERE
    (sqrt (+ (expt (- (get-lat city-a) (get-lat city-b)) 2.0) (expt (- (get-lon city-a) (get-lon city-b)) 2.0)))
)
```

## Q3: Closer city

**lab12/lab12.scm**

```py
(define (closer-city lat lon city-a city-b)
  'YOUR-CODE-HERE
  (define target (make-city 'tar lat lon))
  (define dist1 (distance city-a target))
  (define dist2 (distance city-b target))
  (if (< dist1 dist2)   (get-name city-a)
                        (get-name city-b))
)
```

## Q4: Teachers and Students: Selectors

**lab12/lab12.scm**

```py
(define (student-get-name student)
  'YOUR-CODE-HERE
  (car student)
)

(define (student-get-classes student)
  'YOUR-CODE-HERE
  (cdr student)
)

(define (teacher-get-name teacher)
  'YOUR-CODE-HERE
  (car teacher)
)

(define (teacher-get-class teacher)
  'YOUR-CODE-HERE
  (car (cdr teacher))
)

(define (teacher-get-students teacher)
  'YOUR-CODE-HERE
  (cdr (cdr teacher))
)
```

## Q5: Students: Attend Class

**lab12/lab12.scm**

```py
(define (student-attend-class student class)
  'YOUR-CODE-HERE
  (student-create (student-get-name student)
                  (cons class (student-get-classes student)))
)
```

## Q6: Teachers: Hold Discussion

**lab12/lab12.scm**

```py
(define (teacher-hold-class teacher)
  'YOUR-CODE-HERE
  (define class (teacher-get-class teacher))
  (define new-students
          (map (lambda (x) (student-attend-class x class))
               (teacher-get-students teacher)))
  (teacher-create (teacher-get-name teacher)
                  (teacher-get-class teacher)
                  new-students)
)
```

## Running tests

```py
$ python3 ok
=====================================================================
Assignment: Lab 12
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    12 test cases passed! No cases failed.
```