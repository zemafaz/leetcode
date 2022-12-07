package integertoroman

import(
	"testing"
	"leetcode-solutions/utils"
)

type args struct {
	num int
	output string
}

func TestSolution(t *testing.T) {
	testArgs := []args {
		{
			num: 3,
			output: "III",
		},
		{
			num: 58,
			output: "LVIII",
		},
		{
			num: 1994,
			output: "MCMXCIV",
		},
	}
	for i, test := range testArgs {
		res := intToRoman(test.num)
		if res != test.output {
			utils.GenTestErrorMessage(t, i + 1, test.output, res)
		}
	}
}
