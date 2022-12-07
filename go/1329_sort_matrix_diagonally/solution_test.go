package sortmatrixdiagonally

import "testing"

type args struct {
	mat [][]int
	output [][]int
}

func TestSolution(t *testing.T) {
	testArgs := []args {
		{
			mat: [][]int{
				{3,3,1,1},
				{2,2,1,2},
				{1,1,1,2},
			},
			output: [][]int{
				{1,1,1,1},
				{1,2,2,2},
				{1,2,3,3},
			},
		},
		{
			mat: [][]int{
				{11,25,66,1,69,7},
				{23,55,17,45,15,52},
				{75,31,36,44,58,8},
				{22,27,33,25,68,4},
				{84,28,14,11,5,50},
			},
			output: [][]int{
				{5,17,4,1,52,7},
				{11,11,25,45,8,69},
				{14,23,25,44,58,15},
				{22,27,31,36,50,66},
				{84,28,75,33,55,68},
			},
		},
	}
	for i, test := range testArgs {
		res := diagonalSort(test.mat)
		Loop:
		for j := range res {
			for k := range res[j] {
				if res[j][k] != test.output[j][k] {
					t.Errorf("Failed test %d: expected %v, returned %v", i+1, test.output, res)
					break Loop
				}
			}
		}
	}
}
