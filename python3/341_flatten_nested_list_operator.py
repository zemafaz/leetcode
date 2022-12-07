import unittest

class NestedIterator:
	def __init__(self, nested_list: list[int]):
		self.flat_list = []
		self.flatten_list(nested_list)
	
	def flatten_list(self, l):
		for e in l:
			if isinstance(e,int):
				self.flat_list.append(e)
			else:
				self.flatten_list(e)
		
	def next(self) -> int:
		return self.flat_list.pop(0)

	def has_next(self) -> bool:
		return len(self.flat_list) != 0

class TestSolution(unittest.TestCase):

	def my_test(iterator: NestedIterator):
		res = []
		while iterator.has_next():
			res.append(iterator.next())
		return res
	
	def test_1(self):
		iterator = NestedIterator([[1,1],2,[1,1]])
		res = TestSolution.my_test(iterator)
		self.assertEqual(res, [1,1,2,1,1])
	
	def test_2(self):
		iterator = NestedIterator([1,[4,[6]]])
		res = TestSolution.my_test(iterator)
		self.assertEqual(res, [1,4,6])

if __name__ == "__main__":
	unittest.main()
		

