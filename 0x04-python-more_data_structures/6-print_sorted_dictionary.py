#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortedBykey = {k: v for k, v in sorted(a_dictionary.items())}
    for key in sortedBykey:
        print("{}: {}".format(key, sortedBykey[key]))
