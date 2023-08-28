#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    b = 0
    try:
        while 1:
            if b == x:
                break
            if type(my_list[b]) is int:
                print(my_list[b], end="")
            b += 1
    except IndexError as e:
        pass
#        print(e.args[0])
    else:
        print()
        return b
