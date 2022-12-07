import unittest
from tree_node import TreeNode


class Solution:

	def __init__(self):
		self.total = 0

	def convert_bst(self, root: TreeNode) -> TreeNode:
		if root != None:
			self.convert_bst(root.right)
			self.total += root.val
			root.val = self.total
			self.convert_bst(root.left)
		return root
	
	def convert_bst_morris(self, root: TreeNode) -> TreeNode:
		# Get the node with the smallest value greater than this one.
		def get_successor(node):
				succ = node.right
				while succ.left != None and succ.left != node:
					succ = succ.left
				return succ
		
		total = 0
		node = root
		
		while node != None:
			# If there is no right subtree, then we can visit this node and
			# continue traversing left.
			if node.right == None:
				total += node.val
				node.val = total
				node = node.left

			# If there is a right subtree, then there is a node that has a
			# greater value than the current one. therefore, we must traverse
			# that node first.
			else:
				succ = get_successor(node)
				# If there is no left subtree (or right subtree, because we are
				# in this branch of control flow), make a temporary connection
				# back to the current node.
				if succ.left is None:
					succ.left = node
					node = node.right
				# If there is no left subtree (or right subtree, because we are
				# in this branch of control flow), make a temporary connection
				# back to the current node.
				else:
					succ.left = None
					total += node.val
					node.val = total
					node = node.left
		return root
	
	


	
class TestSolution(unittest.TestCase):
	def test_1(self):
		tree_arg = TreeNode.stringToTreeNode('[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]')
		tree_res = TreeNode.stringToTreeNode('[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]')
		self.assertEqual(Solution().convert_bst(tree_arg), tree_res)
	
	def test_2(self):
		tree_arg = TreeNode.stringToTreeNode('[0,null,1]')
		tree_res = TreeNode.stringToTreeNode('[1,null,1]')
		self.assertEqual(Solution().convert_bst(tree_arg), tree_res)

if __name__ == '__main__':
	unittest.main()