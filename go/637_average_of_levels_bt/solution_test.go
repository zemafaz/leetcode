package averageoflevelsbt

import (
	"testing"
	"leetcode-solutions/utils"
)

type args struct {
	root *utils.TreeNode
	output []float64
}	

func TestSolution(t *testing.T) {
	argsTest := []args {
		{
			root: utils.StringToTreeNode("[3,9,20,null,null,15,7]"),
			output: []float64{3,14.5,11},
		},
		{
			root: utils.StringToTreeNode("[3,9,20,15,7]"),
			output: []float64{3,14.5,11},
		},
	}
	for i, test := range argsTest {
		res := averageOfLevels(test.root)

		if len(res) != len(test.output) {
			t.Errorf("Failed test %d: expected %v, returned %v", i+1, test.output, res)
		}	
		for j := range res {
			if res[j] != test.output[j] {
				t.Errorf("Failed test %d: expected %v, returned %v", i+1, test.output, res)
			}
		}
	}
}
