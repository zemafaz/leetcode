package trappingrainwater

import (
	"testing"
	"leetcode-solutions/utils"
)

type args struct {
	height []int
	output int
}

func TestSolution(t *testing.T) {
	testArgs := []args {
		{
			height: []int{0,1,0,2,1,0,1,3,2,1,2,1},
			output: 6,
		},
		{
			height: []int{4,2,0,3,2,5},
			output: 9,
		},
	}
	for i, test := range testArgs {
		res := trap(test.height)
		if res != test.output {
			utils.GenTestErrorMessage(t, i+1, test.output, res)
		}
	}
}
