# Lab 11 Solution

## Problem 1

**lab11/buffer.py**

```py
def __init__(self, source):
    """
    Initialize a Buffer instance based on the given source.
    """

    # BEGIN
    "*** YOUR CODE HERE ***"
    self.lines = []
    self.curr_line = []
    self.token = self.create_generator(source)
    self.current = next(self.token, None)
    # END

def create_generator(self, source):
    """
    Yield tokens from the source. At the end of every line of source input,
    yield EOL_TOKEN.
    """
    # BEGIN
    "*** YOUR CODE HERE ***"
    for line in source:
        for item in line:
            yield item
        yield EOL_TOKEN
    # END

def pop_first(self):
    """
    Return the current token from self, and update the current token to
    be the next token. If there are no more tokens in the source, update
    the current token to be None.
    """
    # BEGIN
    "*** YOUR CODE HERE ***"
    current = self.current
    if current is EOL_TOKEN:
        self.lines.append(self.curr_line)
        self.curr_line = []
    else:
        self.curr_line.append(current)
    self.current = next(self.token, None)
    return current
    # END
```

## Problem 2

```py
$ python3 ok -q scheme_read -u
=====================================================================
Assignment: Lab 11
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
scheme_read > Suite 1 > Case 1
(cases remaining: 8)

-- Already unlocked --

---------------------------------------------------------------------
scheme_read > Suite 1 > Case 2
(cases remaining: 7)

>>> from scheme_reader import *
>>> tokens = tokenize_lines(["(+ 1 ", "(23 4)) ("])
>>> src = Buffer(tokens)
>>> src.current
? '('
-- OK! --

>>> src.pop_first()
? '('
-- OK! --

>>> src.current
? '+'
-- OK! --

>>> src.pop_first()
? '+'
-- OK! --

>>> src.pop_first()
? 1
-- OK! --

>>> src.current
? This is a token representing the end of a line.
-- OK! --

>>> src.end_of_line()
? True
-- OK! --

>>> src.pop_first()
? This is a token representing the end of a line.
-- OK! --

>>> scheme_read(src)  # Removes the next complete expression in src and returns it as a Pair
? Pair(23, Pair(4, nil))
-- OK! --

>>> src.current
? ')'
-- OK! --

---------------------------------------------------------------------
scheme_read > Suite 1 > Case 3
(cases remaining: 6)

>>> from scheme_reader import *
>>> scheme_read(Buffer(tokenize_lines(['(18 6)']))) # Type SyntaxError if you think this errors
? Pair(18, Pair(6, nil))
-- OK! --

>>> read_line('(18 6)')  # Shorter version of above!
? Pair(18, Pair(6, nil))
-- OK! --

---------------------------------------------------------------------
scheme_read > Suite 1 > Case 4
(cases remaining: 5)

>>> from scheme_reader import *
>>> read_tail(Buffer(tokenize_lines([')'])))
? nil
-- OK! --

>>> read_tail(Buffer(tokenize_lines(['1 2 3)'])))
? Pair(1, Pair(2, Pair(3, nil)))
-- OK! --

>>> read_tail(Buffer(tokenize_lines(['2 (3 4))'])))
? Pair(2, Pair(Pair(3, Pair(4, nil)), nil))
-- OK! --

---------------------------------------------------------------------
scheme_read > Suite 1 > Case 5
(cases remaining: 4)

>>> from scheme_reader import *
>>> read_tail(Buffer(tokenize_lines(['(1 2 3)']))) # Type SyntaxError if you think this errors
? SyntaxError
-- OK! --

>>> read_line('((1 2 3)') # Type SyntaxError if you think this errors
? SyntaxError
-- OK! --

---------------------------------------------------------------------
scheme_read > Suite 1 > Case 6
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
scheme_read > Suite 1 > Case 7
(cases remaining: 2)

>>> from scheme_reader import *
>>> read_line("(+ (- 2 3) 1)")
Choose the number of the correct choice:
0) Pair('+', Pair('-', Pair(2, Pair(3, nil))), Pair(1, nil))
1) Pair('+', Pair(Pair('-', Pair(2, Pair(3, nil))), Pair(1, nil)))
2) Pair('+', Pair('-', Pair(2, Pair(3, Pair(1, nil)))))
? 1
-- OK! --

---------------------------------------------------------------------
scheme_read > Suite 1 > Case 8
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for scheme_read unlocked.
```

**lab11/scheme_reader.py**

```py
def scheme_read(src):
    """Read the next expression from SRC, a Buffer of tokens.

    >>> scheme_read(Buffer(tokenize_lines(['nil'])))
    nil
    >>> scheme_read(Buffer(tokenize_lines(['1'])))
    1
    >>> scheme_read(Buffer(tokenize_lines(['true'])))
    True
    >>> scheme_read(Buffer(tokenize_lines(['(+ 1 2)'])))
    Pair('+', Pair(1, Pair(2, nil)))
    """
    if src.current is None:
        raise EOFError
    val = src.pop_first()  # Get and remove the first token
    if val == 'nil':
        # BEGIN PROBLEM 2
        "*** YOUR CODE HERE ***"
        return nil
        # END PROBLEM 2
    elif val == '(':
        # BEGIN PROBLEM 2
        "*** YOUR CODE HERE ***"
        return read_tail(src)
        # END PROBLEM 2
    elif val == "'":
        # BEGIN PROBLEM 3
        "*** YOUR CODE HERE ***"
        # END PROBLEM 3
    elif val not in DELIMITERS:
        return val
    else:
        raise SyntaxError('unexpected token: {0}'.format(val))


def read_tail(src):
    """Return the remainder of a list in SRC, starting before an element or ).

    >>> read_tail(Buffer(tokenize_lines([')'])))
    nil
    >>> read_tail(Buffer(tokenize_lines(['2 3)'])))
    Pair(2, Pair(3, nil))
    """
    try:
        while src.end_of_line():
            src.pop_first()
        if src.current is None:
            raise SyntaxError('unexpected end of file')
        elif src.current == ')':
            # BEGIN PROBLEM 2
            "*** YOUR CODE HERE ***"
            src.pop_first()
            return nil
            # END PROBLEM 2
        else:
            # BEGIN PROBLEM 2
            "*** YOUR CODE HERE ***"
            first = scheme_read(src)
            rest = read_tail(src)
            return Pair(first, rest)
            # END PROBLEM 2
    except EOFError:
        raise SyntaxError('unexpected end of file')
```

## Problem 3

```py
$ python3 ok -q quote -u
=====================================================================
Assignment: Lab 11
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
quote > Suite 1 > Case 1
(cases remaining: 4)

>>> from scheme_reader import *
>>> read_line(" 'x ")
Choose the number of the correct choice:
0) Pair('quote', Pair('x', nil))
1) 'x'
2) Pair('x', nil)
3) Pair('quote', 'x')
? 0
-- OK! --

>>> read_line(" '(a b) ")
Choose the number of the correct choice:
0) Pair('quote', Pair('a', Pair('b', nil)))
1) Pair('quote', Pair(Pair('a', Pair('b', nil)), nil))
2) Pair('quote', Pair('a', 'b'))
3) Pair('a', Pair('b', nil))
? 1
-- OK! --

---------------------------------------------------------------------
quote > Suite 1 > Case 2
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
quote > Suite 1 > Case 3
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
quote > Suite 1 > Case 4
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for quote unlocked.
```

**lab11/scheme_reader.py**

```py
def scheme_read(src):
    """Read the next expression from SRC, a Buffer of tokens.

    >>> scheme_read(Buffer(tokenize_lines(['nil'])))
    nil
    >>> scheme_read(Buffer(tokenize_lines(['1'])))
    1
    >>> scheme_read(Buffer(tokenize_lines(['true'])))
    True
    >>> scheme_read(Buffer(tokenize_lines(['(+ 1 2)'])))
    Pair('+', Pair(1, Pair(2, nil)))
    """
    if src.current is None:
        raise EOFError
    val = src.pop_first()  # Get and remove the first token
    if val == 'nil':
        # BEGIN PROBLEM 2
        "*** YOUR CODE HERE ***"
        return nil
        # END PROBLEM 2
    elif val == '(':
        # BEGIN PROBLEM 2
        "*** YOUR CODE HERE ***"
        return read_tail(src)
        # END PROBLEM 2
    elif val == "'":
        # BEGIN PROBLEM 3
        "*** YOUR CODE HERE ***"
        return Pair('quote', Pair(scheme_read(src), nil))
        # END PROBLEM 3
    elif val not in DELIMITERS:
        return val
    else:
        raise SyntaxError('unexpected token: {0}'.format(val))
```

## Running tests

```py
$ python3 ok
=====================================================================
Assignment: Lab 11
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    13 test cases passed! No cases failed.
```