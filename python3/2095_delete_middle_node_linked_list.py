import unittest
from list_node import ListNode

class Solution:

    def delete_middle(self, head: ListNode) -> ListNode:
        iter = head
        fast_iter = head
        previous = None

        while fast_iter != None and fast_iter.next != None:
            previous = iter
            iter = iter.next
            fast_iter = fast_iter.next.next
        
        if previous == None:
            return ListNode.list_to_list_node([])
        previous.next = iter.next
        return head

class TestSolution(unittest.TestCase):

    def test_1(self):
        head = ListNode.list_to_list_node([1,3,4,7,1,2,6])
        output = ListNode.list_to_list_node([1,3,4,1,2,6])
        self.assertEqual(Solution().delete_middle(head), output)

    def test_2(self):
        head = ListNode.list_to_list_node([1,3,4,7,1,2,6])
        output = ListNode.list_to_list_node([1,3,4,1,2,6])
        self.assertEqual(Solution().delete_middle(head), output)

    def test_3(self):
        head = ListNode.list_to_list_node([2,1])
        output = ListNode.list_to_list_node([2])
        self.assertEqual(Solution().delete_middle(head), output)

if __name__ == "__main__":
    unittest.main()
