import unittest

from tree_node import TreeNode

class BSTIterator:
	def __init__(self, root: TreeNode = None):
		self.stack = []
		self.root = root
		while self.root:
			self.stack.append(self.root)
			self.root = self.root.left

	def next(self) -> int:
		if self.root and self.root.right:
			self.root = self.root.right
			while self.root:
				self.stack.append(self.root)
				self.root = self.root.left
		self.root = self.stack.pop()
		return self.root.val

	def hasNext(self) -> bool:
		return True if self.stack or self.root.right else False

class TestSolution(unittest.TestCase):
	def test_1(self):
		funcs = ["__init__", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
		args = [[TreeNode.stringToTreeNode('[7, 3, 15, null, null, 9, 20]')], [], [], [], [], [], [], [], [], []]
		output = [None, 3, 7, True, 9, True, 15, True, 20, False]
		res = []

		bst = BSTIterator()

		for i in range(len(funcs)):
			func = getattr(BSTIterator, funcs[i])
			arg = args[i]
			res.append(func(bst, *arg))
		
		self.assertEqual(res, output)

if __name__ == '__main__':
	unittest.main()