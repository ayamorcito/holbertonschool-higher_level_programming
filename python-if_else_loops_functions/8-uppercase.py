#!/usr/bin/python3
def uppercase(str):
    newstr = ''
    ascci = 0
    for i in str:
        ascci = ord(i)
        if (ascci >= 97 and ascci <= 122):
            newstr = newstr + chr((ord(i) - 32))
        else:
            newstr += i
    print("{}".format(newstr))
