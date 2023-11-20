#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(int(value)))
        return True
    except ValueError as e:
        error_message = str(e)
        return False, error_message
