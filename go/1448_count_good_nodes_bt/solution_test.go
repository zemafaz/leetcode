package countgoodnodesbt

import (
	"leetcode-solutions/utils"
	"testing"
)

type args struct {
	root *utils.TreeNode
	output int
}

func TestSolution(t *testing.T) {
	argsTest := []args{
		{
			root: utils.StringToTreeNode("[3,1,4,3,null,1,5]"),
			output: 4,
		},
		{
			root: utils.StringToTreeNode("[3,3,null,4,2]"),
			output: 3,
		},
		{
			root: utils.StringToTreeNode("[1]"),
			output: 1,
		},
	}

	for i, test := range argsTest {
		res := goodNodes(test.root)
		if res != test.output {
			t.Errorf("Failed test %d: expected %v, returned %v", i+1, test.output, res)
		}
	}
}
