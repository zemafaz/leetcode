package bagoftokens

import (
	"testing"
	"leetcode-solutions/utils"
)

type args struct {
	tokens []int
	power int
	output int
}

func TestSolution(t *testing.T) {
	testArgs := []args {
		{
			tokens: []int{100},
			power: 50,
			output: 0,
		},
		{
			tokens: []int{100,200},
			power: 150,
			output: 1,
		},
		{
			tokens: []int{100,200,300,400},
			power: 200,
			output: 2,
		},
	}
	for i, test := range testArgs {
		res := bagOfTokensScore(test.tokens, test.power)
		if res != test.output {
			utils.GenTestErrorMessage(t, i+1, test.output, res)
		}
	}
}
