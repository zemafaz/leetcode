import unittest

class Solution:
    def count_vowel_permutation(self, n: int) -> int:
        dp = [[1] * 5 for _ in range(n)]
        
        for i in range(1, n):
            now = dp[i]
            previous = dp[i-1]
            now[0] = previous[1] + previous[2] + previous[4]
            now[1] = previous[0] + previous[2]
            now[2] = previous[1] + previous[3]
            now[3] = previous[2]
            now[4] = previous[2] + previous[3]
        return sum(dp[-1])

class TestSolution(unittest.TestCase):
    def test_1(self):
        n = 1
        output = 5
        self.assertEqual(Solution().count_vowel_permutation(n), output)

    
    def test_2(self):
        n = 2
        output = 10
        self.assertEqual(Solution().count_vowel_permutation(n), output)

    def test_3(self):
        n = 5
        output = 68
        self.assertEqual(Solution().count_vowel_permutation(n), output)

if __name__ == "__main__":
    unittest.main()
