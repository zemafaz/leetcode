package binarytreepruning

import (
	"leetcode-solutions/utils"
	"testing"
)

type args struct {
	root *utils.TreeNode
	output *utils.TreeNode
}

func TestSolution(t *testing.T) {
	testArgs := []args{
		{
			root: utils.StringToTreeNode("[1,null,0,0,1]"),
			output: utils.StringToTreeNode("[1,null,0,null,1]"),
		},
		{
			root: utils.StringToTreeNode("[1,0,1,0,0,0,1]"),
			output: utils.StringToTreeNode("[1,null,1,null,1]"),
		},
		{
			root: utils.StringToTreeNode("[1,1,0,1,1,0,1,0]"),
			output: utils.StringToTreeNode("[1,1,0,1,1,null,1]"),
		},
	}

	for i, test := range testArgs {
		res := pruneTree(test.root)
		if !utils.TreeNodeEquals(res, test.output) {
			utils.GenTestErrorMessage(t, i+1, test.output, res)
		}
	}
}
