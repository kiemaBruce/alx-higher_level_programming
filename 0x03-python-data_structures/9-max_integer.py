#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    list_len = len(my_list)
    t = 0
    for i in my_list:
        ind = my_list.index(i)
        if ind == 0:
            if i > my_list[ind + 1] and i > t:
                t = i
        elif ind == list_len - 1:
            if i > my_list[ind - 1] and i > t:
                t = i
        else:
            if i > my_list[ind - 1] and i > my_list[ind + 1] and i > t:
                t = i
    return t
