import unittest

class MyHashSet:
	__RANDOM_ODD_NUMBER = 3916297 # random odd number, good if prime
	__M = 15 # lenghth of output in bits, since its given that there are no more than 10**4 operations overall, chose a number as 2**m > 10**4
	__W = 20 # size of the machine word, trivial to this problem, w > m

	def __init__(self):
		self.__hash_set = [[] for _ in range(1 << self.__M)]

	def __multiplicative_hash(self, key) -> int:
		return ((key*self.__RANDOM_ODD_NUMBER) & (1<< self.__M) - 1) >> (self.__W - self.__M)

	def add(self, key: int) -> None:
		hashed = self.__multiplicative_hash(key)
		if key not in self.__hash_set[hashed]:
			self.__hash_set[hashed].append(key)

	def remove(self, key: int) -> None:
		hashed = self.__multiplicative_hash(key)
		if key in self.__hash_set[hashed]:
			self.__hash_set[hashed].remove(key)

	def contains(self, key: int) -> bool:
		hashed = self.__multiplicative_hash(key)
		return key in self.__hash_set[hashed]

	def __eq__(self, other) -> bool:
		other_conv = [[] for _ in range(1<<self.__M)]
		for e in other:
			hashed = self.__multiplicative_hash(e)
			other_conv[hashed].append(e)
		return self.__hash_set == other_conv

class TestSolution(unittest.TestCase):

	def test_1(self):
		hash_set = MyHashSet()
		hash_set.add(1)
		hash_set.add(2)
		self.assertEqual(hash_set, [1, 2])
		self.assertEqual(hash_set.contains(1), True)
		self.assertEqual(hash_set.contains(3), False)
		hash_set.add(2)
		self.assertEqual(hash_set, [1,2])
		self.assertEqual(hash_set.contains(2), True)
		hash_set.remove(2)
		self.assertEqual(hash_set, [1])
		self.assertEqual(hash_set.contains(2), False)

if __name__ == '__main__':
	unittest.main()