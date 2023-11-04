#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for num in row:
            print("{:d}".format(num), end="\t")
        print()  # Start a new line for the next row
