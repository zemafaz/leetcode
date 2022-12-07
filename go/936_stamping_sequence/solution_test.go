package stampingsequence

import (
	"reflect"
	"testing"
)

type args struct {
    stamp string
    target string
    output []int
}

func TestSolution(t *testing.T) {
    testArgs := []args {
        {
            stamp: "abc",
            target: "ababc",
            output: []int{0,2},
        },
        {
            stamp: "abca",
            target: "aabcaca",
            output: []int{3,0,1},
        },
    }
    for i, test := range testArgs {
        res := movesToStamp(test.stamp,test.target)
        if !reflect.DeepEqual(res, test.output){
            t.Fatalf("Failed test %d: wanted %v, returned %v", i+1, test.output, res)
        }
    }
}
