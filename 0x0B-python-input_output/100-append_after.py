#!/usr/bin/python3
"""function that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """function defination"""

    with open(filename, "r+") as file:
        if file:
            line = file.readline()
            while line:
                if line == search_string:
                    line.append(new_string)
                line = file.readline()
