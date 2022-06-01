#!/usr/bin/python3
""" Defines instance of same class """


def is_same_class(obj, a_class):
    """ Returns true if object is exact instance of specified class
    Otherwise returns false
    """
    if type(obj) == a_class:
        return True
    return False
