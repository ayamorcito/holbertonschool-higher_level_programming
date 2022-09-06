#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    resulta2 = []
    for i in my_list:
        if i % 2 == 0:
            resulta2.append(True)
        else:
            resulta2.append(False)
    return resulta2
