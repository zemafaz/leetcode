package besttimebuysellstock4

import (
	"testing"
	"leetcode-solutions/utils"
)

type args struct {
	k int
	prices []int
	output int
}

func TestSolution(t *testing.T) {
	testArgs := []args {
		{
			k: 2,
			prices: []int{2,4,1},
			output: 2,
		},
		{
			k: 2,
			prices: []int{3,2,6,5,0,3},
			output: 7,
		},
	}
	for i, test := range testArgs {
		res := maxProfit(test.k, test.prices)
		if res != test.output {
			utils.GenTestErrorMessage(t, i+1, test.output, res)
		}
	}
}
