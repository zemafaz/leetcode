package poweroffour

import "testing"

type args struct {
    n int
    output bool
}

func TestSolution(t *testing.T) {
    testArgs := []args{
        {
            n: 16,
            output: true,
        },
        {
            n: 5,
            output: false,
        },
        {
            n: 16,
            output: true,
        },
    }

    for i, test := range testArgs {
        res := isPowerOfFour(test.n)
        if res != test.output {
            t.Errorf("Failed test %d: expected %v, returned %v", i+1, test.output, res)
        }
    }
}
