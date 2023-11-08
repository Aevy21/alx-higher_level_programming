#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # Sort the keys in alphabetical order
    sorted_keys = sorted(a_dictionary.keys())

    # Iterate over the sorted keys and print key-value pairs
    for key in sorted_keys:
        value = a_dictionary[key]
        print("{}: {}".format(key, value))
