#!/usr/bin/python3
"""
This module defines the Square class.
"""


from .rectangle import Rectangle


class Square(Rectangle):
    """Square class attributes."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes Square attributes.
        Args:
                size (int): dimensions of one side of the Square.
                x (int): specifies the horizontal offset when printing a
                         Square
                y (int): specifies the vertical offset when printing a
                         Square.
                id: Identifies the Square object.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns reaadable string representation of Square object.
        """
        class_name = self.__class__.__name__
        ret_s = (
            f"[{class_name}] "
            + f"({self.id}) {self.x}/{self.y} - "
            + f"{self.width}"
        )
        return ret_s

    @property
    def size(self):
        """ Returns the 'size' attribute of the Square object.
        """
        return self._Rectangle__width

    @size.setter
    def size(self, value):
        """ Sets the value of the size attribute of the Square object.
        Args:
            value (int): the value to be assigned to the size attribute.
        """
        self.integer_validator("width", value)
        self._Rectangle__width = value
        self._Rectangle__height = value

    def update(self, *args, **kwargs):
        """Updates Square attributes."""
        if args and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.size = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
        else:
            if kwargs:
                for key in kwargs:
                    if key == "id":
                        self.id = kwargs[key]
                    if key == "size":
                        self.size = kwargs[key]
                    if key == "x":
                        self.x = kwargs[key]
                    if key == "y":
                        self.y = kwargs[key]

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        square_dict = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
        return square_dict
