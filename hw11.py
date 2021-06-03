
###################################
## Iterator/Generator Questions ##
###################################

def naturals(initial=1, step=1):
    i = initial
    while True:
        yield i
        i += step

# Q1
class IteratorRestart:
    """
    >>> iterator = IteratorRestart(2, 7)
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    """
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1
        
    def __iter__(self):
        self.current = self.start
        return self


# Q2
def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    print(n)
    while n > 1:
        if n % 2 == 0:
            n//=2
        else:
            n = 3*n + 1
        yield n

# Q3
def generate_perms(lst):
    """
    Generates the permutations of lst one by one.
    >>> perms = generate_perms([1, 2, 3])
    >>> hasattr(perms, '__next__')
    True
    >>> p = list(perms)
    >>> p.sort()
    >>> p
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    if len(lst) <= 1:
        yield lst
    else:
        for permutation in generate_perms([x for x in lst if x!= lst[0]]):  #we can take any index in lst as long as it is between 0 and len(lst) - 1
            for i in range(len(permutation) + 1):
                yield permutation[:i] + [lst[0]] + permutation[i:]