#!/usr/bin/python3
"""class square with size"""


class Square:
    """size instantiation"""

    def __init__(self , size = 0):
        """instance"""

        if not isinstance(size ,int):
            raise TypeError(" size must be an integer")

        if size < 0 :
            raise ValueError("size must be >= 0")

        self.__size = size  

    def area(self):
        """returns the current area"""

        return (self.__size * self.__size)

