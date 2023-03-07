#!/usr/bin/python3
def uppercase(str):
    i = len(str)
    for n in range(i):
        k = ord(str[n])
        if k > 96 and k < 124:
            k -= 32
            str[n] = chr(k)


print(str)
