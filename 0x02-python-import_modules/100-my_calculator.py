#!/usr/bin/python3

if __name__ == "__main__":
    """accepts arguments and does the operation"""
    import sys

    num = len(sys.argv) - 1
    result = 0

    if num == 3:
        a = int(sys.argv[1])
        oper = sys.argv[2]
        b = int(sys.argv[3])

        if oper == "+":
            result = a + b
        elif oper == "-":
            result = a - b
        elif oper == "*":
            result = a * b
        elif oper == "/":
            result = a / b
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    print("{} {} {} = {}".format(a, oper, b, result))
