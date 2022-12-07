import unittest
from tree_node import TreeNode

class Solution:
    def is_valid_bst(self, root: TreeNode) -> bool:
        if root != None:
            if root.left != None:
                if root.left.val >= root.val:
                    return False
            if root.right != None:
                if root.right.val <= root.val:
                    return False
            return self.is_valid_bst(root.left) and self.is_valid_bst(root.right)
        return True

class TestSolution(unittest.TestCase):
    def test_1(self):
        root = TreeNode.stringToTreeNode("[2,1,3]")
        output = True
        self.assertEqual(Solution().is_valid_bst(root), output)

    def test_2(self):
        root = TreeNode.stringToTreeNode("[5,1,4,null,null,3,6]")
        output = False
        self.assertEqual(Solution().is_valid_bst(root), output)

if __name__ == "__main__":
    unittest.main()
