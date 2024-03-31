#!/usr/bin/python3
"""function that reads a text file"""


def read_file(filename=""):
    """function that reads a text file"""
    
    with open(filename, "r") as f:
        content = f.read()
        print(content, end='')
