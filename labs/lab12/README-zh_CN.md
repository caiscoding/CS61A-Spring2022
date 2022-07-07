# Lab 12: Scheme Data Abstraction

## 起始文件

下载 [lab12.zip](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab12/lab12.zip) 。在该压缩包中，你将找到本实验中问题的起始文件，以及 [Ok](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab12/ok) 自动评分器的副本。

# 主题

如果你需要复习本实验的材料，请参考这一部分。你可以直接跳到 [问题](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab12/#required-questions) 上，如果卡住了，可以回到这里。

## Data Abstractions

数据抽象是计算机科学中一个强大的概念，它允许程序员把代码当作对象。例如，用代码来表示汽车、椅子、人等等。这样一来，程序员就不必担心代码是如何实现的，他们只需要知道它是做什么的。

数据抽象模仿了我们对世界的思考方式。如果你想驾驶一辆汽车，你不需要知道发动机是如何建造的，或者轮胎是由什么材料制成的，就可以做到这一点。你只需要知道如何使用汽车来驾驶，比如如何转动车轮或踩下油门踏板。

一个数据抽象由两种类型的函数组成：

- **构造器：** 构建抽象数据类型的函数。
- **选择器：** 从数据类型中检索信息的函数。

程序员设计数据抽象是为了抽象出信息的存储和计算方式，这样终端用户就不需要知道构造器和选择器是如何实现的。抽象的性质允许使用它们的人假设这些函数是正确编写的，并按照描述的方式工作。利用这种思想，开发人员能够使用各种强大的库来完成数据处理、安全、可视化等任务，而不需要自己编写代码！

在 Python 中，你主要使用面向 `对象` 编程来处理数据抽象，它使用 Python 对象来存储数据。值得注意的是，这在 Scheme 中是不可能的，它是一种函数式编程语言。相反，我们创建并返回新的结构，代表数据的当前状态。

## Example Data Abstractions

### `Rational`

回顾一下， [有理数](https://en.wikipedia.org/wiki/Rational_number) 是可以表示为 *p / q* 的任何数字，其中 *p* 和 *q* 是整数。

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

下面是本学期我们一直在使用的 Tree 类的 Scheme-ified 数据抽象。

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

# 问题

## What Would Scheme Do?

### Q1: WWSD: Data Abstractions

让我们来熟悉一下 Scheme 的一些数据抽象吧！

> 如果你需要复习一下 `tree` 和 `rational` 的抽象，请参考本实验的介绍或 [04/11 星期一的讲座](https://cs61a.org/lecture/lec31/) 。

使用 Ok 来测试你对以下“Python会显示什么？”问题的认识：

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

## 代码编写问题

> 请记住，在处理数据抽象时，如果可能的话，你 **不应该** 打破抽象的屏障！后面的问题会有抽象检查，抽象的底层表示会被改变；因此，试图参考实现的具体内容会被打破。尽量使用你所创建的函数来与类对接。

### Cities

假设我们有一个抽象数据类型——城市。一个城市有一个名字，一个纬度坐标，和一个经度坐标。

我们的数据抽象有一个 **构造函数** ：

- `(make-city name lat lon)`： 创建一个具有给定名称、纬度和经度的城市对象。

我们还有以下 **选择器** ，以便获得每个城市的信息：

- `(get-name city)`：返回城市的名称
- `(get-lat city)`：返回城市的纬度
- `(get-lon city)`：返回城市的经度

下面是我们如何使用构造函数和选择器来创建城市并提取其信息：

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

所有的选择器和构造函数都可以在实验文件中找到，如果你好奇，可以看看它们是如何实现的。然而，数据抽象的意义在于，我们不需要知道一个抽象的数据类型是如何实现的，而只需要知道我们如何与数据类型进行交互和使用。

### Q2: Distance

我们现在要实现函数 `distance` ，它可以计算两个城市对象之间的 *欧氏距离* ；两个坐标对 `(x1, y1)` 和 `(x2, y2)` 之间的欧氏距离可以通过计算 `sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)` 得到。使用一个城市的经纬度作为它的坐标；你需要使用选择器来获取这些信息！

> 你可能会发现以下方法很有用：
>
> - `(expt base exp)`: calculate `base ** exp`
> - `(sqrt x)` calculate `sqrt(x)`

```py
(define (distance city-a city-b)
    'YOUR-CODE-HERE
)
```

使用 Ok 测试你的代码：

```py
python3 ok -q city_distance
```

### Q3: Closer city

接下来，实现 `closer-city` ，这个函数接收一个纬度、经度和两个城市，并返回相对更接近所提供经纬度的城市名称。

在这个问题上，你只能使用上面介绍的选择器和构造器以及你刚才定义的 `distance` 函数。

> **提示：** 你如何使用你的 `distance` 函数来寻找给定地点和每个给定城市之间的距离？

```py
(define (closer-city lat lon city-a city-b)
    'YOUR-CODE-HERE
)
```

使用 Ok 测试你的代码：

```py
python3 ok -q city_closer
```

### Teachers and Students

在下面的问题中，你将为学生和教师实现数据抽象：

1. `teacher` 抽象记录了教师的 `name` ，他们所教的 `class` ，以及在他们班上注册的 `students` 。具体来说， `teacher` 的 `name` 和 `class` 是原子符号，而他们的 `students` 是 `student` 对象的列表。
2. `student` 抽象记录了一个学生的 `name` 和所上的 `classes` 的数量。具体来说， `student` 的 `name` 是一个原子符号，而他们的 `classes` 是一个原子符号的列表，代表所有上过的课。例如，如果一个学生上过 `cs61a` 和 `astronomy` ，他们的 `classes` 列表就是 `(cs61a astronomy)` 。

你可以在下面找到这些课程的构造函数：

```py
(define (student-create name classes) (cons name classes))
(define (teacher-create name class students) (cons name (cons class students)))
```

### Q4: Teachers and Students: Selectors

实现 `student-get-name`、 `student-get-classes`、 `teacher-get-name`、 `teacher-get-class` 和 `teacher-get-students` 。这些函数接收一个 `student` 或 `teacher` 的抽象，并返回相关属性；例如， `student-get-name` 接收一个 `student` 作为输入，并返回 `name` 。

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

使用 Ok 测试你的代码：

```py
python3 ok -q teacher_student_selectors
```

### Q5: Students: Attend Class

实现 `student-attend-class` 。这个方法接收一个 `student` 和一个 `class` 作为输入，并返回一个 *新* 的 `student` 抽象，同时更新 `class` 列表以反映加入的 `class` 。

> 一定要记住抽象！

```py
(define (student-attend-class student class)
    'YOUR-CODE-HERE
)
```

使用 Ok 测试你的代码：

```py
python3 ok -q student_attend_class
```

### Q6: Teachers: Hold Discussion

实现 `teacher-hold-class` 。这个方法接收一个 `teacher` 作为输入，并模拟持有一个班级。具体来说，该函数应该返回一个新的更新的 `teacher` ，其中 `teacher` 的 `students` 列表中的所有 `student` 对象都有更新的 `class` 列表以反映他们的参加情况。

> 请务必牢记抽象！请自由使用本实验前面部分实现的任何函数。你可能还会发现 `map` 函数很有用。

```py
(define (teacher-hold-class teacher)
    'YOUR-CODE-HERE
)
```

使用 Ok 测试你的代码：

```py
python3 ok -q teacher_hold_class
```

## 提交

请确保提交本实验：

```py
python3 ok --submit
```