#!/usr/bin/python3
"""it appends a string at the end of a text"""


def append_write(filename="", text=""):
    """appends"""

    with open(filename, "a",encoding="utf-8") as file:
        nb = file.write(text)
        return nb
