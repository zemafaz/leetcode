package averageoflevelsbt

import "leetcode-solutions/utils"

func averageOfLevels(root *utils.TreeNode) []float64 {
	if root == nil {
		return []float64{}
	}
	res := []float64{}
	current := []*utils.TreeNode{root}
	next := []*utils.TreeNode{}
	for len(current) != 0 {
		sum := 0
		for _, elem := range current {
			sum += elem.Val
			if elem.Left != nil {
				next = append(next, elem.Left)
			}
			if elem.Right != nil {
				next = append(next, elem.Right)
			}
		}
		res = append(res, float64(sum) / float64(len(current)))
		current = make([]*utils.TreeNode, len(next))
		copy(current, next)
		next = []*utils.TreeNode{}
	}
	return res
}
