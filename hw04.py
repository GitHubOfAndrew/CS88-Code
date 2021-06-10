######################
# Required Questions #
######################
def f1():
    """
    >>> f1()
    3
    """
    return 3

def f2():
    """
    >>> f2()()
    3
    """
    return lambda: 3
    
def f3():
    """
    >>> f3()(3)
    3
    """
    return lambda x: x

def f4():
    """
    >>> f4()()(3)()
    3
    """
    return lambda : lambda x : lambda : x

def lambda_curry2(fn):
    """
    Returns a Curried version of a two argument function func.
    >>> from operator import add
    >>> x = lambda_curry2(add)
    >>> y = x(3)
    >>> y(5)
    8
    """
    return lambda x: lambda y: fn(x,y)
    



def make_politician(name, party, age):
    """
    >>> woodrow = make_politician('Woodrow Wilson', 'Democrat', 57)
    >>> isinstance(woodrow, dict)
    True
    """
    # Make sure you use a dictionary in your implementation!
    return {"name": name, "party": party, "age": age}
    

def get_pol_name(politician):
    """
    >>> woodrow = make_politician('Woodrow Wilson', 'Democrat', 57)
    >>> get_pol_name(woodrow)
    'Woodrow Wilson'
    """
    return politician['name']
    

def get_party(politician):
    """
    >>> woodrow = make_politician('Woodrow Wilson', 'Democrat', 57)
    >>> get_party(woodrow)
    'Democrat'
    """
    return politician['party']


def get_age(politician):
    """
    >>> woodrow = make_politician('Woodrow Wilson', 'Democrat', 57)
    >>> get_age(woodrow)
    57
    """
    return politician['age']
    


import random
random.seed(42)

def dice(x, y):
    """Construct a die that is a list from x to y inclusive.
    >>> dice(1, 6)
    [1, 2, 3, 4, 5, 6]
    >>> dice(3, 5)
    [3, 4, 5]
    >>> dice(5, 5)
    [5]
    """
    if x < y:
        return list(range(x, y+1, 1))
    elif x == y:
        return [x]
    else:
        return []

def smallest(die):
    """Return the lowest value die can take on."""
    return min(die)

def largest(die):
    """Return the largest value die can take on."""
    return max(die)

def str_dice(die):
    """Return a string representation of die.

    >>> str_dice(dice(1, 6))
    'die takes on values from 1 to 6'
    """
    return 'die takes on values from {0} to {1}'.format(smallest(die), largest(die))

def roll_dice(die, a):
    """Roll the die a times and return an array of the rolled values.
    >>> roll_dice(dice(5, 5), 4)
    [5, 5, 5, 5]
    >>> max(roll_dice(dice(1, 6), 100))
    6
    >>> min(roll_dice(dice(1, 6), 100))
    1
    >>> x = sum(roll_dice(dice(1, 6), 1000))/1000 # Finds the mean of 1000 dice rolls
    >>> 3 <= x <= 4 # Checks if the mean is between 3 and 4
    True
   """
   return [random.choice(die) for i in range(a)]

def rolls_until_six(die):
    """Roll the die until you get a 6 and return the number of rolls it took to do so.
    If six is not a the possible values to roll, return a string saying '6 is not a possible value of this die'
    >>> rolls_until_six(dice(1, 5))
    '6 is not a possible value of this die'
    >>> rolls_until_six(dice(6, 6)) # Takes one roll to get 6
    1
    >>> x = sum([rolls_until_six(dice(1, 6)) for _ in range(1000)])/1000 # Repeat 1000 times and average
    >>> 5 <= x <= 7 # Check that it takes between 5 and 7 rolls overall on average
    True
    """
    count = 0
    roll = 0
    if 6 in die:
        while roll != 6:
            roll = random.choice(die)
            count += 1
        return count
    else:
        return '6 is not a possible value of this die'

def cup(die_1, die_2):
    """Construct a cup that contains die1 and die2.
    >>> cup(dice(1, 1), dice(1, 2))
    [[1], [1, 2]]
    """
    return [die1, die2]

def add_to_cup(cup, die):
    """Add die to cup.
    >>> cup1 = cup(dice(1, 1), dice(1, 2))
    >>> add_to_cup(cup1, dice(1, 3))
    [[1], [1, 2], [1, 2, 3]]
    """
    return cup + [die]

def roll_cup(cup):
    """Roll every die in the cup and return an array of the rolled values.
    >>> roll_cup(cup(dice(1, 1), dice(2, 2)))
    [1, 2]
    """
    return [random.choice(cup[i]) for i in range(len(cup))]
