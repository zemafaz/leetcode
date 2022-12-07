import unittest
from list_node import ListNode

class Solution:

    def __init__(self, head: list[int]):
        self.head: ListNode = ListNode.list_to_list_node(head)

    def delete_node(self, node: int) -> None:
        if self.head.val == node:
            self.head = self.head.next
            return
        iter: ListNode = self.head.next
        previous: ListNode = self.head
        while iter.next != None:
            if iter.val == node:
                previous.next = iter.next
                return
            previous = iter
            iter = iter.next

class TestSolution(unittest.TestCase):

    def test_1(self):
        node = 5
        sol = Solution([4,5,1,9])
        sol.delete_node(node)
        output: ListNode = ListNode.list_to_list_node([4,1,9])
        self.assertEqual(sol.head, output)

    def test_2(self):
        node = 1
        sol = Solution([4,5,1,9])
        sol.delete_node(node)
        output: ListNode = ListNode.list_to_list_node([4,5,9])
        self.assertEqual(sol.head, output)

if __name__ == "__main__":
    unittest.main()
