#!/usr/bin/python3
from sys import argv
"""
This line import sys to get the command
line argument
"""

"""
This program takes an integer input from
the user and solves the N queens problem
"""


"""
Checks if the length of argument passed
is not more than 2

>>> ./101-nqueens.py
Usage: nqueens N
"""

"""Checks if the argument passed is an integer

>>> ./101-nqueens.py h
N must be a number
"""

"""Checks if the value of N is less than 4

>>> ./101-nqueens.py 2
N must be at least 4
"""

if len(argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

N = argv[1]
if not N.isnumeric():
    print("N must be a number")
    sys.exit(1)

elif int(N) < 4:
    print("N must be at least 4")
    sys.exit(1)

elif N.isnumeric() and int(N) >= 4:
    N = int(N)
    j = []
    for w in range(N - 2):
        s = []
        k = w + 1
        for i in range(N):
            if k > N:
                k -= N+1
            s.append([i, k])
            h = w + 2
            k += h
        j.append(s)
    for d in j:
        print(d)
if __name__ == "__main__":
    import doctest
    doctest.testmod()
