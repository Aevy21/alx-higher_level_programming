#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Initialize the sum to 0
    total = 0

    # Check if there are command-line arguments
    if len(sys.argv) > 1:
        # Iterate through the command-line arguments starting from the second one
        for arg in sys.argv[1:]:
            # Convert each argument to an integer and add it to the total
            total += int(arg)

    # Print the sum of the arguments
    print("{}".format(total))
