#!/usr/bin/bash
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            elem1 = my_list_1[i]
            elem2 = my_list_2[i]
            new_list.append(elem1 / elem2)
        except IndexError:
            new_list.append(0)
            print("out of range")
        except TypeError:
            new_list.append(0)
            print("wrong type")
        except ZeroDivisionError:
            new_list.append(0)
            print("division by 0")
        finally:
            pass
    return new_list
