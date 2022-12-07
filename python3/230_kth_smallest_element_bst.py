import unittest
from tree_node import TreeNode

class Solution:
	def kth_smallest(self, root: TreeNode, k: int) -> int:
		stack = []

		while root.left != None:
			stack.append(root)
			root = root.left
		stack.append(root)

		visited = []

		while True:
			root = stack.pop()
			visited.append(root)
			if k == 1:
				return root.val
			if root.left != None:
				if root.left not in visited:
					stack.append(root)
					stack.append(root.left)
					continue
			if root.right != None:
				stack.append(root.right)
				k -= 1
				continue
			k -= 1
			continue
	
	def kth_smallest_inorder(self, root: TreeNode, k: int) -> int:

		def inorder(r):
			return inorder(r.left) + [r.val] + inorder(r.right) if r else []
		
		return inorder(root)[k-1]
	
	def kth_smallest_inorder_stack(self, root: TreeNode, k: int) -> int:
		stack = []

		while True:
			while root:
				stack.append(root)
				root = root.left
			root = stack.pop()
			k -= 1
			if not k:
				return root.val
			root = root.right

class TestSolution(unittest.TestCase):
	def test_1(self):
		tree_arg = TreeNode.stringToTreeNode('[3,1,4,null,2]')
		self.assertEqual(Solution().kth_smallest(tree_arg, 1), 1)

	def test_2(self):
		tree_arg = TreeNode.stringToTreeNode('[5,3,6,2,4,null,null,1]')
		self.assertEqual(Solution().kth_smallest(tree_arg, 3), 3)

	def test_3(self):
		tree_arg = TreeNode.stringToTreeNode('[5,3,6,2,4,null,null,1]')
		self.assertEqual(Solution().kth_smallest(tree_arg, 4), 4)
	
	def test_1_inorder_stack(self):
		tree_arg = TreeNode.stringToTreeNode('[3,1,4,null,2]')
		self.assertEqual(Solution().kth_smallest_inorder_stack(tree_arg, 1), 1)

	def test_2_inorder_stack(self):
		tree_arg = TreeNode.stringToTreeNode('[5,3,6,2,4,null,null,1]')
		self.assertEqual(Solution().kth_smallest_inorder_stack(tree_arg, 3), 3)

	def test_3_inorder_stack(self):
		tree_arg = TreeNode.stringToTreeNode('[5,3,6,2,4,null,null,1]')
		self.assertEqual(Solution().kth_smallest_inorder_stack(tree_arg, 4), 4)


if __name__ == '__main__':
	unittest.main()
	