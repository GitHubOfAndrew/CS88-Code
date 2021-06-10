# Diner ADT
def make_diner(name):
    """ Diners are represented by their name and the number of free tables they have."""
    return [name, 0]

def num_free_tables(diner):
    return diner[1]

def name(diner):
    return diner[0]
# You will implement add_table and serve which are part of the Diner ADT

# Group ADT
def make_group(name):
    """ Groups are represented by their name and their status."""
    return [name, 'waiting']

def name(group):
    return group[0]

def status(group):
    return group[1]

def start_eating(group, diner):
    group[1] = 'eating'

# You will implement finish_eating which is part of the Group ADT

def add_table(diner):
    """
    >>> din = make_diner("Croads")
    >>> num_free_tables(din)
    0
    >>> add_table(din)
    >>> add_table(din)
    >>> num_free_tables(din)
    2
    """
    diner[1] += 1


def serve(diner, group):
    """
    >>> din = make_diner("Cafe 3")
    >>> add_table(din)
    >>> g1 = make_group("Vandana's Group")
    >>> g2 = make_group("Shreya's Group")
    >>> serve(din, g1)
    >>> status(g1)
    'eating'
    >>> num_free_tables(din)
    0
    >>> serve(din, g2)
    'table not free'
    >>> status(g2)
    'waiting'
    """
    assert(diner[1] >= 0)
    if diner[1] == 0:
        return 'table not free'
    else:
        group[1] = 'eating'
        diner[1] -= 1

def finish_eating(group, diner):
    """
    >>> din = make_diner("Foothill")
    >>> add_table(din)
    >>> g1 = make_group("Nick's Group")
    >>> serve(din, g1)
    >>> num_free_tables(din)
    0
    >>> finish_eating(g1, din)
    >>> num_free_tables(din)
    1
    >>> status(g1)
    'finished'
    """
    group[1] = 'finished'
    diner[1] += 1

def replace_all(d, x, y):
    """
    >>> d = {'foo': 2, 'bar': 3, 'garply': 3, 'xyzzy': 99}
    >>> e = replace_all(d, 3, 'poof')
    >>> e == {'foo': 2, 'bar': 'poof', 'garply': 'poof', 'xyzzy': 99}
    True
    """
    for key in d:
        if d[key] == x:
            d[key] = y
    return d
    

def common_players(roster):
    """Returns a dictionary containing values along with a corresponding
    list of keys that had that value from the original dictionary.
    >>> full_roster = {"bob": "Team A", "barnum": "Team B", "beatrice": "Team C", "bernice": "Team B", "ben": "Team D", "belle": "Team A", "bill": "Team B", "bernie": "Team B", "baxter": "Team A"}
    >>> common_players(full_roster)
    {'Team A': ['bob', 'belle', 'baxter'], 'Team B': ['barnum', 'bernice', 'bill', 'bernie'], 'Team C': ['beatrice'], 'Team D': ['ben']}
    """
    common = {}
    for key, value in roster.items():
        common[value] = [key] if value not in common.keys() else common[value] + [key]
    return common
    


