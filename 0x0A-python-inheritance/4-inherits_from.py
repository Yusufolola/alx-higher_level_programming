#!/usr/bin/python3
"""a function that return true if the object is an instance of a class that inherited from the specified class.
"""

def inherits_from(obj, a_class):
    """prototype"""

    if issubclass (type(obj), a_class):
        return True
    else:
        return False
