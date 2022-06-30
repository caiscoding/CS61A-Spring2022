# Lab 11: Interpreters

## Starter Files

Download [lab11.zip](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab11/lab11.zip). Inside the archive, you will find starter files for the questions in this lab, along with a copy of the [Ok](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab11/ok) autograder.

# Introduction

In the [Scheme project](https://cs61a.org/proj/scheme/), you'll be implementing a Python interpreter for Scheme.

Part of the process of interpreting Scheme expressions is being able to **parse** a string of Scheme code as our input into our interpreter's internal Python representation of Scheme expressions. As all Scheme expressions are Scheme lists (and therefore linked lists), we represent all Scheme expressions using the `Pair` class, which behaves as a linked list. **This class is defined in** `pair.py`.

When given an input such as `(+ 1 2)`, there are two main steps we want to take.

The first part of interpreting expressions is taking the input and breaking it down into each component. In our example, we want to treat each of `(`, `+`, `1`, `2`, and `)` as a separate token that we can then figure out how to represent. This is called **lexical analysis**, and has been implemented for you in the `tokenize_lines` function in `scheme_tokens.py`.

Now that we've broken down the input into its component parts, we want to turn these Scheme tokens into our interpreter's internal representations of them. This is called **syntactic analysis**, which happens in `scheme_reader.py` in the `scheme_read` and `read_tail` functions.

- `(` tells us we are starting a call expression.
- `+` will be the operator, as it's the first element in the call expression.
- `1` is our first operand.
- `2` is our second operand.
- `)` tells us that we are ending the call expression.

The main idea is that we'd like to first recognize what the input represents, before we do any of the evaluating, or calling the operator on the operands, and so on.

The goal of this lab is to work with the various parts that go into parsing; while in this lab and in the project, we're focusing on the Scheme language, the general ideas of how we're setting up the Scheme interpreter can be applicable to other languages -- such as Python itself!

# Required Questions

> Check out the [introduction](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab11/#introduction) for the context of this lab.

## Part 1

### Context

We store tokens ready to be parsed in `Buffer` instances. For example, a buffer containing the input `(+ (2 3))` would have the tokens `'('`, `'+'`, `'('`, `2`, `3`, `')'`, and `')'`.

In this part, we will implement the `Buffer` class.

A `Buffer` provides a way of accessing a sequence of tokens across lines.

Its constructor takes an iterator, called "the `source`", that returns the next line of tokens as a list each time it is queried, until it runs out of lines.

For example, `source` could be defined as follows:

```py
line1 = ['(', '+', 6, 1, ')']      # (+ 6 1)
line2 = ['(', 'quote', 'A', ')']  # (quote A)
line3 = [2, 1, 0]                 # 2 1 0
input_lines = [line1, line2, line3]
source = iter(input_lines)
```

In effect, the `Buffer` combines the sequences returned from its source and then supplies the items from them one at a time through its `pop_first` method, calling the `source` for more sequences of items only when needed.

In addition, `Buffer` provides a `current` instance attribute to look at the next item to be supplied, without moving past it.

### Problem 1

> **Important:** Your code for this part should go in `buffer.py`.

Your job in this part is to implement the `create_generator`, `__init__`, and `pop_first` methods of the `Buffer` class.

> **Note:** For this question, you may want to use the built-in function `next` with its `default` argument. Here's an example:
>
> ```py
> >>> iterator = iter([1, 2])
> >>> next(iterator) # Here, there is no default arg given.
> 1
> >>> next(iterator, 5) # Here, there is a default arg given, but not used.
> 2
> >>> next(iterator, 5) # The iterator is exhausted, so next returns default.
> 5
> ```
>
> For more about `next`, feel free to read through the `next` [Python documentation](https://docs.python.org/3/library/functions.html#next).

#### `create_generator`

Implement `create_generator`, a generator function which takes in `source`, an iterator over line(s), each of which is a list that contains token(s).

This function should yield a single token from a line of the source at a time. If there are no more tokens on a line, then it should yield `EOL_TOKEN` (an object that represents an end-of-line token).

If there are no more tokens in the entire source, it should have no more yields. If you were to call `next` on a generator of this function in this case, a `StopIteration` would be raised, as there would be no more applicable yields.

You can reference this function in your implementations for `__init__` and `pop_first`.

> Remember that generator functions can be used as follows:
> 
> ```py
> >>> gen = some_generator_function()
> >>> next(gen)
> # Returns the first yield from some_generator_function
> >>> next(gen)
> # Returns the next yield from some_generator_function
> ```

#### `__init__`

`__init__` takes in the input source `source`. You should define the following instance attributes:

- An instance attribute that holds a generator created by `create_generator` based off of the `source`, and
- `self.current` to represent the current token of the generator that the `Buffer` instance is on. In `__init__`, the current token should be the very first token that the generator yields.

If you wish, you may define more instance attributes as you see fit.

#### `pop_first`

Implement `pop_first`, which does the following:

- Saves the current token of the `Buffer` instance, to be returned later.
- Updates the current token of the `Buffer` instance to the next token from its generator instance.
- If there are no more tokens after the initial current token, then update the current token to be `None`. (Hint: see the note on the default argument to `next` at the beginning of this problem.)
- Returns the initial current token (not the updated current token!).

#### Testing your code

Use Ok to test your code:

```py
python3 ok -q buffer
```

## Part 2

### Internal Representations

The reader will parse Scheme code into Python values with the following representations:

<table>
<tr>
<th>
Input Example
</th>
<th>
Scheme Expression Type
</th>
<th>
Our Internal Representation
</th>
</tr>
<tr>
<td>

`scm> 1`

</td>
<td>
Numbers
</td>
<td>

Python's built-in `int` and `float` values

</td>
</tr>
<tr>
<td>

`scm> x`

</td>
<td>
Symbols
</td>
<td>

Python's built-in `string` values

</td>
</tr>
<tr>
<td>

`scm> #t`

</td>
<td>

Booleans (`#t`, `#f`)

</td>
<td>

Python's built-in `True`, `False` values

</td>
</tr>
<tr>
<td>

`scm> (+ 2 3)`

</td>
<td>
Combinations
</td>
<td>

Instances of the `Pair` class, defined in `scheme_reader.py`. This example is represented as: `Pair('+', Pair(2, Pair(3, nil)))`.

</td>
</tr>
<tr>
<td>

`scm> nil`

</td>
<td>

`nil`

</td>
<td>

The `nil` object, defined in `scheme_reader.py`

</td>
</tr>
</table>

When we refer to combinations here, we are referring to both call expressions and special forms.

### Problem 2

> **Important:** Your code for this part should go in `scheme_reader.py`.

> **Important:** While unlocking this problem, if the token yielded from the `Buffer` instance should be `EOL_TOKEN`, it will be displayed according to the `__repr__` function of the `EOL_TOKEN` class. Specifically, you would get:
>
> ```py
> >>> EOL_TOKEN
> This is a token representing the end of a line.
> ```

Your job in this part is to write the parsing functionality, which consists of two mutually recursive functions: `scheme_read` and `read_tail`. Each function takes in a single `src` parameter, which is a `Buffer` instance.

- `scheme_read` removes enough tokens from `src` to form a single expression and returns that expression in the correct [internal representation](https://inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab11/#internal-representations).
- `read_tail` expects to read the rest of a list or `Pair`, assuming the open parenthesis of that list or `Pair` has already been removed by `scheme_read`. It will read expressions (and thus remove tokens) until the matching closing parenthesis `)` is seen. This list of expressions is returned as a linked list of `Pair` instances.

In short, `scheme_read` returns the next single complete expression in the buffer and `read_tail` returns the rest of a list or `Pair` in the buffer. Both functions mutate the buffer, removing the tokens that have already been processed.

The behavior of both functions depends on the first token currently in `src`. They should be implemented as follows:

`scheme_read`:

- If the current token is the string `"nil"`, return the `nil` object.
- If the current token is `(`, the expression is a pair or list. Call `read_tail` on the rest of `src` and return its result.
- If the current token is `'`, the rest of the buffer should be processed as a `quote` expression. You will implement this portion in the next problem.
- If the next token is not a delimiter, then it must be a primitive expression (i.e. a number, boolean). Return it. **Provided**
- If none of the above cases apply, raise an error. **Provided**

`read_tail`:

- If there are no more tokens, then the list is missing a close parenthesis and we should raise an error. **Provided**
- If the token is `)`, then we've reached the end of the list or pair. **Remove this token from the buffer** and return the `nil` object.
- If none of the above cases apply, the next token is the operator in a combination. For example, `src` could contain `+ 2 3)`. To parse this:
    1. `scheme_read` the next complete expression in the buffer.
    2. Call `read_tail` to read the rest of the combination until the matching closing parenthesis.
    3. Return the results as a `Pair` instance, where the first element is the next complete expression from (1) and the second element is the rest of the combination from (2).

Use Ok to unlock and test your code:

```py
python3 ok -q scheme_read -u
python3 ok -q scheme_read
```

### Problem 3

> **Important:** Your code for this part should go in `scheme_reader.py`.

Your task in this problem is to complete the implementation of `scheme_read` by allowing the function to now be able to handle quoted expressions.

In Scheme, quoted expressions such as `'<expr>` are equivalent to `(quote <expr>)`. That means that we need to wrap the expression following `'` (which you can get by recursively calling `scheme_read`) into the `quote` special form, which is a Scheme list (as with all special forms).

In our representation, a `Pair` represents a Scheme list. You should therefore wrap the expression following `'` in a `Pair`.

For example, `'bagel`, or `["'", "bagel"]` after being tokenized, should be represented as `Pair('quote', Pair('bagel', nil))`. `'(1 2)` (or `["'", "(", 1, 2, ")"]`) should be represented as `Pair('quote', Pair(Pair(1, Pair(2, nil)), nil))`.

Use Ok to unlock and test your code:

```py
python3 ok -q quote -u
python3 ok -q quote
```

## Running your parser

Now that your parser is complete, you can test the read-eval-print loop by running:

```py
python3 scheme_reader.py --repl
```

Every time you type in a value into the prompt, both the `str` and `repr` values of the parsed expression are printed. You can try the following inputs:

```py
read> 42
str : 42
repr: 42
read> nil
str : ()
repr: nil
read> (1 (2 3) (4 (5)))
str : (1 (2 3) (4 (5)))
repr: Pair(1, Pair(Pair(2, Pair(3, nil)), Pair(Pair(4, Pair(Pair(5, nil), nil)), nil)))
```

To exit the interpreter, you can type `exit`.

## Submit

Make sure to submit this assignment by running:

```py
python3 ok --submit
```