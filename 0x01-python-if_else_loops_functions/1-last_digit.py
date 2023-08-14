#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    working_number = 0 - number
    last_digit = working_number % 10
    if last_digit == 0:
        s = "and is 0"
        s2 = ""
    else:
        s = "and is less than 6 and not 0"
        s2 = "-"
    print(f"Last digit of {number:d} is {s2}{last_digit} {s}")
else:
    last_digit = number % 10
    if last_digit > 5:
        s = "and is greater than 5"
    elif last_digit == 0:
        s = "and is 0"
    else:
        s = "and is less than 6 and not 0"
    print(f"Last digit of {number:.0f} is {last_digit:.0f} {s:s}")
