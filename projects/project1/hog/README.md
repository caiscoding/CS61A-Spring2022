# Project 1 Solution

## Problem 0 (0 pt)

```py
$  python3 ok -q 00 -u
=====================================================================
Assignment: Project 1: Hog
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 0 > Suite 1 > Case 1
(cases remaining: 2)

>>> from hog import *
>>> test_dice = make_test_dice(4, 1, 2)
>>> test_dice()
? 4
-- OK! --

>>> test_dice() # Second call
? 1
-- OK! --

>>> test_dice() # Third call
? 2
-- OK! --

>>> test_dice() # Fourth call
? 4
-- OK! --

---------------------------------------------------------------------
Question 0 > Suite 2 > Case 1
(cases remaining: 1)

Q: Which of the following is the correct way to "roll" a fair, six-sided die?
Choose the number of the correct choice:
0) six_sided()
1) make_fair_dice(6)
2) make_test_dice(6)
3) six_sided
? 0
-- OK! --

---------------------------------------------------------------------
OK! All cases for Question 0 unlocked.
```

## Problem 1 (2 pt)

```py
$ python3 ok -q 01 -u
=====================================================================
Assignment: Project 1: Hog
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 1 > Suite 1 > Case 1
(cases remaining: 59)

>>> from hog import *
>>> roll_dice(2, make_test_dice(4, 6, 1))
? 10
-- OK! --

---------------------------------------------------------------------
Question 1 > Suite 1 > Case 2
(cases remaining: 58)

>>> from hog import *
>>> roll_dice(3, make_test_dice(4, 6, 1))
? 1
-- OK! --

---------------------------------------------------------------------
Question 1 > Suite 1 > Case 3
(cases remaining: 57)

>>> from hog import *
>>> roll_dice(4, make_test_dice(2, 2, 3))
? 9
-- OK! --

---------------------------------------------------------------------
Question 1 > Suite 1 > Case 4
(cases remaining: 56)

>>> from hog import *
>>> a = roll_dice(4, make_test_dice(1, 2, 3))
>>> a # check that the value is being returned, not printed
? 1
-- OK! --

---------------------------------------------------------------------
Question 1 > Suite 1 > Case 5
(cases remaining: 55)

>>> from hog import *
>>> counted_dice = make_test_dice(4, 1, 2, 6)
>>> roll_dice(3, counted_dice)
? 1
-- OK! --

>>> # Make sure you call dice exactly num_rolls times!
>>> # If you call it fewer or more than that, it won't be at the right spot in the cycle for the next roll
>>> # Note that a return statement within a loop ends the loop
>>> roll_dice(1, counted_dice)
? 6
-- OK! --

---------------------------------------------------------------------
Question 1 > Suite 1 > Case 6
(cases remaining: 54)

>>> from hog import *
>>> roll_dice(9, make_test_dice(6))
? 54
-- OK! --

>>> roll_dice(7, make_test_dice(2, 2, 2, 2, 2, 2, 1))
? 1
-- OK! --

---------------------------------------------------------------------
OK! All cases for Question 1 unlocked.
```

**hog/hog.py**

```py
def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    sum = 0
    hadOne = False
    while num_rolls:
        temp = dice()
        if temp == 1:
            hadOne = True
        sum += temp
        num_rolls -= 1
    return 1 if hadOne else sum
    # END PROBLEM 1
```

## Problem 2 (4 pt)

```py
# python3 ok -q 02 -u
=====================================================================
Assignment: Project 1: Hog
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 2 > Suite 1 > Case 1
(cases remaining: 38)

Q: The opponent's score is 123. The current player's score is 5.
Say the current player decides to roll 0 dice on this turn.
What is the first function applied to the current player's score (5)
according to Hefty Hogs?
Choose the number of the correct choice:
0) The function mapped to the digit 5
1) The function mapped to the digit 2
2) The function mapped to the digit 1
3) The function mapped to the digit 3
? 3
-- OK! --

---------------------------------------------------------------------
Question 2 > Suite 1 > Case 2
(cases remaining: 37)

Q: What is the second function applied to the result of the first?
Choose the number of the correct choice:
0) The function mapped to the digit 5
1) The function mapped to the digit 2
2) The function mapped to the digit 3
3) The function mapped to the digit 1
? 1
-- OK! --

---------------------------------------------------------------------
Question 2 > Suite 1 > Case 3
(cases remaining: 36)

Q: What is the third function applied to the result of the second?
Choose the number of the correct choice:
0) The function mapped to the digit 3
1) The function mapped to the digit 5
2) The function mapped to the digit 1
3) The function mapped to the digit 2
? 2
-- OK! --

---------------------------------------------------------------------
Question 2 > Suite 1 > Case 4
(cases remaining: 35)

Q: What is the overall result of Hefty Hogs for this turn?
The opponent's score is 123, and the current player's score is 5.
Choose the number of the correct choice:
0) f3( f2( f1(5) ))
1) f1( f2( f3(5) ))
2) f3( f2( f1(5) )) % 30
3) f1( f2( f3(5) )) % 30
? 3
-- OK! --

---------------------------------------------------------------------
Question 2 > Suite 2 > Case 1
(cases remaining: 34)

>>> from hog import *
>>> import tests.construct_check as test
>>> hefty_hogs(5, 123)
? 9
-- OK! --

---------------------------------------------------------------------
Question 2 > Suite 2 > Case 2
(cases remaining: 33)

>>> from hog import *
>>> import tests.construct_check as test
>>> hefty_hogs(5, 456)
? 29
-- OK! --

---------------------------------------------------------------------
Question 2 > Suite 2 > Case 3
(cases remaining: 32)

>>> from hog import *
>>> import tests.construct_check as test
>>> a = hefty_hogs(5, 123)
>>> a # check that the value is being returned, not printed
? 9
-- OK! --

---------------------------------------------------------------------
OK! All cases for Question 2 unlocked.
```

**hog/hog.py**

```py
def hefty_hogs(player_score, opponent_score):
    """Return the points scored by player due to Hefty Hogs.

    player_score:   The total score of the current player.
    opponent_score: The total score of the other player.
    """
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    if opponent_score == 0:
        return 1
    else:
        sum = player_score
        while opponent_score:
            sum = digit_fn(opponent_score % 10)(sum)
            opponent_score //= 10
        return sum % 30
    # END PROBLEM 2
```

## Problem 3 (2 pt)

```py
# python3 ok -q 03 -u
=====================================================================
Assignment: Project 1: Hog
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 3 > Suite 1 > Case 1
(cases remaining: 10)

>>> from hog import *
>>> take_turn(2, 5, 0, make_test_dice(4, 5, 1))
? 9
-- OK! --

---------------------------------------------------------------------
Question 3 > Suite 1 > Case 2
(cases remaining: 9)

>>> from hog import *
>>> take_turn(3, 5, 0, make_test_dice(4, 6, 1))
? 1
-- OK! --

---------------------------------------------------------------------
Question 3 > Suite 1 > Case 3
(cases remaining: 8)

>>> from hog import *
>>> take_turn(0, 3, 2)
? 9
-- OK! --

---------------------------------------------------------------------
Question 3 > Suite 1 > Case 4
(cases remaining: 7)

>>> from hog import *
>>> take_turn(0, 2, 15)
? 4
-- OK! --

---------------------------------------------------------------------
OK! All cases for Question 3 unlocked.
```

**hog/hog.py**

```py
def take_turn(num_rolls, player_score, opponent_score, dice=six_sided, goal=GOAL_SCORE):
    """Simulate a turn rolling NUM_ROLLS dice,
    which may be 0 in the case of a player using Hefty Hogs.
    Return the points scored for the turn by the current player.

    num_rolls:       The number of dice rolls that will be made.
    player_score:    The total score of the current player.
    opponent_score:  The total score of the opponent.
    dice:            A function that simulates a single dice roll outcome.
    goal:            The goal score of the game.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert max(player_score, opponent_score) < goal, 'The game should be over.'
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    if num_rolls == 0:
        return hefty_hogs(player_score, opponent_score)
    else:
        return roll_dice(num_rolls, dice)
    # END PROBLEM 3
```

## Problem 4 (1 pt)

```py
$  python3 ok -q 04 -u
=====================================================================
Assignment: Project 1: Hog
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 1
(cases remaining: 107)

>>> from hog import *
>>> hog_pile(25, 43)
? 0
-- OK! --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 2
(cases remaining: 106)

>>> from hog import *
>>> hog_pile(32, 33)
? 0
-- OK! --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 3
(cases remaining: 105)

>>> from hog import *
>>> hog_pile(7, 7)
? 7
-- OK! --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 4
(cases remaining: 104)

>>> from hog import *
>>> hog_pile(26, 26)
? 6
-- OK! --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 5
(cases remaining: 103)

>>> from hog import *
>>> hog_pile(23, 23)
? 3
-- OK! --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 6
(cases remaining: 102)

>>> from hog import *
>>> hog_pile(193, 42)
? 0
-- OK! --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 7
(cases remaining: 101)

>>> from hog import *
>>> a = hog_pile(187, 187)
>>> a # check that the value is being returned, not printed
? 7
-- OK! --

---------------------------------------------------------------------
OK! All cases for Question 4 unlocked.
```

**hog/hog.py**

```py
def hog_pile(player_score, opponent_score):
    """Return the points scored by player due to Hog Pile.

    player_score:   The total score of the current player.
    opponent_score: The total score of the other player.
    """
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    if player_score % 10 == opponent_score % 10:
        return player_score % 10
    else:
        return 0
    # END PROBLEM 4
```

## Problem 5 (5 pt)

```py
 python3 ok -q 05 -u
=====================================================================
Assignment: Project 1: Hog
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 5 > Suite 1 > Case 1
(cases remaining: 110)

Q: The variables score0 and score1 are the scores for Player 0
and Player 1, respectively. Under what conditions should the
game continue?
Choose the number of the correct choice:
0) While score1 is less than goal
1) While at least one of score0 or score1 is less than goal
2) While score0 and score1 are both less than goal
3) While score0 is less than goal
? 2
-- OK! --

---------------------------------------------------------------------
Question 5 > Suite 1 > Case 2
(cases remaining: 109)

Q: What is a strategy in the context of this game?
Choose the number of the correct choice:
0) A player's desired turn outcome
1) A function that returns the number of dice a player will roll
2) The number of dice a player will roll
? 1
-- OK! --

---------------------------------------------------------------------
Question 5 > Suite 1 > Case 3
(cases remaining: 108)

Q: If strategy1 is Player 1's strategy function, score0 is
Player 0's current score, and score1 is Player 1's current
score, then which of the following demonstrates correct
usage of strategy1?
Choose the number of the correct choice:
0) strategy1(score1)
1) strategy1(score0, score1)
2) strategy1(score0)
3) strategy1(score1, score0)
? 3
-- OK! --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 1
(cases remaining: 107)

>>> import hog
>>> always_three = hog.make_test_dice(3)
>>> always = hog.always_roll
>>> #
>>> # Play function stops at goal
>>> s0, s1 = hog.play(always(5), always(3), score0=91, score1=10, dice=always_three)
>>> s0
? 106
-- OK! --

>>> s1
? 10
-- OK! --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 2
(cases remaining: 106)

>>> import hog
>>> always_three = hog.make_test_dice(3)
>>> always = hog.always_roll
>>> #
>>> # Goal score is not hardwired
>>> s0, s1 = hog.play(always(5), always(5), goal=10, dice=always_three)
>>> s0
? 15
-- OK! --

>>> s1
? 0
-- OK! --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 3
(cases remaining: 105)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 3 > Case 1
(cases remaining: 104)

>>> import hog
>>> always_three = hog.make_test_dice(3)
>>> always_seven = hog.make_test_dice(7)
>>> #
>>> # Use strategies
>>> # We recommend working this out turn-by-turn on a piece of paper (use Python for difficult calculations).
>>> strat0 = lambda score, opponent: opponent % 10
>>> strat1 = lambda score, opponent: max((score // 10) - 4, 0)
>>> s0, s1 = hog.play(strat0, strat1, score0=71, score1=80, dice=always_seven)
>>> s0
? 91
-- OK! --

>>> s1
? 108
-- OK! --

---------------------------------------------------------------------
OK! All cases for Question 5 unlocked.
```

**hog/hog.py**

```py
def play(strategy0, strategy1, score0=0, score1=0, dice=six_sided,
         goal=GOAL_SCORE, say=silence):
    """Simulate a game and return the final scores of both players, with Player
    0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first.
    strategy1:  The strategy function for Player 1, who plays second.
    score0:     Starting score for Player 0
    score1:     Starting score for Player 1
    dice:       A function of zero arguments that simulates a dice roll.
    goal:       The game ends and someone wins when this score is reached.
    say:        The commentary function to call every turn.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    leader = None  # To be used in problem 7
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    while score0 < goal and score1 < goal:
        if who:
            score1 += take_turn(strategy1(score1, score0), score1, score0, dice, goal)
            score1 += hog_pile(score1, score0)
            who = next_player(who)
        else:
            score0 += take_turn(strategy0(score0, score1), score0, score1, dice, goal)
            score0 += hog_pile(score0, score1)
            who = next_player(who)
    # END PROBLEM 5
    # (note that the indentation for the problem 7 prompt (***YOUR CODE HERE***) might be misleading)
    # BEGIN PROBLEM 7
    "*** YOUR CODE HERE ***"
    # END PROBLEM 7
    return score0, score1
```

## Problem 6 (2 pt)

```py
$ python3 ok -q 06 -u
=====================================================================
Assignment: Project 1: Hog
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 6 > Suite 1 > Case 1
(cases remaining: 4)

Q: What does announce_lead_changes return?
Choose the number of the correct choice:
0) The previous leader and a message.
1) The current leader and a message.
2) Nothing (None).
3) A message.
4) A player.
? 1
-- OK! --

---------------------------------------------------------------------
Question 6 > Suite 1 > Case 2
(cases remaining: 3)

Q: When is the message returned by announce_lead_changes
not just an empty string?
Choose the number of the correct choice:
0) When the current leader is different from the previous leader.
1) After each turn.
2) When the current leader is the same as the previous leader.
? 0
-- OK! --

---------------------------------------------------------------------
Question 6 > Suite 1 > Case 3
(cases remaining: 2)

Q: What does the parameter last_leader represent?
Choose the number of the correct choice:
0) The leading player from the previous turn.
1) The leading player in the current turn.
2) The opponent player of this turn.
3) The current player of this turn.
? 0
-- OK! --

---------------------------------------------------------------------
Question 6 > Suite 2 > Case 1
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Question 6 unlocked.
```

**hog/hog.py**

```py
def announce_lead_changes(score0, score1, last_leader=None):
    """A commentary function that announces when the leader has changed.

    >>> leader, message = announce_lead_changes(5, 0)
    >>> print(message)
    Player 0 takes the lead by 5
    >>> leader, message = announce_lead_changes(5, 12, leader)
    >>> print(message)
    Player 1 takes the lead by 7
    >>> leader, message = announce_lead_changes(8, 12, leader)
    >>> print(leader, message)
    1 None
    >>> leader, message = announce_lead_changes(8, 13, leader)
    >>> leader, message = announce_lead_changes(15, 13, leader)
    >>> print(message)
    Player 0 takes the lead by 2
    """
    # BEGIN PROBLEM 6
    "*** YOUR CODE HERE ***"
    if score0 == score1:
        return None, None
    elif score0 > score1:
        if last_leader == 0:
            return last_leader, None
        else:
            return 0, "Player 0 takes the lead by " + str(score0 - score1)
    else:
        if last_leader == 1:
            return last_leader, None
        else:
            return 1, "Player 1 takes the lead by " + str(score1 - score0)
    # END PROBLEM 6
```

## Problem 7 (2 pt)

```py
$ python3 ok -q 07 -u
=====================================================================
Assignment: Project 1: Hog
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 7 > Suite 1 > Case 1
(cases remaining: 9)

Q: What does a commentary function return?
Choose the number of the correct choice:
0) A player and a message (in that order).
1) A player.
2) A message.
3) A message and a player (in that order).
? 0
-- OK! --

---------------------------------------------------------------------
Question 7 > Suite 2 > Case 1
(cases remaining: 8)

-- Already unlocked --

---------------------------------------------------------------------
Question 7 > Suite 2 > Case 2
(cases remaining: 7)

-- Already unlocked --

---------------------------------------------------------------------
Question 7 > Suite 2 > Case 3
(cases remaining: 6)

>>> from hog import play, always_roll, announce_lead_changes
>>> from dice import make_test_dice
>>> #
>>> def echo(s0, s1, player=None):
...     return player, f"{s0} {s1}" # message of the form: "s0 s1"
>>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(3), goal=5, say=echo)
(line 1)? 3 0
(line 2)? 3 6
-- OK! --

---------------------------------------------------------------------
Question 7 > Suite 2 > Case 4
(cases remaining: 5)

>>> from hog import play, always_roll, announce_lead_changes
>>> from dice import make_test_dice
>>> def count(n):
...     def say(s0, s1, curr_count=None):
...         if curr_count is None:
...           curr_count = n
...         return curr_count + 1, str(curr_count) + " " + str(s0)
...     return say
>>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(5), goal=15, say=count(1))
(line 1)? 1 5
(line 2)? 2 5
(line 3)? 3 10
(line 4)? 4 10
-- OK! --

---------------------------------------------------------------------
Question 7 > Suite 3 > Case 1
(cases remaining: 4)

>>> from hog import play, always_roll, both, announce_lead_changes, say_scores
>>> from dice import make_test_dice
>>> #
>>> def echo(s0, s1, player=None):
...     return player, str(s0) + " " + str(s1)
>>> strat0 = lambda score, opponent: 1 - opponent // 10
>>> strat1 = always_roll(3)
>>> s0, s1 = play(strat0, strat1, dice=make_test_dice(4, 2, 6), goal=15, say=echo)
(line 1)? 4 0
(line 2)? 4 12
(line 3)? 28 12
-- OK! --

---------------------------------------------------------------------
Question 7 > Suite 3 > Case 2
(cases remaining: 3)

>>> from hog import play, always_roll, both, announce_lead_changes, say_scores
>>> from dice import make_test_dice
>>> #
>>> def total(s0, s1, player=None):
...     return player, str(s0 + s1)
>>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(2, 5), goal=10, say=total)
(line 1)? 2
(line 2)? 7
(line 3)? 9
(line 4)? 14
-- OK! --

---------------------------------------------------------------------
Question 7 > Suite 3 > Case 3
(cases remaining: 2)

>>> from hog import play, always_roll, both, announce_lead_changes, say_scores
>>> from dice import make_test_dice
>>> #
>>> def echo_0(s0, s1, player=None):
...     return player, f"* {s0}" # message of the form: "* s0"
>>> def echo_1(s0, s1, player=None):
...     return player, f"** {s1}" # message of the form: "** s1"
>>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(2), goal=5, say=both(echo_0, echo_1))
(line 1)? * 2
(line 2)? ** 0
(line 3)? * 2
(line 4)? ** 4
(line 5)? * 8
(line 6)? ** 4
-- OK! --

---------------------------------------------------------------------
Question 7 > Suite 3 > Case 4
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Question 7 unlocked.
```

**hog/hog.py**

```py
def play(strategy0, strategy1, score0=0, score1=0, dice=six_sided,
         goal=GOAL_SCORE, say=silence):
    """Simulate a game and return the final scores of both players, with Player
    0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first.
    strategy1:  The strategy function for Player 1, who plays second.
    score0:     Starting score for Player 0
    score1:     Starting score for Player 1
    dice:       A function of zero arguments that simulates a dice roll.
    goal:       The game ends and someone wins when this score is reached.
    say:        The commentary function to call every turn.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    leader = None  # To be used in problem 7
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    while score0 < goal and score1 < goal:
        if who:
            score1 += take_turn(strategy1(score1, score0), score1, score0, dice, goal)
            score1 += hog_pile(score1, score0)
            who = next_player(who)
        else:
            score0 += take_turn(strategy0(score0, score1), score0, score1, dice, goal)
            score0 += hog_pile(score0, score1)
            who = next_player(who)
    # END PROBLEM 5
    # (note that the indentation for the problem 7 prompt (***YOUR CODE HERE***) might be misleading)
    # BEGIN PROBLEM 7
        "*** YOUR CODE HERE ***"
        leader, message = say(score0, score1, leader)
        if message != None:
            print(message)
    # END PROBLEM 7
    return score0, score1
```

## Problem 8 (2 pt)

```py
$ python3 ok -q 08 -u
=====================================================================
Assignment: Project 1: Hog
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 8 > Suite 1 > Case 1
(cases remaining: 7)

Q: What is one reason that make_averaged is a higher order function?
Choose the number of the correct choice:
0) It uses the *args keyword
1) It calls a function that is not itself
2) It contains a nested function
3) It takes in a function as an argument
? 3
-- OK! --

---------------------------------------------------------------------
Question 8 > Suite 1 > Case 2
(cases remaining: 6)

Q: How many arguments does the function passed into make_averaged take?
Choose the number of the correct choice:
0) An arbitrary amount, which is why we need to use *args to call it
1) Two
2) None
? 0
-- OK! --

---------------------------------------------------------------------
Question 8 > Suite 2 > Case 1
(cases remaining: 5)

>>> from hog import *
>>> dice = make_test_dice(3, 1, 5, 6)
>>> averaged_dice = make_averaged(dice, 1000)
>>> # Average of calling dice 1000 times
>>> averaged_dice()
? 3.75
-- OK! --

---------------------------------------------------------------------
Question 8 > Suite 2 > Case 2
(cases remaining: 4)

>>> from hog import *
>>> dice = make_test_dice(3, 1, 5, 6)
>>> averaged_roll_dice = make_averaged(roll_dice, 1000)
>>> # Average of calling roll_dice 1000 times
>>> # Enter a float (e.g. 1.0) instead of an integer
>>> averaged_roll_dice(2, dice)
? 6.0
-- OK! --

---------------------------------------------------------------------
Question 8 > Suite 3 > Case 1
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Question 8 > Suite 3 > Case 2
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Question 8 > Suite 3 > Case 3
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Question 8 unlocked.
```

**hog/hog.py**

```py
def make_averaged(original_function, total_samples=1000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    called TOTAL_SAMPLES times.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(roll_dice, 1000)
    >>> averaged_dice(1, dice)
    3.0
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    def averaged(*args):
        sum = 0
        i = 0
        while i < total_samples:
            sum += original_function(*args)
            i += 1
        return float(sum / total_samples)
    return averaged
    # END PROBLEM 8
```

## Problem 9 (2 pt)

```py
$  python3 ok -q 09 -u
=====================================================================
Assignment: Project 1: Hog
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 9 > Suite 1 > Case 1
(cases remaining: 10)

Q: If multiple num_rolls are tied for the highest scoring
average, which should you return?
Choose the number of the correct choice:
0) The highest num_rolls
1) A random num_rolls
2) The lowest num_rolls
? 2
-- OK! --

---------------------------------------------------------------------
Question 9 > Suite 2 > Case 1
(cases remaining: 9)

>>> from hog import *
>>> dice = make_test_dice(3)   # dice always returns 3
>>> max_scoring_num_rolls(dice, total_samples=1000)
? 10
-- OK! --

---------------------------------------------------------------------
Question 9 > Suite 2 > Case 2
(cases remaining: 8)

-- Already unlocked --

---------------------------------------------------------------------
Question 9 > Suite 2 > Case 3
(cases remaining: 7)

-- Already unlocked --

---------------------------------------------------------------------
Question 9 > Suite 3 > Case 1
(cases remaining: 6)

>>> from hog import *
>>> dice = make_test_dice(2)     # dice always rolls 2
>>> max_scoring_num_rolls(dice, total_samples=1000)
? 10
-- OK! --

---------------------------------------------------------------------
Question 9 > Suite 3 > Case 2
(cases remaining: 5)

>>> from hog import *
>>> dice = make_test_dice(1)     # dice always rolls 1
>>> max_scoring_num_rolls(dice, total_samples=1000)
? 1
-- OK! --

---------------------------------------------------------------------
Question 9 > Suite 3 > Case 3
(cases remaining: 4)

>>> from hog import *
>>> dice = make_test_dice(1, 2)  # dice alternates 1 and 2
>>> max_scoring_num_rolls(dice, total_samples=1000)
? 1
-- OK! --

---------------------------------------------------------------------
Question 9 > Suite 3 > Case 4
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Question 9 > Suite 3 > Case 5
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Question 9 > Suite 3 > Case 6
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Question 9 unlocked.
```

**hog/hog.py**

```py
def max_scoring_num_rolls(dice=six_sided, total_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn score
    by calling roll_dice with the provided DICE a total of TOTAL_SAMPLES times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    maxScoreNumRolls = -1
    roll = 0
    for i in range(1, 11):
        ma = make_averaged(roll_dice, total_samples)(i, dice)
        if ma > maxScoreNumRolls:
            maxScoreNumRolls = ma
            roll = i
    return roll
    # END PROBLEM 9
```

## Problem 10 (1 pt)

```py
$ python3 ok -q 10 -u
=====================================================================
Assignment: Project 1: Hog
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 10 > Suite 1 > Case 1
(cases remaining: 106)

>>> from hog import *
>>> hefty_hogs_strategy(4, 12, threshold=7, num_rolls=5)
? 5
-- Not quite. Try again! --

? 0
-- OK! --

---------------------------------------------------------------------
Question 10 > Suite 1 > Case 2
(cases remaining: 105)

>>> from hog import *
>>> hefty_hogs_strategy(9, 3, threshold=6, num_rolls=5)
? 5
-- OK! --

---------------------------------------------------------------------
Question 10 > Suite 1 > Case 3
(cases remaining: 104)

>>> from hog import *
>>> hefty_hogs_strategy(6, 1, threshold=6, num_rolls=5)
? 0
-- OK! --

---------------------------------------------------------------------
Question 10 > Suite 1 > Case 4
(cases remaining: 103)

>>> from hog import *
>>> hefty_hogs_strategy(32, 0, threshold=8, num_rolls=4)
? 4
-- OK! --

---------------------------------------------------------------------
Question 10 > Suite 1 > Case 5
(cases remaining: 102)

>>> from hog import *
>>> hefty_hogs_strategy(20, 0, threshold=1, num_rolls=4)
? 0
-- OK! --

---------------------------------------------------------------------
OK! All cases for Question 10 unlocked.
```

**hog/hog.py**

```py
def hefty_hogs_strategy(score, opponent_score, threshold=8, num_rolls=6):
    """This strategy returns 0 dice if that gives at least THRESHOLD points, and
    returns NUM_ROLLS otherwise.
    """
    # BEGIN PROBLEM 10
    #return 6  # Remove this line once implemented.
    if hefty_hogs(score, opponent_score) >= threshold:
        return 0
    return num_rolls
    # END PROBLEM 10
```

## Problem 11 (1 pt)

```py
$  python3 ok -q 11 -u
=====================================================================
Assignment: Project 1: Hog
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 11 > Suite 1 > Case 1
(cases remaining: 105)

>>> from hog import *
>>> hog_pile_strategy(2, 10, threshold=10, num_rolls=6)
? 6
-- OK! --

---------------------------------------------------------------------
Question 11 > Suite 1 > Case 2
(cases remaining: 104)

>>> from hog import *
>>> hog_pile_strategy(30, 54, threshold=10, num_rolls=6)
? 6
-- OK! --

---------------------------------------------------------------------
Question 11 > Suite 1 > Case 3
(cases remaining: 103)

>>> from hog import *
>>> hog_pile_strategy(20, 32, threshold=7, num_rolls=6)
? 0
-- OK! --

---------------------------------------------------------------------
Question 11 > Suite 1 > Case 4
(cases remaining: 102)

>>> from hog import *
>>> hog_pile_strategy(24, 5, threshold=8, num_rolls=6)
? 6
-- OK! --

---------------------------------------------------------------------
OK! All cases for Question 11 unlocked.
```

**hog/hog.py**

```py
def hog_pile_strategy(score, opponent_score, threshold=8, num_rolls=6):
    """This strategy returns 0 dice when this would result in Hog Pile taking
    effect. It also returns 0 dice if it gives at least THRESHOLD points.
    Otherwise, it returns NUM_ROLLS.
    """
    # BEGIN PROBLEM 11
    #return 6  # Remove this line once implemented.    if not hefty_hogs_strategy(score, opponent_score, threshold , num_rolls):
        return 0
    elif hog_pile(score + hefty_hogs(score, opponent_score), opponent_score) != 0:
        return 0
    elif hefty_hogs(score, opponent_score) + hog_pile(score + hefty_hogs(score, opponent_score), opponent_score) >= threshold:
        return 0
    return num_rolls
    # END PROBLEM 11
```

## Running tests

```py
$ python3 ok
=====================================================================
Assignment: Project 1: Hog
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    568 test cases passed! No cases failed.
```