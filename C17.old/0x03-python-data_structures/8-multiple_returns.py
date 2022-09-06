#!/usr/bin/python3
def multiple_returns(sentence):
    que_tuple = ()
    if len(sentence) == 0:
        que_tuple = 0, "None"
    else:
        que_tuple = len(sentence), sentence[0]
    return que_tuple
