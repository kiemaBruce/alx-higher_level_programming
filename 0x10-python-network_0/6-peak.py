#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers."""


def find_peak_helper(list_of_integers, sub_list, sub_start, sub_end, flag):
    """Recursively finds the peak in an unsorted list of integers"""

    # FIRST we deal with the list sectioning into sublists
    if flag == 0:
        mid_index = len(list_of_integers) // 2
    else:
        mid_index = (len(sub_list) // 2) + sub_start
    if len(sub_list) == 1:
        # Here we cannot sub-divide the list further, i.e. base case
        pass
    elif len(sub_list) == 2:  # can only have a left sub-list
        """Some of these cases might be at start or end of list, check to avoid
        invalid indices"""
        l_sub_start = mid_index - 1
        l_sub_end = mid_index - 1
        l_sub = list_of_integers[l_sub_start:l_sub_end + 1]
    else:
        """
        right sub_list
        keep track of sub_list position in original list with the variables
        r_sub_start, r_sub_end, l_sub_start, l_sub_end
        """
        r_sub_start = mid_index + 1
        r_sub_end = sub_end
        r_sub = list_of_integers[r_sub_start:]
        # left sub_list
        l_sub_end = mid_index - 1
        l_sub_start = sub_start
        l_sub = list_of_integers[:l_sub_end + 1]
    # SECONDLY we check if the mid_element is a peak
    if len(sub_list) == 1:
        # start of list, only check element to its right
        if sub_start == 0:
            if sub_list[0] >= list_of_integers[sub_start + 1]:
                return sub_list[0]
        # list end, only check left
        elif sub_start == len(list_of_integers) - 1:
            if sub_list[0] >= list_of_integers[sub_start - 1]:
                r = sub_list[0]
                return sub_list[0]
        elif (sub_list[0] >= list_of_integers[sub_start + 1] and
                sub_list[0] >= list_of_integers[sub_start - 1]):
            return sub_list[0]
        return None
    elif len(sub_list) == 2:
        # only compare to its left
        if list_of_integers[mid_index] >= list_of_integers[mid_index - 1]:
            return list_of_integers[mid_index]
        # if not a peak, search it's left sub-list(doesn't have a right one)
        return (find_peak_helper(list_of_integers, l_sub, l_sub_start,
                l_sub_end, 1))
    else:
        if (list_of_integers[mid_index] >= list_of_integers[mid_index + 1] and
                list_of_integers[mid_index] >=
                list_of_integers[mid_index - 1]):
            return list_of_integers[mid_index]
        elif list_of_integers[mid_index] >= list_of_integers[mid_index - 1]:
            # There must be a peak on right sub-list
            return (find_peak_helper(list_of_integers, r_sub, r_sub_start,
                    r_sub_end, 1))
        elif list_of_integers[mid_index] >= list_of_integers[mid_index + 1]:
            # recursively search left, since there must be a peak there
            return (find_peak_helper(list_of_integers, l_sub, l_sub_start,
                    l_sub_end, 1))


def find_peak(list_of_integers):
    """Finds the peak in an unsorted list of integers"""
    list_len = len(list_of_integers)
    if list_len == 0:
        return None
    return find_peak_helper(
            list_of_integers, list_of_integers[:], 0, (list_len - 1), 0
            )
