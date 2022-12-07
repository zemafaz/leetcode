package rotateimage

import "testing"

type args struct {
	matrix [][]int
	output [][]int
}

func TestSolution(t *testing.T) {
	argsTest := []args {
		{
			matrix: [][]int {
				{1,2,3},
				{4,5,6},
				{7,8,9},
			},
			output: [][]int {
				{7,4,1},
				{8,5,2},
				{9,6,3},
			},
		},
		{
			matrix: [][]int {
				{5,1,9,11},
				{2,4,8,10},
				{13,3,6,7},
				{15,14,12,16},
			},
			output: [][]int {
				{15,13,2,5},
				{14,3,4,1},
				{12,6,8,9},
				{16,7,10,11},
			},
		},
	}
	for k, test := range argsTest {
		rotate(test.matrix)
		Loop:
		for i, row := range test.output {
			for j := range row {
				if test.matrix[i][j] != test.output[i][j] {
					t.Errorf("Failed test %d: expected %v, returned %v", k+1, test.output, test.matrix)
					break Loop
				}
			}
		}
	}
}
