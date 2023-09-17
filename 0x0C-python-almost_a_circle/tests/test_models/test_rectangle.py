#!/usr/bin/python3
"""
This module includes unittests for the Rectangle class.
"""


import unittest
import textwrap
from models.base import Base
from models.rectangle import Rectangle
from unittest.mock import patch
import sys
import io


class TestRectangle(unittest.TestCase):
    """Tests the Rectangle class."""

    def test_init(self):
        """Tests whether all Rectangle attributes have been initialized
        properly.
        """
        rec1 = Rectangle(2, 5, 0, 0, 1)
        self.assertEqual(rec1.width, 2)
        self.assertEqual(rec1.height, 5)
        self.assertEqual(rec1.x, 0)
        self.assertEqual(rec1.y, 0)
        self.assertEqual(rec1.id, 1)
        with self.assertRaises(TypeError) as con:
            res = Rectangle(2)
        self.assertEqual(
            str(con.exception),
            "__init__() missing 1 required positional argument: 'height'",
        )
        with self.assertRaises(TypeError) as con:
            res = Rectangle()
        self.assertEqual(
            str(con.exception),
            (
                "__init__() missing 2 required positional "
                "arguments: 'width' and 'height'"
            ),
        )

    def test_integer_validator(self):
        """Tests whether integer validator works as intended."""
        # Check for wrong values.
        self.assertRaises(TypeError, Rectangle, "s", 2)
        with self.assertRaises(TypeError) as con:
            res = Rectangle("s", 2)
        self.assertEqual(str(con.exception), "width must be an integer")
        with self.assertRaises(TypeError) as con:
            Rectangle(2, "s")
        self.assertEqual(str(con.exception), "height must be an integer")
        with self.assertRaises(TypeError) as con:
            Rectangle(2, 3, "s")
        self.assertEqual(str(con.exception), "x must be an integer")
        with self.assertRaises(TypeError) as con:
            Rectangle(2, 3, 4, "l")
        self.assertEqual(str(con.exception), "y must be an integer")
        with self.assertRaises(ValueError) as con:
            Rectangle(0, 2)
        with self.assertRaises(TypeError) as con:
            Rectangle(2, True)
        self.assertEqual(str(con.exception), "height must be an integer")
        with self.assertRaises(TypeError) as con:
            Rectangle(2, [1, 2])
        self.assertEqual(str(con.exception), "height must be an integer")
        with self.assertRaises(TypeError) as con:
            Rectangle(2, (1, 2, 3))
        self.assertEqual(str(con.exception), "height must be an integer")
        with self.assertRaises(TypeError) as con:
            Rectangle(2, {"hope": True, "age": 23})
        self.assertEqual(str(con.exception), "height must be an integer")
        with self.assertRaises(TypeError) as con:
            Rectangle(2, None)
        self.assertEqual(str(con.exception), "height must be an integer")
        with self.assertRaises(ValueError) as con:
            Rectangle(2, -1)
        self.assertEqual(str(con.exception), "height must be > 0")
        with self.assertRaises(ValueError) as con:
            Rectangle(2, 1, -1)
        self.assertEqual(str(con.exception), "x must be >= 0")
        with self.assertRaises(ValueError) as con:
            Rectangle(2, 1, 4, -2)
        self.assertEqual(str(con.exception), "y must be >= 0")
        rec1 = Rectangle(34, 2)
        with self.assertRaises(ValueError) as con:
            rec1.integer_validator("width", 0)
        self.assertEqual(str(con.exception), "width must be > 0")
        with self.assertRaises(ValueError) as con:
            rec1.integer_validator("height", 0)
        self.assertEqual(str(con.exception), "height must be > 0")
        with self.assertRaises(ValueError) as con:
            rec1.integer_validator("x", -1)
        self.assertEqual(str(con.exception), "x must be >= 0")
        with self.assertRaises(ValueError) as con:
            rec1.integer_validator("y", -1)
        self.assertEqual(str(con.exception), "y must be >= 0")
        with self.assertRaises(TypeError) as con:
            rec1.integer_validator()
        self.assertEqual(
            str(con.exception),
            "integer_validator()"
            " missing 2 required positional arguments: 'name' and 'value'",
        )
        with self.assertRaises(TypeError) as con:
            rec1.integer_validator(2)
        self.assertEqual(
            str(con.exception),
            "integer_validator()" " missing 1 required positional"
            " argument: 'value'"
        )

    def test_setters(self):
        """Tests whether attribute setters work as intended."""
        rec2 = Rectangle(3, 5)
        rec2.width = 22
        rec2.height = 33
        rec2.x = 9
        rec2.y = 11
        self.assertEqual(rec2.width, 22)
        self.assertEqual(rec2.height, 33)
        self.assertEqual(rec2.x, 9)
        self.assertEqual(rec2.y, 11)

    def test_area(self):
        """Tests whether area is returned correctly."""
        rec1 = Rectangle(2, 5)
        self.assertEqual(rec1.area(), 10)
        with self.assertRaises(TypeError) as con:
            Rectangle.area()
        self.assertEqual(
            str(con.exception),
            "area() missing 1 required positional argument: 'self'"
        )

    def test_display(self):
        """Test if the display method of Rectangle class works as expected."""
        rec1 = Rectangle(2, 3)
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            rec1.display()
            captured_output = mock_stdout.getvalue()
        self.assertEqual(captured_output, "##\n##\n##\n")
        rec1 = Rectangle(2, 3, 2, 1)
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            rec1.display()
            captured_output = mock_stdout.getvalue()
        self.assertEqual(captured_output, "\n  ##\n  ##\n  ##\n")
        with self.assertRaises(TypeError) as con:
            Rectangle.display()
        self.assertEqual(
            str(con.exception),
            "display() missing 1 required positional argument: 'self'",
        )

    def test_str(self):
        """Tests whether the __str__ method works as expected."""
        rec1 = Rectangle(4, 5)
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            print(rec1)
            captured_output = mock_stdout.getvalue().strip()
        self.assertEqual(captured_output, "[Rectangle] (20) 0/0 - 4/5")
        with self.assertRaises(TypeError) as con:
            Rectangle.__str__()
        self.assertEqual(
            str(con.exception),
            "__str__() missing 1 required positional argument: 'self'",
        )

    def test_update(self):
        """Tests whether the update method works as intended.
        """
        rec1 = Rectangle(2, 5)
        self.assertEqual((rec1.id, rec1.width, rec1.height), (21, 2, 5))
        rec1.update()
        self.assertEqual(
            (rec1.id, rec1.width, rec1.height, rec1.x, rec1.y),
            (21, 2, 5, 0, 0)
        )
        rec1.update(1)
        self.assertEqual(rec1.id, 1)
        rec1.update(1, 6)
        self.assertEqual((rec1.id, rec1.width), (1, 6))
        rec1.update(1, 6, 7)
        self.assertEqual((rec1.id, rec1.width, rec1.height), (1, 6, 7))
        rec1.update(1, 6, 7, 4)
        self.assertEqual(
            (rec1.id, rec1.width, rec1.height, rec1.x), (1, 6, 7, 4)
        )
        rec1.update(1, 6, 7, 4, 5)
        self.assertEqual(
            (rec1.id, rec1.width, rec1.height, rec1.x, rec1.y),
            (1, 6, 7, 4, 5)
        )
        with self.assertRaises(ValueError) as con:
            rec1.update(1, -3)
        self.assertEqual(str(con.exception), "width must be > 0")
        with self.assertRaises(ValueError) as con:
            rec1.update(1, 3, -5)
        self.assertEqual(str(con.exception), "height must be > 0")
        with self.assertRaises(ValueError) as con:
            rec1.update(2, 3, 4, -1)
        self.assertEqual(str(con.exception), "x must be >= 0")
        with self.assertRaises(ValueError) as con:
            rec1.update(1, 3, 8, 3, -1)
        self.assertEqual(str(con.exception), "y must be >= 0")
        with self.assertRaises(TypeError) as con:
            Rectangle.update()
        self.assertEqual(
            str(con.exception),
            "update() missing 1 required positional argument: 'self'",
        )
