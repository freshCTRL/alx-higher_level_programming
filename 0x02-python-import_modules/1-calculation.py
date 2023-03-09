if __name__ == "__main__":
    import calculator_1 as add, sub, mul, div
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}". format(a, b, a + b))
    print("{:d} - {:d} = {:d}". format(a, b, a - b))
    print("{:d} * {:d} = {:d}". format(a, b, a * b))
    print("{:d} / {:d} = {:d}". format(a, b, int(a / b)))
