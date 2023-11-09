#!/usr/bin/python3
"""Contains TestRectangle class which tests Rectangle class.
"""


import models.rectangle as rectangle
import unittest


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
             "__init__() missing 2 required positional arguments: 'width' and "
             "'height'"
            )
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
            (
             "'Rectangle' object has no attribute '_TestRectangle__x'"
            )
        )
