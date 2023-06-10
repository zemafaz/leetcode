package powerofthree

import "testing"

type args struct {
    n int
    output bool
}

func TestSolution(t *testing.T) {
    testArgs := []args{
        {
            n: 27,
            output: true,
        },
        {
            n: 0,
            output: false,
        },
        {
            n: 9,
            output: true,
        },
        {
            n: 19683,
            output: true,
        },
    }
    for i, test := range testArgs {
        res := isPowerOfThree(test.n)
        if res != test.output {
            t.Fatalf("Failed test %d: expected %v, returned %v", i+1, test.output, res)
        }
    }
}
