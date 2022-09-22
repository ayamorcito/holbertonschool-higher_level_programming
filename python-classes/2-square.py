#!/usr/bin/python3
"""writes a class Square that defines a sq based on 1-square.py"""


class Square:
    """creates a square"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
