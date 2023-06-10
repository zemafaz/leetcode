package main

import (
	"fmt"
)

type test struct {
    n int
    index int
    maxSum int
    expectedResult int
}

func maxValue(n int, index int, maxSum int) int  {
    maxSum -= n
    var left int = 0
    var right int = maxSum

    var check func(int) int = func (a int) int {
        var b int;
        if a - index < 0 {
            b = 0
        } else {
            b = a - index
        }
        var res int = (a + b) * (a - b + 1) / 2
        if a - ((n - 1) - index) < 0 {
            b = 0
        } else {
            b = a - ((n - 1) - index)
        }
        res += (a + b) * (a - b + 1) / 2
        return res - a
    }

    for left < right {
        var mid int = (left + right + 1) / 2
        if check(mid) <= maxSum {
            left = mid
        } else {
            right = mid - 1
        }
    }
    return left + 1
}

func main() {
    function := maxValue
    tests := map[string]test{
        "test 1": {
            n: 4,
            index: 2,
            maxSum: 6,
            expectedResult: 2,
        },
        "test 2": {
            n: 6,
            index: 1,
            maxSum: 10,
            expectedResult: 3,
        },
    }

    failed := false
    for test_name, test := range tests {
        res := function(test.n, test.index, test.maxSum)
        if res != test.expectedResult {
            fmt.Printf("Failed %s: expected %d, returned %d\n", test_name, test.expectedResult, res)
            failed = true
        }
    }
    if !failed {
        fmt.Print("Passed all tests")
    }
}
