#!/usr/bin/python3
"""
This module defines the TestSquare class.
"""


import unittest
from models.square import Square


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
