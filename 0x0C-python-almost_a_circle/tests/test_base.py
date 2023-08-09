import unittest
"""
THis module contain possible test cases for the
class Base, Square, and Rectangle
"""
from models.base import Base
"""
importing base
"""


class Test_1(unittest.TestCase):
    """
    this is a test class containing all
    possible test cases
    """
    def test_Base(self):
        """
        THis test definition tests all the possible test cases
        on class Base
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        ist_3 = Base(99)
        self.assertEqual(ist_3.id, 99)
        self.assertIsNotNone(ist_3.to_json_string(None))
        self.assertIsNotNone(ist_3.to_json_string([]))
        self.assertIsNotNone(ist_3.to_json_string([{'id': 12}]))
        self.assertIsInstance(ist_3.to_json_string([{'id': 12}]), str)
        self.assertIsNotNone(ist_3.from_json_string(None))
        self.assertIsNotNone(ist_3.from_json_string("[]"))
        self.assertIsNotNone(ist_3.from_json_string('[{"id": 12}]'))
        self.assertIsInstance(ist_3.from_json_string('[{"id": 12}]'), list)
