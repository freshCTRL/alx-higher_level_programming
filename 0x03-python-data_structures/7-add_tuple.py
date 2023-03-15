#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_b = list(tuple_b)
    if len(tuple_b) == 1:
        tuple_b.append(0)
        tuple_b = tuple(tuple_b)
    elif len(tuple_b) == 0:
        tuple_b.append(0)
        tuple_b.append(0)
        tuple_b = tuple(tuple_b)
    else:
        tuple_b = tuple(tuple_b)

    tuple_a = list(tuple_a)
    if len(tuple_a) == 1:
        tuple_a.append(0)
        tuple_a = tuple(tuple_a)
    elif len(tuple_a) == 0:
        tuple_a.append(0)
        tuple_a.append(0)
        tuple_a = tuple(tuple_a)
    else:
        tuple_a = tuple(tuple_a)

    c = []
    for i in range(2):
        c.append(tuple_a[i] + tuple_b[i])
    return tuple(c)
