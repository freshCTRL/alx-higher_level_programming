#!/usr/bin/python3
for i in range(0, 100):
    if i != 99:
        print("{}{}, ".format(i // 10, i % 10), end="")
    else:
        print("{}{}".format(i // 10, i % 10),)
