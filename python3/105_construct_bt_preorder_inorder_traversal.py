import unittest
from tree_node import TreeNode

class Solution:
    def build_tree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        def aux(i: int, subtree: list):
            root = TreeNode(preorder[i])
            pos_s = subtree.index(preorder[i])
            if pos_s != 0:
                root.left = aux(i+1, subtree[:pos_s])
            if pos_s != len(subtree) - 1:
                root.right = aux(i+2, subtree[pos_s+1:])
            return root
        
        return aux(0, inorder)

class TestSolution(unittest.TestCase):
    def test_1(self):
        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]
        res = TreeNode.stringToTreeNode("[3,9,20,null,null,15,7]")
        self.assertEqual(Solution().build_tree(preorder, inorder), res)

    def test_2(self):
        preorder = [-1]
        inorder = [-1]
        res = TreeNode.stringToTreeNode("[-1]")
        self.assertEqual(Solution().build_tree(preorder, inorder), res)

if __name__ == '__main__':
    unittest.main()