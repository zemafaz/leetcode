from platform import node
import unittest

from tree_node import TreeNode

class Solution:
	def deepest_leaves_sum(self, root: TreeNode) -> int:
		q, ans, curr = [root], 0, 0
		while len(q):
			qlen, ans = len(q), 0
			for _ in range(qlen):
				curr = q.pop(0)
				ans += curr.val
				if curr.left: q.append(curr.left)
				if curr.right: q.append(curr.right)
		return ans

class TestSolution(unittest.TestCase):
	def test_1(self):
		root = TreeNode.stringToTreeNode("[1,2,3,4,5,null,6,7,null,null,null,null,8]")
		self.assertEqual(Solution().deepest_leaves_sum(root), 15)

	def test_2(self):
		root = TreeNode.stringToTreeNode("[6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]")
		self.assertEqual(Solution().deepest_leaves_sum(root), 19)

if __name__ == '__main__':
	unittest.main()