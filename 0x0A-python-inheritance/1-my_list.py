#!/usr/bin/python3
""" Defines class that inherits class MyList. """


class Mylist(list):
    """ Prints sorted list for built in list class """

    def print_sorted(self):
        """ Print list in sorted ascending order """
        print(sorted(self))
