import unittest
from list_node import ListNode

def swap_pairs(head: ListNode) -> ListNode:
    if head == None or head.next == None:
        return head
    new_head = head.next
    next_node = head.next.next
    head.next.next = head
    head.next = swap_pairs(next_node)
    return new_head

class TestSolution(unittest.TestCase):
    
    def test_1(self):
        head = ListNode.list_to_list_node([1,2,3,4])
        expected = ListNode.list_to_list_node([2,1,4,3])
        res = swap_pairs(head)
        self.assertEqual(res, expected)
        
    def test_2(self):
        head = ListNode.list_to_list_node([])
        expected = ListNode.list_to_list_node([])
        res = swap_pairs(head)
        self.assertEqual(res, expected)
        
    def test_3(self):
        head = ListNode.list_to_list_node([1])
        expected = ListNode.list_to_list_node([1])
        res = swap_pairs(head)
        self.assertEqual(res, expected)
        
if __name__ == '__main__':
    unittest.main()
