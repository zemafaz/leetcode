from copy import copy
import unittest

class PeekingIterator:
	def __init__(self, iterator):
		"""
		Initialize your data structure here.
		:type iterator: Iterator
		"""
		self.iterator = iterator
		

	def peek(self):
		"""
		Returns the next element in the iteration without advancing the iterator.
		:rtype: int	
		"""
		aux = copy(self.iterator)
		return next(aux)
	

	def next(self):
		"""
		:rtype: int
		"""
		return next(self.iterator)
		

	def hasNext(self):
		"""
		:rtype: bool
		"""
		try:
			aux = copy(self.iterator)
			next(aux)
			return True
		except:
			return False

class TestSolution(unittest.TestCase):
	def test_1(self):
		peeking_iterator = PeekingIterator(iter([1,2,3]))
		self.assertEqual(peeking_iterator.next(), 1)
		self.assertEqual(peeking_iterator.peek(), 2)
		self.assertEqual(peeking_iterator.next(), 2)
		self.assertEqual(peeking_iterator.next(), 3)
		self.assertEqual(peeking_iterator.hasNext(), False)

if __name__ == '__main__':
	unittest.main()