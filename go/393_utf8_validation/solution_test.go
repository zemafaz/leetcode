package utf8validation

import (
	"testing"
	"leetcode-solutions/utils"
)

type args struct {
	data []int
	output bool
}

func TestSolution(t *testing.T) {
	testArgs := []args{
		{
			data: []int{197,130,1},
			output: true,
		},
		{
			data: []int{235,140,4},
			output: false,
		},
	}
	for i, test := range testArgs {
		res := validUtf8(test.data)
		if res != test.output {
			utils.GenTestErrorMessage(t, i+1, test.output, res)
		}
	}
}
