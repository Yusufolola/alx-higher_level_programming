#!/usr/bin/python3
"""a function that returns true if the object is an instance of or if the 
    the object is an instance of a class that inherited fromthe specified class otherwise false.
"""

def is_kind_of_class(obj, a_class):
    """prottype"""

    if isinstance (obj, a_class):
        return True
    else:
        return False
