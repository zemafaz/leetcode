import unittest

class Solution:
    def min_partitions(self, n: str) -> int:
        return int(max(n))

class TestSolution(unittest.TestCase):
    def test_1(self):
        n = "32"
        self.assertEqual(Solution().min_partitions(n), 3)

    def test_2(self):
        n = "82734"
        self.assertEqual(Solution().min_partitions(n), 8)
    
    def test_3(self):
        n = "27346209830709182346"
        self.assertEqual(Solution().min_partitions(n), 9)

if __name__ == '__main__':
    unittest.main()
