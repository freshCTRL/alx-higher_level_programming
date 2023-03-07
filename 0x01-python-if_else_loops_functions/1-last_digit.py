#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = abs(number)
last_digit = num % 10
if number < 0:
    if last_digit == 0:
        print(f"Last digit of {number:d}"
              f"is {last_digit:d} and is 0")
    else:
        print(f"Last digit of {number:d} "
              f"is {'-'}{last_digit:d} and "
              f"is less than 6 and not 0")
else:
    if last_digit == 0:
        print(f"Last digit of {number:d} "
              f"is {last_digit:d} and is 0")
    elif last_digit > 5:
        print(f"Last digit of {number:d} "
              f"is {last_digit:d} and "
              f"is greater than 5")
    elif last_digit != 0 and last_digit < 6:
        print(f"Last digit of {number:d} "
              f"is {last_digit:d} and "
              f"is less than 6 and not 0")
