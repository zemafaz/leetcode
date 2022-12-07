package sumevennumbersafterqueries

import (
	"testing"
	"leetcode-solutions/utils"
)

type args struct {
	nums []int
	queries [][]int
	output []int
}

func TestSolution(t *testing.T) {
	argsTest := []args{
		{
			nums: []int{1,2,3,4},
			queries: [][]int{{1,0},{-3,1},{-4,0},{2,3}},
			output: []int{8,6,2,4},
		},
		{
			nums: []int{1},
			queries: [][]int{{4,0}},
			output: []int{0},
		},
	}
	for k, test := range argsTest {
		res := sumEvenAfterQueries(test.nums, test.queries)
		if len(res) != len(test.output) {
			utils.GenTestErrorMessage(t, k+1, test.output, res)
		} else {
			for i := range res {
				if res[i] != test.output[i] {
					utils.GenTestErrorMessage(t, k+1, test.output, res)
					break
				}
			}
		}
	}
}
