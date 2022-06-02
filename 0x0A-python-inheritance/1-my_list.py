#!/usr/bin/python3
""" Defines class that inherits class MyList. """


class MyList(list):
    """ Class inherited from list """

    def print_sorted(self):
        """ prints list in sorted ascending order"""
        if issubclass(MyList, list):
            print(sorted(self))
