import unittest

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = None

    @staticmethod
    def treeNodeToString(root) -> str:
        if not root:
            return "[]"
        output = ""
        queue = [root]
        current = 0
        while current != len(queue):
            node = queue[current]
            current = current + 1

            if not node:
                output += "null, "
                continue

            output += str(node.val) + ", "
            queue.append(node.left)
            queue.append(node.right)
        return "[" + output[:-2] + "]"

    @staticmethod
    def stringToTreeNode(input: str):
        input = input.strip()
        input = input[1:-1]
        if not input:
            return TreeNode()

        inputValues = [s.strip() for s in input.split(',')]
        root = TreeNode(int(inputValues[0]))
        nodeQueue = [root]
        front = 0
        index = 1
        while index < len(inputValues):
            node = nodeQueue[front]
            front = front + 1

            item = inputValues[index]
            index = index + 1
            if item != "null":
                leftNumber = int(item)
                node.left = TreeNode(leftNumber)
                nodeQueue.append(node.left)

            if index >= len(inputValues):
                break

            item = inputValues[index]
            index = index + 1
            if item != "null":
                rightNumber = int(item)
                node.right = TreeNode(rightNumber)
                nodeQueue.append(node.right)
        return root

    def __eq__(self, other):
        if other != None:
            if self.val == other.val:
                return self.right == other.right and self.left == other.left
        return False

class TestSolution(unittest.TestCase):
    def test_eq1(self):
        t1 = TreeNode.stringToTreeNode('[2,1,3]')
        t2 = TreeNode.stringToTreeNode('[2,1,3]')
        self.assertEqual(t1 == t2, True)

    def test_eq2(self):
        t1 = TreeNode.stringToTreeNode('[2,1,3]')
        t2 = TreeNode.stringToTreeNode('[1,2,3]')
        self.assertEqual(t1 == t2, False)

if __name__ == '__main__':
    unittest.main()
