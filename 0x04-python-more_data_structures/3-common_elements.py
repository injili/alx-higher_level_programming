#!/usr/bin/python3
def common_elements(set_1, set_2):
    if not set_1 or not set_2:
        return None
    else:
        new_list = [elem for elem in set_1 if elem in set_2]
        '''
        for i in set_1:
            for j in set_2:
                if i == j and :
                    new_list.append(j)
         '''
        return new_list
