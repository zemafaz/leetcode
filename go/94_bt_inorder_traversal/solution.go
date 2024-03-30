package btinordertraversal

import "leetcode-solutions/utils"

func inorderTraversal(root *utils.TreeNode) []int {
	if root == nil {
		return []int{}
	}
	res := append(inorderTraversal(root.Left), root.Val)
	return append(res, inorderTraversal(root.Right)...)
}
