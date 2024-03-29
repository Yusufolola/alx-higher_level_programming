#!/usr/bin/python3
"""a class that inherit from basegeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle
class Square(Rectangle):
    """inherited from rectangle"""

    def __init__(self, size):
        """instantiation with width and height"""

        BaseGeometry.integer_validator(self, 'size', size)
        self.__size = size

    def area(self):
        """return the area of the rectangle"""

        return self.__size * self.__size

    def __str__(self):
        """return the rectangle description"""

        return f"[Rectangle] {self.__size}/{self.__size}"
