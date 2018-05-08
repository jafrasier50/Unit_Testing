import unittest
from CalcMod import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        print("SETUP")
        self.calculator = Calculator()

    def test_add(self):
        print("test_add")
        result = self.calculator.add(4,5)
        self.assertEqual(9,result)

    def test_subtract(self):
        print("test_subtract")
        result = self.calculator.subtract(9,3)
        self.assertEqual(6,result)

    def test_multiply(self):
        print("test_multiply")
        result = self.calculator.multiply(4,4)
        self.assertEqual(16,result)

    def test_divide(self):
        print("test_divide")
        result = self.calculator.divide(4,4)
        self.assertEqual(1,result)


if __name__ == '__main__':
    unittest.main()
