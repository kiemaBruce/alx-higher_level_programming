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


if __name__ == "__main__":
    unittest.main()
