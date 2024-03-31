#!/usr/bin/python3
"""defines a square that inherit from the rectangle class"""


from models.rectangle import Rectangle
class Square(Rectangle):
    """defining a square object """

    def __init__(self, size, x=0, y=0, id=None):
        """initialize attributes"""
        
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overriding str"""

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        return self.__height

    @size.setter
    def size(self, value):
        """width setter"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value 

    def update(self, *args, **kwargs):
        """this assigns attributes"""

        if args:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.size = args[1]
            if len(args) == 3:
                self.x = args[2]
            if len(args) == 4:
                self.y = args[3]
        else:
            self.id = kwargs.get("id")
            self.__x = kwargs.get("x")
            self.__y = kwargs.get("y")
            self.__size = kwargs.get("size")

if __name__ == "__main__":

    s1 = Square(5)
    print(s1)

    s1.update(10)
    print(s1)

    s1.update(1, 2)
    print(s1)

    s1.update(1, 2, 3)
    print(s1)

    s1.update(1, 2, 3, 4)
    print(s1)

    s1.update(x=12)
    print(s1)

    s1.update(size=7, y=1)
    print(s1)

    s1.update(size=7, id=89, y=1)
    print(s1)



