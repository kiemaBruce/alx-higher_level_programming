#!/usr/bin/python3
"""
This module defines the tests for the Base class.
"""


import unittest
import os
from models.base import Base


class TestBase(unittest.TestCase):
    """
    This classs performs unittests on the Base class.
    """

    def test_init(self):
        """Tests whether the id is properly initialized."""
        base1 = Base(24)
        self.assertEqual(base1.id, 24)
        base2 = Base()
        self.assertEqual(base2.id, 1)

    def test_to_json_string(self):
        """Tests the to_json_string method of Base class."""
        base1 = Base(24)
        comp_list = [
            {"age": "young", "stat": "strength", "limit": 4, "schooled": True}
        ]
        json_comp_list = (
            '[{"age": "young", "stat": "strength",'
            ' "limit": 4, "schooled": true}]'
        )
        self.assertEqual(base1.to_json_string(comp_list), json_comp_list)
        self.assertEqual(Base.to_json_string(comp_list), json_comp_list)

    def test_save_to_file(self):
        """ Tests the save_to_file() method if Base class.
        """
        lis = [{"id": 8, "height": 8, "width": 2, "x": 4, "y": 9}]
        filename = "Base.json"
        Base.save_to_file(lis)
        with open(filename, "r", encoding="utf-8") as myfile:
            self.assertEqual(
                myfile.read(),
                '[{"id": 8, "height": 8, "width": 2, "x": 4, "y": 9}]'
            ) 
