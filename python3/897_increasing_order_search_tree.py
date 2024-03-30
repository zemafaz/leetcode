import unittest
from tree_node import TreeNode


class Solution:
	def increasing_bst(self, root: TreeNode) -> TreeNode:
		self.list = []
		self.convert_to_list(root)
		self.list.sort()
		if len(self.list) == 0:
			return None
		else:
			new_root = TreeNode(self.list[0])
			root = new_root
			for e in self.list[1:]:
				root.right = TreeNode(e)
				root = root.right
			return new_root

	def convert_to_list(self, root):
		if (root != None):
			self.list.append(root.val)
			self.convert_to_list(root.left)
			self.convert_to_list(root.right)

		

class TestSolution(unittest.TestCase):
	def test_1(self):
		tree_arg = TreeNode.stringToTreeNode('[5,3,6,2,4,null,8,1,null,null,null,7,9]')
		tree_result = TreeNode.stringToTreeNode('[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]')
		self.assertEqual(Solution().increasing_bst(tree_arg), tree_result)
	
	def test_2(self):
		tree_arg = TreeNode.stringToTreeNode('[5,1,7]')
		tree_result = TreeNode.stringToTreeNode('[1,null,5,null,7]')
		self.assertEqual(Solution().increasing_bst(tree_arg), tree_result)
	
if __name__ == '__main__':
	unittest.main()