import unittest
from tree_node import TreeNode

class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth == 1:
            return TreeNode(val,left=root)
        queue = [[root]]
                
        depth_i = 1
        while depth_i + 1 != depth:
            node = queue[depth_i-1].pop(0)
            if node.left != None:
                if len(queue) <= depth_i:
                    queue.append([node.left])
                else:
                    queue[depth_i].append(node.left)
            if node.right != None:
                if len(queue) <= depth_i:
                    queue.append([node.right])
                else:
                    queue[depth_i].append(node.right)
            if queue[depth_i-1] == []:
                depth_i += 1
        for node in queue[-1]:
            node.left = TreeNode(val=val, left=node.left)
            node.right = TreeNode(val=val, right= node.right)
        return root

class TestSolution(unittest.TestCase):
    def test_1(self):
        root = TreeNode.stringToTreeNode("[4,2,6,3,1,5]")
        val = 1
        depth = 2
        output = TreeNode.stringToTreeNode("[4,1,1,2,null,null,6,3,1,5]")
        self.assertEqual(Solution().addOneRow(root, val, depth), output)

    def test_2(self):
        root = TreeNode.stringToTreeNode("[4,2,null,3,1]")
        val = 1
        depth = 3
        output = TreeNode.stringToTreeNode("[4,2,null,1,1,3,null,null,1]")
        self.assertEqual(Solution().addOneRow(root, val, depth), output)

if __name__ == "__main__":
    unittest.main()
