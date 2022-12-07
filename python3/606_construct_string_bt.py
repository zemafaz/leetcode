import unittest
from tree_node import TreeNode

class Solution:

	def tree2str(self, root: TreeNode) -> str:
		tree_left = ""
		tree_right = ""
		
		if root.left == None and root.right != None:
			tree_left = '()'
		elif root.left != None:
			tree_left = '({})'.format(self.tree2str(root.left))
		
		if root.right != None:
			tree_right = '({})'.format(self.tree2str(root.right))

		return str(root.val) + tree_left + tree_right

class TestSolution(unittest.TestCase):
	def test_1(self):
		tree_arg = TreeNode.stringToTreeNode('[1,2,3,4]')
		self.assertEqual(Solution().tree2str(tree_arg), "1(2(4))(3)")
	
	def test_2(self):
		tree_arg = TreeNode.stringToTreeNode('[1,2,3,null,4]')
		self.assertEqual(Solution().tree2str(tree_arg), "1(2()(4))(3)")
	
if __name__ == '__main__':
	unittest.main()