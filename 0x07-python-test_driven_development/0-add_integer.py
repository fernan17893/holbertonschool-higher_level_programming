#!/usr/bin/python3
""" Function will add two integers """

def add_integer(a, b=98):

    """ Function adds 2 integers
        a and b must be casted to integers
        if they are float

        Returns: the addition of a and b

        Raises:
        TypeError: If a or b is a non-integer or non-float
        """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError('a must be an integer')
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError('a must be an integer')
    return (int(a) +int(b))
