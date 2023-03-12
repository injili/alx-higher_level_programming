#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num = len(sys.argv) - 1
    i = 1

    if num == 0:
        print("{} arguments.".format(num))
    elif num == 1:
        print("{} argument:")
    else:
        print("{} arguments:".format(num))

    while i <= num:
        print("{}:".format(i), sys.argv[i])
        i += 1
