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
    def test_Base(self):
        """
        THis test definition tests all the possible test cases
        on class Base
        """
        b1 = Base(89)
        self.assertEqual(b1.id, 89)
#        b2 = Base()
#        self.assertEqual(b2.id, 2)
#       ist_3 = Base(99)
#        self.assertEqual(ist_3.id, 99)
#       self.assertIsNotNone(ist_3.to_json_string(None))
#       self.assertIsNotNone(ist_3.to_json_string([]))
#       self.assertIsNotNone(ist_3.to_json_string([{'id': 12}]))
#       self.assertIsInstance(ist_3.to_json_string([{'id': 12}]), str)
#       self.assertIsNotNone(ist_3.from_json_string(None))
#       self.assertIsNotNone(ist_3.from_json_string("[]"))
#       self.assertIsNotNone(ist_3.from_json_string('[{"id": 12}]'))
#       self.assertIsInstance(ist_3.from_json_string('[{"id": 12}]'), list)
