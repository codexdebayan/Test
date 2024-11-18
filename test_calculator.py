import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(3, 2), 5)
        self.assertEqual(self.calc.add(1, 1), 2)
        with self.assertRaises(ValueError):
            self.calc.add(-1, 2)
        with self.assertRaises(ValueError):
            self.calc.add(2, -2)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(5, 5), 0)
        with self.assertRaises(ValueError):
            self.calc.subtract(-1, 2)
        with self.assertRaises(ValueError):
            self.calc.subtract(2, -2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 2), 6)
        self.assertEqual(self.calc.multiply(1, 5), 5)
        with self.assertRaises(ValueError):
            self.calc.multiply(-1, 2)
        with self.assertRaises(ValueError):
            self.calc.multiply(2, -2)

if __name__ == '__main__':
    unittest.main()
