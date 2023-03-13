#!/usr/bin/python3
def no_c(my_string):
    myland = list(my_string)
    for i in myland:
        if i == "C" or i == "c":
            myland.remove(i)
    return ''.join(myland)
