import unittest

class Solution:
    def reverseWords(self, s: str) -> str:
        left, right = 0, -1
        for i in range(len(s)+1):
            if i == len(s) or s[i] == " ":
                while left < right:
                    s = s[:left] + s[right] + s[left+1:right] + s[left] + s[right+1:]
                    left, right = left + 1, right - 1
                left, right = i + 1, i
            else:
                right += 1
        return s

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = "Let's take LeetCode contest"
        output = "s'teL ekat edoCteeL tsetnoc"
        self.assertEqual(Solution().reverseWords(s), output)

    def test_2(self):
        s = "God Ding"
        output = "doG gniD"
        self.assertEqual(Solution().reverseWords(s), output)

if __name__ == "__main__":
    unittest.main()
