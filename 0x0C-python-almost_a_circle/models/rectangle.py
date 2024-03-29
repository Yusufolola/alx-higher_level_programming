#!/usr/bin/python3
from base import Base


class Rectangle(Base):
    """
    defining a rectangle object
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize attributes"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        for j in range(self.__y):
            print('')
        for i in range(self.__height):
            print(f"{' ' * self.__x}{'#' * self.__width}")

    def __str__(self):
        """overriding str"""
        return f"Rectangle ({self.__id}) \
                {self.__x}/{self.__y} - \
                {self.__width}/{self>__height}"


if __name__ == "__main__":

    r1 = Rectangle(2, 3, 2, 2)
    r1.display()

    print("---")

    r2 = Rectangle(3, 2, 1, 0)
    r2.display()
