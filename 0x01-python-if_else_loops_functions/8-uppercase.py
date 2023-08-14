#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        asc = ord(str[i])
        if asc > 96 and asc < 123:
            print("{:s}{:s}".format(chr(asc - 32), "\n"
                  if i == (len(str) - 1) else ""), end="")
        else:
            print("{:s}{:s}".format(chr(asc), "\n"
                  if i == (len(str) - 1) else ""), end="")
