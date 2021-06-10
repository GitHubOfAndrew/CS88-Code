def merge_dict(d1, d2):
    """Returns a dictionary with two dictionaries merged together. You can assume that the same keys appear in both dictionaries.
    >>> data8 = {"midterms":1, "projects":3}
    >>> data100 = {"midterms":2, "projects":3}
    >>> combined_exams = merge_dict(data8, data100)
    >>> combined_exams
    {'midterms': 3, 'projects': 6}
    >>> sunday_orders = {"pizza": 3, "hot dogs": 2, "fries": 5}
    >>> monday_orders = {"pizza": 1, "hot dogs": 1, "fries": 8}
    >>> combined_orders = merge_dict(sunday_orders, monday_orders)
    >>> combined_orders
    {'pizza': 4, 'hot dogs': 3, 'fries': 13}
    """
    new_dict = {}
    for key1 in d1.keys():
        new_dict[key1] = d1[key1]
        if key1 in d2.keys():
            new_dict[key1] += d2[key1]
    return new_dict
    


def polynomial(degree, coeffs):
    """
    >>> fourth = polynomial(4, [3,6,2,1, 100])
    >>> fourth(3)   # 3*(3**4) + 6*(3**3) + 2*(3**2) + 1*(3**1) + 100
    526
    >>> third = polynomial(3, [2, 0, 0, 0])
    >>> third(4)   # 2*(4**3) + 0*(4**2) + 0*(4**1) + 0
    128
    """
    assert(degree == len(coeffs) - 1)
    return lambda x: sum([coeffs[i]*x**(degree - i) for i in range(degree + 1)])
    

