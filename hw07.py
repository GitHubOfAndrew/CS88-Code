from operator import add, mul

def reduce(reducer, seq, base):
    """Reduce a sequence under a two-argument function starting from a base value.

    >>> def add(x, y):
    ...     return x + y
    >>> def mul(x, y):
    ...     return x*y
    >>> reduce(add, [1,2,3,4], 0)
    10
    >>> reduce(mul, [1,2,3,4], 0)
    0
    >>> reduce(mul, [1,2,3,4], 1)
    24
    """
    if not seq:
        return base
    else:
        return reducer(seq[0], reduce(reducer, seq[1:], base))
    

def remove_last(x, s):
    """Create a new list that is identical to s but with the last
    element from the list that is equal to x removed.

    >>> remove_last(1,[])
    []
    >>> remove_last(1,[1])
    []
    >>> remove_last(1,[1,1])
    [1]
    >>> remove_last(1,[2,1])
    [2]
    >>> remove_last(1,[3,1,2])
    [3, 2]
    >>> remove_last(1,[3,1,2,1])
    [3, 1, 2]
    >>> remove_last(5, [3, 5, 2, 5, 11])
    [3, 5, 2, 11]
    """
    if not s:
        return []
    else:
        if s[-1] == x:
            return s[:-1]
        else:
            return remove_last(x, s[:-1]) + [s[len(s) - 1]]

def create_num_from_lsts(lst1, lst2):
    """ Create a number with the elements from lst1 and lst2 as digits in that order.

    >>> create_num_from_lsts([1, 2, 3], [4, 5, 6])
    123456
    >>> create_num_from_lsts([5, 4, 2, 4], [1, 7])
    542417
    >>> create_num_from_lsts([3], [9, 8])
    398
    """
    if len(lst1) + len(lst2) == 0:
        return 0
    else:
        num_1, num_2 = 0, 0
        if len(lst1) > 0:
            len_tot_1 = len(lst1) + len(lst2)
            num_1 = lst1[0]*(10**len_tot_1)//10 + create_num_from_lsts(lst1[1:], lst2)
        
        if (len(lst1) == 0) and (len(lst2) > 0):
            len_tot_2 = len(lst2)
            num_2 = lst2[0]*(10**len_tot_2)//10 + create_num_from_lsts([], lst2[1:])
        return num_1 + num_2
        
def count_change(amount, denominations):
    """Returns the number of ways to make change for amount.

    >>> denominations = [50, 25, 10, 5, 1]
    >>> count_change(7, denominations)
    2
    >>> count_change(100, denominations)
    292
    >>> denominations = [16, 8, 4, 2, 1]
    >>> count_change(7, denominations)
    6
    >>> count_change(10, denominations)
    14
    >>> count_change(20, denominations)
    60
    """
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    if len(denominations) <= 0 and amount > 0:
        return 0
    return count_change(amount, denominations[:-1]) + count_change(amount - denominations[-1], denominations)

