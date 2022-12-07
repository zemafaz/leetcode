import unittest
from tree_node import TreeNode

class Solution:
    def lowest_common_ancestor(self, root: TreeNode, p: int, q: int) -> int:
        def aux(node: TreeNode, val: int) -> list[int]:
            if node.val == val:
                return [val]
            if val < node.val:
                return [node.val] + aux(node.left, val)
            else:
                return [node.val] + aux(node.right, val)
        p_path = aux(root, p)
        q_path = aux(root, q)
        
        ancestor = p_path[0]
        for i in range(min(len(p_path), len(p_path))):
            if p_path[i] != q_path[i]:
                break
            ancestor = p_path[i]
        return ancestor

    def lowest_common_ancestor_sane(self, root: TreeNode, p:int, q:int) -> int:
        if p < root.val > q:
            return self.lowest_common_ancestor_sane(root.left, p, q)
        if p > root.val < q:
            return self.lowest_common_ancestor_sane(root.right, p, q)
        return root.val

    def lowest_common_ancestor_iter(self, root: TreeNode, p:int, q:int) -> int:
        while (root.val-p) * (root.val-q) > 0:
            root = (root.left, root.right)[p > root.val]
        return root.val

class TestSolution(unittest.TestCase):
    def test1(self):
        root = TreeNode.stringToTreeNode("[6,2,8,0,4,7,9,null,null,3,5]")
        p = 2
        q = 8
        output = 6
        self.assertEqual(Solution().lowest_common_ancestor(root, p, q), output)

    def test2(self):
        root = TreeNode.stringToTreeNode("[6,2,8,0,4,7,9,null,null,3,5]")
        p = 2
        q = 4
        output = 2
        self.assertEqual(Solution().lowest_common_ancestor(root, p, q), output)

    def test3(self):
        root = TreeNode.stringToTreeNode("[2,1]")
        p = 2
        q = 1
        output = 2
        self.assertEqual(Solution().lowest_common_ancestor(root, p, q), output)

    def test1_sane(self):
        root = TreeNode.stringToTreeNode("[6,2,8,0,4,7,9,null,null,3,5]")
        p = 2
        q = 8
        output = 6
        self.assertEqual(Solution().lowest_common_ancestor_sane(root, p, q), output)

    def test2_sane(self):
        root = TreeNode.stringToTreeNode("[6,2,8,0,4,7,9,null,null,3,5]")
        p = 2
        q = 4
        output = 2
        self.assertEqual(Solution().lowest_common_ancestor_sane(root, p, q), output)

    def test3_sane(self):
        root = TreeNode.stringToTreeNode("[2,1]")
        p = 2
        q = 1
        output = 2
        self.assertEqual(Solution().lowest_common_ancestor_sane(root, p, q), output)

    def test1_iter(self):
        root = TreeNode.stringToTreeNode("[6,2,8,0,4,7,9,null,null,3,5]")
        p = 2
        q = 8
        output = 6
        self.assertEqual(Solution().lowest_common_ancestor_iter(root, p, q), output)

    def test2_iter(self):
        root = TreeNode.stringToTreeNode("[6,2,8,0,4,7,9,null,null,3,5]")
        p = 2
        q = 4
        output = 2
        self.assertEqual(Solution().lowest_common_ancestor_iter(root, p, q), output)

    def test3_iter(self):
        root = TreeNode.stringToTreeNode("[2,1]")
        p = 2
        q = 1
        output = 2
        self.assertEqual(Solution().lowest_common_ancestor_iter(root, p, q), output)

if __name__ == "__main__":
    unittest.main()
