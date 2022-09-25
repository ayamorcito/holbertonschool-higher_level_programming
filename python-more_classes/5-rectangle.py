#!/usr/bin/python3
""" Rectangle Class"""


class Rectangle:
    """Rectangle"""

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__width*2 + self.__height*2

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return (f"{'#'*self.width}\n"*self.height).strip('\n')

    def __repr__(self):
        return (f"{self.__class__.__name__}({self.width}, {self.height})")

    def __del__(self):
        print("Bye rectangle...")
