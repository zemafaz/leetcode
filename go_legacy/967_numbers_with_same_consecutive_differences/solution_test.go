package numberswithsameconsecutivedifferences

import (
	"testing"
)

type args struct {
	n int
	k int
	output []int
}

func TestSolution(t *testing.T) {
	argsTest := []args{
		{
			n: 3,
			k: 7,
			output: []int{181,292,707,818,929},
		},
		{
			n: 2,
			k: 1,
			output: []int{10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98},
		},
	}
	for k, test := range argsTest {
		res := numsSameConsecDiff(test.n, test.k)
		if len(res) != len(test.output){
			t.Errorf("Failed test %d: expected %v, returned %v", k+1, test.output, res)
		} else {
			for i := range res {
				if res[i] != test.output[i] {
					t.Errorf("Failed test %d: expected %v, returned %v", k+1, test.output, res)
					break
				}
			}
		}
	}
}
