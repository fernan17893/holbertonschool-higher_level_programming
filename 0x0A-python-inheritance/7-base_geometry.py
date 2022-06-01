#!/usr/bin/python3
""" Empty class BaseGeometry """


class BaseGeometry:
    """Public instance method raises exeption for area
    not implemented
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value,int):
            raise TypeError("<name> must be an integer")
        elif value <= 0:
            raise ValueError("<name> must be greater than 0")
