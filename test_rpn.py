import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate('1 1 +')
        self.assertEqual(2, result)
    
    def test_subtract(self):
        self.assertEqual(1, rpn.calculate('3 2 -'))
    
    def test_mul(self):
        self.assertEqual(96, rpn.calculate('12 8 *'))

    def test_div(self):
        self.assertEqual(5, rpn.calculate('17 3 /'))

    def test_modulo(self):
        self.assertEqual(2, rpn.calculate('17 3 %'))

    def test_power(self):
        self.assertEqual(125, rpn.calculate('5 3 **'))

    def test_factorial(self):
        self.assertEqual(1, rpn.calculate('0 !'))
        self.assertEqual(240, rpn.calculate('6 !'))

    def test_badinput(self):
        with self.assertRaises(TypeError):
            rpn.calculate('1 2 3 +')