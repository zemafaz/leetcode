package pacificatlanticwaterflow

import "testing"

type args struct {
	height [][]int
	output [][]int
}

func TestSolution(t *testing.T) {
	argsTest := []args{
		{
			height: [][]int {
				{1,2,2,3,5},
				{3,2,3,4,4},
				{2,4,5,3,1},
				{6,7,1,4,5},
				{5,1,1,2,4},
			},
			output: [][]int {
				{0,4},
				{1,3},
				{1,4},
				{2,2},
				{3,0},
				{3,1},
				{4,0},
			},
		},
		{
			height: [][]int {
				{1},
			},
			output: [][]int {
				{0,0},
			},
		},
	}
	for k, test := range argsTest {
		res := pacificAtlantic(test.height)
		Loop:
		for i, row := range res {
			for j, elem := range row {
				if test.output[i][j] != elem {
					t.Errorf("Failed test %d: expected %v, returned %v", k+1, test.output, res)
					break Loop
				}
			}
		}
	}
}
