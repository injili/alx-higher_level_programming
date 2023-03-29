#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 1
    y = 0
    length = 0
    count = 0
    for element in my_list:
        length += 1

    while y < length:
        if i > x:
            break
        print("{}".format(my_list[y]), end="" if i <= x or y + 1 < length else "\n")
        i += 1
        y += 1
        count += 1
    return count
