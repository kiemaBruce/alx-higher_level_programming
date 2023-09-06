#!/usr/bin/python3
"""
This module contains the matrix_divided function.
"""


def matrix_divided(matrix, div):
    """ Divides all elements of a matrix
        Args:
            matrix(list): a list of lists which is the matrix..
            div(int/ float): the divisor used to divide all elements of the
            matrix.
        Returns:
            list: a new matrix with the results of the division which are
            rounded off to two decimal places..
        Raises:
            TypeError: if matrix is not a matrix (list of lists) of
            integers/floats
            TypeError: If the rows of the matrix aren't all of same size.
            TypeError: if div is not an integer or float.
            ZeroDivisionError: if div is equal to 0.
    """
    size = counter = 0
    str1 = "matrix must be a matrix (list of lists) of integers/floats"
    str2 = "Each row of the matrix must have the same size"
    str3 = "division by zero"
    str4 = "div must be a number"
    # matrix is not a list
    if not isinstance(matrix, list):
        raise TypeError(str1)
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError(str1)
        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError(str1)
            if isinstance(j, bool):
                raise TypeError(str1)
    # Test the lengths of the individual lists
    for i in matrix:
        if len(i) != size and counter != 0:
            raise TypeError(str2)
        size = len(i)
        counter += 1
    if div == 0:
        raise ZeroDivisionError(str3)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError(str4)
    if isinstance(div, bool):
        raise TypeError(str4)
    new_list = []
    m = 0
    for i in matrix:
        sublist = []
        n = 0
        for j in i:
            sublist.append(round(matrix[m][n] / div, 2))
            n += 1
        new_list.append(sublist)
        m += 1
    return new_list
