#!/usr/bin/python3
def max_integer(my_list=[]):
    greatest = 0
    if len(my_list) == 0:
        return None
    else:
        for i in range(0, len(my_list)):
            for j in range(0, len(my_list)):
                if my_list[i] < my_list[j] and my_list[j] > greatest:
                    greatest = my_list[j]
    return greatest
