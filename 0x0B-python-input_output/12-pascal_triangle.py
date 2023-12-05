#!/usr/bin/python3
""" This module supplies a function pascal_triangle
to return a list of lists\
        of integers representing the
Pascal’s triangle of n"""


def pascal_triangle(n):
    """ Calculate Pascal's triangle for a given number of rows """
    triangle_matrix = []

    for current_row in range(n):
        if current_row == 0:
            row = [1]
            triangle_matrix.append(row)
        else:
            previous_row = triangle_matrix[-1]
            new_row_length = len(previous_row) + 1
            new_row = [0] * new_row_length

            for i in range(new_row_length):
                if i == 0 or i == new_row_length - 1:
                    new_row[i] = 1
                else:
                    new_row[i] = previous_row[i - 1] + previous_row[i]

            triangle_matrix.append(new_row)

    return triangle_matrix
