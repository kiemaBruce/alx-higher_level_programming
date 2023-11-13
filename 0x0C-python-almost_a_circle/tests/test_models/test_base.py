#!/usr/bin/python3
"""Contains TestBase which tests base.py.
"""


import unittest
import os
import sys
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


os.chdir("models")
current_dir = os.getcwd()
sys.path.append(current_dir)


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

    def test_save_to_file(self):
        """Tests the save_to_file() method"""
        rec1 = Rectangle(12, 24, 3, 2, 44)
        rec2 = Rectangle(21, 7, 4, 5, 23)
        list_objs = [rec1, rec2]
        Base.save_to_file(list_objs)
        expected_saved_str = (
            '[{"id": 44, "width": 12, "height": 24, "x": 3, "y": 2}'
            ', {"id": 23, "width": 21, "height": 7, "x": 4, "y": 5}]'
        )
        filename = list_objs[0].__class__.__name__ + ".json"
        with open(filename, mode="r", encoding="utf-8") as myfile:
            str_from_file = myfile.read()
        self.assertEqual(str_from_file, expected_saved_str)
        with self.assertRaises(TypeError) as c:
            Base.save_to_file()
        self.assertEqual(
            str(c.exception),
            "save_to_file() missing 1 required positional argument: "
            "'list_objs'"
        )
        sq1 = Square(5, 1, 2, 22)
        sq2 = Square(6, 2, 3, 44)
        list_objs = [sq1, sq2]
        Base.save_to_file(list_objs)
        expected_saved_str = (
            '[{"id": 22, "size": 5, "x": 1, "y": 2}'
            ', {"id": 44, "size": 6, "x": 2, "y": 3}]'
        )
        filename = list_objs[0].__class__.__name__ + ".json"
        with open(filename, mode="r", encoding="utf-8") as myfile:
            str_from_file = myfile.read()
        self.assertEqual(str_from_file, expected_saved_str)
        list_objs = None
        Base.save_to_file(list_objs)
        expected_saved_str = "[]"
        filename = list_objs.__class__.__name__ + ".json"
        with open(filename, mode="r", encoding="utf-8") as myfile:
            str_from_file = myfile.read()
        self.assertEqual(str_from_file, expected_saved_str)

    def test_from_json_string(self):
        """Tests the from_json_string() method"""
        with self.assertRaises(TypeError) as c:
            Base.from_json_string()
        self.assertEqual(
            str(c.exception),
            "from_json_string() missing 1 required positional "
            "argument: 'json_string'"
        )
        s_str = (
            '[{"id": 22, "size": 5, "x": 1, "y": 2}'
            ', {"id": 44, "size": 6, "x": 2, "y": 3}]'
        )
        self.assertEqual(
            Base.from_json_string(s_str),
            [
                {"id": 22, "size": 5, "x": 1, "y": 2},
                {"id": 44, "size": 6, "x": 2, "y": 3}
            ]
        )
        e_list = []
        self.assertEqual(Base.from_json_string(None), e_list)
        self.assertEqual(Base.from_json_string([]), e_list)
