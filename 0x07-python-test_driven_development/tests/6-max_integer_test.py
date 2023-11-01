#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
import os
import sys


cwd = os.getcwd()
sys.path.append(cwd)
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines the various tests for max_integer([..])"""

    def test_type(self):
        """Tests the data type of the list items."""
        with self.assertRaises(TypeError) as context:
            max_integer([1, "s"])
        self.assertEqual(
            str(context.exception),
            "'>' not supported between instances of 'str' and 'int'",
        )
        with self.assertRaises(TypeError) as context:
            max_integer([1, [1, 2, 3]])
        self.assertEqual(
            str(context.exception),
            "'>' not supported between instances of 'list' and 'int'",
        )
        with self.assertRaises(TypeError) as context:
            max_integer([1, {1, 2, 3, "s"}])
        self.assertEqual(
            str(context.exception),
            "'>' not supported between instances of 'set' and 'int'",
        )
        with self.assertRaises(TypeError) as context:
            max_integer([1, {"one": 1, "two": 2, "three": 3}])
        self.assertEqual(
            str(context.exception),
            "'>' not supported between instances of 'dict' and 'int'",
        )
        with self.assertRaises(TypeError) as context:
            max_integer([1, (1, 2, 3, "till")])
        self.assertEqual(
            str(context.exception),
            "'>' not supported between instances of 'tuple' and 'int'",
        )
        with self.assertRaises(TypeError) as context:
            max_integer([1, None])
        self.assertEqual(
            str(context.exception),
            "'>' not supported between instances of 'NoneType' and 'int'",
        )

    def test_valid_values(self):
        """Tests max_integer() with list of valid values."""
        self.assertEqual(max_integer([99, 2, 1]), 99)
        self.assertEqual(max_integer([1, 2, 99]), 99)
        self.assertEqual(max_integer([1, 2.2, 0.5]), 2.2)
        self.assertEqual(max_integer([True, 5]), 5)
        self.assertEqual(max_integer([None]), None)
        self.assertEqual(max_integer(["s"]), "s")
        self.assertEqual(max_integer([]), None)

    def test_arg_type(self):
        """Tests whether the argument is a list or not."""
        with self.assertRaises(TypeError) as context:
            max_integer(5)
        self.assertEqual(str(context.exception),
                         "object of type 'int' has no len()")
        with self.assertRaises(TypeError) as context:
            max_integer({1, 2, 4})
        self.assertEqual(str(context.exception),
                         "'set' object is not subscriptable")
