import unittest

class Solution:
    def roman_to_int(self,s:str):
        d = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000
                }
        res = 0
        for i in range(len(s)):
            v=d[s[i]]
            if i + 1 < len(s):
                if d[s[i+1]] > v:
                    res -= v
                    continue
            res +=v
        return res

class TestSolution(unittest.TestCase):
    def test_1(self):
        s="III"
        output=3
        self.assertEqual(Solution().roman_to_int(s),output)

    def test_2(self):
        s="LVIII"
        output=58
        self.assertEqual(Solution().roman_to_int(s),output)

    def test_3(self):
        s="MCMXCIV"
        output=1994
        self.assertEqual(Solution().roman_to_int(s),output)

if __name__=="__main__":
    unittest.main()
