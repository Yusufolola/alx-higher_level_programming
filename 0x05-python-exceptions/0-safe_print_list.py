#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    # function that print x number of the list
    try:
        idx = 0
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
            idx = idx + 1
    except (TypeError, NameError , IndexError, ValueError):
        pass
    print("")
    return (idx)
