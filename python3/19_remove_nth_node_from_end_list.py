import unittest
from list_node import ListNode

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def reverseList(node: ListNode, previous: ListNode) -> ListNode:
            if node == None:
                return previous
            next = node.next
            node.next = previous
            return reverseList(next, node)

        current = reverseList(head, None)
        previous = None
        while current != None:
            if current == None:
                return previous
            if n == 1:
                current = current.next
            else:
                next = current.next
                current.next = previous
                previous = current
                current = next
            n -= 1
        return previous

    def removeNthFromEndEfficient(self, head: ListNode, n:int) -> ListNode:
        iter = head
        iter_delayed = ListNode(0,head)

        while iter != None:
            iter = iter.next
            if n == 0:
                iter_delayed = iter_delayed.next
            else:
                n -= 1
        if iter_delayed.next == head:
            head = head.next
        else:
            iter_delayed.next = iter_delayed.next.next
        return head

class TestSolution(unittest.TestCase):
    def test_1(self):
        head = ListNode.list_to_list_node([1,2,3,4,5])
        n = 2
        output = ListNode.list_to_list_node([1,2,3,5])
        self.assertEqual(Solution().removeNthFromEnd(head, n),output)

    def test_2(self):
        head = ListNode.list_to_list_node([1])
        n = 1
        output = ListNode.list_to_list_node([])
        self.assertEqual(Solution().removeNthFromEnd(head, n),output)

    def test_3(self):
        head = ListNode.list_to_list_node([1,2])
        n = 1
        output = ListNode.list_to_list_node([1])
        self.assertEqual(Solution().removeNthFromEnd(head, n),output)

    def test_1_efficient(self):
        head = ListNode.list_to_list_node([1,2,3,4,5])
        n = 2
        output = ListNode.list_to_list_node([1,2,3,5])
        self.assertEqual(Solution().removeNthFromEndEfficient(head, n),output)

    def test_2_efficient(self):
        head = ListNode.list_to_list_node([1])
        n = 1
        output = ListNode.list_to_list_node([])
        self.assertEqual(Solution().removeNthFromEndEfficient(head, n),output)

    def test_3_efficient(self):
        head = ListNode.list_to_list_node([1,2])
        n = 1
        output = ListNode.list_to_list_node([1])
        self.assertEqual(Solution().removeNthFromEndEfficient(head, n),output)

if __name__ == "__main__":
    unittest.main()
