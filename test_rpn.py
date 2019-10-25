import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate('1 1 +')
        self.assertEqual(2, result)
    
    def test_subtract(self):
        self.assertEqual(1, rpn.calculate('3 2 -'))
        self.assertEqual(-1, rpn.calculate('2 3 -'))

    def test_badinput(self):
        with self.assertRaises(TypeError):
            rpn.calculate('1 2 3 +')