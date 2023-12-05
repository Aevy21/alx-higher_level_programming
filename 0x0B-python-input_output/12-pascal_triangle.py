#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.

    Parameters:
    - n (int): The number of rows to generate.

    Returns:
    list of lists: Pascal's triangle up to the nth row.
    """
    triangle = []

    for i in range(n):
        row = [1] + [sum(pair) for pair in zip(*([0] + triangle[-1] + [0],))]
        triangle.append(row)

    return triangle
