#!/usr/bin/python3

def print_list_integer(my_list=[]):

    i = 0
    num = len(my_list)
    while i < num:
        print("{}".format(int(my_list[i])))
        i += 1
