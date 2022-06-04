#!/usr/bin/python3
""" Defines a Pascal's Triangle """


def pascal_triangle(n):
    """ Pascal's Triangle of size n.
        Returns list of integers representing triangle 
        """

    if n <= 0:
        return []


    triangle = [[1]]
    while len(triangle) != n:
        t = triangle[-1]
        tmp = [1]
        for i in range(len(t) - 1):
            tmp.append(t[i] + t[i + 1])
        tmp.append(1)
        triangle.append(tmp)
    return triangle
