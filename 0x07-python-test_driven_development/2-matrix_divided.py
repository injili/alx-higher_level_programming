#!/usr/bin/python3
"""
Module 2-matrix_divided
Function matrix_divided that takes in a matrix and divides it
Returns a new matrix
"""


def matrix_divided(matrix, div):
    """
    returns the matrix / div
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    msg1 = "Each row of the matrix must have the same size"
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if type(matrix[i][j]) != int and type(matrix[i][j]) != float:
                    raise TypeError(msg)
                elif len(matrix) != len(matrix[i]):
                    raise TypeError(msg1)
                else:
                    matrix[i][j] = round((matrix[i][j] / div), 2)
    return (matrix)
