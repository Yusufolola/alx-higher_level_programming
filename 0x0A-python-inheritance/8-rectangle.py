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


