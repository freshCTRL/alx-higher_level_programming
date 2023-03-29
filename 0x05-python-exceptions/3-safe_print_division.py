#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        answer = int(a / b)
        return answer
    except:
        answer = None
        return None
    finally:
        print("Inside result: {}".format(answer))
