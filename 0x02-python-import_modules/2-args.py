#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Subtracting 1 for the script name itself
    arg_num = len(sys.argv) - 1
    if arg_num == 0:
        print("{} arguments.".format(arg_num))
    elif arg_num == 1:
        print("{} argument:".format(arg_num))
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(arg_num))
        for index in range(1, arg_num + 1):
            print("{}: {}".format(index, sys.argv[index]))
