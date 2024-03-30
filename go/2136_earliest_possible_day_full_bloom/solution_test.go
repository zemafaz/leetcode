package earliestpossibledayfullbloom

import (
	"testing"
	"leetcode-solutions/utils"
)

type args struct {
	plantTime []int
	growTime []int
	output int
}

func TestSolution(t *testing.T) {
	testArgs := []args{
		{
			plantTime: []int{1,4,3},
			growTime: []int{2,3,1},
			output: 9,
		},
		{
			plantTime: []int{1,2,3,2},
			growTime: []int{2,1,2,1},
			output: 9,
		},
		{
			plantTime: []int{1},
			growTime: []int{1},
			output: 2,
		},
	}

	for i, test := range testArgs {
		res := earliestFullBloom(test.plantTime, test.growTime)
		if res != test.output {
			utils.GenTestErrorMessage(t, i + 1, test.output, res)
		}
	}
}
