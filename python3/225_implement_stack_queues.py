import unittest

class MyStack:

	def __init__(self) -> None:
		self.stack = []

	def push(self, x: int) -> None:
		self.stack.append(x)

	def pop(self) -> int:
		return self.stack.pop()

	def top(self) -> int:
		return self.stack[-1]

	def empty(self) -> bool:
		return len(self.stack) == 0

class TestSolution(unittest.TestCase):
	def test_1(self):
		my_stack = MyStack()
		my_stack.push(1)
		my_stack.push(2)
		self.assertEqual(my_stack.top(), 2)
		self.assertEqual(my_stack.pop(), 2)
		self.assertEqual(my_stack.pop(), 1)
		self.assertEqual(my_stack.empty(), True)

if __name__ == "__main__":
	unittest.main()