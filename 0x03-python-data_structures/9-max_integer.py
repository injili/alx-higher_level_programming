#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        greatest = my_list[0]
        for i in range(len(my_list)):
            for j in range(i+1, len(my_list)):
                if my_list[j] > greatest:
                    greatest = my_list[j]
    return greatest
