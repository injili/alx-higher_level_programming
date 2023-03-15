#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if not set_1:
        return set_2
    elif not set_2:
        return set_1
    else:
        new1 = set_1.difference(set_2)
        new2 = set_2.difference(set_1)
        new3 = new1 | new2

        return new3
