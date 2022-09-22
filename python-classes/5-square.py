#!/usr/bin/python3
"""writes a class Square that defines a sq based on 2-square.py"""


class Square:
    """creates a square"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    def area(self):
        return self.__size * self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print("#" * self.size)
