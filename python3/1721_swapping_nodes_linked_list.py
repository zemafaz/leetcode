import unittest
from list_node import ListNode

def swap_nodes(head: ListNode, k: int) -> ListNode:
    current_node = head
    previous_node = None
    for _ in range(k-1):
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
    
    to_swap = current_node.val
    current_node.val = 101

    while current_node is not None:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
    
    current_node = previous_node
    previous_node = None

    for _ in range(k-1):
        if current_node.val == 101:
            current_node.val, to_swap = to_swap, current_node.val
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node

    current_node.val, to_swap = to_swap, current_node.val

    while current_node is not None:
        if current_node.val == 101:
            current_node.val, to_swap = to_swap, current_node.val
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node

    return previous_node


class TestSolution(unittest.TestCase):

    def test_1(self):
        head = ListNode.list_to_list_node([1,2,3,4,5])
        k = 2
        output = ListNode.list_to_list_node([1,4,3,2,5])
        res = swap_nodes(head, k)
        self.assertEqual(res, output)

    def test_2(self):
        head = ListNode.list_to_list_node([7,9,6,6,7,8,3,0,9,5])
        k = 5
        output = ListNode.list_to_list_node([7,9,6,6,8,7,3,0,9,5])
        res = swap_nodes(head, k)
        self.assertEqual(res, output)

if __name__ == '__main__':
    unittest.main()
