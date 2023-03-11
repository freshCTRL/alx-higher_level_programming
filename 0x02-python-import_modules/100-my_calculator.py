#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <a> <operator> <b>")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        operator = sys.argv[2]

        if operator == '+':
            print("{} {} {} = {}".format(a, operator, b, add(a, b)))
            exit(0)
        elif operator == '-':
            print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
            exit(0)
        elif operator == '*':
            print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
            exit(0)
        elif operator == '/':
            print("{} {} {} = {}".format(a, operator, b, div(a, b)))
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
