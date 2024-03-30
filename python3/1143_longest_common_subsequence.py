import unittest


class Solution:

    def longest_common_subsequence(self, text1: str, text2: str) -> int:
        dp: list[list[int]] = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = dp[i-1][j-1] + 1 if text1[i-1] == text2[j-1] else max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]


class TestSolution(unittest.TestCase):

    def test_1(self):
        text1: str = "abcde"
        text2: str = "ace"
        output: int = 3
        self.assertEqual(Solution().longest_common_subsequence(text1, text2), output)

    def test_2(self):
        text1: str = "abc"
        text2: str = "abc"
        output: int = 3
        self.assertEqual(Solution().longest_common_subsequence(text1, text2), output)

    def test_3(self):
        text1: str = "abc"
        text2: str = "def"
        output: int = 0
        self.assertEqual(Solution().longest_common_subsequence(text1, text2), output)


if __name__ == "__main__":
    unittest.main()
