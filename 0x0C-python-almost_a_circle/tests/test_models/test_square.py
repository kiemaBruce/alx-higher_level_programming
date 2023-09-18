#!/usr/bin/python3
"""
This module defines the TestSquare class.
"""


import unittest
from models.square import Square
from unittest.mock import patch
import sys
import io


class TestSquare(unittest.TestCase):
    """Defines tests for the Square class.
    """
    def test_init(self):
        """ Tests for correct initialization of Square attributes.
        """
        s1 = Square(2, 5, 0, 1)
        self.assertEqual(s1.height, 2)
        self.assertEqual(s1.x, 5)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)
        with self.assertRaises(TypeError) as con:
            res = Square()
        self.assertEqual(
            str(con.exception),
            "__init__() missing 1 required positional argument: 'size'",
        )

    def test_str(self):
        """Tests whether the __str__ method works as expected."""
        s1 = Square(5)
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            print(s1)
            captured_output = mock_stdout.getvalue().strip()
        self.assertEqual(captured_output, "[Square] (3) 0/0 - 5")
        with self.assertRaises(TypeError) as con:
            Square.__str__()
        self.assertEqual(
            str(con.exception),
            "__str__() missing 1 required positional argument: 'self'",
        )

    def test_sizesetterandgetter(self):
        """Tests whether size setter and getter works as intended.
        """
        s1 = Square(6)
        self.assertEqual(s1.size, 6)
        s1.size = 8
        self.assertEqual(s1.size, 8)
        with self.assertRaises(TypeError) as con:
            s1.size = 's'
        self.assertEqual(str(con.exception), "width must be an integer")
        s1 = Square(9)
        with self.assertRaises(ValueError) as con2:
            s1.size = 0
        self.assertEqual(str(con2.exception), "width must be > 0")
