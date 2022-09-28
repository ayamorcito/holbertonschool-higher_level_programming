#!/usr/bin/python3
""" Write a class BaseGeometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class based on BaseGeometry """

    def __init__(self, width, height):
        """ instantiation """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ area = width * height """
        return (self.__width * self.__height)

    def __str__(self):
        """ rectangle description """
        return (f"[Rectangle] {self.__width}/{self.__height}")
