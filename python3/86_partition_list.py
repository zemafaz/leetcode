import unittest
from list_node import ListNode

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        iter = head
        last_in = ListNode(None, head)
        prev = last_in

        while iter:
            next = iter.next
            if iter.val < x:
                # Detach
                prev.next = next
                
                # Insert
                last_in_next = last_in.next
                last_in.next = iter
                iter.next = last_in_next
                last_in = iter
                if head.val >= x:
                    head = iter
            else:
                prev = iter
            iter = next
        return head

class TestSolution(unittest.TestCase):
    def test_1(self):
        head, x = ListNode.list_to_list_node([1,4,3,2,5,2]), 3
        output = ListNode.list_to_list_node([1,2,2,4,3,5])
        self.assertEqual(Solution().partition(head, x), output)

    def test_2(self):
        head, x = ListNode.list_to_list_node([2,1]), 2
        output = ListNode.list_to_list_node([1,2])
        self.assertEqual(Solution().partition(head, x), output)

if __name__ == "__main__":
    unittest.main()