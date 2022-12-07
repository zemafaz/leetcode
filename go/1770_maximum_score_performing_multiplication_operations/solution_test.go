package maximumscoreperformingmultiplicationoperations

import (
	"testing"
	"leetcode-solutions/utils"
)

type args struct {
	nums []int
	multipliers []int
	output int
}

func TestSolution(t *testing.T) {
	testArgs := []args {
		{
			nums: []int{1,2,3},
			multipliers: []int{3,2,1},
			output: 14,
		},
		{
			nums: []int{-5,-3,-3,-2,7,1},
			multipliers: []int{-10,-5,3,4,6},
			output: 102,
		},
	}
	for i, test := range testArgs {
		res := maximumScore(test.nums, test.multipliers)
		if res != test.output {
			utils.GenTestErrorMessage(t, i+1, test.output, res)
		}
	}
}
