#!/usr/bin/python3
"""Contains the definition of pascal_triangle() function.
"""


def pascal_triangle(n):
    """Returns a list of lists representing the Pascal's triangle of n.
    Args:
            n (int): number whose Pascal's triangle is to be determined.
    """
    ret_list = []
    c = 0
    if n <= 0:
        return ret_list
    for i in range(1, n + 1):
        sub_list = []
        for j in range(i):
            if j == 0 or j == i - 1:
                sub_list.append(1)
            else:
                sub_list.append((ret_list[c - 1])[j - 1]
                                + (ret_list[c - 1])[j]
                                )
        ret_list.append(sub_list)
        c += 1
    return ret_list
