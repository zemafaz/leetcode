import unittest

class Solution:
    def numDecodings(self, s: str) -> int:
        counter = 1
        for i in range(len(s)):
            if (s[i] == "0" and 
                    (i - 1 >= 0 and 
                    (s[i-1] != "1" or s[i-1] != "2") or
                    i - 1 < 0)):
                return 0
            if ((s[i] == "1" and 
                    i + 1 < len(s) and 
                    s[i+1] != "0") or (s[i] == "2" and 
                    i + 1 < len(s) and 
                    int("1") <= int(s[i + 1]) <= int("6"))):
                counter += 1
        return counter

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = "12"
        output = 2
        self.assertEqual(Solution().numDecodings(s), output)

    def test_2(self):
        s = "226"
        output = 3
        self.assertEqual(Solution().numDecodings(s), output)

    def test_3(self):
        s = "06"
        output = 0
        self.assertEqual(Solution().numDecodings(s), output)

if __name__ == "__main__":
    unittest.main()
