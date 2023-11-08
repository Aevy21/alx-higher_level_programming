#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_numbers = []
    # Create an empty list to store unique integers
    total = 0  # Initialize the total sum

    for number in my_list:
        if number not in unique_numbers:
            unique_numbers.append(number)
            # Add the unique number to the list
            total += number
            # Add the unique number to the total sum

    return total
