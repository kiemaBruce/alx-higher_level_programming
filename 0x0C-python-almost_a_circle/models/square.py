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
