package countgoodnodesbt

import "leetcode-solutions/utils"

func goodNodes(root *utils.TreeNode) int {
	if root == nil {
		return 0
	}
	res := 1
	checkNode(root.Left, root.Val, &res)
	checkNode(root.Right, root.Val, &res)
	return res
}

func checkNode(node *utils.TreeNode, max int, total *int) {
	if node == nil {
		return
	}
	if node.Val <= max {
		*total++
	} else {
		max = node.Val
	}
	checkNode(node.Left, max, total)
	checkNode(node.Right, max, total)
}
