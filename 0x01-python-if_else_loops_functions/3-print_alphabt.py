#!/usr/bin/python3
for ch in range(97, 123):
    if ch == 101 or ch == 113:
        continue
    print(chr(ch), end='' if ch < 122 else '\n')
