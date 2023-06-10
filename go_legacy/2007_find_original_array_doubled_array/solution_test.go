package findoriginalarraydoubledarray

import (
	"testing"
	"leetcode-solutions/utils"
)

type args struct {
	changed []int
	output []int
}

func TestSolution(t *testing.T) {
	testArgs := []args{
		{
			changed: []int{1,3,4,2,6,8},
			output: []int{1,3,4},
		},
		{
			changed: []int{6,3,0,1},
			output: []int{},
		},
		{
			changed: []int{1},
			output: []int{},
		},
	}
	for k, test := range testArgs {
		res := findOriginalArray(test.changed)
		if len(res) != len(test.output) {
			utils.GenTestErrorMessage(t, k+1, test.output, res)
		} else {
			for i := range res {
				if res[i] != test.output[i] {
					utils.GenTestErrorMessage(t, k+1, test.output, res)
					break
				}
			}
		}
	}
}
