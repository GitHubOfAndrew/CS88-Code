######################
# Required Questions #
######################

def add_matrices(x, y):
    """
    >>> matrix1 = [[1, 3],
    ...            [2, 0]]
    >>> matrix2 = [[-3, 0],
    ...            [1, 2]]
    >>> add_matrices(matrix1, matrix2)
    [[-2, 3], [3, 2]]
    """
    return [ [ x[i][j] + y[i][j] for j in len(x[i])] for i in len(x)]
    


