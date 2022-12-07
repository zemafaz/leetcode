import unittest
from tree_node import TreeNode

class Solution:
    def lowest_common_ancestor(self, root: TreeNode, p: int, q: int) -> int:
        def aux(node: TreeNode, path: list[int]):
            path = path + [node.val]
            if node.val == p:
                self.p_path = path 
            if node.val == q:
                self.q_path = path
            if self.p_path and self.q_path: return
            if node.left != None:
                aux(node.left, path)
            if node.right != None:
                aux(node.right, path)
        
        self.p_path = []
        self.q_path = []
        aux(root, [])

        for i in range(max(len(self.p_path), len(self.q_path))):
            if i == min(len(self.p_path), len(self.q_path)):
                return self.p_path[i-1]
            if self.q_path[i] != self.p_path[i]:
                return self.p_path[i-1] 
        return root.val
    
    def lowest_common_ancestor_alt(self, root: TreeNode, p: int, q: int) -> int:
        if not root: return None
        if root.val in (p, q): return root.val
        left, right = (self.lowest_common_ancestor_alt(kid, p, q) for kid in (root.left, root.right))
        return root.val if left and right else left or right

class TestSolution(unittest.TestCase):
    def test_1(self):
        root = TreeNode.stringToTreeNode("[3,5,1,6,2,0,8,null,null,7,4]")
        p = 5
        q = 1
        output = 3
        self.assertEqual(Solution().lowest_common_ancestor(root, p, q), output)

    def test_2(self):
        root = TreeNode.stringToTreeNode("[3,5,1,6,2,0,8,null,null,7,4]")
        p = 5
        q = 4
        output = 5
        self.assertEqual(Solution().lowest_common_ancestor(root, p, q), output)

    def test_1_alt(self):
        root = TreeNode.stringToTreeNode("[3,5,1,6,2,0,8,null,null,7,4]")
        p = 5
        q = 1
        output = 3
        self.assertEqual(Solution().lowest_common_ancestor_alt(root, p, q), output)

    def test_2_alt(self):
        root = TreeNode.stringToTreeNode("[3,5,1,6,2,0,8,null,null,7,4]")
        p = 5
        q = 4
        output = 5
        self.assertEqual(Solution().lowest_common_ancestor_alt(root, p, q), output)

if __name__ == "__main__":
    unittest.main()
