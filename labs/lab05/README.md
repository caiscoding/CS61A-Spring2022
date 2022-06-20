# Lab 5: Python Lists, Mutability

## Starter Files

Download [lab05.zip](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab05/lab05.zip). Inside the archive, you will find starter files for the questions in this lab, along with a copy of the [Ok](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab05/ok) autograder.

# Topics

Consult this section if you need a refresher on the material for this lab. It's okay to skip directly to [the questions](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab05/#required-questions) and refer back here should you get stuck.

## Lists

A list is a data structure that can store multiple elements. Each element can be any type, even a list itself. We write a list as a comma-separated list of expressions in square brackets:

```py
>>> list_of_ints = [1, 2, 3, 4]
>>> list_of_bools = [True, True, False, False]
>>> nested_lists = [1, [2, 3], [4, [5]]]
```

Each element in the list has an index, with the index of the first element starting at `0`. We say that lists are therefore "zero-indexed."

With list indexing, we can specify the index of the element we want to retrive. A negative index represents starting from the end of the list, so the negative index `-i` is equivalent to the positive index `len(lst)-i`.

```py
>>> lst = [6, 5, 4, 3, 2, 1, 0]
>>> lst[0]
6
>>> lst[3]
3
>>> lst[-1] # Same as lst[6]
0
```

To create a copy of part or all of a list, we can use list slicing. The syntax to slice a list `lst` is: `lst[<start index>:<end index>:<step size>]`.

This expression evaluates to a new list containing the elements of `lst`:

- Starting at and including the element at `<start index>`.
- Up to but not including the element at `<end index>`.
- With `<step size>` as the difference between indices of elements to include.

If the start, end, or step size are not explicitly specified, Python has default values for them. A negative step size indicates that we are stepping backwards through a list when including elements.

```py
>>> lst[:3]   # Start index defaults to 0
[6, 5, 4]
>>> lst[3:]   # End index defaults to len(lst)
[3, 2, 1, 0]
>>> lst[::-1]   # Make a reversed copy of the entire list
[0, 1, 2, 3, 4, 5, 6]
>>> lst[::2]  # Skip every other; step size defaults to 1 otherwise
[6, 4, 2, 0]
```

## List Comprehensions

List comprehensions are a compact and powerful way of creating new lists out of sequences. The general syntax for a list comprehension is the following:

```py
[<expression> for <element> in <sequence> if <conditional>]
```

where the `if <conditional>` section is optional.

The syntax is designed to read like English: "Compute the expression for each element in the sequence (if the conditional is true for that element)."

```py
>>> [i**2 for i in [1, 2, 3, 4] if i % 2 == 0]
[4, 16]
```

This list comprehension will:

- Compute the expression `i**2`
- For each element `i` in the sequence `[1, 2, 3, 4]`
- Where `i % 2 == 0` (`i` is an even number),

and then put the resulting values of the expressions into a new list.

In other words, this list comprehension will create a new list that contains the square of every even element of the original list `[1, 2, 3, 4]`.

We can also rewrite a list comprehension as an equivalent `for` statement, such as for the example above:

```py
>>> lst = []
>>> for i in [1, 2, 3, 4]:
...     if i % 2 == 0:
...         lst = lst + [i**2]
>>> lst
[4, 16]
```

## Mutability

We say that an object is **mutable** if its state can change as code is executed. The process of changing an object's state is called **mutation**. Examples of mutable objects include lists and dictionaries. Examples of objects that are not mutable include tuples and functions.

# Required Questions

## What Would Python Do?

### Q1: WWPD: List-Mutation

> Use Ok to test your knowledge with the following "What Would Python Display?" questions:
>
> ```
> python3 ok -q list-mutation -u
> ```
>
> **Important:** For all WWPD questions, type `Function` if you believe the answer is `<function...>`, `Error` if it errors, and `Nothing` if nothing is displayed.

```py
>>> lst = [5, 6, 7, 8]
>>> lst.append(6)
______

>>> lst
______

>>> lst.insert(0, 9)
>>> lst
______

>>> x = lst.pop(2)
>>> lst
______

>>> lst.remove(x)
>>> lst
______

>>> a, b = lst, lst[:]
>>> a is lst
______

>>> b == lst
______

>>> b is lst
______

>>> lst = [1, 2, 3]
>>> lst.extend([4,5])
>>> lst
______

>>> lst.extend([lst.append(9), lst.append(10)])
>>> lst
______
```

## Parsons Problems

To work on these problems, open the Parsons editor:

```
python3 parsons
```

### Q2: Replace Elements

Complete the function `replace_elements`, a function which takes in `source_list` and `dest_list` and mutates the elements of `dest_list` to be the elements at the corresponding index in `source_list`.

`dest_list` always has a length greater than or equal to the length of `source_list`.

```py
def replace_elements(source_list, dest_list):
    """
    Complete the function replace_elements, a function which takes in source_list
    and dest_list and mutates the elements of dest_list to be the elements at the
    corresponding index in source_list.

    dest_list always has a length greater than or equal to the length of
    source_list.

    >>> s1 = [1, 2, 3]
    >>> s2 = [5, 4]
    >>> replace_elements(s2, s1)
    >>> s1
    [5, 4, 3]
    >>> s3 = [0, 0, 0, 0, 0]
    >>> replace_elements(s1, s3)
    >>> s3
    [5, 4, 3, 0, 0]
    """
    "*** YOUR CODE HERE ***"
```

## Code Writing Questions

### Q3: Flatten

Write a function `flatten` that takes a list and "flattens" it. The list could be a deep list, meaning that there could be a multiple layers of nesting within the list.

For example, one use case of `flatten` could be the following:

```py
>>> lst = [1, [[2], 3], 4, [5, 6]]
>>> flatten(lst)
[1, 2, 3, 4, 5, 6]
```

Make sure your solution does not mutate the input list.

> **Hint:** you can check if something is a list by using the built-in `type` function. For example:
>
> ```py
> >>> type(3) == list
> False
> >>> type([1, 2, 3]) == list
> True
> ```

```py
def flatten(s):
    """Returns a flattened version of list s.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]     # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x # Ensure x is not mutated
    [1, [2, 3], 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    >>> x
    [[1, [1, 1]], 1, [1, 1]]
    """
    "*** YOUR CODE HERE ***"
```

Use Ok to test your code:

```
python3 ok -q flatten
```

### Q4: Couple

Implement the function `couple`, which takes in two lists and returns a list that contains lists with i-th elements of two sequences coupled together. You can assume the lengths of two sequences are the same. Try using a list comprehension.

> *Hint:* You may find the built in [range](https://www.w3schools.com/python/ref_func_range.asp) function helpful.

```py
def couple(s, t):
    """Return a list of two-element lists in which the i-th element is [s[i], t[i]].

    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> couple(a, b)
    [[1, 4], [2, 5], [3, 6]]
    >>> c = ['c', 6]
    >>> d = ['s', '1']
    >>> couple(c, d)
    [['c', 's'], [6, '1']]
    """
    assert len(s) == len(t)
    "*** YOUR CODE HERE ***"
```

Use Ok to test your code:

```
python3 ok -q couple
```

### Q5: Insert Items

Write a function which takes in a list `lst`, an argument `entry`, and another argument `elem`. This function will check through each item in `lst` to see if it is equal to `entry`. Upon finding an item equal to `entry`, the function should modify the list by placing `elem` into `lst` right after the item. At the end of the function, the modified list should be returned.

See the doctests for examples on how this function is utilized.

**Important:** Use list mutation to modify the original list. No new lists should be created or returned.

> **Note:** If the values passed into `entry` and `elem` are equivalent, make sure you're not creating an infinitely long list while iterating through it. If you find that your code is taking more than a few seconds to run, the function may be in a loop of inserting new values.

```py
def insert_items(lst, entry, elem):
    """Inserts elem into lst after each occurence of entry and then returns lst.

    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> double_lst = [1, 2, 1, 2, 3, 3]
    >>> double_lst = insert_items(double_lst, 3, 4)
    >>> double_lst
    [1, 2, 1, 2, 3, 4, 3, 4]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    >>> # Ban creating new lists
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'insert_items',
    ...       ['List', 'ListComp', 'Slice'])
    True
    """
    "*** YOUR CODE HERE ***"
```

Use Ok to test your code:

```
python3 ok -q insert_items
```

## Submit

Make sure to submit this assignment by running:

```
python3 ok --submit
```