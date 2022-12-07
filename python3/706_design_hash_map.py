import unittest

class HashMap:

	__RANDOM_ODD_NUMBER = 3916297 # random odd number, good if prime
	__M = 15 # lenghth of output in bits, since its given that there are no more than 10**4 operations overall, chose a number as 2**m > 10**4
	__W = 20 # size of the machine word, trivial to this problem, w > m

	def __init__(self):
		self.__hash_map = [-1 for _ in range(1<<self.__M)]

	def __multiplicative_hash(self, key) -> int:
		return ((key*self.__RANDOM_ODD_NUMBER) & (1 << self.__M) - 1) >> (self.__W - self.__M)

	def put(self, key: int, value: int) -> None:
		key_hashed = self.__multiplicative_hash(key)
		self.__hash_map[key_hashed] = value

	def get(self, key: int) -> int:
		key_hashed = self.__multiplicative_hash(key)
		return self.__hash_map[key_hashed]

	def remove(self, key: int) -> None:
		key_hashed = self.__multiplicative_hash(key)
		self.__hash_map[key_hashed] = -1

	def __eq__(self, other) -> bool:
		other_conv = [-1 for _ in range(1 << self.__M)]
		for e in other:
			key = self.__multiplicative_hash(e[0])
			value = e[0]
			other_conv[key] = value
		return self.__hash_map == other_conv

class TestSolution(unittest.TestCase):
	def test_1(self):
		hash_map = HashMap()
		hash_map.put(1, 1)
		hash_map.put(2, 2)
		self.assertEqual(hash_map, [[1,1],[2,2]])
		self.assertEqual(hash_map.get(1), 1)
		self.assertEqual(hash_map.get(3), -1)
		hash_map.put(2, 1)
		self.assertEqual(hash_map.get(2), 1)
		hash_map.remove(2)
		self.assertEqual(hash_map.get(2), -1)

if __name__ == '__main__':
	unittest.main()