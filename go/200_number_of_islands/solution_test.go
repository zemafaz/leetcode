package numberofislands

import "testing"

type args struct {
	grid [][]byte
	output int
}

func TestSolution(t *testing.T) {
	argsTest := []args{
		{
			grid: [][]byte{
				{1,1,1,1,0},
				{1,1,0,1,0},
				{1,1,0,0,0},
				{0,0,0,0,0},
			},
			output: 1,
		},
		{
			grid: [][]byte{
				{1,1,0,0,0},
				{1,1,0,0,0},
				{0,0,1,0,0},
				{0,0,0,1,1},
			},
			output: 3,
		},
	}
	for i, test := range argsTest {
		res := numIslands(test.grid)
		if res != test.output {
			t.Errorf("Failed test %d: expected %v, returned %v", i+1, test.output, res)
		}
	}
}
