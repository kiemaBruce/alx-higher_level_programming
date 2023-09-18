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
        self.assertEqual(captured_output, "[Square] (4) 0/0 - 5")
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

    def test_update(self):
        """Tests the update method of Square class.
        """
        s1 = Square(5)
        self.assertEqual((s1.id, s1.size), (5, 5))
        s1.update()
        self.assertEqual(
            (s1.id, s1.size, s1.x, s1.y),
            (5, 5, 0, 0)
        )
        s1.update(1)
        self.assertEqual(s1.id, 1)
        s1.update(1, 6)
        self.assertEqual((s1.id, s1.size), (1, 6))
        s1.update(1, 6, 7)
        self.assertEqual((s1.id, s1.size, s1.x), (1, 6, 7))
        s1.update(1, 6, 7, 4)
        self.assertEqual(
            (s1.id, s1.size, s1.x, s1.y), (1, 6, 7, 4)
        )
        with self.assertRaises(ValueError) as con:
            s1.update(1, -3)
        self.assertEqual(str(con.exception), "width must be > 0")
        with self.assertRaises(ValueError) as con:
            s1.update(2, 3, 4, -1)
        self.assertEqual(str(con.exception), "y must be >= 0")
        with self.assertRaises(TypeError) as con:
            Square.update()
        self.assertEqual(
            str(con.exception),
            "update() missing 1 required positional argument: 'self'",
        )
        s1.update(size=2)
        self.assertEqual(s1.size, 2)
        s1.update(size=21, x=11)
        self.assertEqual((s1.size, s1.x), (21, 11))
        s1.update(x=15, id=90, y=12)
        self.assertEqual((s1.x, s1.id, s1.y), (15, 90, 12))
        s1.update(x=15, id=90, y=12, size=87)
        self.assertEqual(
            (s1.x, s1.id, s1.y, s1.size),
            (15, 90, 12, 87)
        )
        s1.update(1, 23, 12, size=44)
        self.assertEqual(s1.size, 23)

    def test_to_dictionary(self):
        """ Tests the to_dictionary method of Square class."""
        r1 = Square(2, 0, 0, 2)
        comp_dict = {"id": 2, "size": 2, "x": 0, "y": 0}
        r1_dict = r1.to_dictionary()
        self.assertEqual(comp_dict, r1_dict)
        with self.assertRaises(TypeError) as con:
            Square.to_dictionary()
        self.assertEqual(
            str(con.exception),
            "to_dictionary() missing 1 required positional argument: 'self'"
        )
        self.assertEqual(type(comp_dict), type(r1_dict))

    def test_square(self):
        """Tests create() method in Square class."""
        s1 = Square(3, 5, 0, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))


if __name__ == '__main__':
    unittest.main()
