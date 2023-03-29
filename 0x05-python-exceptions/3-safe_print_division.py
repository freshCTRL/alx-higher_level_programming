#!/usr/bin/python3
def safe_print_division(a, b):
    answer = []
    try:
        answer.append(a / b)
    except ZeroDivisionError:
        answer.append(None)
    finally:
        print("Inside result: {}".format(answer[0]))
    return answer[0]
