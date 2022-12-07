package maximumlengthrepeatedsubarray

import (
	"testing"
	"leetcode-solutions/utils"
)

type args struct {
	nums1 []int
	nums2 []int
	output int
}

func TestSolution(t *testing.T) {
	argsTest := []args{
		{
			nums1: []int{1,2,3,2,1},
			nums2: []int{3,2,1,4,7},
			output: 3,
		},
		{
			nums1: []int{0,0,0,0,0},
			nums2: []int{0,0,0,0,0},
			output: 5,
		},
	}
	for i, test := range argsTest {
		res := findLength(test.nums1, test.nums2)
		if res != test.output {
			utils.GenTestErrorMessage(t, i+1, test.output, res)
		}
	}
}
