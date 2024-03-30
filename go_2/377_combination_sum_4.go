package main

import (
	"fmt"
	"sort"
)

type args struct {
    nums []int;
    target int;
    output int;
}

func combinationSums4 (nums []int, target int) int {
    sort.Slice(nums, func(i, j int) bool {
        return nums[i] < nums[j]
    })
    return combinationSums4Rec(nums, target)
}

func combinationSums4Rec(nums []int, target int) int {
    if target == 0 {
        return 1
    }
    if target < 0 {
        return 0
    }
    total := 0
    for i := range nums {
        if nums[i] > target {
            break
        }
        total += combinationSums4Rec(nums, target - nums[i])
    }
    return total
}

func combinationSums4DP(nums []int, target int) int {
    dp := make([]int, target + 1)
    dp[0] = 1
    for t:=1; t < len(dp); t++ {
        for _, num := range nums {
            if num > t {
                continue
            }
            dp[t] += dp[t - num]
        }
    }
    return dp[len(dp) - 1]
}

func main() {
    testArgs := []args {
        {
            []int{1,2,3},
            4,
            7,
        },
        {
            []int{9},
            3,
            0,
        },
    }

    testFunc := map[string]func([]int, int)int{
        "combinationSums4Rec": combinationSums4,
        "combinationSums4DP": combinationSums4DP,
    }

    failed := false
    for i, test := range testArgs {
        for k, function := range testFunc {
            res := function(test.nums, test.target)
            if res != test.output {
                fmt.Printf("Failed function %s, test %d: expected %d, returned %d\n", k, i+1, test.output, res)
                failed = true
            }
        }
    }

    if !failed {
        fmt.Printf("Passed all tests!\n")
    }
}
