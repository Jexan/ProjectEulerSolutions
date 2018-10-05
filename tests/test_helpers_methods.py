from src.helpers import *
import unittest

class HelpersTests(unittest.TestCase):
    def test_generate_fibonacci(self):
        first_fib = (1, 1, 2, 3, 5, 8, 13, 21)
        self.assertEqual(tuple(take(8, generate_fibonacci())), first_fib)

    def test_primes_until_works_ok(self):
        first_primes = (2, 3, 5, 7, 11, 13, 17, 19)
        self.assertEqual(tuple(primes_until(20)), first_primes)

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(12321))
        self.assertTrue(is_palindrome(123321))
        self.assertTrue(is_palindrome(11))
        self.assertTrue(is_palindrome(12388321))

        self.assertFalse(is_palindrome(1234))
        self.assertFalse(is_palindrome(-123))
        self.assertFalse(is_palindrome(10))

    def test_mcm(self):
        self.assertEqual(mcm(2, 4, 6), 12)
        self.assertEqual(mcm(1, 3), 3)
        self.assertEqual(mcm(1, 2, 3, 4, 5), 60)