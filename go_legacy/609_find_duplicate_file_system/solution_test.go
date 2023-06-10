package findduplicatefilesystem

import (
	"testing"
	"leetcode-solutions/utils"
)

type args struct {
	paths []string
	output [][]string
}

func TestSolution(t *testing.T) {
	testArgs := []args {
		{
			paths: []string{"root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"},
			output: [][]string{{"root/a/1.txt","root/c/3.txt"},{"root/a/2.txt","root/c/d/4.txt","root/4.txt"}},
		},
		{
			paths: []string{"root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"},
			output: [][]string{{"root/a/1.txt","root/c/3.txt"},{"root/a/2.txt","root/c/d/4.txt"}},
		},
	}
	for k, test := range testArgs {
		res := findDuplicate(test.paths)
		if len(res) != len(test.output) {
			utils.GenTestErrorMessage(t, k+1, test.output, res)
		} else {
			Loop:
			for i := range res {
				if len(res[i]) != len(test.output[i]) {
					utils.GenTestErrorMessage(t, k+1, test.output, res)
					break Loop
				} else {
					for j := range res[i] {
						if res[i][j] != test.output[i][j] {
							utils.GenTestErrorMessage(t, k+1, test.output, res)
							break Loop
						}
					}
				}

			}
		}
	}
}
