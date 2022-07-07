# Homework 7 Solution

## Q1: Keyword List: Construct

**hw07/hw07.scm**

```py
(define (make-kwlist1 keys values)
  'YOUR-CODE-HERE
  (list keys values)
)

(define (get-keys-kwlist1 kwlist)
  'YOUR-CODE-HERE
  (car kwlist)
)

(define (get-values-kwlist1 kwlist)
  'YOUR-CODE-HERE
  (cadr kwlist)
)

(define (make-kwlist2 keys values)
  'YOUR-CODE-HERE
  (if (null? keys) nil
                   (cons (list (car keys) (car values))
                         (make-kwlist2 (cdr keys) (cdr values))))
)

(define (get-keys-kwlist2 kwlist)
  'YOUR-CODE-HERE
  (map (lambda (x) (car x)) kwlist)
)

(define (get-values-kwlist2 kwlist)
  'YOUR-CODE-HERE
  (map (lambda (x) (cadr x)) kwlist)
)
```

## Q2: Keyword List: Add

**hw07/hw07.scm**

```py
(define (add-to-kwlist kwlist key value)
  'YOUR-CODE-HERE
  (make-kwlist
    (append (get-keys-kwlist kwlist) (list key))
    (append (get-values-kwlist kwlist) (list value)))
)
```

## Q3: (Optional) Keyword List: Get

**hw07/hw07.scm**

```py
(define (get-first-from-kwlist kwlist key)
  'YOUR-CODE-HERE
  (if (null? (get-keys-kwlist kwlist)) nil
      (let ((values (get-values-kwlist kwlist))
            (keys (get-keys-kwlist kwlist)))
        (cond 
          ((equal? (car keys) key) (car values))
           (else (get-first-from-kwlist (make-kwlist (cdr keys) (cdr values)) key)))))
)
```

## Q4: Prune

**hw07/hw07.scm**

```py
(define (prune-expr expr)
  (define (prune-helper lst)
    'YOUR-CODE-HERE
    (if (or (null? lst) (null? (cdr lst))) lst
        (cons (car lst) (prune-helper (cdr (cdr lst)))))
  )
  'YOUR-CODE-HERE
  (cons (car expr) (prune-helper (cdr expr)))
)
```

## Q5: Cooking Curry

**hw07/hw07.scm**

```py
(define (curry-cook formals body)
  'YOUR-CODE-HERE
  (if (null? formals) body
      `(lambda (,(car formals)) ,(curry-cook (cdr formals) body)))
)
```

## Q6: Consuming Curry

**hw07/hw07.scm**

```py
(define (curry-consume curries args)
  'YOUR-CODE-HERE
  (if (null? args) curries
      (curry-consume (curries (car args)) (cdr args)))
)
```

## Running tests

```py
$ python3 ok
=====================================================================
Assignment: Homework 7
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    7 test cases passed! No cases failed.
```