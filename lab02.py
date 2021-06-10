# Question 1
def square(x):
    return x * x

def twice(f,x):
    """Apply f to the result of applying f to x"
    >>> twice(square,3)
    81
    """
    return f(f(x))

def increment(x):
    return x + 1

def apply_n(f, x, n):
    """Apply function f to x n times.

    >>> apply_n(increment, 2, 10)
    12
    """
    while n > 0:
        x = f(x)
        n-=1



# Question 2
def make_buzzer(n):
    """ Returns a function that prints numbers in a specified
    range except those divisible by n.

    >>> i_hate_fives = make_buzzer(5)
    >>> i_hate_fives(10)
    Buzz!
    1
    2
    3
    4
    Buzz!
    6
    7
    8
    9
    """
    def f(m):
        count = 0
            while count < m:
                if count % n == 0:
                    print('Buzz!')
                else:
                    print(count)
                count += 1
    return f
    



# Question 3
def piecewise(f, g, b):
    """Returns the piecewise function h where:

    h(x) = f(x) if x < b,
           g(x) otherwise

    >>> def negate(x):
    ...     return -x
    >>> def identity(x):
    ...     return x
    >>> abs_value = piecewise(negate, identity, 0)
    >>> abs_value(6)
    6
    >>> abs_value(-1)
    1
    """
    def h(x):
        if x < b:
            return f(x)
        else:
            return g(x)
    return h
    



# Question 4
def funception(func_a, start):
    """ Takes in a function (function A) and a start value.
    Returns a function (function B) that will find the product of 
    function A applied to the range of numbers from 
    start (inclusive) to stop (exclusive)

    >>> def func_a(num):
    ...     return num + 1
    >>> func_b1 = funception(func_a, 3)
    >>> func_b1(2)
    4
    >>> func_b2 = funception(func_a, -2)
    >>> func_b2(-3)
    >>> func_b3 = funception(func_a, -1)
    >>> func_b3(4)
    >>> func_b4 = funception(func_a, 0)
    >>> func_b4(3)
    6
    >>> func_b5 = funception(func_a, 1)
    >>> func_b5(4)
    24
    """
    def func_b(stop):
        if start < 0:
            return None
        elif start > stop:
            return func_a(start)
        else:
            product = 1
            counter = start
            while counter < stop:
                product *= func_a(counter)
                counter += 1
            return product
    
    return func_b








# Extra Practice problems
def lab02_extra_practice_questions():
  """
  Fill in the values for these two variables.
  You will get the special code from the study tool when you complete all quesitons from lab.
  This code will be unique to your okpy email and this lab.
  Go here to practice: https://codestyle.herokuapp.com/cs88/lab02
  """
  okpy_email = "my_email@berkeley.edu"
  practice_result_code = "aaabbxxxxx"
  return (okpy_email, practice_result_code)
