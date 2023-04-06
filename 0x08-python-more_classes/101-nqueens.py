#!/usr/bin/python3
""" This program takes an integer input from
    the user and solves the N queens problem

    """

import sys
"""This line import sys to get the command
    line argument

    """

if len(sys.argv) != 2:
    """Checks if the length of argument passed
    is not more than 2

    """

    print("Usage: nqueens N")
    exit(1)

N = sys.argv[1]
if not N.isnumeric():
    """Checks if the argument passed is an integer

    """

    print("N must be a number")
    exit(1)

elif int(N) < 4:
    """checks if the value of N is less than 4

    """

    print("N must be at least 4")
    exit(1)

elif N.isnumeric() and int(N) >= 4:
    """Checks if argument passed is an integer and
    if >= 4

    """

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
