#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return  None
    else:
        sum_uniq = 0
        for i in my_list:
            count = 0
            for j in range(0, len(my_list)):
                if i == my_list[j]:
                    count += 1
                if count > 1:
                    del my_list[j]
                    break
        for a in my_list:
            sum_uniq += a
        return sum_uniq
