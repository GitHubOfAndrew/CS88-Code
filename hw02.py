"""Homework 2."""

def fib(n):
    """Returns the nth Fibonacci number.

    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    5
    >>> fib(6)
    8
    >>> fib(100)
    354224848179261915075
    """
    fibnow = 1
    fibprev = 0
    if n == 0:
        return fibprev
    elif n == 1:
        return fibnow
    elif n >= 2:
        count = 2
        while count <= n:
            fibprev, fibnow = fibnow, fibprev + fibnow
            count += 1
        return fibnow


def mul_by_num(factor):
    """
    Returns a function that takes one argument and returns num
    times that argument.
    >>> x = mul_by_num(5)
    >>> y = mul_by_num(2)
    >>> x(3)
    15
    >>> y(-4)
    -8
    """
    def f(second_factor_:
        product = factor*second_factor
        return product
    return f
    


def make_derivative(f):
    """Returns a function that approximates the derivative of f.

    Recall that f'(a) = (f(a + h) - f(a)) / h as h approaches 0. We will
    approximate the derivative by choosing a very small value for h.

    >>> def square(x): 
    ...     # equivalent to: square = lambda x: x*x
    ...     return x*x
    >>> derivative = make_derivative(square)
    >>> result = derivative(3)
    >>> round(result, 3) # approximately 2*3
    6.0
    """
    h=0.00001
    def eval(a):
        derivative = (f(a + h) - f(a))/h
        return derivative
    return eval


def count_cond(mystery_function, n):
    """
    >>> def divisible(n, i):
    ...     return n % i == 0
    >>> count_cond(divisible, 2) # 1, 2
    2
    >>> count_cond(divisible, 4) # 1, 2, 4
    3
    >>> count_cond(divisible, 12) # 1, 2, 3, 4, 6, 12
    6

    >>> def is_prime(n, i):
    ...     return count_cond(divisible, i) == 2
    >>> count_cond(is_prime, 2) # 2
    1
    >>> count_cond(is_prime, 3) # 2, 3
    2
    >>> count_cond(is_prime, 4) # 2, 3
    2
    >>> count_cond(is_prime, 5) # 2, 3, 5
    3
    >>> count_cond(is_prime, 20) # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    i, count = 1, 0
    while i <= n:
        if mystery_function(n, i) == True:
            count += 1
        else:
            count = count
        i += 1
    return count
    


def cycle(f1, f2, f3):
    """ Returns a function that is itself a higher order function
    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    def counter(arg):
        def composition(x):
            n = arg
            value = x
            output = 0
            while n > 2:
                value = f3(f2(f1(value)))
                n -= 3
             
            if n % 3 == 0:
                output = value
            elif n % 3 == 1:
                output = f1(value)
            elif n % 3 == 2:
                output = f2(f1(value))
            return output 
        return composition
    return counter




