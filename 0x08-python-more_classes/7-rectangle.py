#!/usr/bin/python3
"""
Defines an empty Rectangle class.
"""


class Rectangle:
    """Definition of the Rectangle class.
    Attributes:
        number_of_instances: the number of instances that have been created.
        print_symbol: the symbol to be used in the string representation of
        theRectangle instance.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes instance attributes.
        Args:
            width (int): width of the Rectangle object.
            height (int): height of the Rectangle object.
        """
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

    @property
    def width(self):
        """Returns the width of the Rectangle object.
        The setter raises a TypeError if width is not an int, and a ValueError
        if width is less than 0.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of the Rectangle object.
        The setter raises a TypeError if height is not an int, and a ValueError
        if it is less than 0.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the Rectangle area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Returns the Rectangle perimeter.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a Rectangle representation using hashes.
        """
        rect_str = ""
        if self.__width == 0 or self.__height == 0:
            return rect_str
        for i in range(self.__height):
            for j in range(self.__width):
                rect_str += str(self.print_symbol)
            if i != self.__height - 1:
                rect_str += '\n'
        return rect_str

    def __repr__(self):
        """Returns a string that can be used to reproduce the object.
        """
        repr_str = ("Rectangle(" + str(self.__width) + ", "
                    + str(self.__height) + ")"
                    )
        return repr_str

    def __del__(self):
        """Prints a string when an instance is being deleted.
        """
        print("Bye rectangle...")
        self.__class__.number_of_instances -= 1
