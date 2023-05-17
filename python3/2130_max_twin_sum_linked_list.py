import unittest
from list_node import ListNode

def pair_sum(head: ListNode) -> int:
    n = 0
    current = head
    previous = None
    while current != None:
        next = current.next
        current.next = previous
        previous = current
        current = next
        n += 1
    
    n = n // 2
    current = previous
    previous = None

    while n != 0:
        if current == None:
            raise Exception()
        next = current.next
        current.next = previous
        previous = current
        current = next
        n -= 1
    
    while current != None:
        if previous == None:
            raise Exception()
        n = max(n, current.val + previous.val)
        current, previous = current.next, previous.next

    return n

class TestSolution(unittest.TestCase):

    def test_1(self):
        head = ListNode.list_to_list_node([5,4,2,1])
        output = 6
        res = pair_sum(head)
        self.assertEqual(res, output)

    def test_2(self):
        head = ListNode.list_to_list_node([4,2,2,3])
        output = 7
        res = pair_sum(head)
        self.assertEqual(res, output)

    def test_3(self):
        head = ListNode.list_to_list_node([1,100000])
        output = 100001
        res = pair_sum(head)
        self.assertEqual(res, output)

if __name__ == '__main__':
    unittest.main()
