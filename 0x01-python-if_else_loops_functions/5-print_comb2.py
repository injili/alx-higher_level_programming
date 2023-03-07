#!/usr/bin/python3
for num in range(0, 100):
    print("{m:02}".format(m=num), end=', ' if num < 99 else "\n")
