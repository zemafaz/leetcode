import unittest
from tree_node import TreeNode

class Solution:
    def level_order(self, root: TreeNode) -> list[list[int]]:
        if not root: return []

        queue = [[root]]
        res = [[root.val]]        
        i = 0
        added = False

        while i != len(queue):
            for j in range(len(queue[i])):
                node = queue[i][j]
                if node.left != None or node.right != None and added == False:
                    queue.append([])
                    res.append([])
                    added = True
                if node.left != None:
                    queue[i+1].append(node.left)
                    res[i+1].append(node.left.val)
                if node.right != None:
                    queue[i+1].append(node.right)
                    res[i+1].append(node.right.val)
            i += 1
            added = False
        return res

class TestSolution(unittest.TestCase):
    def test_1(self):
        root = TreeNode.stringToTreeNode('[3,9,20,null,null,15,7]')
        self.assertEqual(Solution().level_order(root), [[3],[9,20],[15,7]])

    def test_2(self):
        root = TreeNode.stringToTreeNode('[1]')
        self.assertEqual(Solution().level_order(root), [[1]])
        
    def test_3(self):
        root = TreeNode.stringToTreeNode('[]')
        self.assertEqual(Solution().level_order(root), [])

if __name__ == '__main__':
    unittest.main() 