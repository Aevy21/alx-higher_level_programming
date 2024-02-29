#!/usr/bin/python3
"""
function that finds a peak in a list of unsorted integers.
"""

def find_peak(list_of_integers):
    """
    Find a peak in a list of integers using binary search.

    Args:
        list_of_integers (list): A list of integers.

    Returns:
        int: The peak value found in the list.
    """
    left = 0
    right = len(list_of_integers) - 1
    
    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid
            
    return list_of_integers[left]
