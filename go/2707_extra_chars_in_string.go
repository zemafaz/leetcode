package main

import (
	"fmt"
)

type args struct {
    s string;
    dictionary []string;
    output int;
}

type solution func(s string, dictionary []string) int

func minExtraChar(s string, dictionary []string) int {
    dp := make([]int, len(s) + 1)
    trie := make([]int, len(dictionary))

    for i := range dp {
        if i == 0 {
            dp[i] = 0
            continue
        }
        found := false
        for j := range trie {
            if dictionary[j][trie[j]] == s[i-1] {
                trie[j]++
                if trie[j] == len(dictionary[j]){
                    dp[i] = dp[i - len(dictionary[j])]
                    trie[j] = 0
                    found = true
                }
            } else {
                trie[j] = 0
            }
        }
        if !found {
            dp[i] = dp[i-1] + 1
        }
    }
    return dp[len(dp) - 1]
}

func main() {
    testArgs := []args{
        {
            "leetscode",
            []string{"leet", "code", "leetcode"},
            1,
        },
        {
            "sayhelloworld",
            []string{"hello", "world"},
            3,
        },
    }

    failed := false
    for i, test := range testArgs {
        res := minExtraChar(test.s, test.dictionary)
        if res != test.output {
            fmt.Printf("Failed test %d: expected %d, returned %d", i, test.output, res)
            failed = true
        }
    }

    if !failed {
        fmt.Printf("Passed all tests!")
    }
}
