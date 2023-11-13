#!/usr/bin/python3
"""Contains TestBase which tests base.py.
"""


import unittest
import os
import sys


os.chdir("models")
current_dir = os.getcwd()
sys.path.append(current_dir)

Base = __import__("base").Base


class TestBase(unittest.TestCase):
    """Contains the tests for Base class."""

    def test_init(self):
        """Tests whether attributes are initialized properly."""
        base1 = Base()
        self.assertEqual(1, base1.id)
        base1 = Base(12)
        self.assertEqual(12, base1.id)
        base1 = Base()
        self.assertEqual(2, base1.id)

    def test_list_dictionaries(self):
        """Tests to_json_string()"""
        t_dict = dict(width=2, x=7, height=22, y=77, info=True)
        json_s = '{"width": 2, "x": 7, "height": 22, "y": 77, "info": true}'
        self.assertEqual(Base.to_json_string(t_dict), json_s)
        self.assertEqual(Base.to_json_string(None), "[]")
        empty_list = []
        self.assertEqual(Base.to_json_string(empty_list), "[]")
        with self.assertRaises(TypeError) as c:
            Base.to_json_string()
        self.assertEqual(
            str(c.exception),
            "to_json_string() missing 1 required positional argument: "
            "'list_dictionaries'"
        )
