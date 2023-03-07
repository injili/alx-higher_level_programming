#!/usr/bin/python3
letter = 122
n = 0
while letter > 96:
    if n % 2 == 0:
        print("{}".format(chr(letter)), end='')
    else:
        i = letter
        i -= 32
        print("{}".format(chr(i)), end='')
    letter -= 1
    n += 1
