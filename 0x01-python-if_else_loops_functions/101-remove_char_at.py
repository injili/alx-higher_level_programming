#!/usr/bin/python3
def remove_char_at(str, n):
    newstr = ""
    loop = 0

    for letter in str:
        if loop == n:
            loop += 1
            continue
        else:
            newstr += letter
        loop += 1
    return newstr
