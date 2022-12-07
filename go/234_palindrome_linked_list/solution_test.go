package palindromelinkedlist

import (
	"leetcode-solutions/utils"
	"testing"
)

type args struct {
    head *utils.ListNode
    output bool
}

func TestSolution(t *testing.T) {
    argsTest := []args{
        {
            head: utils.ConvertToLinkedList([]int{1,2,2,1}),
            output: true,
        },
        {
            head: utils.ConvertToLinkedList([]int{1,2}),
            output: false,
        },
    }
    for i, test := range argsTest {
        res := isPalindrome(test.head)
        if res != test.output {
            t.Errorf("Failed test %d: expected %v, returned %v", i+1, test.output, res) 
        }
    }
}
