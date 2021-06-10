######################
# Required Questions #
######################

def nonzero(lst):
    """ Returns the first nonzero element of a list

    >>> nonzero([1, 2, 3])
    1
    >>> nonzero([0, 1, 2])
    1
    >>> nonzero([0, 0, 0, 0, 0, 0, 5, 0, 6])
    5
    """
    return [x for x in lst if x!=0][0]


def has_n(lst, n):
    """ Returns whether or not a list contains the value n.

    >>> has_n([1, 2, 2], 2)
    True
    >>> has_n([0, 1, 2], 3)
    False
    >>> has_n([], 5)
    False
    """
    return n in lst


def deep_list(seq):
    """Returns a new list containing elements of the original list that are lists.

    >>> seq = [49, 8, 2, 1, 102]
    >>> deep_list(seq)
    []
    >>> seq = [[500], [30, 25, 24], 8, [0]]
    >>> deep_list(seq)
    [[500], [30, 25, 24], [0]]
    >>> seq = ["hello", [12, [25], 24], 8, [0]]
    >>> deep_list(seq)
    [[12, [25], 24], [0]]
    """
    return [x for x in seq if type(x) == list]
    


def total_price(prices):
    """
    Finds the total price of all products in prices including a
    50% tax on products with a price greater than or equal to 20.
    >>> total_price([5, 20, 30, 7])
    87
    >>> total_price([8, 4, 3])
    15
    >>> total_price([10, 100, 4])
    164
    """
    return int( sum( [1.5*x for x in prices if x >= 20] + [y for y in prices if y < 20] ) )


def arange(start, end, step=1):
    """
    arange behaves just like np.arange(start, end, step).
    You only need to support positive values for step.

    >>> arange(1, 3)
    [1, 2]
    >>> arange(0, 25, 2)
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
    >>> arange(999, 1231, 34)
    [999, 1033, 1067, 1101, 1135, 1169, 1203]

    """
    #solution WITHOUT using the range function
    og_list = []
    x = start
    if step >= 0:
        while x <= end:
            og_list.append(x)
            x += step
        return og_list
    else:
        while x >= end:
            og_list.append(x)
            x -= abs(step)
        return og_list
    



def tax(shopping_cart, percent):
    """
    Adds a `percent` tax to each item's price in a shopping cart.

    >>> fruitCart = [("apple", 0.5, 3), ("banana", 0.25, 4)]
    >>> tax(fruitCart, 10)
    [('apple', 0.55, 3), ('banana', 0.275, 4)]

    >>> calCart = [("oski", 1000, 1), ("go", 1.25, 2), ("bears", 3.5, 2)]
    >>> tax(calCart, 100)
    [('oski', 2000.0, 1), ('go', 2.5, 2), ('bears', 7.0, 2)]
    """
    return [ (item[0], (1 + 0.01*percent)*item[1], item[2]) for item in shopping_cart ]
    

def cartSum(shopping_cart):
    """
    Sums a shopping cart returning a float.

    >>> fruitCart = [("apple", 0.5, 3), ("banana", 0.25, 4)]
    >>> taxedFruit = tax(fruitCart, 10)
    >>> cartSum(taxedFruit)
    2.75
    >>> calCart = [("oski", 1000, 1), ("go", 1.25, 2), ("bears", 3.5, 2)]
    >>> taxedCal = tax(calCart, 100)
    >>> cartSum(taxedCal)
    2019.0
    """
    prices = [item[2]*item[1] for item in shopping_cart]
    total = 0
    for x in prices:
        total += x
    return total
    

