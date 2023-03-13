#!/usr/bin/python3
def max_integer(my_list):
    s = len(my_list)
    if len(my_list) == 0:
        return None
    else:
        for i in range(s-1):
            if my_list[i] >= my_list[i+1]:
                my_list[i+1] = my_list[i]
        k = my_list[s-1]
        return k
