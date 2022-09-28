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
