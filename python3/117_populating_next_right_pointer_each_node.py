from tree_node import TreeNode

class Solution:
	def connect(self, root: TreeNode) -> TreeNode:
		node = root

		while node:
			curr = dummy = TreeNode()
			while node:
				if node.left:
					curr.next = node.left
					curr = curr.next
				if node.right:
					curr.next = node.right
					curr = curr.next
				node = node.next
			node = dummy.next
		return root

if __name__ == '__main__':
	root = TreeNode.stringToTreeNode('[1,2,3,4,5,null,7]')
	res = Solution().connect(root)