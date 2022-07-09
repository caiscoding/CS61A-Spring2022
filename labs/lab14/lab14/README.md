# Lab 14 Solution

## Q1: Split

**lab14/lab14.scm**

```py
(define (split-at lst n)
  'YOUR-CODE-HERE
  (cond ((= n 0) (cons nil lst))
        ((null? lst) (cons lst nil))
        (else
          (let ((rec (split-at (cdr lst) (- n 1))))
          (cons (cons (car lst) (car rec)) (cdr rec)))))
)
```

## Q2: Filter Odd Tree

**lab14/lab14.scm**

```py
(define (filter-odd t)
  'YOUR-CODE-HERE
  (cond 
    ((null? t) nil)
    ((odd? (label t)) (tree (label t) (map filter-odd (branches t))))
    (else (tree nil (map filter-odd (branches t)))))
)
```

## Q3: Swap

**lab14/lab14.scm**

```py
(define (swap expr)
  'YOUR-CODE-HERE
  (let ((op (car expr))
        (first (car (cdr expr)))
        (second (caddr expr))
        (rest (cdr (cddr expr))))
     (if (> (eval second) (eval first))
        (cons op (cons second (cons first rest)))
        expr))
)
```

## Q4: Address First Line

**lab14/lab14.py**

```py
def address_oneline(text):
    """
    Finds and returns if there are expressions in text that represent the first line
    of a US mailing address.

    >>> address_oneline("110 Sproul Hall, Berkeley, CA 94720")
    True
    >>> address_oneline("What's at 39177 Farwell Dr? Is there a 39177 Nearwell Dr?")
    True
    >>> address_oneline("I just landed at 780 N McDonnell Rd, and I need to get to 1880-ish University Avenue. Help!")
    True
    >>> address_oneline("123 Le Roy Ave")
    True
    >>> address_oneline("110 Unabbreviated Boulevard")
    False
    >>> address_oneline("790 lowercase St")
    False
    """
    block_number = r'\d{3,5}'
    cardinal_dir = r'(?:[NEWS] )?'  # whitespace is important!
    street = r'(?:[A-Z][A-Za-z]+ )+'
    type_abbr = r'[A-Z][a-z]{1,4}\b'
    street_name = f"{cardinal_dir}{street}{type_abbr}"
    return bool(re.search(f"{block_number} {street_name}", text))
```

## Q5: WWPD: PyCombinator

```py
$ python3 ok -q wwpd-bnf -u
=====================================================================
Assignment: Lab 14
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
ebnf-pycombinator > Suite 1 > Case 1
(cases remaining: 4)

Q: Which of the following expressions would NOT be parsable according to this BNF?
Choose the number of the correct choice:
0) add()
1) sub(3, 4)
2) add(1, 2)
3) add(sub(1, 2))
? 0
-- OK! --

---------------------------------------------------------------------
ebnf-pycombinator > Suite 1 > Case 2
(cases remaining: 3)

Q: Which of these expressions WOULD be parsable according to this BNF?
Choose the number of the correct choice:
0) All of these
1) add("a", "b")
2) add(10, 20)
3) add(a, b)
? 2
-- OK! --

---------------------------------------------------------------------
ebnf-pycombinator > Suite 1 > Case 3
(cases remaining: 2)

Q: What line of the BNF should we modify to add support for a "div" operation?
Choose the number of the correct choice:
0) func: FUNCNAME
1) FUNCNAME: "add" | "mul" | "sub"
2) pycomb_call: func "(" arg ("," arg)* ")"
3) arg: pycomb_call | NUMBER
? 1
-- OK! --

---------------------------------------------------------------------
ebnf-pycombinator > Suite 1 > Case 4
(cases remaining: 1)

Q: Which of the following are considered a terminal?
Choose the number of the correct choice:
0) func
1) arg
2) pycomb_call
3) All of these
4) FUNCNAME
5) NUMBER
6) both FUNCNAME and NUMBER
? 6
-- OK! --

---------------------------------------------------------------------
OK! All cases for ebnf-pycombinator unlocked.
```

## Q6: Prune Min

**lab14/lab14.py**

```py
def prune_min(t):
    """Prune the tree mutatively.

    >>> t1 = Tree(6)
    >>> prune_min(t1)
    >>> t1
    Tree(6)
    >>> t2 = Tree(6, [Tree(3), Tree(4)])
    >>> prune_min(t2)
    >>> t2
    Tree(6, [Tree(3)])
    >>> t3 = Tree(6, [Tree(3, [Tree(1), Tree(2)]), Tree(5, [Tree(3), Tree(4)])])
    >>> prune_min(t3)
    >>> t3
    Tree(6, [Tree(3, [Tree(1)])])
    """
    "*** YOUR CODE HERE ***"
    if t.branches == []:
        return
    prune_min(t.branches[0])
    prune_min(t.branches[1])
    if (t.branches[0].label > t.branches[1].label):
        t.branches.pop(0)
    else:
        t.branches.pop(1)
    return
```

## Q7: Add trees

**lab14/lab14.py**

```py
def add_trees(t1, t2):
    """
    >>> numbers = Tree(1,
    ...                [Tree(2,
    ...                      [Tree(3),
    ...                       Tree(4)]),
    ...                 Tree(5,
    ...                      [Tree(6,
    ...                            [Tree(7)]),
    ...                       Tree(8)])])
    >>> print(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print(add_trees(Tree(2), Tree(3, [Tree(4), Tree(5)])))
    5
      4
      5
    >>> print(add_trees(Tree(2, [Tree(3)]), Tree(2, [Tree(3), Tree(4)])))
    4
      6
      4
    >>> print(add_trees(Tree(2, [Tree(3, [Tree(4), Tree(5)])]), \
    Tree(2, [Tree(3, [Tree(4)]), Tree(5)])))
    4
      6
        8
        5
      5
    """
    "*** YOUR CODE HERE ***"
    if not t1:
        return t2
    if not t2:
        return t1
    new_label = t1.label + t2.label
    t1_branches, t2_branches = list(t1.branches), list(t2.branches)
    length_t1, length_t2 = len(t1_branches), len(t2_branches)
    if length_t1 < length_t2:
        t1_branches += [None for _ in range(length_t1, length_t2)]
    elif length_t1 > length_t2:
        t2_branches += [None for _ in range(length_t2, length_t1)]
    return Tree(new_label, [add_trees(branch1, branch2) for branch1, branch2 in zip(t1_branches, t2_branches)])
```

## Q8: Player

**lab14/lab14.py**

```py
### Phase 1: The Player Class
class Player:
    """
    >>> random = make_test_random()
    >>> p1 = Player('Hill')
    >>> p2 = Player('Don')
    >>> p1.popularity
    100
    >>> p1.debate(p2)  # random() should return 0.0
    >>> p1.popularity
    150
    >>> p2.popularity
    100
    >>> p2.votes
    0
    >>> p2.speech(p1)
    >>> p2.votes
    10
    >>> p2.popularity
    110
    >>> p1.popularity
    135

    """
    def __init__(self, name):
        self.name = name
        self.votes = 0
        self.popularity = 100

    def debate(self, other):
        "*** YOUR CODE HERE ***"
        prob = max(0.1, self.popularity / (self.popularity + other.popularity))
        if random() < prob:
            self.popularity += 50
        else:
            self.popularity = max(0, self.popularity - 50)

    def speech(self, other):
        "*** YOUR CODE HERE ***"
        self.votes += self.popularity // 10
        self.popularity += self.popularity // 10
        other.popularity -= other.popularity // 10

    def choose(self, other):
        return self.speech
```

## Q9: Game

**lab14/lab14.py**

```py
# Phase 2: The Game Class
class Game:
    """
    >>> p1, p2 = Player('Hill'), Player('Don')
    >>> g = Game(p1, p2)
    >>> winner = g.play()
    >>> p1 is winner
    True

    """

    def __init__(self, player1, player2):
        self.p1 = player1
        self.p2 = player2
        self.turn = 0

    def play(self):
        while not self.game_over():
            "*** YOUR CODE HERE ***"
            if self.turn % 2 == 0:
                curr, other = self.p1, self.p2
            else:
                curr, other = self.p2, self.p1
            curr.choose(other)(other)
            self.turn += 1
        return self.winner()

    def game_over(self):
        return max(self.p1.votes, self.p2.votes) >= 50 or self.turn >= 10

    def winner(self):
        "*** YOUR CODE HERE ***"
        if self.p1.votes > self.p2.votes:
            return self.p1
        elif self.p2.votes > self.p1.votes:
            return self.p2
        else:
            return None
```

## Q10: New Players

**lab14/lab14.py**

```py
# Phase 3: New Players
class AggressivePlayer(Player):
    """
    >>> random = make_test_random()
    >>> p1, p2 = AggressivePlayer('Don'), Player('Hill')
    >>> g = Game(p1, p2)
    >>> winner = g.play()
    >>> p1 is winner
    True

    """

    def choose(self, other):
        "*** YOUR CODE HERE ***"
        if self.popularity <= other.popularity:
            return self.debate
        else:
            return self.speech


class CautiousPlayer(Player):
    """
    >>> random = make_test_random()
    >>> p1, p2 = CautiousPlayer('Hill'), AggressivePlayer('Don')
    >>> p1.popularity = 0
    >>> p1.choose(p2) == p1.debate
    True
    >>> p1.popularity = 1
    >>> p1.choose(p2) == p1.debate
    False

    """

    def choose(self, other):
        "*** YOUR CODE HERE ***"
        if self.popularity == 0:
            return self.debate
        else:
            return self.speech
```

## Q11: Intersection - Summer 2015 MT1 Q4

**lab14/lab14.py**

```py
def intersection(lst_of_lsts):
    """Returns a list of distinct elements that appear in every list in
    lst_of_lsts.

    >>> lsts1 = [[1, 2, 3], [1, 3, 5]]
    >>> intersection(lsts1)
    [1, 3]
    >>> lsts2 = [[1, 4, 2, 6], [7, 2, 4], [4, 4]]
    >>> intersection(lsts2)
    [4]
    >>> lsts3 = [[1, 2, 3], [4, 5], [7, 8, 9, 10]]
    >>> intersection(lsts3)         # No number appears in all lists
    []
    >>> lsts4 = [[3, 3], [1, 2, 3, 3], [3, 4, 3, 5]]
    >>> intersection(lsts4)         # Return list of distinct elements
    [3]
    """
    elements = []
    "*** YOUR CODE HERE ***"
    for elem in lst_of_lsts[0]:
        condition = elem not in elements
        for lst in lst_of_lsts[1:]:
            if elem not in lst:
                condition = False
        if condition:
            elements = elements + [elem]
    return elements
```

## Q12: Deck of cards

**lab14/lab14.py**

```py
def deck(suits, ranks):
    """Creates a deck of cards (a list of 2-element lists) with the given
    suits and ranks. Each element in the returned list should be of the form
    [suit, rank].

    >>> deck(['S', 'C'], [1, 2, 3])
    [['S', 1], ['S', 2], ['S', 3], ['C', 1], ['C', 2], ['C', 3]]
    >>> deck(['S', 'C'], [3, 2, 1])
    [['S', 3], ['S', 2], ['S', 1], ['C', 3], ['C', 2], ['C', 1]]
    >>> deck([], [3, 2, 1])
    []
    >>> deck(['S', 'C'], [])
    []
    """
    "*** YOUR CODE HERE ***"
    return [[suit, rank] for suit in suits for rank in ranks]
```

## Q13: O!-Pascal - Fall 2017 Final Q4

**lab14/lab14.py**

```py
def pascal_row(s):
    """
    >>> a = Link.empty
    >>> for _ in range(5):
    ...     a = pascal_row(a)
    ...     print(a)
    <1>
    <1 1>
    <1 2 1>
    <1 3 3 1>
    <1 4 6 4 1>
    """
    "*** YOUR CODE HERE ***"
    if s is Link.empty:
        return Link(1)
    start = Link(1)
    last, current = start, s
    while current.rest is not Link.empty:
        last.rest = Link(current.first + current.rest.first)
        last, current = last.rest, current.rest
    last.rest = Link(1)
    return start
```

## Running tests

```py
$ python3 ok
=====================================================================
Assignment: Lab 14
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    16 test cases passed! No cases failed.
```