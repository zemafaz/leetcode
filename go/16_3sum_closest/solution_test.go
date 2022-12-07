package threesumclosest

import (
	"testing"
	"leetcode-solutions/utils"
)

type args struct {
	nums []int
	target int
	output int
}

func TestSolution(t *testing.T) {
	testArgs := []args {
		{
			nums: []int{-1,2,1,-4},
			target: 1,
			output: 2,
		},
		{
			nums: []int{0,0,0},
			target: 1,
			output: 0,
		},
	}
	
	for i, test := range testArgs {
		res := threeSumClosest(test.nums, test.target)
		if res != test.output {
			utils.GenTestErrorMessage(t, i+1, test.output, res)
		}
	}
}

func TestSolutionEfficient(t *testing.T) {
	testArgs := []args {
		{
			nums: []int{-1,2,1,-4},
			target: 1,
			output: 2,
		},
		{
			nums: []int{0,0,0},
			target: 1,
			output: 0,
		},
	}
	
	for i, test := range testArgs {
		res := threeSumClosestEfficient(test.nums, test.target)
		if res != test.output {
			utils.GenTestErrorMessage(t, i+1, test.output, res)
		}
	}
}
