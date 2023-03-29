#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0
    i = 0
    while x > 0:
        try:
            print(my_list[i], end="")
        except IndexError:
            break

        i += 1
        x -= 1
        j += 1
    print()
    return j
