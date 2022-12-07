import unittest

class Solution:
    def is_Valid(self, s: str) -> bool:
        open_bracket = None
        OPENING_BRACKETS = ["(", "{", "["]
        CLOSING_BRACKETS = [")", "}", "]"]

        for c in s:
            if c in OPENING_BRACKETS:
                if open_bracket != None:
                    return False
                open_bracket = OPENING_BRACKETS.index(c)
            if c in CLOSING_BRACKETS:
                if open_bracket != CLOSING_BRACKETS.index(c):
                    return False
                open_bracket = None
        return True

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = "()"
        self.assertEqual(Solution().is_Valid(s), True)

    def test_2(self):
        s = "()[]{}"
        self.assertEqual(Solution().is_Valid(s), True)

    def test_3(self):
        s = "(]"
        self.assertEqual(Solution().is_Valid(s), False)

if __name__ == '__main__':
    unittest.main()