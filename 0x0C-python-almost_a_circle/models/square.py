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

    @property
    def size(self):
        """Dimensions of one side of the square.
        It is validated in the setter to ensure that it is an integer and that
        it is greater than 0. If not a ValueError is raised for values less
        than or equal to 0, and a TypeError is raised for values that aren't
        integers.
        """
        return super().width

    @size.setter
    def size(self, value):
        #        super(Square, self).width.__set__(self, value)
        #        super(Square, self).height.__set__(self, value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates Square attributes."""
        if args:
            for index, value in enumerate(args):
                if index == 0:
                    self.id = args[0]
                if index == 1:
                    self.width = args[1]
                    self.height = args[1]
                if index == 2:
                    self.x = args[2]
                if index == 3:
                    self.y = args[3]
        elif kwargs:
            for key in kwargs:
                if key == "size":
                    self.width = kwargs[key]
                    self.height = kwargs[key]
                else:
                    setattr(self, key, kwargs[key])
