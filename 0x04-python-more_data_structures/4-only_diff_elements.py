#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    unique_elements_set = set()  # Create an empty set to store unique elements

    for item in set_1:
        if item not in set_2:
            unique_elements_set.add(item)

    for item in set_2:
        if item not in set_1:
            unique_elements_set.add(item)

    return unique_elements_set
