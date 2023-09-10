package main

import (
	"fmt"
	"math"
)

type args struct {
    n int;
    output int;
}

func countOrders(n int) int {
    count := 1
    for i:=1; i<=n; i++ {
        count *= (i * 2 - 1) * i % (int(math.Pow10(9)) + 7)
    }
    return count
}

func main() {
    testArgs := []args{
        {
            1,
            1,
        },
        {
            2,
            6,
        },
        {
            3,
            90,
        },
    }

    failed := false
    for i, test := range testArgs {
        res := countOrders(test.n)
        if res != test.output {
            fmt.Printf("Failed test %d: expected %d, returned %d\n", i+1, test.output, res)
            failed = true
        }
    }

    if !failed {
        fmt.Println("Passed all tests!")
    }
}
