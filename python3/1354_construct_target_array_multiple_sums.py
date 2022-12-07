import unittest
import heapq

class Solution:
    def is_possible(self, target: list[int]) -> bool:
        psum = sum(target)
        target = [-a for a in target]
        heapq.heapify(target)

        while True:
            a = - heapq.heappop(target)
            psum -= a
            if a == 1 or psum ==1:
                return True
            if a < psum or psum == 0 or a % psum == 0:
                return False
            a %= psum
            psum += a
            heapq.heappush(target, -a)

class TestSolution(unittest.TestCase):
    def test_1(self):
        target = [9,3,5]
        self.assertEqual(Solution().is_possible(target), True)

    def test_2(self):
        target = [1,1,1,2]
        self.assertEqual(Solution().is_possible(target), False)

    def test_3(self):
        target = [8,5]
        self.assertEqual(Solution().is_possible(target), True)

if __name__ == '__main__':
    unittest.main()
