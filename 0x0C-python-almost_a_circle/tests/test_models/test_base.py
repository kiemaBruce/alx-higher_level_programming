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
