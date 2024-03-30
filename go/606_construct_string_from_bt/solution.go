package constructstringfrombt

import (
	"leetcode-solutions/utils"
	"strconv"
)

func tree2str(root *utils.TreeNode) string {
	res := ""
	if root == nil {
		return res
	}
	res += strconv.Itoa(root.Val)
	if root.Left != nil || root.Right != nil {
		res += "(" + tree2str(root.Left) + ")"
		if root.Right != nil {
			res += "(" + tree2str(root.Right) + ")"
		}
	}
	return res
}
