import unittest

class Node:

    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

    def clear(self):
        self.val = None

    def __eq__(self, other):
        return id(self) == id(other)
        

class MyCircularQueue:

    def __init__(self, k:int):
        self.front = Node()
        self.rear = self.front
        iter = self.front
        for i in range(k-1):
            iter.next = Node()
            iter = iter.next
        iter.next = self.front

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.rear.val = value
        else:
            self.rear = self.rear.next
            self.rear.val = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front.clear()
        self.front = self.front.next
        return True

    def Front(self) -> int:
        return self.front.val

    def Rear(self) -> int:
        return self.rear.val

    def isEmpty(self) -> bool:
        return self.front.val == None

    def isFull(self) -> bool:
        return self.rear.next == self.front

class TestSolution(unittest.TestCase):
    
    def test_1(self):
        self.circular_queue = MyCircularQueue(3)
        self.assertEqual(self.circular_queue.isEmpty(), True)
        self.assertEqual(self.circular_queue.enQueue(1), True)
        self.assertEqual(self.circular_queue.enQueue(2), True)
        self.assertEqual(self.circular_queue.enQueue(3), True)
        self.assertEqual(self.circular_queue.Rear(), 3)
        self.assertEqual(self.circular_queue.isFull(), True)
        self.assertEqual(self.circular_queue.deQueue(), True)
        self.assertEqual(self.circular_queue.enQueue(4), True)
        self.assertEqual(self.circular_queue.Rear(), 4)

if __name__ == "__main__":
    unittest.main()
