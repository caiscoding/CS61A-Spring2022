# Lab 12: Scheme Data Abstraction

## Starter Files

Download [lab12.zip](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab12/lab12.zip). Inside the archive, you will find starter files for the questions in this lab, along with a copy of the [Ok](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab12/ok) autograder.

# Topics

Consult this section if you need a refresher on the material for this lab. It's okay to skip directly to [the questions](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab12/#required-questions) and refer back here should you get stuck.

## Data Abstractions

Data abstraction is a powerful concept in computer science that allows programmers to treat code as objects. For example, using code to represent cars, chairs, people, and so on. That way, programmers don't have to worry about how code is implemented; they just have to know what it does.

Data abstraction mimics how we think about the world. If you want to drive a car, you don't need to know how the engine was built or what kind of material the tires are made of to do so. You just have to know how to use the car for driving itself, such as how to turn the wheel or press the gas pedal.

A data abstraction consists of two types of functions:

- **Constructors:** functions that build the abstract data type.
- **Selectors:** functions that retrieve information from the data type.

Programmers design data abstractions to abstract away how information is stored and calculated such that the end user does not need to know how constructors and selectors are implemented. The nature of abstraction allows whoever uses them to assume that the functions have been written correctly and work as described. Using this idea, developers are able to use a variety of powerful libraries for tasks such as data processing, security, visualization, and more without needing to write the code themselves!

In Python, you primarily worked with data abstractions using Object Oriented Programming, which used Python `Object`s to store the data. Notably, this is not possible in Scheme, which is a functional programming language. Instead, we create and return new structures which represent the current state of the data.

## Example Data Abstractions

### `Rational`

Recall that a [rational number](https://en.wikipedia.org/wiki/Rational_number) is any number that can be expressed as *p / q*, where *p* and *q* are integers.

```py
; Creates the rational number n/d (Assume n, d are integers and d != 0)
; Note that the constructor simplifies the numerator and denominator.
(rational n d)

; Gets the numerator of rational number r
(numer r) 

; Gets the denominator of rational number r
(denom r)

; Adds two rational numbers x and y
(add-rational x y)

; Multiplies two rational numbers x and y
(mul-rational x y)
```

### Trees

Below is a Scheme-ified data abstraction of the Tree class we've been working with this semester.

```py
; Constructs tree given label and list of branches
(tree label branches)

; Returns the label of the tree
(label t)

; Returns the list of branches of the given tree
(branches t)

; Returns #t if t is a leaf, #f otherwise
(is-leaf t)
```

# Questions

## What Would Scheme Do?

### Q1: WWSD: Data Abstractions

Let's familiarize ourselves with some Scheme data abstractions!

> If you need a refresher on the `tree` and `rational` abstractions, refer to this lab's introduction or [Monday 04/11's lecture](https://cs61a.org/lecture/lec31/).

Use Ok to test your knowledge with the following "What Would Python Display?" questions:

```py
python3 ok -q abstractions -u
```

```py
scm> (load rational.scm)
scm> (define x (rational 2 5))

scm> (numer x)

scm> (denom x)

scm> (define y (rational 1 4))

scm> (define z1 (add-rational x y))

scm> (numer z1)

scm> (denom z1)

scm> (define z2 (mul-rational x y)) ; don't forget to reduce the rational!

scm> (numer z2)

scm> (denom z2)
```

```py
scm> (load tree.scm)
scm> (define t (tree 1 (list (tree 2 nil)) ))

scm> (label t)

scm> (length (branches t))

scm> (define child (car (branches t)))

scm> (label child)

scm> (is-leaf child)

scm> (branches child)
```

```py
scm> (load tree.scm)
scm> (define b1 (tree 5 (list (tree 6 nil) (tree 7 nil)) )) 

scm> (map is-leaf (branches b1))    ; draw the tree if you get stuck!

scm> (define b2 (tree 8 (list (tree 9 (list (tree 10 nil)) )) )) 

scm> (map is-leaf (branches b2))    ; draw the tree if you get stuck!

scm> (define t (tree 11 (list b1 b2)))

scm> (label t)

scm> (map (lambda (b) (label b)) (branches t)) ; draw the tree if you get stuck!
```

## Code Writing Questions

> Remember that when working with data abstractions, you should **not** break the abstraction barrier if possible! Later questions will have abstraction checks, where the underlying representation of the abstraction will be changed; thus, attempting to refer to specifics of the implementation will break. Attempt to use the functions you are creating to interface with the classes whenever possible.

### Cities

Say we have an abstract data type for cities. A city has a name, a latitude coordinate, and a longitude coordinate.

Our data abstraction has one **constructor**:

- `(make-city name lat lon)`: Creates a city object with the given name, latitude, and longitude.

We also have the following **selectors** in order to get the information for each city:

- `(get-name city)`: Returns the city's name
- `(get-lat city)`: Returns the city's latitude
- `(get-lon city)`: Returns the city's longitude

Here is how we would use the constructor and selectors to create cities and extract their information:

```py
scm> (define berkeley (make-city 'Berkeley 122 37))
berkeley
scm> (get-name berkeley)
Berkeley
scm> (get-lat berkeley)
122
scm> (define new-york (make-city 'NYC 74 40))
new-york
scm> (get-lon new-york)
40
```

All of the selector and constructor functions can be found in the lab file, if you are curious to see how they are implemented. However, the point of data abstraction is that we do not need to know how an abstract data type is implemented, but rather just how we can interact with and use the data type.

### Q2: Distance

We will now implement the function `distance`, which computes the *Euclidean distance* between two city objects; the Euclidean distance between two coordinate pairs `(x1, y1)` and `(x2, y2)` can be found by calculating the `sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)`. Use the latitude and longitude of a city as its coordinates; you'll need to use the selectors to access this info!

> You may find the following methods useful:
>
> - `(expt base exp)`: calculate `base ** exp`
> - `(sqrt x)` calculate `sqrt(x)`

```py
(define (distance city-a city-b)
    'YOUR-CODE-HERE
)
```

Use Ok to test your code:

```py
python3 ok -q city_distance
```

### Q3: Closer city

Next, implement `closer-city`, a function that takes a latitude, longitude, and two cities, and returns the name of the city that is relatively closer to the provided latitude and longitude.

You may only use the selectors and constructors introduced above and the `distance` function you just defined for this question.

> **Hint:** How can you use your `distance` function to find the distance between the given location and each of the given cities?

```py
(define (closer-city lat lon city-a city-b)
    'YOUR-CODE-HERE
)
```

Use Ok to test your code:

```py
python3 ok -q city_closer
```

### Teachers and Students

In the following questions, you'll be implementing data abstractions for students and teachers:

1. The `teacher` abstraction keeps track of the teacher's `name`, the `class` they teach, and the `students` enrolled in their class. Specifically, a `teacher`'s `name` and `class` are atomic symbols, and their `students` is a list of `student` objects.
2. The `student` abstraction keeps track of a student's `name` and number of `classes` attended. Specifically, a `student`'s `name` is an atomic symbol, and their `classes` is a list of atomic symbols representing all classes attended. For example, if a student had attended `cs61a` and `astronomy`, their `classes` list would be `(cs61a astronomy)`.

You can find the constructors for these classes below:

```py
(define (student-create name classes) (cons name classes))
(define (teacher-create name class students) (cons name (cons class students)))
```

### Q4: Teachers and Students: Selectors

Implement `student-get-name`, `student-get-classes`, `teacher-get-name`, `teacher-get-class`, and `teacher-get-students`. These functions take in a `student` or `teacher` abstraction, and return the relevant attribute; for example, `student-get-name` takes a `student` as input, and returns the `name`.

```py
(define (student-get-name student)
    'YOUR-CODE-HERE
)

(define (student-get-classes student)
    'YOUR-CODE-HERE
)

(define (teacher-get-name teacher)
    'YOUR-CODE-HERE
)

(define (teacher-get-class teacher)
    'YOUR-CODE-HERE
)

(define (teacher-get-students teacher)
    'YOUR-CODE-HERE
)
```

Use Ok to test your code:

```py
python3 ok -q teacher_student_selectors
```

### Q5: Students: Attend Class

Implement `student-attend-class`. This method takes in a `student` and a `class` as input, and returns a *new* `student` abstraction with the `class` list updated to reflect the `class` attended.

> Be sure to keep the abstraction barrier in mind!

```py
(define (student-attend-class student class)
    'YOUR-CODE-HERE
)
```

Use Ok to test your code:

```py
python3 ok -q student_attend_class
```

### Q6: Teachers: Hold Discussion

Implement `teacher-hold-class`. This method takes in a `teacher` as input, and emulates holding a class. Specifically, the function should return a *new* updated `teacher`, where all `student` objects in the `teacher`'s `students` list have updated `class` lists to reflect their attendance.

> Be sure to keep the abstraction barrier in mind! Feel free to use any of the functions implemented in previous parts of this lab. You may also find the `map` function useful.

```py
(define (teacher-hold-class teacher)
    'YOUR-CODE-HERE
)
```

Use Ok to test your code:

```py
python3 ok -q teacher_hold_class
```

## Submit

Make sure to submit this assignment by running:

```py
python3 ok --submit
```