#!/usr/bin/python3
""" defines if object is subclass of class """


def inherits_from(obj, a_class):
    """ Check if obj is sub class of class a_class """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
