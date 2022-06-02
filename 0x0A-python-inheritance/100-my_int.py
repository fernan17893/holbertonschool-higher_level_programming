#!/usr/bin/python3
""" Defines class MyInt which inherits from int """


class MyInt(int):
    """ class that inherits from int"""

    def __eq__(self, other):
        return False

    def __ne__(self, other):
        return True
