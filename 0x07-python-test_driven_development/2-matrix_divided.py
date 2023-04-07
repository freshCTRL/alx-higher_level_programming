#!/usr/bin/python3
"""This module contains a function that divide
a matrix by a number and returns a new list of the
division, the divisor is screened and errors are
if an exception occurs
"""


def matrix_divided(matrix, div):
    """Raises 1: ZeroDivisionError if divisor = 0.
    Raises 2: TypeError if dividend != matrix.
    """

    if type(div) == int:
        div = div
    elif type(div) == float:
        div = div
    else:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) != list:
        raise TypeError('matrix must be a matrix (list of lists)'
                        'of integers/floats')

    n = []
    for i in matrix:
        if type(i) != list:
            raise TypeError("matrix must be a matrix (list of lists)"
                            "of integers/floats")
        m = []
        for j in i:
            if type(j) == int or type(j) == float:
                s = j / div
                m.append(round(s, 2))
            else:
                raise TypeError("matrix must be a matrix (list of lists)"
                                "of integers/floats")
        n.append(m)
    return n
