package maxsumrectanglenolargerthank

import "testing"

type args struct {
	matrix [][]int
	k int
	output int
}

func TestSolution(t *testing.T) {
	testArgs := []args{
		{
			matrix: [][]int{
				{1,0,1},
				{0,-2,3},
			},
			k: 2,
			output: 2,
		},
		{
			matrix: [][]int{
				{2,2,-1},
			},
			k: 3,
			output: 3,
		},
	}

	for i, test := range testArgs {
		res := maxSumSubmatrix(test.matrix, test.k)
		if res != test.output {
			t.Errorf("Failed test %d: expected %v, returned %v", i+1, test.output, res)
		}
	}
}
