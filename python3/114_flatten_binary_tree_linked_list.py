import unittest
from tree_node import TreeNode

class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root: return
        if root.left:
            next = root.right
            root.right = root.left
            it = root.left
            while it.right:
                it = it.right
            it.right = next
            self.flatten(root.left)
            root.left = None
        if root.right:
            self.flatten(root.right)

class TestSolution(unittest.TestCase):
    def test_1(self):
        root = TreeNode.stringToTreeNode("[1,2,5,3,4,null,6]")
        Solution().flatten(root)
        output = TreeNode.stringToTreeNode("[1,null,2,null,3,null,4,null,5,null,6]")
        self.assertEqual(root, output)

    def test_2(self):
        root = TreeNode.stringToTreeNode("[]")
        Solution().flatten(root)
        output = TreeNode.stringToTreeNode("[]")
        self.assertEqual(root, output)

    def test_3(self):
        root = TreeNode.stringToTreeNode("[0]")
        Solution().flatten(root)
        output = TreeNode.stringToTreeNode("[0]")
        self.assertEqual(root, output)

if __name__ == '__main__':
    unittest.main()
