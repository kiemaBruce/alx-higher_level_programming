#!/usr/bin/python3
s = 10
for i in range(8):
    for j in range(0, s):
        if j > i:
            print("{:d}{:d}, ".format(i, j), end="")
print("89")
