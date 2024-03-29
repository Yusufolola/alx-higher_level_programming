#!/usr/bin/python3
"""class that define a rectangle"""


class Rectangle:
    """this class defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializes the rectangle instance with width and height"""
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @property
    def width(self):
        """returns the width"""

        return (self.__width)

    @width.setter
    def width(self, value):
        """set the value of the width and check """

        if (type(value) is not int):
            raise TypeError("width must be an integer")

        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns the height"""

        return (self.__height)

    @height.setter
    def height(self, value):
        """set the value of the height"""

        if (type(value) is not int):
            raise TypeError("height must be an integer")

        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle base on area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() == rect_2.area()) or rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2.area()

    def __str__(self):
        """print the rectangle with # character"""

        if (self.__width == 0) or (self.__height == 0):
            return ("")

        return "\n".join(str(self.print_symbol) * self.__width
                         for i in range(self.__height))

    def __repr__(self):
        """return instance representation"""

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """delete an instance of the class"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    def area(self):
        """returns the area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """ returns the perimeter"""
        if (self.__height == 0) or (self.__width == 0):
            self.perimeter = 0

        return ((self.__height * 2) + (self.__width * 2))
