#!/usr/bin/python3
""" returns the numbers of characters written"""


def write_file(filename="", text=""):
    """function defination"""

    with open(filename, "w") as file:
        nb = file.write(text)
        return(nb)
