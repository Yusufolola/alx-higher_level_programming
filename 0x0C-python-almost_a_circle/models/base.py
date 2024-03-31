#!/usr/bin/python3
"""base class"""


class Base:
    """ base of all classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """intialize id"""

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        if id is not None:
            self.id = id
