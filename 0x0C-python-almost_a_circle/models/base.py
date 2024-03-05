#!/usr/bin/python3
class Base:
    """
    base of all classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        intialize id
        """
        if id is not None:
            id = self.id
        else:
            __nb_objects += 1
        id = __nb_objects
