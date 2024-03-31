#!/usr/bin/python3
"""defines a square that inherit from the rectangle class"""


from models.rectangle import Rectangle
class Square(Rectangle):
    """defining a square object """

    def __init__(self, size, x=0, y=0, id=None):
        """initialize attributes"""
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

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

        return f"[Square] ({self.id}) {self.__x}/{self.__y} - {size}"


if __name__ == "__main__":

    s1 = Square(5)
    print(s1)
    print(s1.area())
    s1.display()

    print("---")

    s2 = Square(2, 2)
    print(s2)
    print(s2.area())
    s2.display()

    print("---")

    s3 = Square(3, 1, 3)
    print(s3)
    print(s3.area())
    s3.display()


