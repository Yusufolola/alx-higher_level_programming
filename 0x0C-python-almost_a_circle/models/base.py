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
            self.id = id
        else:
            self.__nb_objects += 1
        self.id = self.__nb_objects
