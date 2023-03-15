#!usr/bin/python3
def add(a=(), b=()):
    b = list(b)
    if len(b) == 1:
        b.append(0)
        b = tuple(b)
    elif len(b) == 0:
        b.append(0)
        b.append(0)
        b = tuple(b)
    else:
        b = tuple(b)

    a = list(a)
    if len(a) == 1:
        a.append(0)
        a = tuple(a)
    elif len(a) == 0:
        a.append(0)
        a.append(0)
        a = tuple(a)
    else:
        a = tuple(a)

    c = []
    for i in range(2):
        c.append(a[i] + b[i])
    return tuple(c)
