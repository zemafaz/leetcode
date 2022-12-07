package palindromelinkedlist

import "leetcode-solutions/utils"

func isPalindrome(head *utils.ListNode) bool {
    fast, slow := head, head
    for fast != nil && fast.Next != nil{
        fast = fast.Next.Next
        slow = slow.Next
    }
    var prev *utils.ListNode
    for slow != nil {
        next := slow.Next
        slow.Next = prev
        prev = slow
        slow = next
    }
    for prev != nil{
        if prev.Val != head.Val {
            return false
        }
        prev = prev.Next
        head = head.Next
    }
    return true
}
