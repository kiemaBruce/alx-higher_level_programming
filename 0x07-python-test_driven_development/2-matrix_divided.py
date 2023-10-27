#!/usr/bin/python3
"""
This module contains the definition of the matrix_divided function.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix, rounded to 2 decimal places.

    Args:
        matrix (list): a list of lists of integers or floats.
        div (int or float): the number by which the elements in the matrix are
                            to be divided.

    Returns:
        list: a new matrix (list of lists) that contains the results.

    Raises:
        TypeError: if matrix is not a list of lists of integers or floats.
        TypeError: if not all rows of the matrix have equal size.
        TypeError: if div is not an integer or float.
        ZeroDivisionError: if div is equal to 0.
    """
    str1 = "matrix must be a matrix (list of lists) of integers/floats"
    if not type(matrix) is list:
        raise TypeError(str1)
    for i in matrix:
        if not type(i) is list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )
        for j in i:
            if not type(j) is int and not type(j) is float:
                raise TypeError(str1)
    for index, value in enumerate(matrix):
        size = len(value)
        if index != 0 and size != prev_size:
            raise TypeError("Each row of the matrix must have the same size")
        prev_size = size
    if not type(div) is int and not type(div) is float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for s_list in matrix:
        new_sub_list = []
        for value in s_list:
            res = round(value / div, 2)
            new_sub_list.append(res)
        new_matrix.append(new_sub_list)
    return new_matrix
