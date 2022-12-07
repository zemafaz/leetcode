package numberweakcharactersingame

import (
	"leetcode-solutions/utils"
	"testing"
)

type args struct {
	properties [][]int
	output int
}

func TestSolution(t *testing.T) {
	testArgs := []args{
		{
			properties: [][]int{{5,5},{6,3},{3,6}},
			output: 0,
		},
		{
			properties: [][]int{{2,2},{3,3}},
			output: 1,
		},
		{
			properties: [][]int{{1,5},{10,4},{4,3}},
			output: 1,
		},
	}

	for k, test := range testArgs {
		res := numberOfWeakCharacters(test.properties)
		if res != test.output {
			utils.GenTestErrorMessage(t, k+1, test.output, res)
		}
	}
}
 
