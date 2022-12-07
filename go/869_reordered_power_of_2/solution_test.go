package reorderedpowerof2

import "testing"

type args struct {
	n int
	output bool
}

func TestSolution(t *testing.T) {
	argsTest := []args{
		{
			n: 1,
			output: true,
		},
		{
			n: 10,
			output: false,
		},
		{
			n: 61,
			output: true,
		},
	}
	for i, test := range argsTest {
		res := reorderedPowerOf2(test.n)
		if res != test.output {
			t.Errorf("Failed test %d: expected %v, returned %v", i+1, test.output, res)
		}
	}
}
