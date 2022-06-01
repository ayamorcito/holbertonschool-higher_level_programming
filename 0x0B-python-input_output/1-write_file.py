#!/usr/bin/python3

"""  function that reads a text file (UTF8) and prints it to stdout """


def write_file(filename="", text=""):

    """ function itself"""

    with open(filename, mode="w", encoding="utf-8") as f:
        return(f.write(text))
