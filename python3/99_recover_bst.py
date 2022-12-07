import unittest

from tree_node import TreeNode

class Solution:
	def recover_tree(self, root: TreeNode) -> None:
		cur, prev, drops, stack = root, TreeNode(float('-inf')), [], []
		
		while cur or stack:
			while cur:
				stack.append(cur)
				cur = cur.left
			node = stack.pop()
			if node.val < prev.val:
				drops.append((prev, node))
			prev, cur = node, node.right
		drops[0][0].val, drops[-1][1].val = drops[-1][1].val, drops[0][0].val

class TestSolution(unittest.TestCase):
	def test_1(self):
		tree_arg = TreeNode.stringToTreeNode('[1,3,null,null,2]')
		tree_res = TreeNode.stringToTreeNode('[3,1,null,null,2]')
		Solution().recover_tree(tree_arg)
		self.assertEqual(tree_arg, tree_res)
	
	def test_2(self):
		tree_arg = TreeNode.stringToTreeNode('[3,1,4,null,null,2]')
		tree_res = TreeNode.stringToTreeNode('[2,1,4,null,null,3]')
		Solution().recover_tree(tree_arg)
		self.assertEqual(tree_arg, tree_res)
		
if __name__ == '__main__':
	unittest.main()