import unittest
from math import inf
from tree_node import TreeNode

class Solution:

    def max_ancestor_diff(self, root: TreeNode|None, curMin: float = inf, curMax: float = -inf) -> int:
        if not root: return int(curMax - curMin)

        curMin = min(curMin, root.val)
        curMax = max(curMax, root.val)

        return max(self.max_ancestor_diff(root.left, curMin, curMax),
                self.max_ancestor_diff(root.right, curMin, curMax))

class TestSolution(unittest.TestCase):

    def test_1(self):
        root: TreeNode = TreeNode.stringToTreeNode("[8,3,10,1,6,null,14,null,null,4,7,13]")
        output: int = 7
        self.assertEqual(Solution().max_ancestor_diff(root), output)

    def test_2(self):
        root: TreeNode = TreeNode.stringToTreeNode("[1,null,2,null,0,3]")
        output: int = 3
        self.assertEqual(Solution().max_ancestor_diff(root), output)

if __name__ == "__main__":
    unittest.main()
