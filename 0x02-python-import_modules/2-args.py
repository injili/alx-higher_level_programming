#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num = len(sys.argv) - 1
    i = 1

    print("{} argument".format(num), end="")
    if num > 0:
        print(":")
    else:
        print(".")

    while i <= num:
        print("{}: {}".format(i, sys.argv[i]))
        i = i + 1
