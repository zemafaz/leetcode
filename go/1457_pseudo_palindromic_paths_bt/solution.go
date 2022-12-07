package pseudopalindromicpathsbt

import "leetcode-solutions/utils"

func pseudoPalindromicPaths(root *utils.TreeNode) int {
	if root == nil {
		return 1
	}
	if root.Left == nil && root.Right == nil {
		return 1
	}
	count := [][]int{
		{root.Val, 1},
	}
	res := 0
	if root.Left != nil {
		aux(root.Left, count, &res)
	}
	if root.Right != nil {
		aux(root.Right, count, &res)
	}
	return res
}

func aux(node *utils.TreeNode, count [][]int, res *int) {
	for i := range count {
		if count[i][0] == node.Val {
			count[i][1]++
			goto FoundIt
		}
	}
	count = append(count, []int{node.Val,1})
	// if  _, exists := count[node.Val]; exists {
	// 	count[node.Val]++
	// } else {
	// 	count[node.Val] = 1
	// }
FoundIt:
	if node.Left == nil && node.Right == nil {
		impar := 0
		for i := range count {
			if count[i][1] % 2 == 1 {
				impar++
			}
		}
		if impar < 2 {
			*res++
		}
	}
	if node.Left != nil {
		aux(node.Left, count, res)
	}
	if node.Right != nil {
		aux(node.Right, count, res)
	}
}
