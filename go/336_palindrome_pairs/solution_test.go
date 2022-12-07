package palindromepairs

import (
	"leetcode-solutions/utils"
	"testing"
)

type args struct {
	words  []string
	output [][]int
}

func TestSolution(t *testing.T) {
	testArgs := []args{
		{
			words:  []string{"abcd", "dcba", "lls", "s", "sssll"},
			output: [][]int{{0, 1}, {1, 0}, {2, 4}, {3, 2}},
		},
		{
			words:  []string{"bat", "tab", "cat"},
			output: [][]int{{0, 1}, {1, 0}},
		},
		{
			words:  []string{"a", ""},
			output: [][]int{{0, 1}, {1, 0}},
		},
	}
	for k, test := range testArgs {
		res := palindromePairs(test.words)
		if len(res) != len(test.output) {
			utils.GenTestErrorMessage(t, k+1, test.output, res)
			break
		} else {
			Loop:
			for i := range res {
				if len(res[i]) != len(test.output[i]) {
					utils.GenTestErrorMessage(t, k+1, test.output, res)
					break
				} else {
					if !isInSlice(test.output, res[i]) {
						utils.GenTestErrorMessage(t, k+1, test.output, res)
						break Loop
					}
				}
			}
		}
	}
	for k, test := range testArgs {
		res := palindromePairsMoreEficient(test.words)
		if len(res) != len(test.output) {
			utils.GenTestErrorMessage(t, k+len(testArgs)+1,test.output, res)
			break
		} else {
			Loop2:
			for i := range res {
				if len(res[i]) != len(test.output[i]) {
					utils.GenTestErrorMessage(t, k+len(testArgs)+1,test.output, res)
					break
				} else {
					if !isInSlice(test.output, res[i]) {
						utils.GenTestErrorMessage(t, k+1, test.output, res)
						break Loop2
					}
				}
			}
		}
	}
}

func isInSlice(slice [][]int, elem []int) bool {
	for i := range slice {
		if slice[i][0] == elem[0] && slice[i][1] == elem[1] {
			return true
		}
	}
	return false
}
