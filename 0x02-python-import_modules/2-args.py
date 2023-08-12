#!/usr/bin/python3
import sys
if __name__ == "__main__":
    no = len(sys.argv)
    print(no - 1, end='')
    if no == 2:
        print(" argument", end='')
    else:
        print(" arguments", end='')
    if no == 1:
        print(".")
    else:
        print(":")
        for i in range(1, no):
            print("{:d}: {:s}".format(i, sys.argv[i]))
