#!/usr/bin/python3
"""This module contains a function that
prints the pascal triangle based on
input value passed
"""


def pascal_triangle(n):
    """a function that prints the pascal
    triangle based on input value passed
    """
    k = []
    if n <= 0:
        return k
    for i in range(n):
        s = []
        if i == 0:
            s.append(1)
            k.append(s)
            continue
        if i == 1:
            s.append(1)
            s.append(1)
            k.append(s)
            continue
        if i == 2:
            s.append(1)
            s.append(2)
            s.append(1)
            k.append(s)
            continue
        f = u = 1
        a = 0
        s.append(1)
        j = k[-1][:]
        while f < i:
            s.append(sum(j[a:u + 1]))
            a += 1
            u += 1
            f += 1
        s.append(1)
        k.append(s)
    return k
