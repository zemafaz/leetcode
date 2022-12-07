package constructstringfrombt

import (
	"leetcode-solutions/utils"
	"testing"
)

type args struct {
	root *utils.TreeNode
	output string
}

func TestSolution(t *testing.T) {
	testArgs := []args {
		{
			root: utils.StringToTreeNode("[1,2,3,4]"),
			output: "1(2(4))(3)",
		},
		{
			root: utils.StringToTreeNode("[1,2,3,null,4]"),
			output: "1(2()(4))(3)",
		},
	}
	for i, test := range testArgs {
		res := tree2str(test.root)
		if res != test.output {
			utils.GenTestErrorMessage(t, i+1, test.output, res)
		}
	}
}
