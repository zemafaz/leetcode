import unittest

class Solution:
    def is_interleave(self, s1:str, s2:str, s3:str) -> bool:
        r, c, l = len(s1), len(s2), len(s3)

        if abs(r-c) > 1:
            return False
        
        dp = [True for _ in range(c+1)]
        
        for j in range(1, c+1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
        for i in range(1, r+1):
            dp[0] = (dp[0] and s1[i-1] == s3[i-1])
            for j in range(1, c+1):
                dp[j] = (dp[j] and s1[i-1] == s3[i-1+j]) or (dp[j-1] and s2[j-1] == s3[i-1+j])
        return dp[-1]

class TestSolution(unittest.TestCase):
    def test_1(self):
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbcbcac"

        self.assertEqual(Solution().is_interleave(s1, s2, s3), True)

    def test_2(self):
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbbaccc"

        self.assertEqual(Solution().is_interleave(s1, s2, s3), False)
    
    def test_3(self):
        s1 = ""
        s2 = ""
        s3 = ""

        self.assertEqual(Solution().is_interleave(s1, s2, s3), True)

if __name__ == '__main__':
    unittest.main()