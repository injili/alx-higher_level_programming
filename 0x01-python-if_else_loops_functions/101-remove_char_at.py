#!/usr/bin/python3
def remove_char_at(str, n):
    newstr = ""
    loop = 0

    if n >= 0:
        n = n
    else:
        i = len(str)
        n = 1 + i + n

    for letter in str:
        if loop == n:
            loop += 1
            continue
        else:
            newstr += letter
        loop += 1
    return newstr
