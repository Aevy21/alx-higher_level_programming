#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create an empty result matrix with the same dimensions as the input matrix
    new_matrix = []
    for row in matrix:
        result_row = []
        # Initialize an empty row for the result matrix
        for element in row:
            # Calculate the square of the element
            squared_element = element ** 2
            result_row.append(squared_element)
            # Append the squared element to the result row
        new_matrix.append(result_row)  # Append the result row to the result matrix
    return new_matrix  # Return the result matrix

