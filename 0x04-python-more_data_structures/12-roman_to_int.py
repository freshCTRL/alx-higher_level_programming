#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0

    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_string = list(roman_string)
    r = []
    for i in roman_string:
        for key in roman_dict:
            if i == key:
                r.append(roman_dict[key])
                break

    k = 0
    s = len(r)
    for i in range(len(r)):
        j = i+1
        if i != s-1:
            if r[j] > r[i]:
                r[i] = -1*r[i]
        k += r[i]

    if k <= 3999:
        return k
    return "Enter number between 1 to 3999"
