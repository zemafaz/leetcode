package reducearraysizehalf

import "testing"

type args struct{
    arr []int
    output int
}

func TestSolution(t *testing.T) { 
    testArgs := [2]args{
        {
            arr: []int{3,3,3,3,5,5,5,2,2,7},
            output: 2,
        },
        {
            arr: []int{7,7,7,7,7,7},
            output: 1,
        },
    }

    for _, test := range testArgs{
        res := minSetSize(test.arr) 
        if res != test.output {
            t.Error(res, test.output)
        }
    }
}
