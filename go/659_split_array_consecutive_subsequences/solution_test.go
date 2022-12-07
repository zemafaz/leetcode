package splitarrayconsecutivesubsequences

import "testing"

type args struct {
    nums []int
    output bool
}

func TestSolution(t *testing.T) {
    testArgs := [3]args{
        {
            nums: []int{ 1,2,3,3,4,5 },
            output: true,
        },
        {
            nums: []int{ 1,2,3,3,4,4,5,5 },
            output: true,
        },
        {
            nums: []int{ 1,2,3,4,4,5 },
            output: false,
        },
    }

    for i, test := range testArgs {
        res := isPossible(test.nums) 
        if res != test.output {
            t.Errorf("Failed test %d: wanted %v, returned %v\n", i+1, test.output, res)
        }
    }
}
