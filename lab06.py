def sum(n):
    """Using recursion, computes the sum of all integers between 1 and n, inclusive.
    Assume n is positive.

    >>> sum(1)
    1
    >>> sum(5)  # 1 + 2 + 3 + 4 + 5
    15
    """
    if n <= 1:
        return n
    else:
        return n + sum(n-1)


def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k < 10:
        if k % 10 == 7:
            return True
        else:
            return False
    else:
        if k % 10 == 7:
            return True
        else:
            k -= k%10
            return has_seven(k//10)


def binary(n):
    """Return a list representing the representation of a number in base 2.

    >>> binary(55055)
    [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]
    >>> binary(-136)
    ['-', 1, 0, 0, 0, 1, 0, 0, 0]
    """
    li_bin = []
    if n == 0:
        return li_bin
    else:
        if n > 0:
            li_bin = binary(n//2) + [n%2]
            return li_bin
        else:
            n = -n
            li_bin = ['-'] + binary(n//2) + [n%2]
            return li_bin

