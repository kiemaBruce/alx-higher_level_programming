#!/usr/bin/python3
"""Contains TestSquare class.
"""


import unittest
from models.square import Square as Square


class TestSquare(unittest.TestCase):
    """Defines different tests for Square class."""

    def test_init(self):
        """Tests whether Square instance is instantiated well."""
        sq1 = Square(5, 2, 3, 16)
        self.assertEqual(sq1.width, 5)
        self.assertEqual(sq1.height, 5)
        self.assertEqual(sq1.x, 2)
        self.assertEqual(sq1.y, 3)
        self.assertEqual(sq1.id, 16)
        with self.assertRaises(TypeError) as e:
            sq1 = Square()
        self.assertEqual(
            str(e.exception),
            "__init__() missing 1 required positional argument: 'size'",
        )

    def test_validation(self):
        """Tests integer validation."""
        with self.assertRaises(TypeError) as e:
            sq1 = Square("s")
        self.assertEqual(str(e.exception), "width must be an integer")
        with self.assertRaises(TypeError) as e:
            sq1 = Square(2, [1])
        self.assertEqual(str(e.exception), "x must be an integer")
        with self.assertRaises(ValueError) as e:
            sq1 = Square(0)
        self.assertEqual(str(e.exception), "width must be > 0")
        with self.assertRaises(ValueError) as e:
            sq1 = Square(1, -1)
        self.assertEqual(str(e.exception), "x must be >= 0")
        with self.assertRaises(ValueError) as e:
            sq1 = Square(1, 0, -1)
        self.assertEqual(str(e.exception), "y must be >= 0")
        with self.assertRaises(TypeError) as e:
            sq1 = Square([1, 2])
        self.assertEqual(str(e.exception), "width must be an integer")
        with self.assertRaises(TypeError) as e:
            sq1 = Square((1, 2, "I'm immutable!"))
        self.assertEqual(str(e.exception), "width must be an integer")
        with self.assertRaises(TypeError) as e:
            sq1 = Square({"hope": "sure"})
        self.assertEqual(str(e.exception), "width must be an integer")
        with self.assertRaises(TypeError) as e:
            sq1 = Square({1, "uniqueness is my thing"})
        self.assertEqual(str(e.exception), "width must be an integer")
        # Test validation with setter
        with self.assertRaises(ValueError) as e:
            sq1 = Square(2)
            sq1.width = 0
        self.assertEqual(str(e.exception), "width must be > 0")
        with self.assertRaises(TypeError) as e:
            sq1 = Square(2)
            sq1.width = ["haha!", 1]
        self.assertEqual(str(e.exception), "width must be an integer")

        def test_str(self):
            """Tests the overidden __str__ method."""
            sq1 = Square(5, 1, 2, 20)
            self.assertEqual(str(sq1), "[Square] (20) 1/2 - 5")
