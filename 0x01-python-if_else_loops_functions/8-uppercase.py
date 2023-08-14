#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        asc = ord(str[i])
        if asc > 96 and asc < 123:
            print(chr(asc - 32), end="")
        else:
            print(chr(asc), end="")
    print()
