#!/usr/bin/python3
""" Module contains class rectangle
    Attributes:
        width: width of a Rectangle
        height: height of a Rectangle
"""


class Rectangle:
    """Define Rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializer with default width and height, 0"""
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1


    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns biggest rectangle based on area or
            rect_1 if both have the same area value
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return(rect_1)
        else:
            return(rect_2)

    @classmethod
    def square(cls, size=0):
        g = cls(size, size)
        return (g)

    @property
    def width(self):
        """retrieve width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """To set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """property to retrieve height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """to set height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    
    def area(self):
        """Returns rectangle area"""
   
    def perimeter(self):
        """Returns rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * self.__width + 2 * self.__height)

    def __str__(self):
        new_str = ("")
        if self.__width == 0 or self.__height == 0:
            return (new_str)
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    new_str += str(self.print_symbol)
                if i in range(self.__height - 1):
                    new_str += '\n'
            return (new_str)

    def __repr__(self):
        """repr returns string representation of rectangle """
        return 'Rectangle(%s, %s)' % (self.__width, self.__height)

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
