def filter(f, seq):
    """Filter a sequence to only contain values allowed by filter.

    >>> def is_even(x):
    ...     return x % 2 == 0
    >>> def divisible_by5(x):
    ...     return x % 5 == 0
    >>> filter(is_even, [1,2,3,4])
    [2, 4]
    >>> filter(divisible_by5, [1, 4, 9, 16, 25, 100])
    [25, 100]
    """
    if not seq:
        return []
    else:
        if f(seq[0]):
            return [seq[0]] + fil(f, seq[1:])
        else:
            return fil(f, seq[1:])
    

def sum_diffs(n):
    """ Return the sum of the differences between adjacent digits in the number n.

    >>> sum_diffs(8)
    0
    >>> sum_diffs(154) # 4 + 1 = 5
    5
    >>> sum_diffs(12321) # 1 + 1 + 1 + 1
    4
    >>> sum_diffs(7351) # 4 + 2 + 4
    10
    """
    counter = 0
    if n < 10:
        return counter
    else:
        digi_first, digi_second = n%10, (n//10)%10
        li = [digi_first, digi_second]
        return max(li) - min(li) + sum_diffs(n//10)

def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    assert(m > 0 and n > 0)
    count_paths = 1
    if m==1 or n==1:
        return count_paths
    else:
        counter = 0
        if m > 1:
            counter += paths(m-1,n)
        if n > 1:
            counter += paths(m, n-1)
        return counter


# Required practice problems
def lab07_practice_problems():
  """
  Fill in the values for these two variables.
  You will get the special code from the study tool when you complete all questions from lab.
  This code will be unique to your okpy email and this lab.
  Go here to practice: https://codestyle.herokuapp.com/cs88/lab07
  """
  okpy_email = "my_examil@berkeley.edu"
  okpy_secret_key = "xxxx...xxxxx"
  return (okpy_email, okpy_secret_key)
