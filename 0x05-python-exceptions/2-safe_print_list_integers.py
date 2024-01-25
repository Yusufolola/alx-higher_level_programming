#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    # function that prints x numbers of integers
    idx = 0
    for i in range (x):
        try:
            print("{:d}".format(my_list[i]), end="")
            idx = idx + 1
        except(TypeError, ValueError):
            pass
    print("")
    return idx
