import unittest
from tree_node import TreeNode

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def aux(node, seen: set[int]):
            if node == None:
                return False
            rem = k - node.val
            if rem in seen:
                return True
            seen.add(node.val)
            return aux(node.left, seen) or aux(node.right, seen)
        return aux(root, set())

class TestSolution(unittest.TestCase):

    def test_1(self):
        root = TreeNode.stringToTreeNode("[5,3,6,2,4,null,7]")
        k = 9
        output = True
        self.assertEqual(Solution().findTarget(root, k), output)

    def test_2(self):
        root = TreeNode.stringToTreeNode("[5,3,6,2,4,null,7]")
        k = 28
        output = False
        self.assertEqual(Solution().findTarget(root, k), output)

if __name__ == "__main__":
    unittest.main()
