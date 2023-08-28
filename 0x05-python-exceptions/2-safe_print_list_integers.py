#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    b = 0
    try:
        while 1:
            if b == x:
                break
            if type(my_list[b]) is int:
                print("{:d}".format(b), end="")
            b += 1
    except TypeError as t:
        raise IndexError("list index out of range")
    else:
        print()
        return b
