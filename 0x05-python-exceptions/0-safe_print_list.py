#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    b = 0

    try:
        for i in my_list:
            if b == x:
                break
            print(i, end="" if i < x else "\n")
            b += 1
    except IndexError as r:
        print(r.agrs[0])
    return b
