import unittest

class Solution:
    def push_dominoes(self, dominoes:str) -> str:
        i = 1
        dominoes = "L" + dominoes + "R"
        while i < len(dominoes):
            if dominoes[i] == "." and dominoes[i-1] == "L":
                j = i + 1
                while j < len(dominoes):
                    if dominoes[j] == "R":
                        break
                    if dominoes[j] == "L":
                        dominoes = dominoes[:i] + "L" * (j-i) + dominoes[j:] 
                        break
                    j += 1
                i = j
            if dominoes[i] == "." and dominoes[i-1] == "R":
                j = i + 1
                while j < len(dominoes):
                    if dominoes[j] == "R":
                        dominoes = dominoes[:i] + "R" * (j-i-1) + dominoes[j:]
                        break
                    if dominoes[j] == "L":
                        half = (j - i) // 2
                        if (j - i) % 2 == 0:
                            dominoes = dominoes[:i] + "R" * half + "L" * half + dominoes[j:]
                        else:
                            dominoes = dominoes[:i] + "R" * half + "." + "L" * half + dominoes[j:]
                        break
                    j += 1
                i = j
            i += 1
        return dominoes[1:-1]

class TestSolution(unittest.TestCase):
    def test_1(self):
        dominoes = "RR.L"
        output = "RR.L"
        self.assertEqual(Solution().push_dominoes(dominoes), output)

    def test_2(self):
        dominoes = ".L.R...LR..L.."
        output = "LL.RR.LLRRLL.."
        self.assertEqual(Solution().push_dominoes(dominoes), output)

if __name__ == "__main__":
    unittest.main()
