#!/usr/bin/python3
for n in range (0, 100):
    if ((abs(n) % 100) // 10) == (abs(n) % 10):
        continue
    print("{x:02}".format(x=n), end=", " if n < 99 else "\n")
