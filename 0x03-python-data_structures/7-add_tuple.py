#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = list(tuple_a)
    tuple_b = list(tuple_b)
    if len(tuple_a) >= len(tuple_b):
        for i in range(len(tuple_a)):
            if len(tuple_b) == 1:
                tuple_b.insert(1, 0)
            elif len(tuple_b) == 0:
                tuple_b.insert(1, 0)
                tuple_b.insert(1, 0)
            tuple_a[i] += tuple_b[i]
        return tuple(tuple_a)
    else:
        for i in range(len(tuple_b)):
            if len(tuple_a) == 1:
                tuple_a.insert(1, 0)
            elif len(tuple_b) == 0:
                tuple_a.insert(1, 0)
                tuple_a.insert(1, 0)
            tuple_b[i] += tuple_a[i]
        return tuple(tuple_a)
