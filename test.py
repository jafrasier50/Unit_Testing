import unittest
from Calc import Calculator

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

    def tearDown(self):
        print("TEAR DOWN")

if __name__ == '__main__':
    unittest.main()
