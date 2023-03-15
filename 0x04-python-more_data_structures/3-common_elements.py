#!/usr/bin/python3
def common_elements(set_1, set_2):
    if not set_1 or not set_2:
        return None
    else:
        one = set(set_1)
        two = set(set_2)

        intersection = one.intersection(two)
        return list(intersection)
