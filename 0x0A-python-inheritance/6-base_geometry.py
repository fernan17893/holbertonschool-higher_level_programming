#!/usr/bin/python3
""" Empty class BaseGeometry """


class BaseGeometry:
    """Public instance method raises exeption for area
    not implemented
    """

    def area(self):
        raise Exception("area() is not implemented")
