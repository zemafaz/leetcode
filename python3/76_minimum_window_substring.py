import unittest

class Solution:

    def min_window(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        res = ""
        
        for i in range(len(s)):
            j = t.find(s[i])
            if j != -1:
                if len(t) == 1 and res == "":
                    res = s[i]
                right = Solution.search(s, "".join([t[:j], t[j+1:]]), i + 1)
                if right != -1:
                    if res == "" or len(res) > right - i:
                        res = s[i:right]

        return res

    def search(s: str, t: str, left: int) -> int:
        for i in range(left, len(s)):
            j = t.find(s[i])
            if j != -1:
                if len(t) == 1:
                    return i + 1
                else:
                    return Solution.search(s, "".join([t[:j], t[j+1:]]), i + 1)
        return -1


class TestSolution(unittest.TestCase):

    def test_1(self):
        s = "ADOBECODEBANC"
        t = "ABC"
        output = "BANC"
        self.assertEqual(Solution().min_window(s, t), output)

    def test_2(self):
        s = "a"
        t = "a"
        output = "a"
        self.assertEqual(Solution().min_window(s, t), output)

    def test_3(self):
        s = "a"
        t = "aa"
        output = ""
        self.assertEqual(Solution().min_window(s, t), output)

if __name__ == "__main__":
    unittest.main()
