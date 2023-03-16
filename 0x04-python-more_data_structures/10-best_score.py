#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        max_key = max(a_dictionary)
        return a_dictionary[max_key]
