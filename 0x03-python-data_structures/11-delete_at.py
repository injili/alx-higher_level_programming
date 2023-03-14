#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if not my_list:
        return None
    elif idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        for i in range(0, len(my_list) - 1):
            if i == idx:
                my_list = my_list[:i] + my_list[i + 1:]
    return my_list
