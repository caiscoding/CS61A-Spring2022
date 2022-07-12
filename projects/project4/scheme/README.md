# Project 4 Solution

## Part 1: The Evaluator

```py
$ python3 ok -q eval_apply -u
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Understanding Eval/Apply > Suite 1 > Case 1
(cases remaining: 5)

Q: What types of expressions are represented as Pairs?
Choose the number of the correct choice:
0) All expressions are represented as Pairs
1) Only call expressions
2) Call expressions and special forms
3) Only special forms
? 2
-- OK! --

---------------------------------------------------------------------
Understanding Eval/Apply > Suite 1 > Case 2
(cases remaining: 4)

Q: What expression in the body of scheme_eval finds the value of a name?
Choose the number of the correct choice:
0) scheme_forms.SPECIAL_FORMS[first](rest, env)
1) scheme_symbolp(expr)
2) env.lookup(expr)
3) env.find(name)
? 2
-- OK! --

---------------------------------------------------------------------
Understanding Eval/Apply > Suite 1 > Case 3
(cases remaining: 3)

Q: How do we know if a given combination is a special form?
Choose the number of the correct choice:
0) Check if the first element in the list is a symbol
1) Check if the first element in the list is a symbol and that the
   symbol is in the dictionary SPECIAL_FORMS
2) Check if the expression is in the dictionary SPECIAL_FORMS
? 1
-- OK! --

---------------------------------------------------------------------
Understanding Eval/Apply > Suite 1 > Case 4
(cases remaining: 2)

Q: What is the difference between applying builtins and applying user-defined procedures?
(Choose all that apply)

I.   User-defined procedures open a new frame; builtins do not
II.  Builtins simply execute a predefined function; user-defined
     procedures must evaluate additional expressions in the body
III. Builtins have a fixed number of arguments; user-defined procedures do not

---
Choose the number of the correct choice:
0) III only
1) II only
2) I only
3) I, II and III
4) I and II
5) I and III
6) II and III
? 4
-- OK! --

---------------------------------------------------------------------
Understanding Eval/Apply > Suite 1 > Case 5
(cases remaining: 1)

Q: What exception should be raised for the expression (1)?
Choose the number of the correct choice:
0) SchemeError("malformed list: (1)")
1) AssertionError
2) SchemeError("unknown identifier: 1")
3) SchemeError("1 is not callable")
? 3
-- OK! --

---------------------------------------------------------------------
OK! All cases for Understanding Eval/Apply unlocked.
```

## Problem 1 (1 pt)

```py
$ python3 ok -q 01 -u
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 1 > Suite 1 > Case 1
(cases remaining: 5)

>>> from scheme import *
>>> global_frame = create_global_frame()
>>> global_frame.define("x", 3)
>>> global_frame.parent is None
? True
-- OK! --

>>> global_frame.lookup("x")
? 3
-- OK! --

>>> global_frame.define("x", 2)
>>> global_frame.lookup("x")
? 3
-- Not quite. Try again! --

? 2
-- OK! --

>>> global_frame.lookup("foo")
Choose the number of the correct choice:
0) SchemeError
1) 3
2) None
? 0
-- OK! --

---------------------------------------------------------------------
Problem 1 > Suite 1 > Case 2
(cases remaining: 4)

>>> from scheme import *
>>> first_frame = create_global_frame()
>>> first_frame.define("x", 3)
>>> second_frame = Frame(first_frame)
>>> second_frame.parent == first_frame
? True
-- OK! --

>>> second_frame.define("y", False)
>>> second_frame.lookup("x")
? 3
-- OK! --

>>> second_frame.lookup("y")
? False
-- OK! --

---------------------------------------------------------------------
Problem 1 > Suite 1 > Case 3
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem 1 > Suite 1 > Case 4
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Problem 1 > Suite 2 > Case 1
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 1 unlocked.
```

**scheme/scheme_classes.py**

```py
def define(self, symbol, value):
        """Define Scheme SYMBOL to have VALUE."""
        # BEGIN PROBLEM 1
        "*** YOUR CODE HERE ***"
        self.bindings[symbol] = value
        # END PROBLEM 1

def lookup(self, symbol):
    """Return the value bound to SYMBOL. Errors if SYMBOL is not found."""
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    if symbol in self.bindings.keys():
        return self.bindings[symbol]
    elif self.parent is not None:
        return self.parent.lookup(symbol)`
    # END PROBLEM 1
    raise SchemeError('unknown identifier: {0}'.format(symbol))
```

## Problem 2 (2 pt)

```py
$ python3 ok -q 02 -u
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 2 > Suite 1 > Case 1
(cases remaining: 9)

>>> from scheme import *
>>> env = create_global_frame()
>>> twos = Pair(2, Pair(2, nil))
>>> plus = BuiltinProcedure(scheme_add) # + procedure
>>> scheme_apply(plus, twos, env) # Type SchemeError if you think this errors
? 4
-- OK! --

---------------------------------------------------------------------
Problem 2 > Suite 1 > Case 2
(cases remaining: 8)

>>> from scheme import *
>>> env = create_global_frame()
>>> plus = BuiltinProcedure(scheme_add) # + procedure
>>> scheme_apply(plus, nil, env) # Remember what (+) evaluates to in scheme
? 0
-- OK! --

---------------------------------------------------------------------
Problem 2 > Suite 1 > Case 3
(cases remaining: 7)

>>> from scheme import *
>>> env = create_global_frame()
>>> twos = Pair(2, Pair(2, nil))
>>> oddp = BuiltinProcedure(scheme_oddp) # odd? procedure
>>> scheme_apply(oddp, twos, env) # Type SchemeError if you think this errors
? SchemeError
-- OK! --

---------------------------------------------------------------------
Problem 2 > Suite 1 > Case 4
(cases remaining: 6)

-- Already unlocked --

---------------------------------------------------------------------
Problem 2 > Suite 1 > Case 5
(cases remaining: 5)

-- Already unlocked --

---------------------------------------------------------------------
Problem 2 > Suite 1 > Case 6
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Problem 2 > Suite 1 > Case 7
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem 2 > Suite 1 > Case 8
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Problem 2 > Suite 1 > Case 9
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 2 unlocked.
```

**scheme/scheme_eval_apply.py**

```py
def scheme_apply(procedure, args, env):
    """Apply Scheme PROCEDURE to argument values ARGS (a Scheme list) in
    Frame ENV, the current environment."""
    validate_procedure(procedure)
    if isinstance(procedure, BuiltinProcedure):
        # BEGIN PROBLEM 2
        "*** YOUR CODE HERE ***"
        args_list = pair_to_list(args)
        if procedure.expect_env:
            args_list.append(env)
        try:
            return procedure.py_func(*args_list)
        except TypeError:
            raise SchemeError('incorrect number of arguments')
        # END PROBLEM 2
    elif isinstance(procedure, LambdaProcedure):
        # BEGIN PROBLEM 9
        "*** YOUR CODE HERE ***"
        # END PROBLEM 9
    elif isinstance(procedure, MuProcedure):
        # BEGIN PROBLEM 11
        "*** YOUR CODE HERE ***"
        # END PROBLEM 11
    else:
        assert False, "Unexpected procedure: {}".format(procedure)
```

## Problem 3 (2 pt)

```py
$ python3 ok -q 03 -u
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 3 > Suite 1 > Case 1
(cases remaining: 5)

>>> from scheme_reader import *
>>> from scheme import *
>>> expr = read_line('(+ 2 2)')
>>> scheme_eval(expr, create_global_frame()) # Type SchemeError if you think this errors
? 4
-- OK! --

>>> scheme_eval(Pair('+', Pair(2, Pair(2, nil))), create_global_frame()) # Type SchemeError if you think this errors
? 4
-- OK! --

>>> expr = read_line('(+ (+ 2 2) (+ 1 3) (* 1 4))')
>>> scheme_eval(expr, create_global_frame()) # Type SchemeError if you think this errors
? 12
-- OK! --

>>> expr = read_line('(yolo)')
>>> scheme_eval(expr, create_global_frame()) # Type SchemeError if you think this errors
? SchemeError
-- OK! --

---------------------------------------------------------------------
Problem 3 > Suite 2 > Case 1
(cases remaining: 4)


scm> (* (+ 3 2) (+ 1 7)) ; Type SchemeError if you think this errors
? 40
-- OK! --

scm> (1 2) ; Type SchemeError if you think this errors
? SchemeError
-- OK! --

scm> (1 (print 0)) ; validate_procedure should be called before operands are evaluated
? SchemeError
-- OK! --

---------------------------------------------------------------------
Problem 3 > Suite 2 > Case 2
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem 3 > Suite 2 > Case 3
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Problem 3 > Suite 2 > Case 4
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 3 unlocked.
```

**scheme/scheme_eval_apply.py**

```py
def scheme_eval(expr, env, _=None):  # Optional third argument is ignored
    """Evaluate Scheme expression EXPR in Frame ENV.

    >>> expr = read_line('(+ 2 2)')
    >>> expr
    Pair('+', Pair(2, Pair(2, nil)))
    >>> scheme_eval(expr, create_global_frame())
    4
    """
    # Evaluate atoms
    if scheme_symbolp(expr):
        return env.lookup(expr)
    elif self_evaluating(expr):
        return expr

    # All non-atomic expressions are lists (combinations)
    if not scheme_listp(expr):
        raise SchemeError('malformed list: {0}'.format(repl_str(expr)))
    first, rest = expr.first, expr.rest
    if scheme_symbolp(first) and first in scheme_forms.SPECIAL_FORMS:
        return scheme_forms.SPECIAL_FORMS[first](rest, env)
    else:
        # BEGIN PROBLEM 3
        "*** YOUR CODE HERE ***"
        procedure = scheme_eval(first, env)
        args = rest.map(lambda operand: scheme_eval(operand, env))
        return scheme_apply(procedure, args, env)
        # END PROBLEM 3

def pair_to_list(pair):
    if pair is nil:
        return []
    else:
        return [pair.first] + pair_to_list(pair.rest)
```

## Problem 4 (2 pt)

```py
$ python3 ok -q 04 -u
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 4 > Suite 1 > Case 1
(cases remaining: 9)

Q: What is the structure of the expressions argument to do_define_form?
Choose the number of the correct choice:
0) Pair(A, B), where:
       A is the symbol being bound,
       B is an expression whose value should be evaluated and bound to A
1) Pair('define', Pair(A, Pair(B, nil))), where:
       A is the symbol being bound,
       B is an expression whose value should be evaluated and bound to A
2) Pair(A, Pair(B, nil)), where:
       A is the symbol being bound,
       B is an expression whose value should be evaluated and bound to A
3) Pair(A, Pair(B, nil)), where:
       A is the symbol being bound,
       B is the value that should be bound to A
4) Pair(A, B), where:
       A is the symbol being bound,
       B is the value that should be bound to A
? 2
-- OK! --

---------------------------------------------------------------------
Problem 4 > Suite 1 > Case 2
(cases remaining: 8)

Q: What method of a Frame instance will bind
a value to a symbol in that frame?
Choose the number of the correct choice:
0) bindings
1) define
2) lookup
3) make_child_frame
? 1
-- OK! --

---------------------------------------------------------------------
Problem 4 > Suite 2 > Case 1
(cases remaining: 7)


scm> (define size 2)
? size
-- OK! --

scm> size
? 2
-- OK! --

---------------------------------------------------------------------
Problem 4 > Suite 2 > Case 2
(cases remaining: 6)


scm> (define x (+ 2 3))
? x
-- OK! --

scm> x
? 5
-- OK! --

scm> (define x (+ 2 7))
? x
-- OK! --

scm> x
? 9
-- OK! --

scm> (eval (define tau 6.28)) ; eval takes an expression represented as a list and evaluates it
? 6.28
-- OK! --

---------------------------------------------------------------------
Problem 4 > Suite 2 > Case 3
(cases remaining: 5)

-- Already unlocked --

---------------------------------------------------------------------
Problem 4 > Suite 2 > Case 4
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Problem 4 > Suite 2 > Case 5
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem 4 > Suite 2 > Case 6
(cases remaining: 2)


scm> (define x 15)
? x
-- OK! --

scm> (define y (* 2 x))
? y
-- OK! --

scm> y
? 30
-- OK! --

scm> (+ y (* y 2) 1)
? 91
-- OK! --

scm> (define x 20)
? x
-- OK! --

scm> x
? 20
-- OK! --

---------------------------------------------------------------------
Problem 4 > Suite 2 > Case 7
(cases remaining: 1)


scm> (define x 0)
? x
-- OK! --

scm> ((define x (+ x 1)) 2)
? SchemeError
-- OK! --

scm> x
? 1
-- OK! --

---------------------------------------------------------------------
OK! All cases for Problem 4 unlocked.
```

**scheme/scheme_forms.py**

```py
def do_define_form(expressions, env):
    """Evaluate a define form.
    >>> env = create_global_frame()
    >>> do_define_form(read_line("(x 2)"), env) # evaluating (define x 2)
    'x'
    >>> scheme_eval("x", env)
    2
    >>> do_define_form(read_line("(x (+ 2 8))"), env) # evaluating (define x (+ 2 8))
    'x'
    >>> scheme_eval("x", env)
    10
    >>> # problem 10
    >>> env = create_global_frame()
    >>> do_define_form(read_line("((f x) (+ x 2))"), env) # evaluating (define (f x) (+ x 8))
    'f'
    >>> scheme_eval(read_line("(f 3)"), env)
    5
    """
    validate_form(expressions, 2)  # Checks that expressions is a list of length at least 2
    signature = expressions.first
    if scheme_symbolp(signature):
        # assigning a name to a value e.g. (define x (+ 1 2))
        validate_form(expressions, 2, 2)  # Checks that expressions is a list of length exactly 2
        # BEGIN PROBLEM 4
        "*** YOUR CODE HERE ***"
        value = scheme_eval(expressions.rest.first, env)
        env.define(signature, value)
        return signature
        # END PROBLEM 4
    elif isinstance(signature, Pair) and scheme_symbolp(signature.first):
        # defining a named procedure e.g. (define (f x y) (+ x y))
        # BEGIN PROBLEM 10
        "*** YOUR CODE HERE ***"
        # END PROBLEM 10
    else:
        bad_signature = signature.first if isinstance(signature, Pair) else signature
        raise SchemeError('non-symbol: {0}'.format(bad_signature))
```

## Problem 5 (1 pt)

```py
$ python3 ok -q 05 -u
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 5 > Suite 1 > Case 1
(cases remaining: 4)

Q: What is the structure of the expressions argument to do_quote_form?
Choose the number of the correct choice:
0) A, where:
       A is the quoted expression
1) [A], where:
       A is the quoted expression
2) Pair('quote', Pair(A, nil)), where:
       A is the quoted expression
3) Pair(A, nil), where:
       A is the quoted expression
? 3
-- OK! --

---------------------------------------------------------------------
Problem 5 > Suite 2 > Case 1
(cases remaining: 3)

>>> from scheme import *
>>> global_frame = create_global_frame()
>>> do_quote_form(Pair(3, nil), global_frame)
? 3
-- OK! --

>>> do_quote_form(Pair('hi', nil), global_frame)
? 'hi'
-- OK! --

>>> expr = Pair(Pair('+', Pair('x', Pair(2, nil))), nil)
>>> do_quote_form(expr, global_frame) # Make sure to use Pair notation
? Pair('+', Pair('x', Pair(2, nil)))
-- OK! --

---------------------------------------------------------------------
Problem 5 > Suite 3 > Case 1
(cases remaining: 2)


scm> ''hello
Choose the number of the correct choice:
0) (quote (quote (hello)))
1) hello
2) (hello)
3) (quote hello)
? 3
-- OK! --

scm> (quote (1 2))
? (1 2)
-- OK! --

scm> (car '(1 2 3))
? 1
-- OK! --

scm> (cdr '(1 2))
? (2)
-- OK! --

scm> (cons 'car '('(4 2)))
? (car (quote (4 2)))
-- OK! --

scm> (eval (cons 'car '('(4 2))))
? 4
-- OK! --

---------------------------------------------------------------------
Problem 5 > Suite 4 > Case 1
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 5 unlocked.
```

**scheme/scheme_forms.py**

```py
def do_quote_form(expressions, env):
    """Evaluate a quote form.

    >>> env = create_global_frame()
    >>> do_quote_form(read_line("((+ x 2))"), env) # evaluating (quote (+ x 2))
    Pair('+', Pair('x', Pair(2, nil)))
    """
    validate_form(expressions, 1, 1)
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    return expressions.first
    # END PROBLEM 5
```

## Problem 6 (1 pt)

```py
$ python3 ok -q 06 -u
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 6 > Suite 1 > Case 1
(cases remaining: 6)

>>> from scheme import *
>>> env = create_global_frame()
>>> eval_all(Pair(2, nil), env)
Choose the number of the correct choice:
0) SchemeError
1) 2
? 1
-- OK! --

>>> eval_all(Pair(4, Pair(5, nil)), env)
Choose the number of the correct choice:
0) 4
1) 5
2) (4 5)
3) SchemeError
? 1
-- OK! --

>>> eval_all(nil, env) # return None (meaning undefined)
---------------------------------------------------------------------
Problem 6 > Suite 1 > Case 2
(cases remaining: 5)

>>> from scheme import *
>>> env = create_global_frame()
>>> lst = Pair(1, Pair(2, Pair(3, nil)))
>>> eval_all(lst, env)
? 3
-- OK! --

>>> lst     # The list should not be mutated!
? Pair(1, Pair(2, Pair(3, nil)))
-- OK! --

---------------------------------------------------------------------
Problem 6 > Suite 2 > Case 1
(cases remaining: 4)


scm> (begin (+ 2 3) (+ 5 6))
? 11
-- OK! --

scm> (begin (define x 3) x)
? 3
-- OK! --

---------------------------------------------------------------------
Problem 6 > Suite 2 > Case 2
(cases remaining: 3)


scm> (begin 30 '(+ 2 2))
Choose the number of the correct choice:
0) 4
1) '(+ 2 2)
2) 30
3) (+ 2 2)
? 3
-- OK! --

scm> (define x 0)
? x
-- OK! --

scm> (begin (define x (+ x 1)) 42 (define y (+ x 1)))
? y
-- OK! --

scm> x
? 1
-- OK! --

scm> y
? 2
-- OK! --

---------------------------------------------------------------------
Problem 6 > Suite 2 > Case 3
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Problem 6 > Suite 2 > Case 4
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 6 unlocked.
```

**scheme/scheme_eval_apply.py**

```py
def eval_all(expressions, env):
    """Evaluate each expression in the Scheme list EXPRESSIONS in
    Frame ENV (the current environment) and return the value of the last.

    >>> eval_all(read_line("(1)"), create_global_frame())
    1
    >>> eval_all(read_line("(1 2)"), create_global_frame())
    2
    >>> x = eval_all(read_line("((print 1) 2)"), create_global_frame())
    1
    >>> x
    2
    >>> eval_all(read_line("((define x 2) x)"), create_global_frame())
    2
    """
    # BEGIN PROBLEM 6
    # return scheme_eval(expressions.first, env)  # replace this with lines of your own code
    if expressions is nil:
        return
    expr = expressions
    while expr.rest is not nil:
        scheme_eval(expr.first, env)
        expr = expr.rest
    return scheme_eval(expr.first, env)
    # END PROBLEM 6
```

## Problem 7 (2 pt)

```py
$ python3 ok -q 07 -u
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 7 > Suite 1 > Case 1
(cases remaining: 5)


scm> (lambda (x y) (+ x y))
? (lambda (x y) (+ x y))
-- OK! --

scm> (lambda (x)) ; type SchemeError if you think this causes an error
? SchemeError
-- OK! --

---------------------------------------------------------------------
Problem 7 > Suite 1 > Case 2
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Problem 7 > Suite 1 > Case 3
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem 7 > Suite 2 > Case 1
(cases remaining: 2)

>>> from scheme_reader import *
>>> from scheme import *
>>> env = create_global_frame()
>>> lambda_line = read_line("(lambda (a b c) (+ a b c))")
>>> lambda_proc = do_lambda_form(lambda_line.rest, env)
>>> lambda_proc.formals # use single quotes ' around strings in your answer
? Pair('a', Pair('b', Pair('c', nil)))
-- OK! --

>>> lambda_proc.body # the body is a *list* of expressions! Make sure your answer is a properly nested Pair.
? Pair(Pair('+', Pair('a', Pair('b', Pair('c', nil)))), nil)
-- OK! --

---------------------------------------------------------------------
Problem 7 > Suite 2 > Case 2
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 7 unlocked.
```

**scheme/scheme_forms.py**

```py
def do_lambda_form(expressions, env):
    """Evaluate a lambda form.

    >>> env = create_global_frame()
    >>> do_lambda_form(read_line("((x) (+ x 2))"), env) # evaluating (lambda (x) (+ x 2))
    LambdaProcedure(Pair('x', nil), Pair(Pair('+', Pair('x', Pair(2, nil))), nil), <Global Frame>)
    """
    validate_form(expressions, 2)
    formals = expressions.first
    validate_formals(formals)
    # BEGIN PROBLEM 7
    "*** YOUR CODE HERE ***"
    body = expressions.rest
    return LambdaProcedure(formals, body, env)
    # END PROBLEM 7
```

## Problem 8 (2 pt)

```py
$ python3 ok -q 08 -u
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 8 > Suite 1 > Case 1
(cases remaining: 6)

>>> from scheme import *
>>> global_frame = create_global_frame()
>>> formals = Pair('a', Pair('b', Pair('c', nil)))
>>> vals = Pair(1, Pair(2, Pair(3, nil)))
>>> frame = global_frame.make_child_frame(formals, vals)
>>> global_frame.lookup('a') # Type SchemeError if you think this errors
? SchemeError
-- OK! --

>>> frame.lookup('a')        # Type SchemeError if you think this errors
? 1
-- OK! --

>>> frame.lookup('b')        # Type SchemeError if you think this errors
? 2
-- OK! --

>>> frame.lookup('c')        # Type SchemeError if you think this errors
? 3
-- OK! --

---------------------------------------------------------------------
Problem 8 > Suite 1 > Case 2
(cases remaining: 5)

>>> from scheme import *
>>> global_frame = create_global_frame()
>>> frame = global_frame.make_child_frame(nil, nil)
>>> frame.parent is global_frame
? True
-- OK! --

---------------------------------------------------------------------
Problem 8 > Suite 1 > Case 3
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Problem 8 > Suite 2 > Case 1
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem 8 > Suite 2 > Case 2
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Problem 8 > Suite 2 > Case 3
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 8 unlocked.
```

**scheme/scheme_classes.py**

```py
def make_child_frame(self, formals, vals):
    """Return a new local frame whose parent is SELF, in which the symbols
    in a Scheme list of formal parameters FORMALS are bound to the Scheme
    values in the Scheme list VALS. Both FORMALS and VALS are represented
    as Pairs. Raise an error if too many or too few vals are given.

    >>> env = create_global_frame()
    >>> formals, expressions = read_line('(a b c)'), read_line('(1 2 3)')
    >>> env.make_child_frame(formals, expressions)
    <{a: 1, b: 2, c: 3} -> <Global Frame>>
    """
    if len(formals) != len(vals):
        raise SchemeError('Incorrect number of arguments to function call')
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    child_frame = Frame(self)
    while formals is not nil and vals is not nil:
        child_frame.define(formals.first, vals.first)
        formals, vals = formals.rest, vals.rest
    return child_frame
    # END PROBLEM 8
```

## Problem 9 (2 pt)

```py
$ python3 ok -q 09 -u
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 9 > Suite 1 > Case 1
(cases remaining: 6)

-- Already unlocked --

---------------------------------------------------------------------
Problem 9 > Suite 1 > Case 2
(cases remaining: 5)

-- Already unlocked --

---------------------------------------------------------------------
Problem 9 > Suite 2 > Case 1
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Problem 9 > Suite 2 > Case 2
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem 9 > Suite 3 > Case 1
(cases remaining: 2)


scm> (define outer (lambda (x y)
....   (define inner (lambda (z x)
....     (+ x (* y 2) (* z 3))))
....   (inner x 10)))
? outer
-- OK! --

scm> (outer 1 2)
? 17
-- OK! --

scm> (define outer-func (lambda (x y)
....   (define inner (lambda (z x)
....     (+ x (* y 2) (* z 3))))
....   inner))
? outer-func
-- OK! --

scm> ((outer-func 1 2) 1 10)
? 17
-- OK! --

---------------------------------------------------------------------
Problem 9 > Suite 3 > Case 2
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 9 unlocked.
```

**scheme/scheme_eval_apply.py**

```py
def scheme_apply(procedure, args, env):
    """Apply Scheme PROCEDURE to argument values ARGS (a Scheme list) in
    Frame ENV, the current environment."""
    validate_procedure(procedure)
    if isinstance(procedure, BuiltinProcedure):
        # BEGIN PROBLEM 2
        "*** YOUR CODE HERE ***"
        args_list = pair_to_list(args)
        if procedure.expect_env:
            args_list.append(env)
        try:
            return procedure.py_func(*args_list)
        except TypeError:
            raise SchemeError('incorrect number of arguments')
        # END PROBLEM 2
    elif isinstance(procedure, LambdaProcedure):
        # BEGIN PROBLEM 9
        "*** YOUR CODE HERE ***"
        child_frame = procedure.env.make_child_frame(procedure.formals, args)
        return eval_all(procedure.body, child_frame)
        # END PROBLEM 9
    elif isinstance(procedure, MuProcedure):
        # BEGIN PROBLEM 11
        "*** YOUR CODE HERE ***"
        # END PROBLEM 11
    else:
        assert False, "Unexpected procedure: {}".format(procedure)
```

## Problem 10 (1 pt)

```py
$ python3 ok -q 10 -u
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 10 > Suite 1 > Case 1
(cases remaining: 7)


scm> (define (f x y) (+ x y))
? f
-- OK! --

scm> f
Choose the number of the correct choice:
0) (define f (lambda (x y) (+ x y)))
1) (lambda (f x y) (+ x y))
2) (lambda (x y) (+ x y))
3) (f (x y) (+ x y))
? 2
-- OK! --

---------------------------------------------------------------------
Problem 10 > Suite 1 > Case 2
(cases remaining: 6)

-- Already unlocked --

---------------------------------------------------------------------
Problem 10 > Suite 1 > Case 3
(cases remaining: 5)

-- Already unlocked --

---------------------------------------------------------------------
Problem 10 > Suite 1 > Case 4
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Problem 10 > Suite 1 > Case 5
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem 10 > Suite 1 > Case 6
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Problem 10 > Suite 2 > Case 1
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 10 unlocked.
```

**scheme/scheme_forms.py**

```py
def do_define_form(expressions, env):
    """Evaluate a define form.
    >>> env = create_global_frame()
    >>> do_define_form(read_line("(x 2)"), env) # evaluating (define x 2)
    'x'
    >>> scheme_eval("x", env)
    2
    >>> do_define_form(read_line("(x (+ 2 8))"), env) # evaluating (define x (+ 2 8))
    'x'
    >>> scheme_eval("x", env)
    10
    >>> # problem 10
    >>> env = create_global_frame()
    >>> do_define_form(read_line("((f x) (+ x 2))"), env) # evaluating (define (f x) (+ x 8))
    'f'
    >>> scheme_eval(read_line("(f 3)"), env)
    5
    """
    validate_form(expressions, 2)  # Checks that expressions is a list of length at least 2
    signature = expressions.first
    if scheme_symbolp(signature):
        # assigning a name to a value e.g. (define x (+ 1 2))
        validate_form(expressions, 2, 2)  # Checks that expressions is a list of length exactly 2
        # BEGIN PROBLEM 4
        "*** YOUR CODE HERE ***"
        value = scheme_eval(expressions.rest.first, env)
        env.define(signature, value)
        return signature
        # END PROBLEM 4
    elif isinstance(signature, Pair) and scheme_symbolp(signature.first):
        # defining a named procedure e.g. (define (f x y) (+ x y))
        # BEGIN PROBLEM 10
        "*** YOUR CODE HERE ***"
        formal = signature.rest
        while formal is not nil:
            if not scheme_symbolp(formal.first):
                raise SchemeError
            formal = formal.rest
        
        env.define(signature.first, LambdaProcedure(signature.rest, expressions.rest, env))
        return signature.first
        # END PROBLEM 10
    else:
        bad_signature = signature.first if isinstance(signature, Pair) else signature
        raise SchemeError('non-symbol: {0}'.format(bad_signature))
```

## Problem 11 (1 pt)

```py
$ python3 ok -q 11 -u
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 11 > Suite 1 > Case 1
(cases remaining: 2)


scm> (define y 1)
? y
-- OK! --

scm> (define f (mu (x) (+ x y)))
? f
-- OK! --

scm> (define g (lambda (x y) (f (+ x x))))
? g
-- OK! --

scm> (g 3 7)
? 13
-- OK! --

---------------------------------------------------------------------
Problem 11 > Suite 2 > Case 1
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 11 unlocked.
```

**scheme/scheme_forms.py**

```py
def do_mu_form(expressions, env):
    """Evaluate a mu form."""
    validate_form(expressions, 2)
    formals = expressions.first
    validate_formals(formals)
    # BEGIN PROBLEM 11
    "*** YOUR CODE HERE ***"
    return MuProcedure(formals, expressions.rest)
    # END PROBLEM 11
```

**scheme/scheme_eval_apply.py**

```py
def scheme_apply(procedure, args, env):
    """Apply Scheme PROCEDURE to argument values ARGS (a Scheme list) in
    Frame ENV, the current environment."""
    validate_procedure(procedure)
    if isinstance(procedure, BuiltinProcedure):
        # BEGIN PROBLEM 2
        "*** YOUR CODE HERE ***"
        args_list = pair_to_list(args)
        if procedure.expect_env:
            args_list.append(env)
        try:
            return procedure.py_func(*args_list)
        except TypeError:
            raise SchemeError('incorrect number of arguments')
        # END PROBLEM 2
    elif isinstance(procedure, LambdaProcedure):
        # BEGIN PROBLEM 9
        "*** YOUR CODE HERE ***"
        child_frame = procedure.env.make_child_frame(procedure.formals, args)
        return eval_all(procedure.body, child_frame)
        # END PROBLEM 9
    elif isinstance(procedure, MuProcedure):
        # BEGIN PROBLEM 11
        "*** YOUR CODE HERE ***"
        child_frame = env.make_child_frame(procedure.formals, args)
        return eval_all(procedure.body, child_frame)
        # END PROBLEM 11
    else:
        assert False, "Unexpected procedure: {}".format(procedure)
```

## Problem 12 (2 pt)

```py
$ python3 ok -q 12 -u
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 12 > Suite 1 > Case 1
(cases remaining: 9)


scm> (and)
Choose the number of the correct choice:
0) #f
1) SchemeError
2) #t
? 2
-- OK! --

scm> (and 1 #f)
Choose the number of the correct choice:
0) #t
1) #f
2) 1
? 1
-- OK! --

scm> (and (+ 1 1) 1)
? 1
-- OK! --

scm> (and #f 5)
? #f
-- OK! --

scm> (and 4 5 (+ 3 3))
? 6
-- OK! --

scm> (not (and #t #f 42 (/ 1 0)))
? #t
-- OK! --

---------------------------------------------------------------------
Problem 12 > Suite 1 > Case 2
(cases remaining: 8)

-- Already unlocked --

---------------------------------------------------------------------
Problem 12 > Suite 1 > Case 3
(cases remaining: 7)

-- Already unlocked --

---------------------------------------------------------------------
Problem 12 > Suite 1 > Case 4
(cases remaining: 6)

-- Already unlocked --

---------------------------------------------------------------------
Problem 12 > Suite 2 > Case 1
(cases remaining: 5)


scm> (or)
? #f
-- OK! --

scm> (or (+ 1 1))
? 2
-- OK! --

scm> (not (or #f))
? #t
-- OK! --

scm> (define (zero) 0)
? zero
-- OK! --

scm> (or (zero) 3)
? 0
-- OK! --

scm> (or 4 #t (/ 1 0))
? 4
-- OK! --

---------------------------------------------------------------------
Problem 12 > Suite 2 > Case 2
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Problem 12 > Suite 2 > Case 3
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem 12 > Suite 2 > Case 4
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Problem 12 > Suite 2 > Case 5
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 12 unlocked.
```

**scheme/scheme_forms.py**

```py
def do_and_form(expressions, env):
    """Evaluate a (short-circuited) and form.

    >>> env = create_global_frame()
    >>> do_and_form(read_line("(#f (print 1))"), env) # evaluating (and #f (print 1))
    False
    >>> # evaluating (and (print 1) (print 2) (print 4) 3 #f)
    >>> do_and_form(read_line("((print 1) (print 2) (print 3) (print 4) 3 #f)"), env)
    1
    2
    3
    4
    False
    """
    # BEGIN PROBLEM 12
    "*** YOUR CODE HERE ***"
    if expressions is nil:
        return True
    val = scheme_eval(expressions.first, env)
    if is_scheme_true(val):
        if expressions.rest is nil:
            return val
        else:
            return do_and_form(expressions.rest, env)
    else:
        return False
    # END PROBLEM 12

def do_or_form(expressions, env):
    """Evaluate a (short-circuited) or form.

    >>> env = create_global_frame()
    >>> do_or_form(read_line("(10 (print 1))"), env) # evaluating (or 10 (print 1))
    10
    >>> do_or_form(read_line("(#f 2 3 #t #f)"), env) # evaluating (or #f 2 3 #t #f)
    2
    >>> # evaluating (or (begin (print 1) #f) (begin (print 2) #f) 6 (begin (print 3) 7))
    >>> do_or_form(read_line("((begin (print 1) #f) (begin (print 2) #f) 6 (begin (print 3) 7))"), env)
    1
    2
    6
    """
    # BEGIN PROBLEM 12
    "*** YOUR CODE HERE ***"
    if expressions is nil:
        return False
    val = scheme_eval(expressions.first, env)
    if is_scheme_true(val):
        return val
    else:
        return do_or_form(expressions.rest, env)
    # END PROBLEM 12
```

## Problem 13 (2 pt)

```py
$ python3 ok -q 13 -u
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 13 > Suite 1 > Case 1
(cases remaining: 6)


scm> (cond ((> 2 3) 5)
....       ((> 2 4) 6)
....       ((< 2 5) 7)
....       (else 8))
? 7
-- OK! --

scm> (cond ((> 2 3) 5)
....       ((> 2 4) 6)
....       (else 8))
? 8
-- OK! --

scm> (cond ((= 1 1))
....       ((= 4 4) 'huh)
....       (else 'no))
? #t
-- OK! --

---------------------------------------------------------------------
Problem 13 > Suite 2 > Case 1
(cases remaining: 5)

-- Already unlocked --

---------------------------------------------------------------------
Problem 13 > Suite 2 > Case 2
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Problem 13 > Suite 2 > Case 3
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem 13 > Suite 2 > Case 4
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Problem 13 > Suite 2 > Case 5
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 13 unlocked.
```

**scheme/scheme_forms.py**

```py
def do_cond_form(expressions, env):
    """Evaluate a cond form.

    >>> do_cond_form(read_line("((#f (print 2)) (#t 3))"), create_global_frame())
    3
    """
    while expressions is not nil:
        clause = expressions.first
        validate_form(clause, 1)
        if clause.first == 'else':
            test = True
            if expressions.rest != nil:
                raise SchemeError('else must be last')
        else:
            test = scheme_eval(clause.first, env)
        if is_scheme_true(test):
            # BEGIN PROBLEM 13
            "*** YOUR CODE HERE ***"
            if clause.rest is nil:
                return test
            else:
                return eval_all(clause.rest, env)
            # END PROBLEM 13
        expressions = expressions.rest
```

## Problem 14 (2 pt)

```py
$ python3 ok -q 14 -u
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 14 > Suite 1 > Case 1
(cases remaining: 9)


scm> (define x 1)
? x
-- OK! --

scm> (let ((x 5))
....    (+ x 3))
? 8
-- OK! --

scm> x
? 1
-- OK! --

---------------------------------------------------------------------
Problem 14 > Suite 1 > Case 2
(cases remaining: 8)


scm> (let ((a 1) (b a)) b)
Choose the number of the correct choice:
0) y
1) 1
2) SchemeError
3) x
? 2
-- OK! --

---------------------------------------------------------------------
Problem 14 > Suite 1 > Case 3
(cases remaining: 7)


scm> (let ((x 5))
....    (let ((x 2)
....          (y x))
....        (+ y (* x 2))))
? 9
-- OK! --

---------------------------------------------------------------------
Problem 14 > Suite 1 > Case 4
(cases remaining: 6)


scm> (let ((a 2) (a 3)) (+ a a)) ; how should we catch something like this?
? SchemeError
-- OK! --

scm> (let ((y 2 3)) (+ y y)) ; should this be an allowable form?
? SchemeError
-- OK! --

---------------------------------------------------------------------
Problem 14 > Suite 1 > Case 5
(cases remaining: 5)

-- Already unlocked --

---------------------------------------------------------------------
Problem 14 > Suite 2 > Case 1
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Problem 14 > Suite 2 > Case 2
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem 14 > Suite 2 > Case 3
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Problem 14 > Suite 3 > Case 1
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 14 unlocked.
```

**scheme/scheme_forms.py**

```py
def make_let_frame(bindings, env):
    """Create a child frame of Frame ENV that contains the definitions given in
    BINDINGS. The Scheme list BINDINGS must have the form of a proper bindings
    list in a let expression: each item must be a list containing a symbol
    and a Scheme expression."""
    if not scheme_listp(bindings):
        raise SchemeError('bad bindings list in let form')
    names = vals = nil
    # BEGIN PROBLEM 14
    "*** YOUR CODE HERE ***"
    while bindings is not nil:
        validate_form(bindings.first, 2, 2)
        name = (bindings.first.first)
        val = (scheme_eval(bindings.first.rest.first, env))

        if names is nil:
            names = Pair(name, nil)
            name_tmp = names
        else:
            name_tmp.rest = Pair(name, nil)
            name_tmp = name_tmp.rest
        if vals is nil:
            vals = Pair(val, nil)
            val_tmp = vals
        else:
            val_tmp.rest = Pair(val, nil)
            val_tmp = val_tmp.rest
        bindings = bindings.rest

    validate_formals(names)
    # END PROBLEM 14
    return env.make_child_frame(names, vals)
```

## Problem 15 (2 pt)

**scheme/questions.scm**

```py
;; Problem 15
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 15
  'replace-this-line
  (define (help idx ele)
      (if (null? ele) nil
          (cons (list idx (car ele)) (help (+ idx 1) (cdr ele))))) (help 0 s)
  )
  ; END PROBLEM 15
```

## Problem 16 (2 pt)

**scheme/questions.scm**

```py
;; Problem 16

;; Merge two lists LIST1 and LIST2 according to INORDER? and return
;; the merged lists.
(define (merge inorder? list1 list2)
  ; BEGIN PROBLEM 16
  'replace-this-line
  (cond ((null? list1) list2)
       ((null? list2) list1)
       (else
            (if (inorder? (car list1) (car list2))
                (cons (car list1) (merge inorder? (cdr list1) list2))
                (cons (car list2) (merge inorder? list1 (cdr list2)))
            )
        )
  )
  )
  ; END PROBLEM 16
```

## Problem EC 1 (2 pt)

**scheme/scheme_eval_apply.py**

```py
def optimize_tail_calls(unoptimized_scheme_eval):
    """Return a properly tail recursive version of an eval function."""
    def optimized_eval(expr, env, tail=False):
        """Evaluate Scheme expression EXPR in Frame ENV. If TAIL,
        return an Unevaluated containing an expression for further evaluation.
        """
        if tail and not scheme_symbolp(expr) and not self_evaluating(expr):
            return Unevaluated(expr, env)

        result = Unevaluated(expr, env)
        # BEGIN PROBLEM EC
        "*** YOUR CODE HERE ***"
        while isinstance(result, Unevaluated):
            result = unoptimized_scheme_eval(result.expr, result.env)
        return result
        # END PROBLEM EC
    return optimized_eval
```