#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list  # If idx is negative or out of range, return the same list

    del my_list[idx]
    return my_list
