#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for num in range(x):
        try:
            value = my_list[num]
            if isinstance(value, int):
                print("{:d}".format(value), end="")
                count += 1
        except (ValueError, TypeError):
            pass
    print()
    return count
