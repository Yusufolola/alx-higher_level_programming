#!/usr/bin/python3
def safe_print_integer_err(value):
    # function that prints an integer
    import sys
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        sys.stderr.write("Exception: {}\n".format(Exception))
        return False
