#!/usr/bin/python3

"""  function that reads a text file (UTF8) and prints it to stdout """


def append_write(filename="", text=""):

    """ function itself"""

    with open(filename, mode="a", encoding="utf-8") as f:
        return(f.write(text))
