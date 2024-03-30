package toeplitzmatrix

import (
	"testing"
	"leetcode-solutions/utils"
)

type args struct {
	matrix [][]int
	output bool
}

func TestSolution(t *testing.T) {
	testArgs := []args {
		{
			matrix: [][]int{{1,2,3,4},{5,1,2,3},{9,5,1,2}},
			output: true,
		},
		{
			matrix: [][]int{{1,2},{2,2}},
			output: false,
		},
	}

	for i, test := range testArgs {
		res := isToeplitzMatrix(test.matrix)
		if res != test.output {
			utils.GenTestErrorMessage(t, i+1, test.output, res)
		}
	}
}
