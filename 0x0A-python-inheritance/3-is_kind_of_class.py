#!/usr/bin/python3
"""Defines a kind of inherited class with the function """


def is_kind_of_class(obj, a_class):
    """Checks if an object is a inherited instance of the class
    """

    if isinstance(obj, a_class):
        return True
    return False
