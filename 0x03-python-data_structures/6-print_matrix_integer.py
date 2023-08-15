#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    b = 0
    for i in matrix:
        for j in matrix[b]:
            print("{:d}".format(j), end="\n" if (matrix[b]).index(j) ==
                  (len(matrix[b]) - 1) else " ")
        b += 1
