import unittest
from tree_node import TreeNode

'''
	Binary Search Tree: rooted binary tree whose internal nodes
	each store a value greater than all keys in left subtree and less
	than right subtree.
'''

class Solution:
	def search_bst(self, root: TreeNode, val: int) -> TreeNode:
		while root != None and root.val != val:

			if val < root.val:
				root = root.left
			elif val > root.val:
				root = root.right

		return root

class TestSolution(unittest.TestCase):
	def test_1(self):
		tree_param = TreeNode.stringToTreeNode('[4,2,7,1,3]')
		sol = Solution().search_bst(tree_param, 2)
		self.assertEqual(TreeNode.treeNodeToString(sol), '[2, 1, 3, null, null, null, null]')

	def test_2(self):
		tree_param = TreeNode.stringToTreeNode('[4,2,7,1,3]')
		sol = Solution().search_bst(tree_param, 5)
		self.assertEqual(TreeNode.treeNodeToString(sol), '[]')

if __name__ == '__main__':
	unittest.main()