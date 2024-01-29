#!/usr/bin/python3
class Rectangle:

    """
	this class defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """
		initializes the rectangle instance with width and height
		"""

        self.height = height
        self.width = width
    
    @property
    def width(self):
        """
        returns the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set the value of the width and check if it is greater than 0 and its of type int
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
   
    @property
    def height(self):
        """
        returns the height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        set the value of the height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
