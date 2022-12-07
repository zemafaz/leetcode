import unittest
from tree_node import TreeNode

class Solution:
	def trim_bst(self, root: TreeNode, low: int, high: int) -> TreeNode:
		new_root = root

		while new_root != None:
			if low <= new_root.val <= high:
				break
			if new_root.val < low:
				new_root = new_root.right
			if new_root.val > high:
				new_root = new_root.left

		# Lower Bound
		it = new_root
		while it != None and (it.left != None or it.right != None):
			if it.left != None and it.left.val < low:
				if it.left.right != None and it.left.right.val >= low:
					it.left = it.left.right
					it = it.left
				else:
					it.left = None
					it = it.right
			else:
				it = it.left
		# Upper Bound
		it = new_root
		while it != None and (it.left != None or it.right != None):
			if it.right != None and it.right.val > high:
				if it.right.left != None and it.right.left.val <= high:
					it.right = it.right.left
					it = it.right
				else:
					it.right = None
					it = it.left
			else:
				it = it.right

		return new_root

	def trim_bst_rec(self, root: TreeNode, low: int, high: int) -> TreeNode:
		def trim(node):
			if not node:
				return None
			elif node.val > high:
				return trim(node.left)
			elif node.val < low:
				return trim(node.right)
			else:
				node.left = trim(node.left)
				node.right = trim(node.right)
				return node
		
		return trim(root)

class TestSolution(unittest.TestCase):
	def test_1(self):
		arg_tree = TreeNode.stringToTreeNode('[1,0,2]')
		res_tree = TreeNode.stringToTreeNode('[1,null,2]')
		self.assertEqual(Solution().trim_bst(arg_tree, 1, 2), res_tree)
	
	def test_2(self):
		arg_tree = TreeNode.stringToTreeNode('[3,0,4,null,2,null,null,1]')
		res_tree = TreeNode.stringToTreeNode('[3,2,null,1]')
		self.assertEqual(Solution().trim_bst(arg_tree, 1, 3), res_tree)

	def test_1_rec(self):
		arg_tree = TreeNode.stringToTreeNode('[1,0,2]')
		res_tree = TreeNode.stringToTreeNode('[1,null,2]')
		self.assertEqual(Solution().trim_bst_rec(arg_tree, 1, 2), res_tree)
	
	def test_2_rec(self):
		arg_tree = TreeNode.stringToTreeNode('[3,0,4,null,2,null,null,1]')
		res_tree = TreeNode.stringToTreeNode('[3,2,null,1]')
		self.assertEqual(Solution().trim_bst_rec(arg_tree, 1, 3), res_tree)


if __name__ == '__main__':
	unittest.main()
	