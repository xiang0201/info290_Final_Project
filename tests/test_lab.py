import unittest
from src import *
import sys
sys.path.append('..')



class TestFunctions(unittest.TestCase):


    def test_falling(self):
        self.assertEqual(falling(6, 3), 120)
        self.assertEqual(falling(4, 3), 24)
        self.assertEqual(falling(4, 1), 4)
        self.assertEqual(falling(4, 0), 1)

    def test_divisible_by_k(self):
        self.assertEqual(divisible_by_k(10, 2), 5)
        self.assertEqual(divisible_by_k(3, 1), 3)
        self.assertEqual(divisible_by_k(6, 7), 0)

    def test_sum_digits(self):
        self.assertEqual(sum_digits(10), 1)
        self.assertEqual(sum_digits(4224), 12)
        self.assertEqual(sum_digits(1234567890), 45)
        self.assertEqual(sum_digits(123), 6)

    def test_double_eights(self):
        self.assertFalse(double_eights(8))
        self.assertTrue(double_eights(88))
        self.assertTrue(double_eights(2882))
        self.assertTrue(double_eights(880088))
        self.assertFalse(double_eights(12345))
        self.assertFalse(double_eights(80808080))

    def test_falling_zero_k(self):
        self.assertEqual(falling(10, 0), 1)
#
#     def test_divisible_by_k_zero_n(self):
#         self.assertEqual(divisible_by_k(0, 2), 0)
#
#     def test_sum_digits_single_digit(self):
#         self.assertEqual(sum_digits(5), 5)
#
#     def test_double_eights_no_eights(self):
#         self.assertFalse(double_eights(1234567))
#
#     def test_double_eights_one_eight(self):
#         self.assertFalse(double_eights(12345678))

#     def test_falling_large_numbers(self):
#         self.assertEqual(falling(100, 5), 9034502400)

if __name__ == '__main__':
    unittest.main()