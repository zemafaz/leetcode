package concatenationconsecutivebinarynumbers

import (
	"testing"
	"leetcode-solutions/utils"
)

type args struct {
	n int
	output int
}

func TestSolution(t *testing.T) {
	testArgs := []args {
		{
			n: 1,
			output: 1,
		},
		{
			n: 3,
			output: 27,
		},
		{
			n: 12,
			output: 505379714,
		},
	}
	for i, test := range testArgs {
		res := concatenatedBinary(test.n)
		if res != test.output {
			utils.GenTestErrorMessage(t, i+1, test.output, res)
		}
	}
}
