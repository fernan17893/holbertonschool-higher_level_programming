#!/usr/bin/python3
""" Empty class BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle subclass inherited from BaseGeometry class """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.width = width
        self.integer_validator("height", height)
        self.height = height
