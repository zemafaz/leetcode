package pseudopalindromicpathsbt

import (
	"testing"
	"leetcode-solutions/utils"
)

type args struct {
	root *utils.TreeNode
	output int
}

func TestSolution(t *testing.T) {
	testArgs := []args {
		{
			root: utils.StringToTreeNode("[2,3,1,3,1,null,1]"),
			output: 2,
		},
		{
			root: utils.StringToTreeNode("[2,1,1,1,3,null,null,null,null,null,1]"),
			output: 1,
		},
		{
			root: utils.StringToTreeNode("[9]"),
			output: 1,
		},
	}
	for i, test := range testArgs {
		res := pseudoPalindromicPaths(test.root)
		if res != test.output {
			utils.GenTestErrorMessage(t, i+1, test.output, res)
		}
	}
}
