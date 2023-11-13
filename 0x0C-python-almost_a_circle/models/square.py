#!/usr/bin/python3
"""Definition of Square class that inherits from Rectangle class.
"""


from models.rectangle import Rectangle as Rectangle


class Square(Rectangle):
    """Attributes and methods of Square class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes Square attributes.
        Args:
                size (int): dimensions of one side of the Square.
                x (int): determines the horizontal offset of the Square
                         from the left margin when printed.
                y (int): determines the vertical offset of the Square
                         when printed.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns human-readable string representation of Square object."""
        r_str = (
            f"[Square] ({self.id}) {super().x}/{super().y} - "
            f"{super().width}"
        )
        return r_str
