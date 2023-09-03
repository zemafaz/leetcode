package main

import (
	"fmt"
)

type arg struct {
    m int;
    n int;
    output int;
}

func printDP(i int, j int, dp [][]int) {
    fmt.Printf("Pos: (%d, %d), DP:\n", j, i)
    for i := range dp[0] {
        for j := range dp {
                fmt.Printf("\t%d ", dp[j][i])
        }
        fmt.Print("\n\n")
    }
}

func uniquePathsDP(m int, n int) int {
    dp := make([][]int, n)

    for i := range dp {
        dp[i] = make([]int, m)
        for j := range dp[i] {
            if i == 0 || j == 0{
                dp[i][j] = 1
            } else {
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            }
        }
    }

    return dp[n-1][m-1]
}

func uniquePathsMath(m int, n int) int {
    return factorial(m+n-2)/(factorial(m-1)*factorial(n-1))
}

func factorial(m int) int {
    res := 1
    for i:=1; i<=m ; i++{
        res *= i
    }
    return res
}

func main() {
    testFunc := []func(int, int) int {
        uniquePathsMath,
        uniquePathsDP,
    }
    testArgs := []arg{
        {
            3,
            7,
            28,
        },
        {
            3,
            2,
            3,
        },
    }

    failed := false

    for j, function := range testFunc {
        for i, test := range testArgs {
            res := function(test.m, test.n)
            if res != test.output {
                fmt.Printf("Failed function %d, test %d: expected %d, returned %d\n", j + 1, i + 1, test.output, res)
                failed = true
            }
        }
    }

    if !failed {
        fmt.Printf("Passed all tests!\n")
    }
}
