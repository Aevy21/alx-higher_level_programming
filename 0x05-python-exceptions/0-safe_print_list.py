#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    printed_elements = 0

    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            printed_elements += 1
    except IndexError:
        pass  # Ignore IndexError, as we're handling it gracefully

    print()  # Print a new line after the elements
    return printed_elements
