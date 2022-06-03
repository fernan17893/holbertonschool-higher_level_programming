#!/usr/bin/python3
""" write file """


def write_file(filename="", text=""):
    """ writes string to text file """
    with open("my_file_0.txt", 'w+', encoding="utf-8") as f:
        write = f.write(text)
    return(write)
