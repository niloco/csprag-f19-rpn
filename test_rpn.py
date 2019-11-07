import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result, _ = rpn.calculate('1 1 +', list())
        self.assertEqual(2, result)
    
    def test_subtract(self):
        result, _ = rpn.calculate('3 2 -', list())
        self.assertEqual(1, result)
    
    def test_mul(self):
        result, _ = rpn.calculate('12 8 *', list())
        self.assertEqual(96, result)

    def test_div(self):
        result, _ = rpn.calculate('17 3 /', list())
        self.assertEqual(5, result)

    def test_modulo(self):
        result, _ = rpn.calculate('17 3 %', list())
        self.assertEqual(2, result)

    def test_power(self):
        result, _ = rpn.calculate('5 3 **', list())
        self.assertEqual(125, result)

    def test_factorial(self):
        result, _ = rpn.calculate('0 !', list())
        self.assertEqual(1, result)
        result, _ = rpn.calculate('6 !', list())
        self.assertEqual(720, result)

    def test_sum(self):
        result, _ = rpn.calculate('1 3 2 -6 S', list())
        self.assertEqual(0, result)

    def test_bad_input(self):
        stack = [1, 2, 3, 4, 5, 3342]
        self.assertRaises(  TypeError, 
                            rpn.calculate, 
                            '0 23 k', stack)
        self.assertRaises(  TypeError,
                            rpn.calculate,
                            '1 +', list())
        self.assertEqual([1, 2, 3, 4, 5, 3342], stack)
