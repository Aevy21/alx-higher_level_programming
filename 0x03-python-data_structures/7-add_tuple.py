#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # if tuple is empty fill missing elements with 0
    while len(tuple_a) < 2:
        tuple_a += (0,)
    while len(tuple_b) < 2:
        tuple_b += (0,)

    # Calculate the sum of the 1st and 2nd elements of the tuples
    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return result
