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
        b1 = Base()
        self.assertEquals(b1.id, 1)
        b1 = Base()
        self.assertEquals(b1.id, 2)
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
    
    def test_Rectangle(self):
        """
        THis test definition tests all the possible test cases
        on class Rectangle
        """
        self.assertIsNotNone(Rectangle(1, 2))
        self.assertIsNotNone(Rectangle(1, 2, 3))
        self.assertIsNotNone(Rectangle(1, 2, 3, 4))
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        self.assertRaises(TypeError, Rectangle, 2, "1")
        self.assertRaises(TypeError, Rectangle, 1, 2, "3")
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "4")
        self.assertRaises(ValueError, Rectangle, -1, 2)
        self.assertRaises(ValueError, Rectangle, 1, -2)
        self.assertRaises(ValueError, Rectangle, 0, 2)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(ValueError, Rectangle, 1, 2, -3)
        self.assertRaises(ValueError, Rectangle, 1, 2, 3, -4)
        ist_1r = Rectangle(1, 2)
        self.assertIsNotNone(ist_1r.area())
        self.assertIsNotNone(str(ist_1r))
        ist_1r = Rectangle(1, 2, 3)
        self.assertIsNotNone(ist_1r.to_dictionary())
        self.assertIsNone(ist_1r.update())
        self.assertIsNone(ist_1r.update(78))
        self.assertIsNone(ist_1r.update(78, 1))
        self.assertIsNone(ist_1r.update(78, 1, 2))
        self.assertIsNone(ist_1r.update(78, 1, 2, 3))
        self.assertIsNone(ist_1r.update(78, 1, 2, 3, 4))
        self.assertIsNone(ist_1r.update(**{"id": 89}))
        self.assertIsNone(ist_1r.update(**{"id": 89, "width": 1}))
        self.assertIsNone(ist_1r.update(**{"id": 89, "width": 1, "height": 2}))
        self.assertIsNone(ist_1r.update(**{"id": 89, "width": 1, "height": 2, "x": 3, "y": 4}))
        self.assertIsNotNone(Rectangle.create(**{"id": 89}))
        self.assertIsNotNone(Rectangle.create(**{"id": 89, "width": 1}))
        self.assertIsNotNone(Rectangle.create(**{"id": 89, "width": 1, "height": 2}))
        self.assertIsNotNone(Rectangle.create(**{"id": 89, "width": 1, "height": 2, "x": 3}))
        self.assertIsNotNone(Rectangle.create(**{"id": 89, "width": 1, "height": 2, "x": 3, "y": 4}))
        self.assertIsNone(Rectangle.save_to_file(None))
        self.assertIsNone(Rectangle.save_to_file([]))
        self.assertIsNone(Rectangle.save_to_file([Rectangle(1, 2)]))
        self.assertIsNone(Rectangle.save_to_file([Rectangle(1, 2)]))
        self.assertIsNotNone(Rectangle.load_from_file()) # checkback  # checkback
    
    def test_Square(self):
        """
        THis test definition tests all the possible test cases
        on class Square
        """
        self.assertIsNotNone(Square(1))
        self.assertIsNotNone(Square(1, 2))
        self.assertIsNotNone(Square(1, 2, 3))
        self.assertRaises(TypeError, Square, 1, "2")
        self.assertRaises(TypeError, Square, 1, 2, "3")
        self.assertRaises(ValueError, Square, -1)
        self.assertRaises(ValueError, Square, 1, -2)
        self.assertRaises(ValueError, Square, 1, 2, -3)
        self.assertRaises(ValueError, Square, 0)
        self.assertIsNotNone(str(Square))
        self.assertIsNotNone(Square(1, 2, 3).to_dictionary())
        self.assertIsNone(Square(1, 2, 3).update())
        self.assertIsNone(Square(1, 2, 3).update(99))
        self.assertIsNone(Square(1, 2, 3).update(89, 1))
        self.assertIsNone(Square(1, 2, 3).update(89, 1, 2, 3))
        self.assertIsNone(Square(1, 2, 3).update(**{"id": 89}))
        self.assertIsNone(Square(1, 2, 3).update(**{"id": 89, "size": 1}))
        self.assertIsNone(Square(1, 2, 3).update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3}))
        self.assertIsNotNone(Square.create(**{'id': 89}))
        self.assertIsNotNone(Square.create(**{'id': 89, 'size': 1}))
        self.assertIsNotNone(Square.create(**{'id': 89, 'size': 1, 'x': 2}))
        self.assertIsNotNone(Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3}))
        self.assertEqual(Square.load_from_file(), [])
        self.assertIsNone(Square.save_to_file(None))
        self.assertIsNone(Square.save_to_file([]))
        self.assertIsNone(Square.save_to_file([Square(1)]))
        self.assertIsNotNone(Square.load_from_file())
