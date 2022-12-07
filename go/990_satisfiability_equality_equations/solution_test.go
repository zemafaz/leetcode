package satisfiabilityequalityequations

import(
	"testing"
	"leetcode-solutions/utils"
)

type args struct {
	equations []string
	output bool
}

func TestSolution(t *testing.T) {
	testArgs := []args{
		{
			equations: []string{
				"a==b",
				"b!=a",
			},
			output: false,
		},
		{
			equations: []string{
				"b==a",
				"a==b",
			},
			output: true,
		},
	}
	for i, test := range testArgs {
		res := equationsPossible(test.equations)
		if res != test.output {
			utils.GenTestErrorMessage(t, i+1, test.output, res)
		}
	}
}
