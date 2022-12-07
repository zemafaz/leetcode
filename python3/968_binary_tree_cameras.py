import unittest
from tree_node import TreeNode

class Solution:
	def min_camera_cover(self, root: TreeNode) -> int:
		self.res = 0
		'''
		0 - it's a leaf
		1 - it's a parent of a leaf, with a camera in this node
		2 - it's covered, withou camera on node
		'''
		def dfs(root):
			if not root: return 2
			l, r = dfs(root.left), dfs(root.right)
			if l == 0 or r == 0:
				self. res += 1
				return 1
			return 2 if l == 1 or r == 1 else 0
		
		return (dfs(root) == 0) + self.res

class TestSolution(unittest.TestCase):
	def test_1(self):
		root = TreeNode.stringToTreeNode('[0,0,null,0,0]')
		self.assertEqual(Solution().min_camera_cover(root), 1)
	
	def test_2(self):
		root = TreeNode.stringToTreeNode('[0,0,null,0,null,0,null,null,0]')
		self.assertEqual(Solution().min_camera_cover(root), 2)

if __name__ == '__main__':
	unittest.main()
