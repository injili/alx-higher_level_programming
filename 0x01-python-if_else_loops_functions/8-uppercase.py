#!/usr/bin/python3
def uppercase(str):
    newstr = ""
    for n in str:
        if ord(n) > 96 and ord(n) < 124:
            k = ord(n)
            k -= 32
            character = chr(k)
            newstr += character
        else:
            newstr += n
    print(newstr)
