import unittest

class Solution:

    def min_deletion_size(self, strs: list[str]) -> int:
        res: int = 0
        for i in range(len(strs[0])):
            previous: int = ord(strs[0][i])
            for j in range(1, len(strs)):
                current: int = ord(strs[j][i])
                if previous > current:
                    res += 1
                    break
                previous = current
        return res

class TestSolution(unittest.TestCase):

    def test_1(self):
        strs: list[str] = ["cba","daf","ghi"]
        output: int = 1
        self.assertEqual(Solution().min_deletion_size(strs), output)

    def test_2(self):
        strs: list[str] = ["a","b"]
        output: int = 0
        self.assertEqual(Solution().min_deletion_size(strs), output)

    def test_3(self):
        strs: list[str] = ["zyx","wvu","tsr"]
        output: int = 3
        self.assertEqual(Solution().min_deletion_size(strs), output)

if __name__ == "__main__":
    unittest.main()
