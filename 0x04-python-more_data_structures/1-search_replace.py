#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return my_list
    else:
        new_list = my_list.copy()
        for i in range(0, len(my_list)):
            if my_list[i] == search:
                new_list[i] = replace
    return new_list
