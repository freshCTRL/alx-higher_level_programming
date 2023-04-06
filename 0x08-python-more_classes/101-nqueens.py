#!/usr/bin/python3
from sys import argv

if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)

N = argv[1]
if not N.isnumeric():
    print("N must be a number")
    exit(1)
elif int(N) < 4:
    print("N must be at least 4")
    exit(1)
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
