#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) > 0:
        tuple_new = (len(sentence), sentence[0])
    else:
        tuple_new = (0, None)
    return tuple_new
