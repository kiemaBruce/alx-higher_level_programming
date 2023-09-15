#!/usr/bin/python3
"""
This module includes unittests for the Rectangle class.
"""


import unittest
import textwrap
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests the Rectangle class."""

    def test_init(self):
        """Tests whether all Rectangle attributes have been initialized
        properly.
        """
        rec1 = Rectangle(2, 5)
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
        with self.assertRaises(TypeError) as con2:
            res = Rectangle()
        self.assertEqual(
            str(con2.exception),
            (
                "__init__() missing 2 required positional "
                "arguments: 'width' and 'height'"
            ),
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
