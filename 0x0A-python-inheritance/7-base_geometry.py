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
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
