#!/usr/bin/python3
"""a class that inherit from basegeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """inherited from basegeometry"""

    def __init__(self, width, height):
        """instantiation with width and height"""
        BaseGeometry.integer_validator(self, 'width', width)
        self.__width = width
        BaseGeometry.integer_validator(self, 'height', height)
        self.__height = height

    def area(self):
        """return the area of the rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """return the rectangle description"""

        return f"[Rectangle] {self.__width}/{self.__height}"
