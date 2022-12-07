import unittest

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        middle = len(palindrome) // 2
        res = ""
        for i in range(middle):
            if palindrome[i] != "a":
                res = palindrome[:i] + "a" + palindrome[i+1:]
                break
        if res == "" and len(palindrome) > 1:
            res = "b" + res[1:]
        return res

class TestSolution(unittest.TestCase):
    
    def test_1(self):
        palindrome = "abccba"
        output = "aaccba"
        self.assertEqual(Solution().breakPalindrome(palindrome), output)

    def test_2(self):
        palindrome = "a"
        output = ""
        self.assertEqual(Solution().breakPalindrome(palindrome), output)

if __name__ == "__main__":
    unittest.main()

