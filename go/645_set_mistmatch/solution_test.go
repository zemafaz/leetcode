package setmistmatch

import (
	"testing"
	"leetcode-solutions/utils"
)

type args struct {
	nums []int
	output []int
}

func TestSolution(t *testing.T) {
	argsTest := []args {
		{
			nums: []int{1,2,2,4},
			output: []int{2,3},
		},
		{
			nums: []int{1,1},
			output: []int{1,2},
		},
	}

	for i, test := range argsTest {
		res := findErrorNums(test.nums)
		if len(res) != len(test.output) {
			utils.GenTestErrorMessage(t, i + 1, test.output, res)
			return
		}
		for j := range res {
			if res[j] != test.output[j] {
				utils.GenTestErrorMessage(t, i + 1, test.output, res)
				return
			}
		}
	}
}
