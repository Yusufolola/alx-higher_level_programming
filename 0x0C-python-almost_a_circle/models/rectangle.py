#!/usr/bin/python3
"""defines a rectangle the inherit fromthe base class"""


from base import Base
class Rectangle(Base):
    """defining a rectangle object """

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
        """set the x value"""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """setthe y property"""

        return self.__y

    @y.setter
    def y(self, value):
        """set the value of y"""

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area"""

        return self.__width * self.__height

    def display(self):
        """display"""

        for j in range(self.__y):
            print('')
        for i in range(self.__height):
            print(f"{' ' * self.__x}{'#' * self.__width}")

    def __str__(self):
        """overriding str"""

        return f"[Rectangle] ({self.id}) \
                {self.__x}/{self.__y} - \
                {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            if (len(args) == 1):
                self.id = args[0]
            elif (len(args) == 2):
                self.__width = args[1]
            elif (len(args) == 3):
                self.__height = args[2]
            elif (len(args) == 4):
                self.__x = args[3]
            elif (len(args) == 5):
                self.__y = args[4]

        if kwargs is not None:
            self.id = kwargs.get("id", "1")
            self.__height = kwargs.get("height", "1")
            self.__width = kwargs.get("width", "10")
            self.__x = kwargs.get("x", "10")
            self.__y = kwargs.get("y", "10")

if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(height=1)
    print(r1)

    r1.update(width=1, x=2)
    print(r1)

    r1.update(y=1, width=2, x=3, id=89)
    print(r1)

    r1.update(x=1, height=2, y=3, width=4)
    print(r1)

