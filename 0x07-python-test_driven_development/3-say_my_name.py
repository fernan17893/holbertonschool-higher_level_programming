#!/usr/bin/python3
""" This function that prints my name(first_name, last_name)"""


def say_my_name(first_name, last_name=""):
    """ function that prints My name is <first name> <last name>

    first_name and last_name must be strings otherwise raise TypeError
    with the message first_name must be a string or last_name must be 
    a string """

    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))
