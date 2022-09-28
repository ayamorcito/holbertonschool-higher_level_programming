#!/usr/bin/python3
""" Write a class BaseGeometry """


class BaseGeometry():
    """ the class """
    def area(self):
        """ exception message """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ method that validates value """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
