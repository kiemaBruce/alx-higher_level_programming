#!/usr/bin/python3
"""Contains TestRectangle class which tests Rectangle class.
"""


import models.rectangle as rectangle
import unittest
from unittest.mock import patch
import sys
from io import StringIO


class TestRectangle(unittest.TestCase):
    """Tests for Rectangle class."""

    def test_init(self):
        """Tests whether all attributes are initialized properly."""
        rec1 = rectangle.Rectangle(12, 3, 4, 5, 7)
        self.assertEqual(rec1.width, 12)
        self.assertEqual(rec1.height, 3)
        self.assertEqual(rec1.x, 4)
        self.assertEqual(rec1.y, 5)
        self.assertEqual(rec1.id, 7)
        rec1 = rectangle.Rectangle(7, 5, 0, 0, 1)
        self.assertEqual(rec1.width, 7)
        self.assertEqual(rec1.height, 5)
        self.assertEqual(rec1.x, 0)
        self.assertEqual(rec1.y, 0)
        self.assertEqual(rec1.id, 1)
        with self.assertRaises(TypeError) as c:
            rec1 = rectangle.Rectangle()
        err_s = """__init__() missing 2 required positional arguments: 'width'
                and 'height'
                """
        self.assertEqual(
            str(c.exception),
            (
                "__init__() missing 2 required positional arguments: 'width'"
                " and 'height'"
            ),
        )
        with self.assertRaises(TypeError) as c:
            rec1 = rectangle.Rectangle(1)
        self.assertEqual(
            str(c.exception),
            "__init__() missing 1 required positional argument: 'height'",
        )

    def test_getters_and_setters(self):
        """Tests attribute setters and getters."""
        rec1 = rectangle.Rectangle(12, 7)
        self.assertEqual(rec1.width, 12)
        rec1.width = 13
        self.assertEqual(rec1.width, 13)
        # Attempting to access a private attribute.
        with self.assertRaises(AttributeError) as c:
            ans = rec1.__x
        self.assertEqual(
            str(c.exception),
            ("'Rectangle' object has no attribute '_TestRectangle__x'"),
        )

    def test_validation(self):
        """Tests the validation of the attributes."""
        # Test validation of all attributes.
        with self.assertRaises(TypeError) as c:
            rec1 = rectangle.Rectangle("string", 1)
        self.assertEqual(str(c.exception), "width must be an integer")
        with self.assertRaises(TypeError) as c:
            rec1 = rectangle.Rectangle(1, "string")
        self.assertEqual(str(c.exception), "height must be an integer")
        with self.assertRaises(TypeError) as c:
            rec1 = rectangle.Rectangle(12, 1, "x")
        self.assertEqual(str(c.exception), "x must be an integer")
        with self.assertRaises(TypeError) as c:
            rec1 = rectangle.Rectangle(12, 1, 8, "y")
        self.assertEqual(str(c.exception), "y must be an integer")
        rec1 = rectangle.Rectangle(12, 1, 8, 7, "12")
        self.assertEqual(rec1.id, "12")
        with self.assertRaises(ValueError) as c:
            rec1 = rectangle.Rectangle(-12, 1, 8, 5)
        self.assertEqual(str(c.exception), "width must be > 0")
        with self.assertRaises(ValueError) as c:
            rec1 = rectangle.Rectangle(12, 0, 8, 5)
        self.assertEqual(str(c.exception), "height must be > 0")
        with self.assertRaises(ValueError) as c:
            rec1 = rectangle.Rectangle(12, 1, -8, 5)
        self.assertEqual(str(c.exception), "x must be >= 0")
        with self.assertRaises(ValueError) as c:
            rec1 = rectangle.Rectangle(12, 1, 8, -5)
        self.assertEqual(str(c.exception), "y must be >= 0")
        # More tests with more invalid data types.
        with self.assertRaises(TypeError) as c:
            rec1 = rectangle.Rectangle(12, [1, 2, 3])
        self.assertEqual(str(c.exception), "height must be an integer")
        with self.assertRaises(TypeError) as c:
            rec1 = rectangle.Rectangle(12, "w")
        self.assertEqual(str(c.exception), "height must be an integer")
        with self.assertRaises(TypeError) as c:
            rec1 = rectangle.Rectangle(12, {"age": 12, "name": "B"})
        self.assertEqual(str(c.exception), "height must be an integer")
        with self.assertRaises(TypeError) as c:
            rec1 = rectangle.Rectangle(12, {1, "unique"})
        self.assertEqual(str(c.exception), "height must be an integer")
        with self.assertRaises(TypeError) as c:
            rec1 = rectangle.Rectangle(12, 1.2)
        self.assertEqual(str(c.exception), "height must be an integer")
        with self.assertRaises(TypeError) as c:
            rec1 = rectangle.Rectangle(12, (1, "coordinates"))
        self.assertEqual(str(c.exception), "height must be an integer")

    def test_area(self):
        """Tests for the area() method of Rectangle class."""
        rec1 = rectangle.Rectangle(4, 5)
        self.assertEqual(rec1.area(), 20)
        rec1 = rectangle.Rectangle(1, 2, 3, 4, 6)
        self.assertEqual(rec1.area(), 2)
        with self.assertRaises(TypeError) as c:
            rectangle.Rectangle.area()
        self.assertEqual(
            str(c.exception),
            ("area() missing 1 required positional argument: 'self'")
        )

    def test_display(self):
        """Test the display method of Rectangle class."""
        rec1 = rectangle.Rectangle(4, 5, 2, 2)
        rec_string = (
            "\n\n  ####\n  ####\n  ####\n  ####\n  ####\n"
        )
        with self.assertRaises(TypeError) as c:
            rectangle.Rectangle.display()
        self.assertEqual(
            str(c.exception),
            "display() missing 1 required positional argument: 'self'"
        )
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            rec1.display()
            printed_output = mock_stdout.getvalue()
            self.assertEqual(printed_output, rec_string)

    def test_str(self):
        """Tests __str__ method of Rectangle class"""
        rec1 = rectangle.Rectangle(4, 5, 6, 7, 9)
        r_str = "[Rectangle] (9) 6/7 - 4/5"
        self.assertEqual(str(rec1), r_str)
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            print(rec1)
            printed_output = mock_stdout.getvalue().strip()
            self.assertEqual(printed_output, r_str)
        with self.assertRaises(TypeError) as c:
            rectangle.Rectangle.__str__()
        self.assertEqual(
            str(c.exception),
            "__str__() missing 1 required positional argument: 'self'"
        )

    def test_update(self):
        """Tests the update() function."""
        rec1 = rectangle.Rectangle(4, 5, 6, 3, 2)
        self.assertEqual(rec1.width, 4)
        rec1.update(88)
        self.assertEqual(rec1.id, 88)
        rec1.update(88, 90)
        self.assertEqual(rec1.width, 90)
        rec1.update(88, 90, 2)
        self.assertEqual(rec1.height, 2)
        rec1.update(88, 90, 2, 3)
        self.assertEqual(rec1.x, 3)
        rec1.update(88, 90, 2, 3, 5)
        self.assertEqual(rec1.y, 5)
        rec1 = rectangle.Rectangle(4, 5, 6, 3, 2)
        rec1.update()
        self.assertEqual(rec1.width, 4)
        self.assertEqual(rec1.height, 5)
        self.assertEqual(rec1.x, 6)
        self.assertEqual(rec1.y, 3)
        self.assertEqual(rec1.id, 2)
        with self.assertRaises(TypeError) as c:
            rectangle.Rectangle.update()
        self.assertEqual(
            str(c.exception),
            "update() missing 1 required positional argument: 'self'"
        )
