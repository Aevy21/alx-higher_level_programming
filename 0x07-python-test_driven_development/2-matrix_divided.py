#!/usr/bin/python3
"""
Note:
Divide all elements
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a divisor.

    Parameters:
    - matrix (list of lists): Matrix to be divided.
    - div (int or float): Divisor.

    Returns:
    - list of lists: Resulting matrix after division.
    """

    # Check if matrix is a list of lists of integers or float
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError\
                ("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each element in the lists is an integer or float
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError\
                ("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row has the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform matrix division and round to 2 decimal places
    result_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return result_matrix
