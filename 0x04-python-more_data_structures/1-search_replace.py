#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Create a new list to store the updated elements
    new_list = []

    # Iterate through the original list
    for item in my_list:
        if item == search:
            # Replace the element if it matches the search element
            new_list.append(replace)
        else:
            # Keep the original element
            new_list.append(item)

    return new_list
