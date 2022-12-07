package maximumscoreperformingmultiplicationoperations

import "leetcode-solutions/utils"

func maximumScore(nums []int, multipliers []int) int {
	max := 0
	root := utils.TreeNode{
		Val: 0,
	}
	aux(&root, nums, multipliers, len(multipliers), &max)
	return max
}

func aux(node *utils.TreeNode, nums []int, multipliers []int, level int, max *int) {
	if level == 0 {
		if node.Val > *max {
			*max = node.Val
		}
		return
	}
	node.Left = &utils.TreeNode {
		Val: node.Val + multipliers[len(multipliers) - level] * nums[0],
	}
	node.Right = &utils.TreeNode {
		Val: node.Val + multipliers[len(multipliers) - level] * nums[len(nums)-1],
	}
	aux(node.Left, nums[1:], multipliers, level - 1, max)
	aux(node.Right, nums[:len(nums) - 1], multipliers, level - 1, max)
}
