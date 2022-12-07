import unittest
from list_node import ListNode

class Solution:
    def reverse_between(self, head: ListNode, left: int, right: int) -> ListNode:
        if left >= right: return head
        i = 1
        node_left = ListNode(None,head)
        while i < left or not node_left:
            i += 1
            node_left = node_left.next
        
        node_right, node_previous = node_left.next, None
        node_begin = node_right

        while i < right or not node_right:
            aux = node_right.next
            node_right.next = node_previous
            node_previous = node_right
            node_right = aux
            i += 1
            
        node_begin.next = node_right
        node_left.next = node_previous

        return head


class TestSolution(unittest.TestCase):
    def test_1(self):
        head, left, right = ListNode.list_to_list_node([1,2,3,4,5]), 2, 5
        self.assertEqual(Solution().reverse_between(head, left, right), ListNode.list_to_list_node([1,4,3,2,5]))
    
    def test_2(self):
        head, left, right = ListNode.list_to_list_node([5]), 1, 1
        self.assertEqual(Solution().reverse_between(head, left, right), ListNode.list_to_list_node([5]))
    
if __name__ == '__main__':
    unittest.main()