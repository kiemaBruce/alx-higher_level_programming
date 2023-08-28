#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    b = 0

    try:
        while 1:
            if b == x:
                break
            print(my_list[b], end="")
            b += 1
    except IndexError as r:
        print()  # newline only
    else:
        print()
    return b
