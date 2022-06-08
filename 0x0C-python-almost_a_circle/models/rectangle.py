#!/usr/bin/python3
""" Class Rectangle that inherits from Base """
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ property retireves width """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets private instance width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ property retrieves instace height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set private instance height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ retrieve private instance x """
        return self.__x

    @x.setter
    def x(self, value):
        """ to set private instance x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ retrieve private instance y """
        return self.__y

    @y.setter
    def y(self, value):
        """ set private instance y """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ return rectangle area """
        return self.height * self.width

    def display(self):
        """ print # symbol """
        new_str = ""
        for i in range(self.__y):
            new_str += '\n'
        for i in range(self.__height):
            for i in range(self.__x):
                new_str += ' '
            for j in range(self.__width):
                new_str += '#'
            print(new_str)
            if i in range(self.__height - 1):
                new_str += '\n'
            new_str = ""

    def __str__(self):
        """ updates class overiding __str__ method """
        str = (f"({self.id}) {self.x}/{self.y} - {self.width}/{self.height}")
        return (f"[Rectangle] {str}")

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if len(args) > 0:
            my_list = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                if i < len(my_list):
                    setattr(self, my_list[i], args[i])
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns dictionary representation of Rectangle """
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}
