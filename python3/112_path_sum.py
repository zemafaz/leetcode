import unittest
from tree_node import TreeNode

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root: return False
        def aux(node: TreeNode, rem: int) -> bool:
            if not node:
                if rem == 0:
                    return True
                else:
                    return False
            if rem - node.val < 0:
                return False
            else:
                return aux(node.left, rem - node.val) or aux(node.right, rem - node.val)
        return aux(root, targetSum)

class TestSolution(unittest.TestCase):
    def test_1(self):
        root = TreeNode.stringToTreeNode("[5,4,8,11,null,13,4,7,2,null,null,null,1]")
        targetSum = 22
        output = True
        self.assertEqual(Solution().hasPathSum(root, targetSum), output)

    def test_2(self):
        root = TreeNode.stringToTreeNode("[1,2,3]")
        targetSum = 5
        output = False
        self.assertEqual(Solution().hasPathSum(root, targetSum), output)

    def test_3(self):
        root = TreeNode.stringToTreeNode("[]")
        targetSum = 0
        output = False
        self.assertEqual(Solution().hasPathSum(root, targetSum), output)

if __name__ == "__main__":
    unittest.main()
