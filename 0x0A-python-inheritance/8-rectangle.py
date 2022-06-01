#!/usr/bin/python3
""" Empty class BaseGeometry """


class BaseGeometry:
    """Public instance method raises exeption for area
    not implemented
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Public instance method validates if value is an integer and greater
    than 0, if not TypeError is raised for non integer value, and
    ValueError raised if value is less than or equal to 0
    """

    if not isinstance(value, int):
        raise TypeError("<name> must be an integer")
    elif value <= 0:
        raise ValueError("<name> must be greater than 0")


class Rectangle(BaseGeometry):
    """ Rectangle subclass inherited from BaseGeometry class """

    def __init__(self, width, height):
        self.integer_validator(self, width)
        self.width = width
        self.integer_validator(self, height)
        self.height = height
