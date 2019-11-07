import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        self.assertEqual(2, rpn.calculate('1 1 +', list()))
    
    def test_subtract(self):
        self.assertEqual(1, rpn.calculate('3 2 -', list()))
    
    def test_mul(self):
        self.assertEqual(96, rpn.calculate('12 8 *', list()))

    def test_div(self):
        self.assertEqual(5, rpn.calculate('17 3 /', list()))

    def test_modulo(self):
        self.assertEqual(2, rpn.calculate('17 3 %', list()))

    def test_power(self):
        self.assertEqual(125, rpn.calculate('5 3 **', list()))

    def test_factorial(self):
        self.assertEqual(1, rpn.calculate('0 !', list()))
        self.assertEqual(720, rpn.calculate('6 !', list()))

    def test_sum(self):
        self.assertEqual(0, rpn.calculate('1 3 2 -6 S', list()))

    def test_bad_input(self):
        self.assertRaises(  TypeError, 
                            rpn.calculate, 
                            '0 23 k', list())

    def test_dummy(self):
        self.assertEqual(True, False)