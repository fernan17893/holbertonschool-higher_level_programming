#!/usr/bin/python3
""" Append to existing text file """


def append_write(filename="", text=""):
    """ appends string to end of text file and returns
        the number of characters added
        """
    with open(filename, 'a+',  encoding="utf-8") as f:
        append = f.write(text)
    return(append)
