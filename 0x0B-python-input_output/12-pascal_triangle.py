#!/usr/bin/python3
"""
This module defines the pascal_triangle function.
"""


def pascal_triangle(n):
    """Returns the Pascal's triangle of n.
    Args:
            n (int): the number of rows of the Pascal's triangle that is to
                     be returned.
    Return:
            list: a list of lists of integers representing the Pascal’s
                  triangle of n
    """
    if n <= 0:
        return []
    pasc_list = []
    for i in range(n + 1):
        sub_list = []
        for j in range(i):
            if j == 0:
                sub_list.append(1)
                continue
            if j == i - 1:
                sub_list.append(1)
                continue
            sub_list.append(pasc_list[i - 1][j - 1] + pasc_list[i - 1][j])
        pasc_list.append(sub_list)
    del pasc_list[0]  # Remove zeroth element which is an empty list
    return pasc_list
