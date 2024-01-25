#!/usr/bin/python3
def safe_print_integer(value):
    # function that true if integer and false otherwise
    try:
        print("{:d}".format(value))
        return True
    except(TypeError, ValueError, NameError):
        return False

