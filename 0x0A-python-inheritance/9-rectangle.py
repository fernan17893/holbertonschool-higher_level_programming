#!/usr/bin/python3
""" Empty class BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle subclass inherited from BaseGeometry class """

    def __init__(self, width, height):
        Rectangle.integer_validator(self, "width", width)
        self.__width = width
        Rectangle.integer_validator(self, "height", height)
        self.__height = height 

    def area(self):
        """Returns Rectangle area"""
        return (self.__width * self.__height)

    def __str__(self):
        return (f"[Rectangle] {self.__width}/{self.__height}")
