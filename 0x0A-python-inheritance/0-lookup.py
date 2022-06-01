#!/usr/bin/python3
""" Define object attribute lookup function """



def lookup(obj):
    """Return list of the object's available attributes and methods."""
    return (dir(obj))
