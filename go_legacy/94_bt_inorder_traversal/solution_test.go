package btinordertraversal

import (
	"leetcode-solutions/utils"
	"testing"
)

type args struct {
	root *utils.TreeNode
	output []int
}

func TestSolution(t *testing.T) {
	testArgs := []args {
		{
			root: utils.StringToTreeNode("[1,null,2,3]"),
			output: []int{1,3,2},
		},
		{
			root: utils.StringToTreeNode("[]"),
			output: []int{},
		},
		{
			root: utils.StringToTreeNode("[1]"),
			output: []int{1},
		},
	}
	for k, test := range testArgs {
		res := inorderTraversal(test.root)
		if len(res) != len(test.output) {
			utils.GenTestErrorMessage(t, k+1, test.output, res)
		} else {
			for i := range res {
				if res[i] != test.output[i] {
					utils.GenTestErrorMessage(t, k+1, test.output, res)
				}
			}
		}
	}
}
