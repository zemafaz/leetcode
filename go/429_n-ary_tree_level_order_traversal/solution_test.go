package narytreelevelordertraversal

import (
	"leetcode-solutions/utils"
	"testing"
)

type args struct {
	root *utils.Node
	output [][]int
}

func TestSolution(t *testing.T) {
	testArgs := []args {
		{
			root: utils.StringToNode("[1,null,3,2,4,null,5,6]"),
			output: [][]int{{1},{3,2,4},{5,6}},
		},
		{
			root: utils.StringToNode("[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]"),
			output: [][]int{{1},{2,3,4,5},{6,7,8,9,10},{11,12,13},{14}},
		},
	}
	for k, test := range testArgs {
		res := levelOrder(test.root)
		if len(res) != len(test.output) {
			utils.GenTestErrorMessage(t, k+1, test.output, res)
		} else {
			Loop:
			for i := range res {
				if len(res[i]) != len(test.output[i]) {
					utils.GenTestErrorMessage(t, k+1, test.output, res)
					break Loop
				} else {
					for j := range res[i] {
						if res[i][j] != test.output[i][j] {
							utils.GenTestErrorMessage(t, k+1, test.output, res)
						}
					}
				}
			}
		}
	}
}
