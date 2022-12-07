package minimumgenericmutation

import (
	"testing"
	"leetcode-solutions/utils"
)

type args struct {
	start string
	end string
	bank []string
	output int
}

func TestSolution(t *testing.T) {
	testArgs := []args {
		{
			start: "AACCGGTT",
			end: "AACCGGTA",
			bank: []string{"AACCGGTA"},
			output: 1,
		},
		{
			start: "AACCGGTT",
			end: "AAACGGTA",
			bank: []string{"AACCGGTA","AACCGCTA","AAACGGTA"},
			output: 2,
		},
		{
			start: "AAAAACCC",
			end: "AACCCCCC",
			bank: []string{"AAAACCCC","AAACCCCC","AACCCCCC"},
			output: 3,
		},
	}

	for i, test := range testArgs {
		res := minMutation(test.start, test.end, test.bank)
		if res != test.output {
			utils.GenTestErrorMessage(t, i+1, test.output, res)
		}
	}
}
