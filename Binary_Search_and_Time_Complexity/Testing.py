"""
This file contains the testcases for linear and binary searches

"""
import unittest
from Search import LinearSearch, BinarySearch

class TestSearchAlgorithms(unittest.TestCase):

	def test_linearSearch(self):
		values = [3,5,2,4,7,8,9,0]
		self.assertEqual(LinearSearch(values, 5), 1)

	def test_BinarySearch(self):
		values = [1,2,3,4,5,6,7,8]
		self.assertEqual(BinarySearch(values, 7), 6)


if __name__ == "__main__":
	unittest.main()