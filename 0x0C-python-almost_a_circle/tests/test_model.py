import unittest
"""
THis module contain possible test cases for the
class Base, Square, and Rectangle
"""
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
"""Import the Base, Square, and the Rectangle class"""


class Test_1(unittest.TestCase):
    def test_ifExists(self):
        b1 = Base()
        self.assertIsNotNone(b1.id)
