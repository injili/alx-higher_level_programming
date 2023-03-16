#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        multiply = 0
        divider = 0
        add = 0
        for i in range(0, len(my_list)):
            multiply = my_list[i][0] * my_list[i][1]
            divider += my_list[i][1]
            add += multiply
        average = add / divider
        return average
