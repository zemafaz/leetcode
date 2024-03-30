package main

import (
    "fmt";
)

type args struct {
    stones []int;
    output bool;
}

func jump(current_position int, current_jump int, stones []int) bool {
    if current_position == len(stones) - 1 {
        return true
    }
    can_jump := false
    for i := current_position + 1; i < len(stones); i++{
        next_jump := stones[i] - stones[current_position]
        if next_jump > current_position + 1 {
            break
        }
        if next_jump - current_position >= -1 {
            can_jump = can_jump || jump(
                i,
                next_jump,
                stones,
            )
        }
    }
    return can_jump
}


func canCross(stones []int) bool {
    return jump(0, 1, stones)
}

func main() {
    test_args := []args{
        {
            stones: []int{0,1,3,5,6,8,12,17},
            output: true,
        },
        {
            stones: []int{0,1,2,3,4,8,9,11},
            output: false,
        },
    }

    failed := false
    for i, test := range test_args {
        res := canCross(test.stones)
        if res != test.output {
            fmt.Printf("Failed test %d: Expected %t, returned %t\n", i + 1, test.output, res)
            failed = true
        }
    }
    if !failed {
        fmt.Print("Passed all tests!\n")
    }
}
