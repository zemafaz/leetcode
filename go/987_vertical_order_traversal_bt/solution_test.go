package verticalordertraversalbt

import (
	"leetcode-solutions/utils"
	"testing"
)

type args struct {
	root *utils.TreeNode
	output [][]int
}

func TestSolution(t *testing.T) {
	testArgs := []args{
		{
			root: utils.StringToTreeNode("[3,9,20,null,null,15,7]"),
			output: [][]int{{9},{3,15},{20},{7}},
		},
		{
			root: utils.StringToTreeNode("[1,2,3,4,5,6,7]"),
			output: [][]int{{4},{2},{1,5,6},{3},{7}},
		},
		{
			root: utils.StringToTreeNode("[1,2,3,4,6,5,7]"),
			output: [][]int{{4},{2},{1,5,6},{3},{7}},
		},
	}
	for k, test := range testArgs {
		res := verticalTraversal(test.root)
		if len(res) != len(test.output) {
			utils.GenTestErrorMessage(t, k+1, test.output, res)
		} else {
			for i := range res {
				if len(res[i]) != len(test.output[i]){
					utils.GenTestErrorMessage(t, k+1, test.output, res)
				} else {
					for j := range res[i] {
						if res[i][j] !=  test.output[i][j] {
							utils.GenTestErrorMessage(t, k+1, test.output, res)
						}
					}
				}
			}
		}
	}
}
