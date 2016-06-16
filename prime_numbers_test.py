import unittest
from prime_numbers import prime

class Test_Prime(unittest.TestCase):
	'''Testing our First Case'''
	def test_prime(self):
		test_a=prime(2,6)
		self.assertEqual(len(test_a),2)

	
unittest.main()