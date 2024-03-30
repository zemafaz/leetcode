package main

import (
	"fmt"
	"sort"
)

type test struct {
    pairs [][]int
    output int
}

func findLongestChain(pairs [][]int) int {
    dp := make([]int, len(pairs))

    max := 0
    for i := range pairs {
        if dp[i] == 0 {
            depthSearch(i, pairs, dp)
        }
        if dp[i] > max {
            max = dp[i]
        }
    }
    return max
}

func depthSearch(i int, pairs [][]int, dp []int) {
    max := 0
    for j := range pairs {
        if i == j {
            continue
        }
        if pairs[i][1] < pairs[j][0] {
            if dp[j] != 0 && dp[j] > max {
                max = dp[j]
                continue
            }
            depthSearch(j, pairs, dp)
            if dp[j] > max {
                max = dp[j]
            }
        }
    }
    dp[i] = max + 1
}

func findLongestChainGreedy(pairs [][]int) int {
    sort.Slice(pairs, func(i, j int) bool {
        return pairs[i][1] < pairs[j][0]
    })
    res := 0
    curr := -1001
    for i := range pairs {
        if curr < pairs[i][0] {
            curr = pairs[i][1]
            res += 1
        }
    }
    return res
}

func main() {
    functions := map[string]func([][]int) int{
        "DP function": findLongestChain,
        "Greedy function": findLongestChainGreedy,
    }
    tests := []test{
        {
            [][]int{{1,2},{2,3},{3,4}},
            2,
        },
        {
            [][]int{{1,2},{7,8},{4,5}},
            3,
        },
    }

    failed := false
    for _, t := range tests {
        for k, f := range functions {
            res := f(t.pairs)
            if res != t.output {
                fmt.Printf("%s: Return %d, Expected %d\n", k, res, t.output)
                failed = true
            }
        }
    }
    if !failed {
        fmt.Println("Passed all tests")
    }
}
