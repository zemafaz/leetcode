import unittest
from tree_node import TreeNode

class Solution:
    def right_side_view(self, root: TreeNode) -> list[int]:
        res = []

        def aux(node: TreeNode):
            if node == None: return
            res.append(node.val)
            if node.right != None:
                aux(node.right)
            elif node.left != None:
                aux(node.left)
        
        aux(root)
        return res
    
    def right_side_view_rec(self, root:TreeNode) -> list[int]:
        if root == None:
            return []
        if root.right != None:
            return [root.val] + self.right_side_view_rec(root.right)
        elif root.left != None:
            return [root.val] + self.right_side_view_rec(root.left)
        else:
            return [root.val] + []

class TestSolution(unittest.TestCase):
    def test_1(self):
        root = TreeNode.stringToTreeNode("[1,2,3,null,5,null,4]")
        self.assertEqual(Solution().right_side_view(root), [1,3,4])
    
    def test_2(self):
        root = TreeNode.stringToTreeNode("[1,null,3]")
        self.assertEqual(Solution().right_side_view(root), [1,3])
    
    def test_3(self):
        root = TreeNode.stringToTreeNode("[]")
        self.assertEqual(Solution().right_side_view(root), [])

    def test_1_rec(self):
        root = TreeNode.stringToTreeNode("[1,2,3,null,5,null,4]")
        self.assertEqual(Solution().right_side_view_rec(root), [1,3,4])
    
    def test_2_rec(self):
        root = TreeNode.stringToTreeNode("[1,null,3]")
        self.assertEqual(Solution().right_side_view_rec(root), [1,3])
    
    def test_3_rec(self):
        root = TreeNode.stringToTreeNode("[]")
        self.assertEqual(Solution().right_side_view_rec(root), [])

if __name__ == '__main__':
    unittest.main()