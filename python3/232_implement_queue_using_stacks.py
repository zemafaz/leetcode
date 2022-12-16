import unittest

class MyQueue:

    def __init__(self):
        self.stack1: list[int] = []
        self.stack2: list[int] = []

    def push(self, x: int) -> None:
        (empty, full) = (self.stack1, self.stack2) if len(self.stack1) == 0 else (self.stack2, self.stack1)
        empty.append(x)
        while full:
            e: int = full.pop()
            empty.append(e)
            
    def pop(self) -> int:
        return self.stack1.pop() if len(self.stack1) != 0 else self.stack2.pop()

    def peek(self) -> int:
        e: int = self.stack1.pop() if len(self.stack1) != 0 else self.stack2.pop()
        if len(self.stack2) == 0:
            self.stack2.append(e)
        else:
            self.stack1.append(e)
        return e

    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0

class TestSolution(unittest.TestCase):

    def test_1(self):
        my_queue: MyQueue = MyQueue()
        my_queue.push(1)
        my_queue.push(2)
        output: int = 1
        self.assertEqual(my_queue.peek(), output)
        self.assertEqual(my_queue.pop(), output)
        self.assertEqual(my_queue.empty(), False)

if __name__ == "__main__":
    unittest.main()
