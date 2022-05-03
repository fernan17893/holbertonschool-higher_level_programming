#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for i in matrix:
        if i != "[" or i != "]":
            print("". join(str(i)))
