package main

import "fmt"

type args struct{
    rec1 []int;
    rec2 []int;
    output bool;
}

func isRectangleOverlap(rec1 []int, rec2 []int) bool {
    return (
        (rec2[0] < rec1[0] && rec1[0] < rec2[2]) ||
            (rec1[0] < rec2[0] && rec2[0] < rec1[2]) &&
        (rec2[1] < rec1[1] && rec1[1] < rec2[3]) ||
            (rec1[1] < rec2[1] && rec2[1] < rec1[3]))
}

func main() {
    testArgs := []args{
        {
            []int{0,0,2,2},
            []int{1,1,3,3},
            true,
        },
        {
            []int{0,0,1,1},
            []int{1,0,2,1},
            false,
        },
        {
            []int{0,0,1,1},
            []int{2,2,3,3},
            false,
        },
    }

    failed := false
    for i, test := range testArgs {
        res := isRectangleOverlap(test.rec1, test.rec2)
        if res != test.output {
            fmt.Printf("Failed %d: expected %t, returned %t\n", i, test.output, res)
            failed = true
        }
    }
    if !failed {
        fmt.Printf("Passed all tests!\n")
    }
}
