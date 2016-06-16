import unittest
from fizz import fizz_buzz

class FizzBuzzTest(unittest.TestCase):
	"""Testing FizzBuzzTest
	"""

	def test_returns_fizz_when_divisible__by_three(self):
		"""Test return fizz when input is divisile
		"""
		self.assertEqual(fizz_buzz(3),"fizz")

	def test_returns_buzz_when_divisible__by_five(self):
		"""Test return buzz when input is divisile
		"""
		self.assertEqual(fizz_buzz(5),"buzz")
		

unittest.main()

