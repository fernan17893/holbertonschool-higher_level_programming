#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """Represents a class Student."""

    def __init__(self, first_name, last_name, age):
        """ Initialize Student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of studenti
            if attrs is a list of strings, only attribute
            names contained in this list must be retrieved
        """
        if (type(attrs) == list and
           all(type(i) == str for i in attrs)):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return self.__dict__
