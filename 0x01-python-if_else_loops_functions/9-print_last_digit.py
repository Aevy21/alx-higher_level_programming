#!/usr/bin/python3
def print_last_digit(number):
    # Use the modulo operator (%) to get the last digit and then take its absolute value
    last_digit = abs(number % 10)
    print(last_digit)
