#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)

    if len_a < 2 or len_b < 2:
        if len_a == 1 and len_b == 1:
            tuple_c = (int(tuple_a[0]) + int(tuple_b[0]), 0)
        elif len_a > 1 and len_b == 1:
            tuple_c = (int(tuple_a[0]) + int(tuple_b[0]), int(tuple_a[1]))
        elif len_a == 1 and len_b > 1:
            tuple_c = (int(tuple_a[0]) + int(tuple_b[0]), int(tuple_b[1]))
        elif len_a == 0 and len_b == 1:
            tuple_c = (int(tuple_b[0]), 0)
        elif len_a == 1 and len_b == 0:
            tuple_c = (int(tuple_a[0]), 0)
        elif len_a > 1 and len_b == 0:
            tuple_c = (int(tuple_a[0]), int(tuple_a[1])) 
        elif len_a == 0 and len_b > 1:
            tuple_c = (int(tuple_b[0]), int(tuple_b[1]))
        else:
            tuple_c = (0, 0)
    else:
        tuple_c = (int(tuple_a[0]) + int(tuple_b[0]) , int(tuple_a[1]) + int(tuple_b[1]))
    return tuple_c
