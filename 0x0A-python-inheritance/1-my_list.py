#!/usr/bin/python3
""" Defines class that inherits class MyList. """


class Mylist(list):
    """ Class inherited from list """

    def print_sorted(self):
        sorti = self.copy()
        sorti.sort()
        print(sorti)
