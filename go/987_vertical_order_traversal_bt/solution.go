package verticalordertraversalbt

import (
	"leetcode-solutions/utils"
	"sort"
)

func verticalTraversal(root *utils.TreeNode) [][]int{
	if root == nil {
		return [][]int{}
	}
	res := [][]int{{root.Val}}
	centerIndex := 0
	aux(root.Left, &res, &centerIndex, -1)
	aux(root.Right, &res, &centerIndex, 1)
	return res
}

func aux(node *utils.TreeNode, res *[][]int, center *int, index int) {
	if node == nil {
		return
	}
	if *center + index > len(*res) - 1 {
		*res = append(*res, []int{})
	}
	if *center + index < 0 {
		*res = append([][]int{{}}, *res...)
		*center++
	}
	i := sort.SearchInts((*res)[*center+index], node.Val)
	if len((*res)[*center+index]) == i {
		(*res)[*center+index] = append((*res)[*center+index], node.Val)
	} else {
		(*res)[*center+index] = append((*res)[*center+index][:i+1], (*res)[*center+index][i:]...)
		(*res)[*center+index][i] = node.Val
	}
	aux(node.Left, res, center, index - 1)
	aux(node.Right, res, center, index + 1)
}
