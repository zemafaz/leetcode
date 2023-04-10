import unittest

class Solution:
    def max_chunks_to_sorted(self, arr: list[int]) -> int:
        if len(arr) == 1: return 1
        chunks = len(arr)
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                chunks -= 1
        return chunks

class TestSolution(unittest.TestCase):

    def test_1(self):
        arr = [5,4,3,2,1]
        output = 1
        self.assertEqual(Solution().max_chunks_to_sorted(arr), output)

    def test_2(self):
        arr = [2,1,3,4,4]
        output = 4
        self.assertEqual(Solution().max_chunks_to_sorted(arr), output)

    def test_3(self):
        arr = [3,2,1,3,4,3]
        output = 3
        self.assertEqual(Solution().max_chunks_to_sorted(arr), output)

if __name__ == '__main__':
    unittest.main()
