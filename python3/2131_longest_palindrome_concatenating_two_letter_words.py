import unittest

class Solution:

    def longest_palindrome(self, words: list[str]) -> int:
        dp = {}
        res = 0
        can_be_odd = False

        for w in words:
            if w[0] == w[1] and can_be_odd == False:
                res += 2
                can_be_odd = True
            rev = w[1] + w[0]
            if rev in dp:
                if dp[rev] == 1:
                    dp.pop(rev)
                else:
                    dp[rev] -= 1
                res += 4
            else:
                dp[w] = 1 if w not in dp else dp[w] + 1

        return res

class TestSolution(unittest.TestCase):

    def test_1(self):
        words = ["lc", "cl", "gg"]
        output = 6
        self.assertEqual(Solution().longest_palindrome(words), output)

    def test_2(self):
        words = ["ab","ty","yt","lc","cl","ab"]
        output = 8
        self.assertEqual(Solution().longest_palindrome(words), output)

    def test_3(self):
        words = ["cc","ll","xx"]
        output = 2
        self.assertEqual(Solution().longest_palindrome(words), output)

if __name__ == "__main__":
    unittest.main()
