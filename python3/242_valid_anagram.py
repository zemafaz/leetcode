import unittest

class Solution:
    def is_anagram(self, s: str, t:str) -> bool:
        if len(s) != len(t): return False
        s_list = list(s)
        for c in t:
            try:
                s_list.remove(c)
            except(ValueError):
                return False
        return True

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = "anagram"
        t = "nagaram"
        output = True
        self.assertEqual(Solution().is_anagram(s, t), output)

    def test_2(self):
        s = "rat"
        t = "car"
        output = False
        self.assertEqual(Solution().is_anagram(s, t), output)

if __name__ == '__main__':
    unittest.main()
