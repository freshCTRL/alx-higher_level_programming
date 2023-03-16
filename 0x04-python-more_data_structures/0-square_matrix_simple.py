#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    for rows in matrix:
        sub_list = []
        for num in rows:
            sub_list.append(num ** 2)
        new_list.append(sub_list)
    return new_list
