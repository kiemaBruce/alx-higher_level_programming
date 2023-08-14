#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if (i % 3 == 0):
            if (i % 5 == 0):
                print("FizzBuzz ", end="")
                continue
            print("Fizz ", end="")
            continue
        if (i % 5 == 0):
            print("Buzz ", end="")
            continue
        print(i, " ", end="")
