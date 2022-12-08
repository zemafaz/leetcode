import unittest
from tree_node import TreeNode

class Solution:

    def leaf_similar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.findLeaf(root1) == self.findLeaf(root2)

    def findLeaf(self, root: TreeNode|None) -> list[int]:
        if not root: return []
        if not root.left and not root.right: return [root.val]
        return self.findLeaf(root.left) + self.findLeaf(root.right)

class TestSolution(unittest.TestCase):
    
    def test_1(self):
        root1 = TreeNode.stringToTreeNode("[3,5,1,6,2,9,8,null,null,7,4]")
        root2 = TreeNode.stringToTreeNode("[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]")
        output = True
        self.assertEqual(Solution().leaf_similar(root1, root2), output)
    
    def test_2(self):
        root1 = TreeNode.stringToTreeNode("[1,2,3]")
        root2 = TreeNode.stringToTreeNode("[1,3,2]")
        output = False
        self.assertEqual(Solution().leaf_similar(root1, root2), output)

if __name__ == "__main__":
    unittest.main()
