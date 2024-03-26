#!/usr/bin/python3
"""a function that returns true if the if the oject is exactly an
    instance of the specified class.
"""


def is_same_class(obj, a_class):
    """function prototype"""

    if type(obj) == a_class:
        return True
    else:
        return False
