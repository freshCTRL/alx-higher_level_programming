#!/usr/bin/python3
def no_c(my_string):
    myland = list(my_string)
    for i in myland:
        if i == "C" or i == "c":
            myland.remove(i)
    new_string = ''.join(myland)
    return new_string
