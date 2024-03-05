#!/usr/bin/python3
"""class square with size"""


class Square:
    """size instantiation"""

    def __init__(self , size = 0):
        """instance"""

        self.size = size  
    
    @getter
    def size(self):
        """get the size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value ,int):
            raise TypeError(" size must be an integer")

        if (value < 0) :
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """returns the current area"""

        return (self.__size * self.__size)

