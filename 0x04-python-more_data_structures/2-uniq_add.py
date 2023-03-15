#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return  0
    else:
        sum_uniq = 0
        new = my_list.copy()
        for i in my_list:
            count = 0
            for j in range(0, len(new)):
                if i == new[j]:
                    count += 1
                if count > 1:
                    del new[j]
                    break
        sum_uniq = sum(new)
        return sum_uniq
