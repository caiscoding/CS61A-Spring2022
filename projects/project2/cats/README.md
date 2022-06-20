# Project 2 Solution

## Problem 1 (1 pt)

```py
$ python3 ok -q 01 -u
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 1 > Suite 1 > Case 1
(cases remaining: 102)

>>> from cats import choose
>>> ps = ['short', 'really long', 'tiny']
>>> s = lambda p: len(p) <= 5
>>> choose(ps, s, 0) # remember to put quotes ('') around strings!
? 'short'
-- OK! --

>>> choose(ps, s, 1)
? 'tiny'
-- OK! --

>>> choose(ps, s, 2)
? ''
-- OK! --

---------------------------------------------------------------------
OK! All cases for Problem 1 unlocked.
```

**cats/cats.py**

```py
def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns True. If there are fewer than K such paragraphs, return
    the empty string.

    Arguments:
        paragraphs: a list of strings
        select: a function that returns True for paragraphs that can be selected
        k: an integer

    >>> ps = ['hi', 'how are you', 'fine']
    >>> s = lambda p: len(p) <= 4
    >>> choose(ps, s, 0)
    'hi'
    >>> choose(ps, s, 1)
    'fine'
    >>> choose(ps, s, 2)
    ''
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    i = 0
    for j in paragraphs:
        if i == k and select(j):
            return j
        if select(j):
            i += 1
    return ''
    # END PROBLEM 1
```

## Problem 2 (1 pt)

```py
$ python3 ok -q 02 -u
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 2 > Suite 1 > Case 1
(cases remaining: 104)

>>> from cats import about
>>> from cats import choose
>>> dogs = about(['dogs', 'hounds'])
>>> dogs('A paragraph about cats.')
? False
-- OK! --

>>> dogs('A paragraph about dogs.')
? True
-- OK! --

>>> dogs('Release the Hounds!')
? True
-- OK! --

>>> dogs('"DOGS" stands for Department Of Geophysical Science.')
? True
-- OK! --

>>> dogs('Do gs and ho unds don\'t count')
? False
-- OK! --

>>> dogs("AdogsParagraph")
? False
-- OK! --

---------------------------------------------------------------------
OK! All cases for Problem 2 unlocked.
```

**cats/cats.py**

```py
def about(topic):
    """Return a select function that returns whether
    a paragraph contains one of the words in TOPIC.

    Arguments:
        topic: a list of words related to a subject

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def isMatch(str):
        str = remove_punctuation(lower(str))
        list = str.split(' ')
        for item in topic:
            for listItem in list:
                if lower(item) == lower(listItem):
                    return True
        return False
    return isMatch
    # END PROBLEM 2
```

## Problem 3 (2 pts)

```py
$ python3 ok -q 03 -u
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 3 > Suite 1 > Case 1
(cases remaining: 103)

>>> from cats import accuracy
>>> accuracy("12345", "12345") # This should return 100.0 (not the integer 100!)
? 100.0
-- OK! --

>>> accuracy("a b c", "a b c")
? 100.0
-- OK! --

>>> accuracy("a  b  c  d", "b  a  c  d")
? 50.0
-- OK! --

>>> accuracy("a b", "c d e")
? 0.0
-- OK! --

>>> accuracy("Cat", "cat") # the function is case-sensitive
? 0.0
-- OK! --

>>> accuracy("a b c d", "a d")
? 25.0
-- OK! --

>>> accuracy("abc", " ")
? 0.0
-- OK! --

>>> accuracy("a b \tc" , "a b c") # Tabs don't count as words
? 100.0
-- OK! --

>>> accuracy("abc", "")
? 0.0
-- OK! --

>>> accuracy("", "abc")
? 0.0
-- OK! --

>>> accuracy("a b c d", "b c d")
? 0.0
-- OK! --

>>> accuracy("cats.", "cats") # punctuation counts
? 0.0
-- OK! --

>>> accuracy("", "") # Returns 100.0
? 100.0
-- OK! --

---------------------------------------------------------------------
OK! All cases for Problem 3 unlocked.
```

**cats/cats.py**

```py
def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    Arguments:
        typed: a string that may contain typos
        reference: a string without errors

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    >>> accuracy('', '')
    100.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    typed_words_len = len(typed_words)
    reference_words_len = len(reference_words)
    if typed_words_len == 0:
        if reference_words_len == 0:
            return 100.0
        else:
            return 0.0
    elif len(reference_words) == 0:
        return 0.0
    sum = 0
    for i in range(0, min(reference_words_len, typed_words_len)):
        if reference_words[i] == typed_words[i]:
            sum += 1
    return sum / typed_words_len * 100
    # END PROBLEM 3
```

## Problem 4 (1 pt)

```py
$  python3 ok -q 04 -u
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 4 > Suite 1 > Case 1
(cases remaining: 104)

>>> from cats import wpm
>>> wpm("12345", 3) # Note: wpm returns a float (with a decimal point)
? 20.0
-- OK! --

>>> wpm("a b c", 20)
? 3.0
-- OK! --

>>> wpm("", 10)
? 0.0
-- OK! --

---------------------------------------------------------------------
OK! All cases for Problem 4 unlocked.
```

**cats/cats.py**

```py
def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string.

    Arguments:
        typed: an entered string
        elapsed: an amount of time in seconds

    >>> wpm('hello friend hello buddy hello', 15)
    24.0
    >>> wpm('0123456789',60)
    2.0
    """
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    return len(typed) / 5 * 60 / elapsed
    # END PROBLEM 4
```

## Problem 5 (2 pts)

```py
$ python3 ok -q 05 -u
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 5 > Suite 1 > Case 1
(cases remaining: 104)

>>> from cats import autocorrect, lines_from_file
>>> abs_diff = lambda w1, w2, limit: abs(len(w2) - len(w1))
>>> autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 10)
? 'cult'
-- OK! --

>>> autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 0)
? 'cul'
-- OK! --

>>> autocorrect("wor", ["worry", "car", "part"], abs_diff, 10)
? 'car'
-- OK! --

>>> first_diff = lambda w1, w2, limit: 1 if w1[0] != w2[0] else 0
>>> autocorrect("wrod", ["word", "rod"], first_diff, 1)
? 'word'
-- OK! --

>>> autocorrect("inside", ["idea", "inside"], first_diff, 0.5)
? 'inside'
-- OK! --

>>> autocorrect("inside", ["idea", "insider"], first_diff, 0.5)
? 'idea'
-- OK! --

>>> autocorrect("outside", ["idea", "insider"], first_diff, 0.5)
? 'outside'
-- OK! --

---------------------------------------------------------------------
OK! All cases for Problem 5 unlocked.
```

**cats/cats.py**

```py
def autocorrect(typed_word, word_list, diff_function, limit):
    """Returns the element of WORD_LIST that has the smallest difference
    from TYPED_WORD. Instead returns TYPED_WORD if that difference is greater
    than LIMIT.

    Arguments:
        typed_word: a string representing a word that may contain typos
        word_list: a list of strings representing reference words
        diff_function: a function quantifying the difference between two words
        limit: a number

    >>> ten_diff = lambda w1, w2, limit: 10 # Always returns 10
    >>> autocorrect("hwllo", ["butter", "hello", "potato"], ten_diff, 20)
    'butter'
    >>> first_diff = lambda w1, w2, limit: (1 if w1[0] != w2[0] else 0) # Checks for matching first char
    >>> autocorrect("tosting", ["testing", "asking", "fasting"], first_diff, 10)
    'testing'
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    if word_list.count(typed_word) > 0:
        return typed_word
    similarTypeWord = typed_word
    similarNum = limit + 1
    for i in word_list:
        curDiff = diff_function(typed_word, i, limit)
        if curDiff <= limit and curDiff < similarNum:
            similarTypeWord = i
            similarNum = curDiff
    return similarTypeWord
    # END PROBLEM 5
```

## Problem 6 (3 pts)

```py
$ python3 ok -q 06 -u
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 6 > Suite 1 > Case 1
(cases remaining: 105)

>>> from cats import sphinx_swaps, autocorrect
>>> import tests.construct_check as test
>>> big_limit = 10
>>> sphinx_swaps("car", "cad", big_limit)
? 1
-- OK! --

>>> sphinx_swaps("this", "that", big_limit)
? 2
-- OK! --

>>> sphinx_swaps("one", "two", big_limit)
? 3
-- OK! --

>>> sphinx_swaps("from", "form", big_limit)
? 2
-- OK! --

>>> sphinx_swaps("awe", "awesome", big_limit)
? 4
-- OK! --

>>> sphinx_swaps("someawe", "awesome", big_limit)
? 6
-- OK! --

>>> sphinx_swaps("awful", "awesome", big_limit)
? 5
-- OK! --

>>> sphinx_swaps("awful", "awesome", 3) > 3
? True
-- OK! --

>>> sphinx_swaps("awful", "awesome", 4) > 4
? True
-- OK! --

>>> sphinx_swaps("awful", "awesome", 5) > 5
? False
-- OK! --

---------------------------------------------------------------------
OK! All cases for Problem 6 unlocked.
```

**cats/cats.py**

```py
def sphinx_swaps(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths and returns the result.

    Arguments:
        start: a starting word
        goal: a string representing a desired goal word
        limit: a number representing an upper bound on the number of chars that must change

    >>> big_limit = 10
    >>> sphinx_swaps("nice", "rice", big_limit)    # Substitute: n -> r
    1
    >>> sphinx_swaps("range", "rungs", big_limit)  # Substitute: a -> u, e -> s
    2
    >>> sphinx_swaps("pill", "pillage", big_limit) # Don't substitute anything, length difference of 3.
    3
    >>> sphinx_swaps("roses", "arose", big_limit)  # Substitute: r -> a, o -> r, s -> o, e -> s, s -> e
    5
    >>> sphinx_swaps("rose", "hello", big_limit)   # Substitute: r->h, o->e, s->l, e->l, length difference of 1.
    5
    """
    # BEGIN PROBLEM 6
    # assert False, 'Remove this line'
    if len(start) == 0:
        return len(goal)
    elif len(goal) == 0:
        return len(start)
    if limit == -1:
        return 1
    if start[0] == goal[0]:
        return 0 + sphinx_swaps(start[1:], goal[1:], limit)
    else:
        return 1 + sphinx_swaps(start[1:], goal[1:], limit - 1)
    # END PROBLEM 6
```

## Problem 7 (3 pts)

```py
$ python3 ok -q 07 -u
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 7 > Suite 1 > Case 1
(cases remaining: 104)

-- Already unlocked --

---------------------------------------------------------------------
Problem 7 > Suite 1 > Case 2
(cases remaining: 103)

>>> from cats import minimum_mewtations, autocorrect
>>> big_limit = 10
>>> minimum_mewtations("cats", "scat", big_limit)
? 2
-- OK! --

>>> minimum_mewtations("purng", "purring", big_limit)
? 2
-- OK! --

>>> minimum_mewtations("ckiteus", "kittens", big_limit)
? 3
-- OK! --

---------------------------------------------------------------------
OK! All cases for Problem 7 unlocked.
```

**cats/cats.py**

```py
def minimum_mewtations(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL.
    This function takes in a string START, a string GOAL, and a number LIMIT.

    Arguments:
        start: a starting word
        goal: a goal word
        limit: a number representing an upper bound on the number of edits

    >>> big_limit = 10
    >>> minimum_mewtations("cats", "scat", big_limit)       # cats -> scats -> scat
    2
    >>> minimum_mewtations("purng", "purring", big_limit)   # purng -> purrng -> purring
    2
    >>> minimum_mewtations("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
    3
    """
    # assert False, 'Remove this line'

    if limit == -1:  # Fill in the condition
        # BEGIN
        "*** YOUR CODE HERE ***"
        return 1
        # END

    elif len(start) == 0 or len(goal) == 0:  # Feel free to remove or add additional cases
        # BEGIN
        "*** YOUR CODE HERE ***"
        return len(start) + len(goal)
        # END

    elif start[0] == goal[0]:
        return minimum_mewtations(start[1:], goal[1:], limit)

    else:
        add = minimum_mewtations(start, goal[1:], limit - 1)  # Fill in these lines
        remove = minimum_mewtations(start[1:], goal, limit - 1)
        substitute = minimum_mewtations(start[1:], goal[1:], limit - 1)
        # BEGIN
        "*** YOUR CODE HERE ***"
        return 1 + min(add, remove, substitute)
        # END
```

## Problem 8 (2 pts)

```py
$ python3 ok -q 08 -u
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 8 > Suite 1 > Case 1
(cases remaining: 102)

>>> from cats import report_progress
>>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
>>> typed = ['I', 'have', 'begun']
>>> prompt = ['I', 'have', 'begun', 'to', 'type']
>>> print_progress({'id': 1, 'progress': 0.6})
? ID: 1 Progress: 0.6
-- OK! --

>>> report_progress(typed, prompt, 1, print_progress) # print_progress is called on the report
(line 1)? ID: 1 Progress: 0.6
(line 2)? 0.6
-- OK! --

>>> report_progress(['I', 'begun'], prompt, 2, print_progress)
(line 1)? ID: 2 Progress: 0.2
(line 2)? 0.2
-- OK! --

>>> report_progress(['I', 'hve', 'begun', 'to', 'type'], prompt, 3, print_progress)
(line 1)? ID: 3 Progress: 0.2
(line 2)? 0.2
-- OK! --

---------------------------------------------------------------------
OK! All cases for Problem 8 unlocked.
```

**cats/cats.py**

```py
def report_progress(sofar, prompt, user_id, upload):
    """Upload a report of your id and progress so far to the multiplayer server.
    Returns the progress so far.

    Arguments:
        sofar: a list of the words input so far
        prompt: a list of the words in the typing prompt
        user_id: a number representing the id of the current user
        upload: a function used to upload progress to the multiplayer server

    >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
    >>> # The above function displays progress in the format ID: __, Progress: __
    >>> print_progress({'id': 1, 'progress': 0.6})
    ID: 1 Progress: 0.6
    >>> sofar = ['how', 'are', 'you']
    >>> prompt = ['how', 'are', 'you', 'doing', 'today']
    >>> report_progress(sofar, prompt, 2, print_progress)
    ID: 2 Progress: 0.6
    0.6
    >>> report_progress(['how', 'aree'], prompt, 3, print_progress)
    ID: 3 Progress: 0.2
    0.2
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    sum = 0
    for i in range(len(sofar)):
        if sofar[i] == prompt[i]:
            sum += 1
        else:
            break
    upload({'id': user_id, 'progress': sum / len(prompt)})
    return sum / len(prompt)
    # END PROBLEM 8
```

## Problem 9 (2 pts)

```py
$ python3 ok -q 09 -u
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 9 > Suite 1 > Case 1
(cases remaining: 101)

>>> from cats import *
>>> p = [[1, 4, 6, 7], [0, 4, 6, 9]]
>>> words = ['This', 'is', 'fun']
>>> match = time_per_word(words, p)
>>> match["words"]
? ['This', 'is', 'fun']
-- OK! --

>>> match["times"]
? [[3, 2, 1], [4, 2, 3]]
-- OK! --

>>> p = [[0, 2, 3], [2, 4, 7]]
>>> match = time_per_word(['hello', 'world'], p)
>>> word_at(match, word_index=1)
? 'world'
-- OK! --

>>> match["times"]
? [[2, 1], [2, 3]]
-- OK! --

>>> time(match, player_num=0, word_index=1)
? 1
-- OK! --

---------------------------------------------------------------------
OK! All cases for Problem 9 unlocked.
```

**cats/cats.py**

```py
def time_per_word(words, times_per_player):
    """Given timing data, return a match dictionary, which contains a
    list of words and the amount of time each player took to type each word.

    Arguments:
        words: a list of words, in the order they are typed.
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.

    >>> p = [[75, 81, 84, 90, 92], [19, 29, 35, 36, 38]]
    >>> match = time_per_word(['collar', 'plush', 'blush', 'repute'], p)
    >>> match["words"]
    ['collar', 'plush', 'blush', 'repute']
    >>> match["times"]
    [[6, 3, 6, 2], [10, 6, 1, 2]]
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    times = []
    for i in times_per_player:
        times_each_player = []
        for k in range(1, len(i)):
            times_each_player.append(i[k] - i[k - 1])
        times.append(times_each_player)
    return {
        "words": words,
        "times": times
    }
    # END PROBLEM 9
```

## Problem 10 (2 pts)

```py
$ python3 ok -q 10 -u
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 10 > Suite 1 > Case 1
(cases remaining: 102)

>>> from cats import match, fastest_words
>>> p0 = [2, 2, 3]
>>> p1 = [6, 1, 2]
>>> fastest_words(match(['What', 'great', 'luck'], [p0, p1]))
? [['What'], ['great', 'luck']]
-- OK! --

>>> p0 = [2, 2, 3]
>>> p1 = [6, 1, 3]
>>> fastest_words(match(['What', 'great', 'luck'], [p0, p1]))  # with a tie, choose the first player
? [['What', 'luck'], ['great']]
-- OK! --

>>> p2 = [4, 3, 1]
>>> fastest_words(match(['What', 'great', 'luck'], [p0, p1, p2]))
? [['What'], ['great'], ['luck']]
-- OK! --

---------------------------------------------------------------------
OK! All cases for Problem 10 unlocked.
```

**cats/cats.py**

```py
def fastest_words(match):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        match: a match dictionary as returned by time_per_word.

    >>> p0 = [5, 1, 3]
    >>> p1 = [4, 1, 6]
    >>> fastest_words(match(['Just', 'have', 'fun'], [p0, p1]))
    [['have', 'fun'], ['Just']]
    >>> p0  # input lists should not be mutated
    [5, 1, 3]
    >>> p1
    [4, 1, 6]
    """
    player_indices = range(len(match["times"]))  # contains an *index* for each player
    word_indices = range(len(match["words"]))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    total_player = [[] for i in range(len(match["times"]))]
    for i in word_indices:
        fastplayer = 0
        fasttime = match["times"][0][i]
        for k in player_indices:
            if match["times"][k][i] < fasttime:
                fastplayer = k
                fasttime = match["times"][k][i]
        total_player[fastplayer].append(word_at(match, word_index=i))
    return total_player
    # END PROBLEM 10
```

## Running tests

```py
$ python3 ok
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    1031 test cases passed! No cases failed.
```