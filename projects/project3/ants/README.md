# Project 3 Solution

## Problem 0 (0 pt)

```py
$ python3 ok -q 00 -u
=====================================================================
Assignment: Project 3: Ants Vs. SomeBees
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 0 > Suite 1 > Case 1
(cases remaining: 9)

Q: What is the significance of an Insect's health attribute? Does this
value change? If so, how?
Choose the number of the correct choice:
0) It represents the strength of an insect against attacks, which
   doesn't change throughout the game
1) It represents the amount of health the insect has left, so the
   insect is eliminated when it reaches 0
2) It represents health protecting the insect, so the insect can only
   be damaged when its health reaches 0
? 1
-- OK! --

---------------------------------------------------------------------
Problem 0 > Suite 1 > Case 2
(cases remaining: 8)

Q: Which of the following is a class attribute of the Insect class?
Choose the number of the correct choice:
0) place
1) bees
2) health
3) damage
? 3
-- OK! --

---------------------------------------------------------------------
Problem 0 > Suite 1 > Case 3
(cases remaining: 7)

Q: Is the health attribute of the Ant class an instance attribute or class attribute? Why?
Choose the number of the correct choice:
0) class, Ants of the same subclass all have the same amount of starting health
1) instance, each Ant starts out with a different amount of health
2) class, when one Ant gets damaged, all ants receive the same amount of damage
3) instance, each Ant instance needs its own health value
? 3
-- OK! --

---------------------------------------------------------------------
Problem 0 > Suite 1 > Case 4
(cases remaining: 6)

Q: Is the damage attribute of an Ant subclass (such as ThrowerAnt) an
instance or class attribute? Why?
Choose the number of the correct choice:
0) instance, the damage an Ant depends on where the Ant is
1) class, all Ants deal the same damage
2) instance, each Ant does damage to bees at different rates
3) class, all Ants of the same subclass deal the same damage
? 3
-- OK! --

---------------------------------------------------------------------
Problem 0 > Suite 1 > Case 5
(cases remaining: 5)

Q: Which class do both Ant and Bee inherit from?
Choose the number of the correct choice:
0) Bee
1) Ant
2) Insect
3) Place
? 2
-- OK! --

---------------------------------------------------------------------
Problem 0 > Suite 1 > Case 6
(cases remaining: 4)

Q: What do instances of Ant and instances of Bee have in common? Please choose the most correct answer.
Choose the number of the correct choice:
0) Ants and Bees both have the attributes health, damage, and place
   and the methods reduce_health and action
1) Ants and Bees both take the same action each turn
2) Ants and Bees have nothing in common
3) Ants and Bees both have the attribute damage and the methods
   reduce_health and action
? 0
-- OK! --

---------------------------------------------------------------------
Problem 0 > Suite 1 > Case 7
(cases remaining: 3)

Q: How many insects can be in a single Place at any given time in the
game (before Problem 8)?
Choose the number of the correct choice:
0) Only one insect can be in a single Place at a time
1) There is no limit on the number of insects of any type in a single Place
2) There can be one Ant and many Bees in a single Place
3) There can be one Bee and many Ants in a single Place
? 2
-- OK! --

---------------------------------------------------------------------
Problem 0 > Suite 1 > Case 8
(cases remaining: 2)

Q: What does a Bee do during one of its turns?
Choose the number of the correct choice:
0) The bee stings the ant in its place and then moves to the next place
1) The bee flies to the nearest Ant and attacks it
2) The bee moves to the next place, then stings the ant in that place
3) The bee stings the ant in its place or moves to the next place if there is no ant in its place
? 3
-- OK! --

---------------------------------------------------------------------
Problem 0 > Suite 1 > Case 9
(cases remaining: 1)

Q: When is the game lost?
Choose the number of the correct choice:
0) When any bee reaches the end of the tunnel and the Queen Ant is killed
1) When any bee reaches the end of the tunnel or when the Queen Ant is killed
2) When the bees enter the colony
3) When no ants are left on the map
4) When the colony runs out of food
? 1
-- OK! --

---------------------------------------------------------------------
OK! All cases for Problem 0 unlocked.
```

## Problem 1 (1 pt)

```py
$ python3 ok -q 01 -u
=====================================================================
Assignment: Project 3: Ants Vs. SomeBees
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 1 > Suite 1 > Case 1
(cases remaining: 5)

Q: What is the purpose of the food_cost attribute?
Choose the number of the correct choice:
0) Each turn, each Ant in the colony eats food_cost food from the
   colony's total available food
1) Each turn, each Ant in the colony adds food_cost food to the
   colony's total available food
2) Placing an ant into the colony will decrease the colony's total
   available food by that ant's food_cost
? 2
-- OK! --

---------------------------------------------------------------------
Problem 1 > Suite 1 > Case 2
(cases remaining: 4)

Q: What type of attribute is food_cost?
Choose the number of the correct choice:
0) instance, the food_cost of an Ant depends on the location it is placed
1) instance, the food_cost of an Ant is randomized upon initialization
2) class, all Ants cost the same to place no matter what type of Ant it is
3) class, all Ants of the same subclass cost the same to place
? 3
-- OK! --

---------------------------------------------------------------------
Problem 1 > Suite 2 > Case 1
(cases remaining: 3)

>>> from ants import *
>>> from ants_plans import *
>>> Ant.food_cost
? 0
-- OK! --

>>> HarvesterAnt.food_cost
? 2
-- OK! --

>>> ThrowerAnt.food_cost
? 3
-- OK! --

---------------------------------------------------------------------
Problem 1 > Suite 2 > Case 2
(cases remaining: 2)

>>> from ants import *
>>> from ants_plans import *
>>> # Testing HarvesterAnt action
>>> # Create a test layout where the colony is a single row with 9 tiles
>>> beehive = Hive(make_test_assault_plan())
>>> gamestate = GameState(None, beehive, ant_types(), dry_layout, (1, 9))
>>> #
>>> gamestate.food = 4
>>> harvester = HarvesterAnt()
>>> # Note: initializing an Ant doesn't cost food,
>>> # only deploying an Ant in the game layout does.
>>> # For this test case, Ants can still take actions
>>> # without being deployed in the game layout.
>>> #
>>> gamestate.food
? 4
-- OK! --

>>> harvester.action(gamestate)
>>> gamestate.food
? 5
-- OK! --

>>> harvester.action(gamestate)
>>> gamestate.food
? 6
-- OK! --

---------------------------------------------------------------------
Problem 1 > Suite 2 > Case 3
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 1 unlocked.
```

**ants/ants.py**

```py
class HarvesterAnt(Ant):
    """HarvesterAnt produces 1 additional food per turn for the colony."""

    name = 'Harvester'
    implemented = True
    # OVERRIDE CLASS ATTRIBUTES HERE
    food_cost = 2

    def action(self, gamestate):
        """Produce 1 additional food for the colony.

        gamestate -- The GameState, used to access game state information.
        """
        # BEGIN Problem 1
        "*** YOUR CODE HERE ***"
        gamestate.food += 1
        # END Problem 1


class ThrowerAnt(Ant):
    """ThrowerAnt throws a leaf each turn at the nearest Bee in its range."""

    name = 'Thrower'
    implemented = True
    damage = 1
    # ADD/OVERRIDE CLASS ATTRIBUTES HERE
    food_cost = 3

    def nearest_bee(self):
        """Return the nearest Bee in a Place that is not the HIVE, connected to
        the ThrowerAnt's Place by following entrances.

        This method returns None if there is no such Bee (or none in range).
        """
        # BEGIN Problem 3 and 4
        return random_bee(self.place.bees)  # REPLACE THIS LINE
        # END Problem 3 and 4

    def throw_at(self, target):
        """Throw a leaf at the TARGET Bee, reducing its health."""
        if target is not None:
            target.reduce_health(self.damage)

    def action(self, gamestate):
        """Throw a leaf at the nearest Bee in range."""
        self.throw_at(self.nearest_bee())
```

## Problem 2 (1 pt)

```py
$ python3 ok -q 02 -u
=====================================================================
Assignment: Project 3: Ants Vs. SomeBees
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 2 > Suite 1 > Case 1
(cases remaining: 5)

Q: What does a Place represent in the game?
Choose the number of the correct choice:
0) Where the bees start out in the game
1) The entire space where the game takes place
2) A single tile that an Ant can be placed on and that connects to
   other Places
3) The tunnel that bees travel through
? 2
-- OK! --

---------------------------------------------------------------------
Problem 2 > Suite 1 > Case 2
(cases remaining: 4)

Q: p is a Place whose entrance is q and exit is r (q and r are not None). When is p.entrance first set to a non-None value?
Choose the number of the correct choice:
0) Never, it is always set to None
1) When q is constructed
2) When p is constructed
? 1
-- OK! --

---------------------------------------------------------------------
Problem 2 > Suite 1 > Case 3
(cases remaining: 3)

Q: p is a Place whose entrance is q and exit is r (q and r are not None). When is p.exit first set to a non-None value?
Choose the number of the correct choice:
0) When q is constructed
1) Never, it is always set to None
2) When p is constructed
? 2
-- OK! --

---------------------------------------------------------------------
Problem 2 > Suite 2 > Case 1
(cases remaining: 2)

>>> from ants import *
>>> from ants_plans import *
>>> #
>>> # Create a test layout where the gamestate is a single row with 3 tiles
>>> beehive, layout = Hive(make_test_assault_plan()), dry_layout
>>> dimensions = (1, 3)
>>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
>>> #
>>> # Simple test for Place
>>> place0 = Place('place_0')
>>> print(place0.exit)
? None
-- OK! --

>>> print(place0.entrance)
? None
-- OK! --

>>> place1 = Place('place_1', place0)
>>> place1.exit is place0
? True
-- OK! --

>>> place0.entrance is place1
? True
-- OK! --

---------------------------------------------------------------------
Problem 2 > Suite 2 > Case 2
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 2 unlocked.
```

**ants/ants.py**

```py
class Place:
    """A Place holds insects and has an exit to another Place."""
    is_hive = False

    def __init__(self, name, exit=None):
        """Create a Place with the given NAME and EXIT.

        name -- A string; the name of this Place.
        exit -- The Place reached by exiting this Place (may be None).
        """
        self.name = name
        self.exit = exit
        self.bees = []        # A list of Bees
        self.ant = None       # An Ant
        self.entrance = None  # A Place
        # Phase 1: Add an entrance to the exit
        # BEGIN Problem 2
        "*** YOUR CODE HERE ***"
        if self.exit is not None:
            self.exit.entrance = self
        # END Problem 2
```

## Problem 3 (2 pt)

```py
$ python3 ok -q 03 -u
=====================================================================
Assignment: Project 3: Ants Vs. SomeBees
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 3 > Suite 1 > Case 1
(cases remaining: 12)

Q: What Bee should a ThrowerAnt throw at?
Choose the number of the correct choice:
0) The ThrowerAnt throws at a random Bee in its own Place
1) The ThrowerAnt finds the nearest place behind its own place
   that has Bees and throws at a random Bee in that place
2) The ThrowerAnt finds the nearest place including and in front of its
   own place that has Bees and throws at a random Bee in that place
3) The ThrowerAnt finds the nearest place in either direction that has
   Bees and throws at a random Bee in that place
? 2
-- OK! --

---------------------------------------------------------------------
Problem 3 > Suite 1 > Case 2
(cases remaining: 11)

Q: How do you get the Place object in front of another Place object?
Choose the number of the correct choice:
0) Decrement the place by 1
1) The place's exit instance attribute
2) Increment the place by 1
3) The place's entrance instance attribute
? 3
-- OK! --

---------------------------------------------------------------------
Problem 3 > Suite 1 > Case 3
(cases remaining: 10)

Q: What is the entrance of the first Place in a tunnel (i.e. where do the bees enter from)?
Choose the number of the correct choice:
0) None
1) The Hive
2) An empty Place
? 1
-- OK! --

---------------------------------------------------------------------
Problem 3 > Suite 1 > Case 4
(cases remaining: 9)

Q: How can you determine if a given Place is the Hive?
Choose the number of the correct choice:
0) by checking the bees attribute of the place instance
1) by using the is_hive attribute of the place instance
2) by checking the ant attribute of the place instance
? 1
-- OK! --

---------------------------------------------------------------------
Problem 3 > Suite 1 > Case 5
(cases remaining: 8)

Q: What should nearest_bee return if there is no Bee in front of the ThrowerAnt in the tunnel?
Choose the number of the correct choice:
0) The closest Bee behind the ThrowerAnt
1) A random Bee in the Hive
2) None
? 2
-- OK! --

---------------------------------------------------------------------
Problem 3 > Suite 2 > Case 1
(cases remaining: 7)

>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
>>> thrower = ThrowerAnt()
>>> ant_place = gamestate.places["tunnel_0_0"]
>>> ant_place.add_insect(thrower)
>>> #
>>> # Testing nearest_bee
>>> near_bee = Bee(2) # A Bee with 2 health
>>> far_bee = Bee(3)  # A Bee with 3 health
>>> hive_bee = Bee(4) # A Bee with 4 health
>>> hive_place = gamestate.beehive
>>> hive_place.is_hive # Check if this place is the Hive
? True
-- OK! --

>>> hive_place.add_insect(hive_bee)
>>> thrower.nearest_bee() is hive_bee # Bees in the Hive can never be attacked
? False
-- OK! --

>>> near_place = gamestate.places['tunnel_0_3']
>>> far_place = gamestate.places['tunnel_0_6']
>>> near_place.is_hive # Check if this place is the Hive
? False
-- OK! --

>>> near_place.add_insect(near_bee)
>>> far_place.add_insect(far_bee)
>>> nearest_bee = thrower.nearest_bee()
>>> nearest_bee is far_bee
? False
-- OK! --

>>> nearest_bee is near_bee
? True
-- OK! --

>>> nearest_bee.health
? 2
-- OK! --

>>> thrower.action(gamestate)    # Attack! ThrowerAnts do 1 damage
>>> near_bee.health
? 1
-- OK! --

>>> far_bee.health
? 3
-- OK! --

>>> thrower.place is ant_place    # Don't change self.place!
? True
-- OK! --

---------------------------------------------------------------------
Problem 3 > Suite 2 > Case 2
(cases remaining: 6)

-- Already unlocked --

---------------------------------------------------------------------
Problem 3 > Suite 2 > Case 3
(cases remaining: 5)

-- Already unlocked --

---------------------------------------------------------------------
Problem 3 > Suite 2 > Case 4
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Problem 3 > Suite 2 > Case 5
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem 3 > Suite 2 > Case 6
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Problem 3 > Suite 2 > Case 7
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 3 unlocked.
```

**ants/ants.py**

```py
class ThrowerAnt(Ant):
    """ThrowerAnt throws a leaf each turn at the nearest Bee in its range."""

    name = 'Thrower'
    implemented = True
    damage = 1
    # ADD/OVERRIDE CLASS ATTRIBUTES HERE
    food_cost = 3

    def nearest_bee(self):
        """Return the nearest Bee in a Place that is not the HIVE, connected to
        the ThrowerAnt's Place by following entrances.

        This method returns None if there is no such Bee (or none in range).
        """
        # BEGIN Problem 3 and 4
        place = self.place
        while not place.is_hive:
            bee = random_bee(place.bees)
            if bee is not None:
                return bee
            place = place.entrance
        return None
        # return random_bee(self.place.bees)  # REPLACE THIS LINE
        # END Problem 3 and 4
```

## Problem 4 (2 pt)

```py
$ python3 ok -q 04 -u
=====================================================================
Assignment: Project 3: Ants Vs. SomeBees
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 4 > Suite 1 > Case 1
(cases remaining: 26)

Q: What class do ShortThrower and LongThrower inherit from?
Choose the number of the correct choice:
0) Bee
1) ShortThrower
2) ThrowerAnt
3) LongThrower
? 2
-- OK! --

---------------------------------------------------------------------
Problem 4 > Suite 1 > Case 2
(cases remaining: 25)

Q: What constraint does a regular ThrowerAnt have on its throwing distance?
Choose the number of the correct choice:
0) There is no restriction on how far a regular ThrowerAnt can throw
1) A regular ThrowerAnt can only attack Bees at most 3 places away
2) A regular ThrowerAnt can only attack Bees at most 5 places away
3) A regular ThrowerAnt can only attack Bees at least 3 places away
? 0
-- OK! --

---------------------------------------------------------------------
Problem 4 > Suite 1 > Case 3
(cases remaining: 24)

Q: What constraint does a LongThrower have on its throwing distance?
Choose the number of the correct choice:
0) A LongThrower can only attack Bees at most 5 places away
1) There is no restriction on how far a LongThrower can throw
2) A LongThrower can only attack Bees at least 5 places away
3) A LongThrower can only attack Bees at least 3 places away
? 2
-- OK! --

---------------------------------------------------------------------
Problem 4 > Suite 1 > Case 4
(cases remaining: 23)

Q: What constraint does a ShortThrower have on its throwing distance?
Choose the number of the correct choice:
0) A ShortThrower can only attack Bees at most 5 places away
1) A ShortThrower can only attack Bees at least 3 places away
2) There is no restriction on how far a ShortThrower can throw
3) A ShortThrower can only attack Bees at most 3 places away
? 3
-- OK! --

---------------------------------------------------------------------
Problem 4 > Suite 1 > Case 5
(cases remaining: 22)

Q: With the addition of these new ThrowerAnt subclasses, we must modify
our definition of nearest_bee. Now what Bee should ThrowerAnts throw
at?
Choose the number of the correct choice:
0) The closest Bee behind it within range
1) Any Bee within range
2) The closest Bee in front of it within range
3) Any Bee in its current Place
? 2
-- OK! --

---------------------------------------------------------------------
Problem 4 > Suite 2 > Case 1
(cases remaining: 21)

>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
>>> #
>>> # Testing Long/ShortThrower parameters
>>> ShortThrower.food_cost
? 2
-- OK! --

>>> LongThrower.food_cost
? 2
-- OK! --

>>> short_t = ShortThrower()
>>> long_t = LongThrower()
>>> short_t.health
? 1
-- OK! --

>>> long_t.health
? 1
-- OK! --

---------------------------------------------------------------------
OK! All cases for Problem 4 unlocked.
```

**ants/ants.py**

```py
class ThrowerAnt(Ant):
    """ThrowerAnt throws a leaf each turn at the nearest Bee in its range."""

    name = 'Thrower'
    implemented = True
    damage = 1
    # ADD/OVERRIDE CLASS ATTRIBUTES HERE
    food_cost = 3
    min_range = 0
    max_range = float('inf')

    def nearest_bee(self):
        """Return the nearest Bee in a Place that is not the HIVE, connected to
        the ThrowerAnt's Place by following entrances.

        This method returns None if there is no such Bee (or none in range).
        """
        # BEGIN Problem 3 and 4
        place = self.place
        dist = 0
        while not place.is_hive:
            bee = random_bee(place.bees)
            if bee is not None and self.min_range <= dist <= self.max_range:
                return bee
            place = place.entrance
            dist += 1
        return None
        # return random_bee(self.place.bees)  # REPLACE THIS LINE
        # END Problem 3 and 4

    def throw_at(self, target):
        """Throw a leaf at the TARGET Bee, reducing its health."""
        if target is not None:
            target.reduce_health(self.damage)

    def action(self, gamestate):
        """Throw a leaf at the nearest Bee in range."""
        self.throw_at(self.nearest_bee())


def random_bee(bees):
    """Return a random bee from a list of bees, or return None if bees is empty."""
    assert isinstance(bees, list), "random_bee's argument should be a list but was a %s" % type(bees).__name__
    if bees:
        return random.choice(bees)

##############
# Extensions #
##############


class ShortThrower(ThrowerAnt):
    """A ThrowerAnt that only throws leaves at Bees at most 3 places away."""

    name = 'Short'
    food_cost = 2
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN Problem 4
    implemented = True   # Change to True to view in the GUI
    min_range = 0
    max_range = 3
    # END Problem 4


class LongThrower(ThrowerAnt):
    """A ThrowerAnt that only throws leaves at Bees at least 5 places away."""

    name = 'Long'
    food_cost = 2
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN Problem 4
    implemented = True   # Change to True to view in the GUI
    min_range = 5
    max_range = float('inf')
    # END Problem 4
```

## Problem 5 (3 pt)

```py
$ python3 ok -q 05 -u
=====================================================================
Assignment: Project 3: Ants Vs. SomeBees
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 5 > Suite 1 > Case 1
(cases remaining: 16)

Q: How can you obtain the current place of a FireAnt?
Choose the number of the correct choice:
0) By calling the FireAnt constructor
1) By accessing the place instance attribute, which is the name of
   some Place object
2) By accessing the place instance attribute, which is a Place object
3) By calling the Place constructor, passing in the FireAnt instance
? 2
-- OK! --

---------------------------------------------------------------------
Problem 5 > Suite 1 > Case 2
(cases remaining: 15)

Q: How can you obtain all of the Bees currently in a given place?
Choose the number of the correct choice:
0) By calling the Bee constructor, passing in the place instance
1) By accessing the bees instance attribute, which is a dictionary of
   Bee objects
2) By calling the add_insect method on the place instance
3) By accessing the bees instance attribute, which is a list of Bee
   objects
? 3
-- OK! --

---------------------------------------------------------------------
Problem 5 > Suite 1 > Case 3
(cases remaining: 14)

Q: Can you iterate over a list while mutating it?
Choose the number of the correct choice:
0) Yes, you can mutate a list while iterating over it with no problems
1) Yes, but you should iterate over a copy of the list to avoid skipping
   elements
2) No, Python doesn't allow list mutation on a list that is being
   iterated through
? 1
-- OK! --

---------------------------------------------------------------------
Problem 5 > Suite 2 > Case 1
(cases remaining: 13)

>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
>>> #
>>> # Testing FireAnt parameters
>>> fire = FireAnt()
>>> FireAnt.food_cost
? 5
-- OK! --

>>> fire.health
? 3
-- OK! --

---------------------------------------------------------------------
Problem 5 > Suite 2 > Case 2
(cases remaining: 12)

-- Already unlocked --

---------------------------------------------------------------------
Problem 5 > Suite 2 > Case 3
(cases remaining: 11)

>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
>>> #
>>> # Testing fire does damage to all Bees in its Place
>>> place = gamestate.places['tunnel_0_4']
>>> fire = FireAnt(health=1)
>>> place.add_insect(fire)        # Add a FireAnt with 1 health
>>> place.add_insect(Bee(3))      # Add a Bee with 3 health
>>> place.add_insect(Bee(5))      # Add a Bee with 5 health
>>> len(place.bees)               # How many bees are there?
? 2
-- OK! --

>>> place.bees[0].action(gamestate)  # The first Bee attacks FireAnt
>>> fire.health
? 0
-- OK! --

>>> fire.place is None
? True
-- OK! --

>>> len(place.bees)               # How many bees are left?
? 1
-- OK! --

>>> place.bees[0].health           # What is the health of the remaining Bee?
? 1
-- OK! --

---------------------------------------------------------------------
Problem 5 > Suite 2 > Case 4
(cases remaining: 10)

>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
>>> #
>>> place = gamestate.places['tunnel_0_4']
>>> ant = FireAnt(health=1)           # Create a FireAnt with 1 health
>>> place.add_insect(ant)      # Add a FireAnt to place
>>> ant.place is place
? True
-- OK! --

>>> place.remove_insect(ant)   # Remove FireAnt from place
>>> ant.place is place         # Is the ant's place still that place?
? False
-- OK! --

---------------------------------------------------------------------
OK! All cases for Problem 5 unlocked.
```

**ants/ants.py**

```py
class FireAnt(Ant):
    """FireAnt cooks any Bee in its Place when it expires."""

    name = 'Fire'
    damage = 3
    food_cost = 5
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN Problem 5
    implemented = True   # Change to True to view in the GUI
    # END Problem 5

    def __init__(self, health=3):
        """Create an Ant with a HEALTH quantity."""
        super().__init__(health)

    def reduce_health(self, amount):
        """Reduce health by AMOUNT, and remove the FireAnt from its place if it
        has no health remaining.

        Make sure to reduce the health of each bee in the current place, and apply
        the additional damage if the fire ant dies.
        """
        # BEGIN Problem 5
        "*** YOUR CODE HERE ***"
        for bee in self.place.bees[:]:
            bee.reduce_health(amount)

        if self.health <= amount:
            for bee in self.place.bees[:]:
                bee.reduce_health(self.damage)
            super().reduce_health(amount)
        else:
            super().reduce_health(amount)
        # END Problem 5
```

## Problem 6 (1 pt)

```py
$ python3 ok -q 06 -u
=====================================================================
Assignment: Project 3: Ants Vs. SomeBees
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 6 > Suite 1 > Case 1
(cases remaining: 8)

Q: What class does WallAnt inherit from?
Choose the number of the correct choice:
0) The WallAnt class does not inherit from any class
1) ThrowerAnt
2) Ant
3) HungryAnt
? 2
-- OK! --

---------------------------------------------------------------------
Problem 6 > Suite 1 > Case 2
(cases remaining: 7)

Q: What is a WallAnt's action?
Choose the number of the correct choice:
0) A WallAnt attacks all the Bees in its place each turn
1) A WallAnt increases its own health by 1 each turn
2) A WallAnt reduces its own health by 1 each turn
3) A WallAnt takes no action each turn
? 3
-- OK! --

---------------------------------------------------------------------
Problem 6 > Suite 1 > Case 3
(cases remaining: 6)

Q: Where do Ant subclasses inherit the action method from?
Choose the number of the correct choice:
0) Ant subclasses inherit the action method from the Ant class
1) Ant subclasses inherit the action method from the Insect class
2) Ant subclasses do not inherit the action method from any class
? 1
-- OK! --

---------------------------------------------------------------------
Problem 6 > Suite 1 > Case 4
(cases remaining: 5)

Q: If a subclass of Ant does not override the action method, what is the
default action?
Choose the number of the correct choice:
0) Move to the next place
1) Nothing
2) Reduce the health of all Bees in its place
3) Throw a leaf at the nearest Bee
? 1
-- OK! --

---------------------------------------------------------------------
OK! All cases for Problem 6 unlocked.
```

**ants/ants.py**

```py
# BEGIN Problem 6
# The WallAnt class
class WallAnt(Ant):
    """WallAnt has a large health value"""
    name = 'Wall'
    damage = 0
    food_cost = 4
    implemented = True   # Change to True to view in the GUI

    def __init__(self, health=4):
        super().__init__(health)
# END Problem 6
```

## Problem 7 (3 pt)

```py
$ python3 ok -q 07 -u
=====================================================================
Assignment: Project 3: Ants Vs. SomeBees
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 7 > Suite 1 > Case 1
(cases remaining: 14)

Q: Should chew_timer be an instance or class attribute? Why?
Choose the number of the correct choice:
0) class, all HungryAnt instances in the game chew simultaneously
1) instance, all HungryAnt instances in the game chew simultaneously
2) instance, each HungryAnt instance chews independently of other
   HungryAnt instances
3) class, each HungryAnt instance chews independently of other
   HungryAnt instances
? 2
-- OK! --

---------------------------------------------------------------------
Problem 7 > Suite 1 > Case 2
(cases remaining: 13)

Q: When is a HungryAnt able to eat a Bee?
Choose the number of the correct choice:
0) Whenever a Bee is in its place
1) When it is chewing, i.e. when its chew_timer attribute is at least 1
2) Each turn
3) When it is not chewing, i.e. when its chew_timer attribute is 0
? 3
-- OK! --

---------------------------------------------------------------------
Problem 7 > Suite 1 > Case 3
(cases remaining: 12)

Q: When a HungryAnt is able to eat, which Bee does it eat?
Choose the number of the correct choice:
0) The closest Bee behind it
1) The closest Bee in either direction
2) A random Bee in the same place as itself
3) The closest Bee in front of it
? 2
-- OK! --

---------------------------------------------------------------------
Problem 7 > Suite 2 > Case 1
(cases remaining: 11)

>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
>>> #
>>> # Testing HungryAnt parameters
>>> hungry = HungryAnt()
>>> HungryAnt.food_cost
? 4
-- OK! --

>>> hungry.health
? 1
-- OK! --

>>> hungry.time_to_chew
? 3
-- OK! --

>>> hungry.chew_timer
? 0
-- OK! --

---------------------------------------------------------------------
Problem 7 > Suite 2 > Case 2
(cases remaining: 10)

-- Already unlocked --

---------------------------------------------------------------------
Problem 7 > Suite 2 > Case 3
(cases remaining: 9)

-- Already unlocked --

---------------------------------------------------------------------
Problem 7 > Suite 2 > Case 4
(cases remaining: 8)

>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
>>> #
>>> # Testing HungryAnt eats and chews
>>> hungry = HungryAnt()
>>> super_bee, wimpy_bee = Bee(1000), Bee(1)
>>> place = gamestate.places["tunnel_0_0"]
>>> place.add_insect(hungry)
>>> place.add_insect(super_bee)
>>> hungry.action(gamestate)         # super_bee is no match for HungryAnt!
>>> super_bee.health
? 0
-- OK! --

>>> place.add_insect(wimpy_bee)
>>> for _ in range(3):
...     hungry.action(gamestate)     # chewing...not eating
>>> wimpy_bee.health
? 1
-- OK! --

>>> hungry.action(gamestate)         # back to eating!
>>> wimpy_bee.health
? 0
-- OK! --

---------------------------------------------------------------------
Problem 7 > Suite 2 > Case 5
(cases remaining: 7)

-- Already unlocked --

---------------------------------------------------------------------
Problem 7 > Suite 2 > Case 6
(cases remaining: 6)

-- Already unlocked --

---------------------------------------------------------------------
Problem 7 > Suite 2 > Case 7
(cases remaining: 5)

-- Already unlocked --

---------------------------------------------------------------------
Problem 7 > Suite 2 > Case 8
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Problem 7 > Suite 2 > Case 9
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem 7 > Suite 2 > Case 10
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Problem 7 > Suite 3 > Case 1
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 7 unlocked.
```

**ants/ants.py**

```py
# BEGIN Problem 7
# The HungryAnt Class
class HungryAnt(Ant):
    """HungryAnt will select a random bee from its place and eat it whole"""
    name = 'Hungry'
    damage = 0
    food_cost = 4
    implemented = True   # Change to True to view in the GUI
    time_to_chew = 3

    def __init__(self, health=1):
        super().__init__(health)
        self.chew_timer = 0

    def action(self, gamestate):
        if self.chew_timer != 0:
            self.chew_timer -= 1
        else:
            if len(self.place.bees) > 0:
                self.chew_timer = self.time_to_chew
                bee = random_bee(self.place.bees)
                bee.reduce_health(bee.health)
# END Problem 7
```

## Problem 8 (3 pt)

```py
$ python3 ok -q 08 -u
=====================================================================
Assignment: Project 3: Ants Vs. SomeBees
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 8 > Suite 1 > Case 1
(cases remaining: 20)

Q: Which Ant does a BodyguardAnt guard?
Choose the number of the correct choice:
0) All the Ant instances in the gamestate
1) The Ant instance in the place closest to its own place
2) The Ant instance that is in the same place as itself
3) A random Ant instance in the gamestate
? 2
-- OK! --

---------------------------------------------------------------------
Problem 8 > Suite 1 > Case 2
(cases remaining: 19)

Q: How does a BodyguardAnt guard its ant?
Choose the number of the correct choice:
0) By allowing Bees to pass without attacking
1) By attacking Bees that try to attack it
2) By increasing the ant's health
3) By protecting the ant from Bees and allowing it to perform its original action
? 3
-- OK! --

---------------------------------------------------------------------
Problem 8 > Suite 1 > Case 3
(cases remaining: 18)

Q: Where is the ant contained by a BodyguardAnt stored?
Choose the number of the correct choice:
0) In its place's ant instance attribute
1) Nowhere, a BodyguardAnt has no knowledge of the ant that it's protecting
2) In the BodyguardAnt's ant_contained instance attribute
3) In the BodyguardAnt's ant_contained class attribute
? 2
-- OK! --

---------------------------------------------------------------------
Problem 8 > Suite 1 > Case 4
(cases remaining: 17)

Q: When can a second Ant be added to a place that already contains an Ant?
Choose the number of the correct choice:
0) When both Ant instances are containers
1) When exactly one of the Ant instances is a container and the
   container ant does not already contain another ant
2) There can never be two Ant instances in the same place
3) When exactly one of the Ant instances is a container
? 1
-- OK! --

---------------------------------------------------------------------
Problem 8 > Suite 1 > Case 5
(cases remaining: 16)

Q: If two Ants occupy the same Place, what is stored in that place's ant
instance attribute?
Choose the number of the correct choice:
0) The Ant being contained
1) Whichever Ant was placed there first
2) The Container Ant
3) A list containing both Ants
? 2
-- OK! --

---------------------------------------------------------------------
Problem 8 > Suite 2 > Case 1
(cases remaining: 15)

>>> from ants import *
>>> # Testing BodyguardAnt parameters
>>> bodyguard = BodyguardAnt()
>>> BodyguardAnt.food_cost
? 4
-- OK! --

>>> bodyguard.health
? 2
-- OK! --

---------------------------------------------------------------------
Problem 8 > Suite 2 > Case 2
(cases remaining: 14)

-- Already unlocked --

---------------------------------------------------------------------
Problem 8 > Suite 3 > Case 1
(cases remaining: 13)

-- Already unlocked --

---------------------------------------------------------------------
Problem 8 > Suite 3 > Case 2
(cases remaining: 12)

>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> gamestate = GameState(None, beehive, ant_types(), layout, (1, 9))
>>> #
>>> # Bodyguard ant added before another ant
>>> bodyguard = BodyguardAnt()
>>> other_ant = ThrowerAnt()
>>> place = gamestate.places['tunnel_0_0']
>>> place.add_insect(bodyguard)  # Bodyguard in place first
>>> place.add_insect(other_ant)
>>> place.ant is bodyguard
? True
-- OK! --

>>> bodyguard.ant_contained is other_ant
? True
-- OK! --

---------------------------------------------------------------------
Problem 8 > Suite 3 > Case 3
(cases remaining: 11)

>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> gamestate = GameState(None, beehive, ant_types(), layout, (1, 9))
>>> #
>>> # Bodyguard ant can be added after another ant
>>> bodyguard = BodyguardAnt()
>>> other_ant = ThrowerAnt()
>>> place = gamestate.places['tunnel_0_0']
>>> place.add_insect(other_ant)  # Other ant in place first
>>> place.ant is other_ant
? True
-- OK! --

>>> place.add_insect(bodyguard)
>>> place.ant is bodyguard
? True
-- OK! --

>>> bodyguard.ant_contained is other_ant
? True
-- OK! --

---------------------------------------------------------------------
OK! All cases for Problem 8 unlocked.
```

**ants/ants.py**

```py
class Ant(Insect):
    """An Ant occupies a place and does work for the colony."""

    implemented = False  # Only implemented Ant classes should be instantiated
    food_cost = 0
    is_container = False

    # ADD CLASS ATTRIBUTES HERE

    def __init__(self, health=1):
        """Create an Insect with a HEALTH quantity."""
        super().__init__(health)

    @classmethod
    def construct(cls, gamestate):
        """Create an Ant for a given GameState, or return None if not possible."""
        if cls.food_cost > gamestate.food:
            print('Not enough food remains to place ' + cls.__name__)
            return
        return cls()

    def can_contain(self, other):
        return False

    def store_ant(self, other):
        assert False, "{0} cannot contain an ant".format(self)

    def remove_ant(self, other):
        assert False, "{0} cannot contain an ant".format(self)

    def add_to(self, place):
        if place.ant is None:
            place.ant = self
        else:
            # BEGIN Problem 8
            # assert place.ant is None, 'Two ants in {0}'.format(place)
            if place.ant.can_contain(self) or self.can_contain(place.ant):
                if place.ant.is_container and place.ant.can_contain(self):
                    place.ant.store_ant(self)
                elif self.is_container and self.can_contain(place.ant):
                    self.store_ant(place.ant)
                    place.ant = self
            else:
                assert place.ant is None, 'Two ants in {0}'.format(place)
            # END Problem 8
        Insect.add_to(self, place)


class ContainerAnt(Ant):
    """
    ContainerAnt can share a space with other ants by containing them.
    """
    is_container = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ant_contained = None

    def can_contain(self, other):
        # BEGIN Problem 8
        "*** YOUR CODE HERE ***"
        return self.ant_contained is None and not other.is_container
        # return False
        # END Problem 8

    def store_ant(self, ant):
        # BEGIN Problem 8
        "*** YOUR CODE HERE ***"
        self.ant_contained = ant
        # END Problem 8

    def remove_ant(self, ant):
        if self.ant_contained is not ant:
            assert False, "{} does not contain {}".format(self, ant)
        self.ant_contained = None

    def remove_from(self, place):
        # Special handling for container ants (this is optional)
        if place.ant is self:
            # Container was removed. Contained ant should remain in the game
            place.ant = place.ant.ant_contained
            Insect.remove_from(self, place)
        else:
            # default to normal behavior
            Ant.remove_from(self, place)

    def action(self, gamestate):
        # BEGIN Problem 8
        "*** YOUR CODE HERE ***"
        if self.ant_contained is not None:
            return self.ant_contained.action(gamestate)
        # END Problem 8


class BodyguardAnt(ContainerAnt):
    """BodyguardAnt provides protection to other Ants."""

    name = 'Bodyguard'
    food_cost = 4
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN Problem 8
    implemented = True  # Change to True to view in the GUI

    def __init__(self, health=2):
        super().__init__(health)
    # END Problem 8
```

## Problem 9 (1 pt)

```py
$ python3 ok -q 09 -u
=====================================================================
Assignment: Project 3: Ants Vs. SomeBees
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 9 > Suite 1 > Case 1
(cases remaining: 13)

Q: Besides costing more to place, what is the only difference between a
TankAnt and a BodyguardAnt?
Choose the number of the correct choice:
0) A TankAnt increases the damage of the ant it contains
1) A TankAnt has greater health than a BodyguardAnt
2) A TankAnt does damage to all Bees in its place each turn
3) A TankAnt can contain multiple ants
? 2
-- OK! --

---------------------------------------------------------------------
Problem 9 > Suite 2 > Case 1
(cases remaining: 12)

>>> from ants_plans import *
>>> from ants import *
>>> beehive, layout = Hive(make_test_assault_plan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
>>> #
>>> # Testing TankAnt parameters
>>> TankAnt.food_cost
? 6
-- OK! --

>>> TankAnt.damage
? 1
-- OK! --

>>> tank = TankAnt()
>>> tank.health
? 2
-- OK! --

---------------------------------------------------------------------
OK! All cases for Problem 9 unlocked.
```

**ants/ants.py**

```py
# BEGIN Problem 9
# The TankAnt class
class TankAnt(ContainerAnt):
    """TankAnt provides both offensive and defensive capabilities."""

    name = 'Tank'
    food_cost = 6
    # OVERRIDE CLASS ATTRIBUTES HERE
    damage = 1

    implemented = True  # Change to True to view in the GUI

    def __init__(self, health=2):
        super().__init__(health)

    def action(self, gamestate):
        if self.ant_contained is not None:
            self.ant_contained.action(gamestate)
        for bee in self.place.bees[:]:
            bee.reduce_health(self.damage)
# END Problem 9
```

## Problem 10 (1 pt)

```py
$ python3 ok -q 10 -u
=====================================================================
Assignment: Project 3: Ants Vs. SomeBees
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 10 > Suite 1 > Case 1
(cases remaining: 8)

Q: What happens when an insect is added to a Water Place?
Choose the number of the correct choice:
0) The insect goes for a swim.
1) The insect's health is reduced to 0.
2) If the insect is not waterproof, its health is reduced to 0.
   Otherwise, nothing happens.
3) Nothing happens.
? 2
-- OK! --

---------------------------------------------------------------------
Problem 10 > Suite 1 > Case 2
(cases remaining: 7)

Q: What type of attribute should "is_waterproof" be?
Choose the number of the correct choice:
0) instance, the is_waterproof attribute depends on the given place of an ant
1) class, all ants should be waterproof
2) instance, the is_waterproof attribute depends on the amount of health a given ant has left
3) class, all ants of a subclass should either be waterproof or not
? 3
-- OK! --

---------------------------------------------------------------------
Problem 10 > Suite 1 > Case 3
(cases remaining: 6)

Q: What method deals damage to an Insect and removes it from its place
if its health reaches 0?
Choose the number of the correct choice:
0) sting, in the Bee class
1) remove_ant, in the GameState class
2) reduce_health, in the Insect class
3) remove_insect, in the Place class
? 2
-- OK! --

---------------------------------------------------------------------
Problem 10 > Suite 2 > Case 1
(cases remaining: 5)

-- Already unlocked --

---------------------------------------------------------------------
Problem 10 > Suite 2 > Case 2
(cases remaining: 4)

>>> from ants import *
>>> from ants_plans import *
>>> beehive, layout = Hive(make_test_assault_plan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
>>> #
>>> # Testing water with soggy (non-waterproof) bees
>>> test_bee = Bee(1000000)
>>> test_bee.is_waterproof = False    # Make Bee non-waterproof
>>> test_water = Water('Water Test2')
>>> test_water.add_insect(test_bee)
>>> test_bee.health
? 0
-- OK! --

>>> len(test_water.bees)
? 0
-- OK! --

---------------------------------------------------------------------
Problem 10 > Suite 2 > Case 3
(cases remaining: 3)

>>> from ants import *
>>> from ants_plans import *
>>> beehive, layout = Hive(make_test_assault_plan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
>>> #
>>> # Testing water with waterproof bees
>>> test_bee = Bee(1)
>>> test_water = Water('Water Test3')
>>> test_water.add_insect(test_bee)
>>> test_bee.health
? 1
-- OK! --

>>> test_bee in test_water.bees
? True
-- OK! --

---------------------------------------------------------------------
Problem 10 > Suite 2 > Case 4
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Problem 10 > Suite 3 > Case 1
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 10 unlocked.
```

**ants/ants.py**

```py
class Insect:
    """An Insect, the base class of Ant and Bee, has health and a Place."""

    damage = 0

    # ADD CLASS ATTRIBUTES HERE
    is_waterproof = False


class Water(Place):
    """Water is a place that can only hold waterproof insects."""

    def add_insect(self, insect):
        """Add an Insect to this place. If the insect is not waterproof, reduce
        its health to 0."""
        # BEGIN Problem 10
        "*** YOUR CODE HERE ***"
        super().add_insect(insect)
        if not insect.is_waterproof:
            insect.reduce_health(insect.health)
        # END Problem 10


class Bee(Insect):
    """A Bee moves from place to place, following exits and stinging ants."""

    name = 'Bee'
    damage = 1

    # OVERRIDE CLASS ATTRIBUTES HERE
    is_waterproof = True
```

## Problem 11 (1 pt)

```py
$ python3 ok -q 11 -u
=====================================================================
Assignment: Project 3: Ants Vs. SomeBees
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 11 > Suite 1 > Case 1
(cases remaining: 9)

Q: How is a ScubaThrower different from a regular ThrowerAnt?
Choose the number of the correct choice:
0) It is not waterproof, so its health will be reduced to 0 when it is
   placed in a Water Place
1) It throws water pellets instead of leaves
2) It is waterproof, so its health won't be reduced to 0 when it is
   placed in a Water Place
? 2
-- OK! --

---------------------------------------------------------------------
Problem 11 > Suite 1 > Case 2
(cases remaining: 8)

Q: Which inherited attributes and/or methods should ScubaThrower
override?
Choose the number of the correct choice:
0) is_waterproof, action
1) name, nearest_bee, is_waterproof
2) food_cost, action, damage
3) name, is_waterproof, food_cost
? 3
-- OK! --

---------------------------------------------------------------------
Problem 11 > Suite 2 > Case 1
(cases remaining: 7)

>>> from ants import *
>>> # Testing ScubaThrower parameters
>>> scuba = ScubaThrower()
>>> ScubaThrower.food_cost
? 6
-- OK! --

>>> scuba.health
? 1
-- OK! --

---------------------------------------------------------------------
Problem 11 > Suite 3 > Case 1
(cases remaining: 6)

>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
>>> #
>>> # Testing if ScubaThrower is waterproof
>>> water = Water('Water')
>>> ant = ScubaThrower()
>>> water.add_insect(ant)
>>> ant.place is water
? True
-- OK! --

>>> ant.health
? 1
-- OK! --

---------------------------------------------------------------------
Problem 11 > Suite 3 > Case 2
(cases remaining: 5)

>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
>>> #
>>> # Testing that ThrowerAnt is not waterproof
>>> water = Water('Water')
>>> ant = ThrowerAnt()
>>> water.add_insect(ant)
>>> ant.place is water
? False
-- OK! --

>>> ant.health
? 0
-- OK! --

---------------------------------------------------------------------
OK! All cases for Problem 11 unlocked.
```

**ants/ants.py**

```py
# BEGIN Problem 11
# The ScubaThrower class
class ScubaThrower(ThrowerAnt):
    """ScubaThrower is water proof"""

    name = 'Scuba'
    food_cost = 6
    # OVERRIDE CLASS ATTRIBUTES HERE
    is_waterproof = True
    implemented = True  # Change to True to view in the GUI

    def __init__(self, health=1):
        super().__init__(health)
# END Problem 11
```

## Problem 12 (3 pt)

```py
$ python3 ok -q 12 -u
=====================================================================
Assignment: Project 3: Ants Vs. SomeBees
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 12 > Suite 1 > Case 1
(cases remaining: 16)

Q: What class does QueenAnt inherit from?
Choose the number of the correct choice:
0) GameState
1) Ant
2) ScubaThrower
3) Insect
? 2
-- OK! --

---------------------------------------------------------------------
Problem 12 > Suite 1 > Case 2
(cases remaining: 15)

Q: What does the true QueenAnt do each turn?
Choose the number of the correct choice:
0) Doubles the damage of all the ants in the colony (that haven't
   already been doubled)
1) Doubles the damage of all the ants behind her (that haven't
   already been doubled)
2) Doubles the damage of all the ants in front of her (that haven't
   already been doubled)
3) Attacks the nearest bee and doubles the damage of all the ants
   behind her (that haven't already been doubled)
? 3
-- OK! --

---------------------------------------------------------------------
Problem 12 > Suite 1 > Case 3
(cases remaining: 14)

Q: Under what circumstances do Ants lose the game?
Choose the number of the correct choice:
0) If a second QueenAnt is placed in the colony
1) If a Bee attacks the true QueenAnt
2) If a Bee reaches the end of a tunnel or the true QueenAnt dies
3) If there are no ants left in the colony
? 2
-- OK! --

---------------------------------------------------------------------
Problem 12 > Suite 2 > Case 1
(cases remaining: 13)

>>> from ants import *
>>> beehive = Hive(AssaultPlan())
>>> dimensions = (2, 9)
>>> gamestate = GameState(None, beehive, ant_types(), dry_layout, dimensions, food=100)
>>> # Testing QueenAnt parameters
>>> QueenAnt.food_cost
? 7
-- OK! --

>>> queen = QueenAnt()
>>> queen.health
? 1
-- OK! --

---------------------------------------------------------------------
OK! All cases for Problem 12 unlocked.
```

**ants/ants.py**

```py
class Ant(Insect):
    """An Ant occupies a place and does work for the colony."""

    implemented = False  # Only implemented Ant classes should be instantiated
    food_cost = 0
    is_container = False

    # ADD CLASS ATTRIBUTES HERE
    is_doubled = False

    def __init__(self, health=1):
        """Create an Insect with a HEALTH quantity."""
        super().__init__(health)

    @classmethod
    def construct(cls, gamestate):
        """Create an Ant for a given GameState, or return None if not possible."""
        if cls.food_cost > gamestate.food:
            print('Not enough food remains to place ' + cls.__name__)
            return
        return cls()

    def can_contain(self, other):
        return False

    def store_ant(self, other):
        assert False, "{0} cannot contain an ant".format(self)

    def remove_ant(self, other):
        assert False, "{0} cannot contain an ant".format(self)

    def add_to(self, place):
        if place.ant is None:
            place.ant = self
        else:
            # BEGIN Problem 8
            # assert place.ant is None, 'Two ants in {0}'.format(place)
            if place.ant.can_contain(self) or self.can_contain(place.ant):
                if place.ant.is_container and place.ant.can_contain(self):
                    place.ant.store_ant(self)
                elif self.is_container and self.can_contain(place.ant):
                    self.store_ant(place.ant)
                    place.ant = self
            else:
                assert place.ant is None, 'Two ants in {0}'.format(place)
            # END Problem 8
        Insect.add_to(self, place)

    def remove_from(self, place):
        if place.ant is self:
            place.ant = None
        elif place.ant is None:
            assert False, '{0} is not in {1}'.format(self, place)
        else:
            place.ant.remove_ant(self)
        Insect.remove_from(self, place)

    def double(self):
        """Double this ants's damage, if it has not already been doubled."""
        # BEGIN Problem 12
        "*** YOUR CODE HERE ***"
        self.damage *= 2
        # END Problem 12


# BEGIN Problem 12
class QueenAnt(ScubaThrower):  # You should change this line
    # END Problem 12
    """The Queen of the colony. The game is over if a bee enters her place."""

    name = 'Queen'
    food_cost = 7
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN Problem 12
    implemented = True  # Change to True to view in the GUI

    # END Problem 12

    @classmethod
    def construct(cls, gamestate):
        """
        Returns a new instance of the Ant class if it is possible to construct, or
        returns None otherwise. Remember to call the construct() method of the superclass!
        """
        # BEGIN Problem 12
        "*** YOUR CODE HERE ***"
        if cls.food_cost > gamestate.food:
            print('Not enough food remains to place ' + cls.__name__)
            return
        if not gamestate.has_queen:
            gamestate.has_queen = True
            return super().construct(gamestate)
        else:
            return None
        # END Problem 12

    def action(self, gamestate):
        """A queen ant throws a leaf, but also doubles the damage of ants
        in her tunnel.
        """
        # BEGIN Problem 12
        "*** YOUR CODE HERE ***"
        super().action(gamestate)
        pos = self.place.exit
        while pos:
            if pos.ant is not None:
                if not pos.ant.is_doubled:
                    pos.ant.is_doubled = True
                    pos.ant.double()
                if pos.ant.is_container and pos.ant.ant_contained is not None:
                    if not pos.ant.ant_contained.is_doubled:
                        pos.ant.ant_contained.double()
                        pos.ant.ant_contained.is_doubled = True
            pos = pos.exit
        # END Problem 12

    def reduce_health(self, amount):
        """Reduce health by AMOUNT, and if the QueenAnt has no health
        remaining, signal the end of the game.
        """
        # BEGIN Problem 12
        "*** YOUR CODE HERE ***"
        if self.health <= amount:
            ants_lose()
        # END Problem 12

    def remove_from(self, place):
        return None


class GameState:
    """An ant collective that manages global game state and simulates time.

    Attributes:
    time -- elapsed time
    food -- the colony's available food total
    places -- A list of all places in the colony (including a Hive)
    bee_entrances -- A list of places that bees can enter
    """

    def __init__(self, strategy, beehive, ant_types, create_places, dimensions, food=2):
        """Create an GameState for simulating a game.

        Arguments:
        strategy -- a function to deploy ants to places
        beehive -- a Hive full of bees
        ant_types -- a list of ant classes
        create_places -- a function that creates the set of places
        dimensions -- a pair containing the dimensions of the game layout
        """
        self.time = 0
        self.food = food
        self.strategy = strategy
        self.beehive = beehive
        self.ant_types = OrderedDict((a.name, a) for a in ant_types)
        self.dimensions = dimensions
        self.active_bees = []
        self.configure(beehive, create_places)
        # Problem 12 add instance variable here
        self.has_queen = False
```

## Extra Credit (2 pt)

```py
$ python3 ok -q EC -u
=====================================================================
Assignment: Project 3: Ants Vs. SomeBees
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem EC > Suite 1 > Case 1
(cases remaining: 10)

>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
>>> # Testing status parameters
>>> slow = SlowThrower()
>>> scary = ScaryThrower()
>>> SlowThrower.food_cost
? 4
-- OK! --

>>> ScaryThrower.food_cost
? 6
-- OK! --

>>> slow.health
? 1
-- OK! --

>>> scary.health
? 1
-- OK! --

---------------------------------------------------------------------
Problem EC > Suite 1 > Case 2
(cases remaining: 9)

>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
>>> # Testing Slow
>>> slow = SlowThrower()
>>> bee = Bee(3)
>>> gamestate.places["tunnel_0_0"].add_insect(slow)
>>> gamestate.places["tunnel_0_4"].add_insect(bee)
>>> slow.action(gamestate)
>>> gamestate.time = 1
>>> bee.action(gamestate)
>>> bee.place.name # SlowThrower should cause slowness on odd turns
? 'tunnel_0_4'
-- OK! --

>>> gamestate.time += 1
>>> bee.action(gamestate)
>>> bee.place.name # SlowThrower should cause slowness on odd turns
? 'tunnel_0_3'
-- OK! --

>>> for _ in range(3):
...    gamestate.time += 1
...    bee.action(gamestate)
>>> bee.place.name
? 'tunnel_0_1'
-- OK! --

---------------------------------------------------------------------
Problem EC > Suite 1 > Case 3
(cases remaining: 8)

>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
>>> # Testing Scare
>>> scary = ScaryThrower()
>>> bee = Bee(3)
>>> gamestate.places["tunnel_0_0"].add_insect(scary)
>>> gamestate.places["tunnel_0_4"].add_insect(bee)
>>> scary.action(gamestate)
>>> bee.action(gamestate)
>>> bee.place.name # ScaryThrower should scare for two turns
? 'tunnel_0_5'
-- OK! --

>>> bee.action(gamestate)
>>> bee.place.name # ScaryThrower should scare for two turns
? 'tunnel_0_6'
-- OK! --

>>> bee.action(gamestate)
>>> bee.place.name
? 'tunnel_0_5'
-- OK! --

---------------------------------------------------------------------
Problem EC > Suite 1 > Case 4
(cases remaining: 7)

>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
>>> # Scary stings an ant
>>> scary = ScaryThrower()
>>> harvester = HarvesterAnt()
>>> bee = Bee(3)
>>> gamestate.places["tunnel_0_0"].add_insect(scary)
>>> gamestate.places["tunnel_0_4"].add_insect(bee)
>>> gamestate.places["tunnel_0_5"].add_insect(harvester)
>>> scary.action(gamestate)
>>> bee.action(gamestate)
>>> bee.place.name # ScaryThrower should scare for two turns
? 'tunnel_0_5'
-- OK! --

>>> harvester.health
? 1
-- OK! --

>>> bee.action(gamestate)
>>> harvester.health
? 0
-- OK! --

---------------------------------------------------------------------
Problem EC > Suite 1 > Case 5
(cases remaining: 6)

-- Already unlocked --

---------------------------------------------------------------------
Problem EC > Suite 1 > Case 6
(cases remaining: 5)

-- Already unlocked --

---------------------------------------------------------------------
Problem EC > Suite 1 > Case 7
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Problem EC > Suite 1 > Case 8
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem EC > Suite 1 > Case 9
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Problem EC > Suite 1 > Case 10
(cases remaining: 1)

>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
>>> ScaryThrower.implemented
? True
-- OK! --

>>> SlowThrower.implemented
? True
-- OK! --

---------------------------------------------------------------------
OK! All cases for Problem EC unlocked.
```

**ants/ants.py**

```py
class Bee(Insect):
    """A Bee moves from place to place, following exits and stinging ants."""

    name = 'Bee'
    damage = 1

    # OVERRIDE CLASS ATTRIBUTES HERE
    is_waterproof = True

    is_slow = False
    is_scared = False

    slow_turns = 0
    scared_turns = 0

    has_been_scared = False

    def sting(self, ant):
        """Attack an ANT, reducing its health by 1."""
        ant.reduce_health(self.damage)

    def move_to(self, place):
        """Move from the Bee's current Place to a new PLACE."""
        self.place.remove_insect(self)
        place.add_insect(self)

    def blocked(self):
        """Return True if this Bee cannot advance to the next Place."""
        # Special handling for NinjaAnt
        # BEGIN Problem Optional 1
        return self.place.ant is not None
        # END Problem Optional 1

    def action(self, gamestate):
        """A Bee's action stings the Ant that blocks its exit if it is blocked,
        or moves to the exit of its current place otherwise.

        gamestate -- The GameState, used to access game state information.
        """
        # destination = self.place.exit
        #
        # # Extra credit: Special handling for bee direction
        # if self.blocked():
        #     self.sting(self.place.ant)
        # elif self.health > 0 and destination is not None:
        #     self.move_to(destination)
        if self.is_scared:
            destination = self.place.entrance
            self.scared_turns -= 1
        else:
            destination = self.place.exit
        if self.is_slow:
            self.slow_turns -= 1
            if self.slow_turns == 0:
                self.is_slow = False
            if gamestate.time % 2 == 0 and self.health > 0 and destination is not None:
                self.move_to(destination)
            elif self.is_scared:
                self.scared_turns += 1
        else:
            if self.blocked():
                self.sting(self.place.ant)
            elif self.health > 0 and destination is not None:
                self.move_to(destination)
        if self.scared_turns == 0:
            self.is_scared = False

    def add_to(self, place):
        place.bees.append(self)
        Insect.add_to(self, place)

    def remove_from(self, place):
        place.bees.remove(self)
        Insect.remove_from(self, place)

    def slow(self, length):
        """Slow the bee for a further LENGTH turns."""
        # BEGIN Problem EC
        "*** YOUR CODE HERE ***"
        self.is_slow = True
        self.slow_turns += length
        # END Problem EC

    def scare(self, length):
        """
        If this Bee has not been scared before, cause it to attempt to
        go backwards LENGTH times.
        """
        # BEGIN Problem EC
        "*** YOUR CODE HERE ***"
        if self.has_been_scared:
            return
        else:
            self.is_scared = True
            self.scared_turns += length
            self.has_been_scared = True
        # END Problem EC


class SlowThrower(ThrowerAnt):
    """ThrowerAnt that causes Slow on Bees."""

    name = 'Slow'
    food_cost = 4
    # BEGIN Problem EC
    implemented = True  # Change to True to view in the GUI

    # END Problem EC

    def throw_at(self, target):
        if target:
            target.slow(3)


class ScaryThrower(ThrowerAnt):
    """ThrowerAnt that intimidates Bees, making them back away instead of advancing."""

    name = 'Scary'
    food_cost = 6
    # BEGIN Problem EC
    implemented = True  # Change to True to view in the GUI

    # END Problem EC

    def throw_at(self, target):
        # BEGIN Problem EC
        "*** YOUR CODE HERE ***"
        if target:
            target.scare(2)
        # END Problem EC
```

## Optional Problem 1

```py
$ python3 ok -q optional1 -u
=====================================================================
Assignment: Project 3: Ants Vs. SomeBees
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem Optional 1 > Suite 1 > Case 1
(cases remaining: 15)

Q: Which Ant types have a blocks_path attribute?
Choose the number of the correct choice:
0) All Ant types except for NinjaAnt have a blocks_path attribute
1) Only the NinjaAnt has a blocks_path attribute
2) All Ant types have a blocks_path attribute that is inherited from
   the Ant superclass
3) None of the Ant subclasses have a blocks_path attribute
? 2
-- OK! --

---------------------------------------------------------------------
Problem Optional 1 > Suite 1 > Case 2
(cases remaining: 14)

Q: What is the value of blocks_path for each Ant subclass?
Choose the number of the correct choice:
0) blocks_path is False for all Ants
1) blocks_path is False for every Ant subclass except NinjaAnt
2) blocks_path is True for all Ants
3) blocks_path is True for every Ant subclass except NinjaAnt
? 3
-- OK! --

---------------------------------------------------------------------
Problem Optional 1 > Suite 1 > Case 3
(cases remaining: 13)

Q: When is the path of a Bee blocked?
Choose the number of the correct choice:
0) When there is not an NinjaAnt in the Bee's place
1) When there are no Ants in the Bee's place
2) When there is an Ant in the Bee's place
3) When there is an Ant whose blocks_path attribute is True in the
   Bee's place
? 3
-- OK! --

---------------------------------------------------------------------
Problem Optional 1 > Suite 1 > Case 4
(cases remaining: 12)

Q: What does a NinjaAnt do to each Bee that flies in its place?
Choose the number of the correct choice:
0) Nothing, the NinjaAnt doesn't damage Bees
1) Reduces the Bee's health by the NinjaAnt's damage attribute
2) Blocks the Bee's path
3) Reduces the Bee's health to 0
? 1
-- OK! --

---------------------------------------------------------------------
Problem Optional 1 > Suite 2 > Case 1
(cases remaining: 11)

>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
>>> #
>>> # Testing NinjaAnt parameters
>>> ninja = NinjaAnt()
>>> ninja.health
? 1
-- OK! --

>>> NinjaAnt.food_cost
? 5
-- OK! --

---------------------------------------------------------------------
Problem Optional 1 > Suite 2 > Case 2
(cases remaining: 10)

>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
>>> #
>>> # Testing blocks_path
>>> NinjaAnt.blocks_path
? False
-- OK! --

>>> HungryAnt.blocks_path
? True
-- OK! --

>>> FireAnt.blocks_path
? True
-- OK! --

---------------------------------------------------------------------
Problem Optional 1 > Suite 2 > Case 3
(cases remaining: 9)

>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
>>> #
>>> # Testing NinjaAnts do not block bees
>>> p0 = gamestate.places["tunnel_0_0"]
>>> p1 = gamestate.places["tunnel_0_1"]  # p0 is p1's exit
>>> bee = Bee(2)
>>> ninja = NinjaAnt()
>>> thrower = ThrowerAnt()
>>> p0.add_insect(thrower)            # Add ThrowerAnt to p0
>>> p1.add_insect(bee)
>>> p1.add_insect(ninja)              # Add the Bee and NinjaAnt to p1
>>> bee.action(gamestate)
>>> bee.place is ninja.place          # Did NinjaAnt block the Bee from moving?
? False
-- OK! --

>>> bee.place is p0
? True
-- OK! --

>>> ninja.health
? 1
-- OK! --

>>> bee.action(gamestate)
>>> bee.place is p0                   # Did ThrowerAnt block the Bee from moving?
? True
-- OK! --

---------------------------------------------------------------------
Problem Optional 1 > Suite 2 > Case 4
(cases remaining: 8)

>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
>>> #
>>> # Testing non-blocking ants do not block bees
>>> p0 = gamestate.places["tunnel_0_0"]
>>> p1 = gamestate.places["tunnel_0_1"]  # p0 is p1's exit
>>> bee = Bee(2)
>>> ninja_fire = FireAnt(1)
>>> ninja_fire.blocks_path = False
>>> thrower = ThrowerAnt()
>>> p0.add_insect(thrower)            # Add ThrowerAnt to p0
>>> p1.add_insect(bee)
>>> p1.add_insect(ninja_fire)              # Add the Bee and NinjaAnt to p1
>>> bee.action(gamestate)
>>> bee.place is ninja_fire.place          # Did the "ninjaish" FireAnt block the Bee from moving?
? False
-- OK! --

>>> bee.place is p0
? True
-- OK! --

>>> ninja_fire.health
? 1
-- OK! --

>>> bee.action(gamestate)
>>> bee.place is p0                   # Did ThrowerAnt block the Bee from moving?
? True
-- OK! --

---------------------------------------------------------------------
OK! All cases for Problem Optional 1 unlocked.
```

**ants/ants.py**

```py
class Ant(Insect):
    """An Ant occupies a place and does work for the colony."""

    implemented = False  # Only implemented Ant classes should be instantiated
    food_cost = 0
    is_container = False

    # ADD CLASS ATTRIBUTES HERE
    is_doubled = False

    blocks_path = True


class Bee(Insect):
    """A Bee moves from place to place, following exits and stinging ants."""

    name = 'Bee'
    damage = 1

    # OVERRIDE CLASS ATTRIBUTES HERE
    is_waterproof = True

    is_slow = False
    is_scared = False

    slow_turns = 0
    scared_turns = 0

    has_been_scared = False

    def sting(self, ant):
        """Attack an ANT, reducing its health by 1."""
        ant.reduce_health(self.damage)

    def move_to(self, place):
        """Move from the Bee's current Place to a new PLACE."""
        self.place.remove_insect(self)
        place.add_insect(self)

    def blocked(self):
        """Return True if this Bee cannot advance to the next Place."""
        # Special handling for NinjaAnt
        # BEGIN Problem Optional 1
        # return self.place.ant is not None
        if self.place.ant is None:
            return False
        if not self.place.ant.blocks_path:
            return False
        return True
        # END Problem Optional 1


class NinjaAnt(Ant):
    """NinjaAnt does not block the path and damages all bees in its place.
    This class is optional.
    """

    name = 'Ninja'
    damage = 1
    food_cost = 5
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN Problem Optional 1
    implemented = True  # Change to True to view in the GUI
    blocks_path = False
    # END Problem Optional 1

    def action(self, gamestate):
        # BEGIN Problem Optional 1
        "*** YOUR CODE HERE ***"
        for bee in self.place.bees[:]:
            bee.reduce_health(self.damage)
        # END Problem Optional 1
```

## Optional Problem 2

**ants/ants.py**

```py
class LaserAnt(ThrowerAnt):
    # This class is optional. Only one test is provided for this class.

    name = 'Laser'
    food_cost = 10
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN Problem Optional 2
    implemented = True  # Change to True to view in the GUI
    damage = 2
    # END Problem Optional 2

    def __init__(self, health=1):
        super().__init__(health)
        self.insects_shot = 0
        self.damage = LaserAnt.damage

    def insects_in_front(self):
        # BEGIN Problem Optional 2
        pos = self.place
        distance = {}
        dis = 0
        while pos:
            if not pos.is_hive:
                for bee in pos.bees:
                    distance[bee] = dis
                if pos.ant is not None and pos.ant is not self:
                    distance[pos.ant] = dis
                    if pos.ant.is_container and pos.ant.ant_contained is not None:
                        if dis != 0:
                            distance[pos.ant.ant_contained] = dis
            dis += 1
            pos = pos.entrance
        return distance
        # END Problem Optional 2

    def calculate_damage(self, distance):
        # BEGIN Problem Optional 2
        damage_result = self.damage - 0.0625 * self.insects_shot - 0.25 * distance
        return damage_result if damage_result > 0 else 0
        # END Problem Optional 2

    def action(self, gamestate):
        insects_and_distances = self.insects_in_front()
        for insect, distance in insects_and_distances.items():
            damage = self.calculate_damage(distance)
            insect.reduce_health(damage)
            if damage:
                self.insects_shot += 1
```

## Running tests

```py
$ python3 ok
=====================================================================
Assignment: Project 3: Ants Vs. SomeBees
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    171 test cases passed! No cases failed.
```