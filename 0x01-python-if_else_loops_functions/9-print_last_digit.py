#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        r = number % 10
    else:
        working_number = 0 - number
        r = working_number % 10
    print(r, end="")
    return r
