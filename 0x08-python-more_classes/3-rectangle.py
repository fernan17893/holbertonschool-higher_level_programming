#!/usr/bin/python3
""" Module contains class rectangle
    Attributes:
        width: width of a Rectangle
        height: height of a Rectangle
"""


class Rectangle:
    """Define Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializer with default width and height, 0"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """retrieve width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """To set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """property to retrieve height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """to set height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Returns rectangle area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Returns rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * self.__width + 2 * self.__height)

    def __str__(self):
        new_str = ("")
        if self.__width == 0 or self.__height == 0:
            return (new_str)
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    new_str += '#'
                if i in range(self.__height - 1):
                    new_str += '\n'
            return (new_str)
