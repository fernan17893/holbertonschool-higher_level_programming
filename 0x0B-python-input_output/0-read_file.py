#!/usr/bin/python3
""" Read file to stdout """


def read_file(filename=""):
    """ read text file and print to stdout """
    with open(filename, encoding="utf-8") as f:
        read = f.read()
    print(read, end="")
