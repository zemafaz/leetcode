package main

import "fmt"

type args struct {
    n int;
    output []int;
}

func countBits(n int) []int {
    res := make([]int,n+1)
    
    for i:=1 ; i<=n ; i++ {
        res[i] += i&1 + res[i>>1]
    }
    return res
}

func main() {
    testArgs := []args{
        {
            2,
            []int{0,1,1},
        },
        {
            5,
            []int{0,1,1,2,1,2},
        },
    }

    failed := false
    for i, test := range testArgs {
        res := countBits(test.n)
        if len(res) != len(test.output) {
            fmt.Printf("Failed test %d: expected %v, returned %v\n", i, test.output, res)
            failed = true
        } else {
            for j := range res {
                if test.output[j] != res[j]{
                    fmt.Printf("Failed test %d: expected %v, returned %v\n", i, test.output, res)
                    failed = true
                    break
                }
            }
        }
    }
    
    if !failed {
        fmt.Printf("Passed all tests!\n")
    }
}
