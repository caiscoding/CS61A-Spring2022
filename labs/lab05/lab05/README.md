# Lab 5 Solution

## Q1: WWPD: List-Mutation

```py
$ python3 ok -q list-mutation -u
=====================================================================
Assignment: Lab 5
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
List Mutation > Suite 1 > Case 1
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> # If nothing would be output by Python, type Nothing
>>> # If the code would error, type Error
>>> lst = [5, 6, 7, 8]
>>> lst.append(6)
? Nothing
-- OK! --

>>> lst
? [5, 6, 7, 8, 6]
-- OK! --

>>> lst.insert(0, 9)
>>> lst
? [9, 5, 6, 7, 8, 6]
-- OK! --

>>> x = lst.pop(2)
>>> lst
? [9, 5, 7, 8, 6]
-- OK! --

>>> lst.remove(x)
>>> lst
? [9, 5, 7, 8]
-- OK! --

>>> a, b = lst, lst[:]
>>> a is lst
? True
-- OK! --

>>> b == lst
? True
-- OK! --

>>> b is lst
? False
-- OK! --

>>> lst = [1, 2, 3]
>>> lst.extend([4,5])
>>> lst
? [1, 2, 3, 4, 5]
-- OK! --

>>> lst.extend([lst.append(9), lst.append(10)])
>>> lst
? [1, 2, 3, 4, 5, 9, 10, None, None]
-- OK! --

---------------------------------------------------------------------
OK! All cases for List Mutation unlocked.
```

## Q2: Replace Elements

**lab05/parsons_probs/replace_elements.py**

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
    for i in range(len(source_list)):
        dest_list[i] = source_list[i]
```

## Q3: Flatten

**lab05/lab05.py**

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
    flatten_list = []
    for item in s:
        if type(item) == list:
            flatten_list += flatten(item)
        else:
            flatten_list += [item]
    return flatten_list
```

## Q4: Couple

**lab05/lab05.py**

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
    couple_list = []
    for i in range(len(s)):
        couple_list.append([s[i], t[i]])
    return couple_list
```

## Q5: Insert Items

**lab05/lab05.py**

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
    i = 0
    while i < len(lst):
        if lst[i] == entry:
            lst.insert(i + 1, elem)
            if elem == entry:
                i += 1
        i += 1
    return lst
```

## Running tests

```py
$ python3 ok
=====================================================================
Assignment: Lab 5
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    5 test cases passed! No cases failed.
```