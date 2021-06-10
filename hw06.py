######################
# Required Questions #
######################

# Probably a die-re situation

def decimal(n):
    """Return a list representing the decimal representation of a number.

    >>> decimal(55055)
    [5, 5, 0, 5, 5]
    >>> decimal(-136)
    ['-', 1, 3, 6]
    """
    li = []
    if n >= 0:
        if n < 10:
            li = [n]
            return li
        else:
            li = decimal(n//10) + [n%10]
            return li
    else:
        n = -n
        if n < 10:
            li = [n]
            return li
        else:
            li = ['-'] + decimal(n//10) + [n%10]
            return li


def hailstone_iterative(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone_iterative(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(int(n))
    count = 1
    while n != 1:
        if n % 2 == 0:
            print(n//2)
            count += 1
        else:
            print(3*n + 1)
            count += 1
    return count


def hailstone_recursive(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone_recursive(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    count = 1
    if n == 1:
        print(int(n))
        return count
    else:
        if n % 2 == 0:
            print(int(n))
            count += hailstone_recursive(n/2)
        else:
            print(int(n))
            count += hailstone_recursive(3*n + 1)
    return count


def is_palindrome(lst):
    """ Returns True if the list is a palindrome. A palindrome is a list 
    that reads the same forwards as backwards
    >>> is_palindrome([1, 2, 3, 4, 5])
    False
    >>> is_palindrome(["p", "a", "l", "i", "n", "d", "r", "o", "m", "e"])
    False
    >>> is_palindrome([True, False, True])
    True
    >>> is_palindrome([])
    True
    >>> is_palindrome(["a", "l", "a", "s", "k", "a"])
    False
    >>> is_palindrome(["r", "a", "d", "a", "r"])
    True
    >>> is_palindrome(["f", "o", "o", "l", "p", "r", "o", "o", "f"])
    False
    >>> is_palindrome(["a", "v", "a"])
    True
    >>> is_palindrome(["racecar", "racecar"])
    True
    >>> is_palindrome(["r", "a", "c", "e", "c", "a", "r"])
    True
    """
    if len(lst) <= 1:
        return True
    else:
        if lst[0] == lst[-1]:
            return is_palindrome(lst[1:-1])
        else:
            return False

