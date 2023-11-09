import unittest

def count_homogenous(s: str) -> int:
    res = 0
    
    current_char = s[0]
    current_count = 0
    for c in s:
        if c == current_char:
            current_count += 1
        else:
            res = (res + sum(range(current_count+1))) % (10 ** 9 + 7)
            current_char = c
            current_count = 1

    res = (res + sum(range(current_count+1))) % (10 ** 9 + 7)
    return res

class TestSolution(unittest.TestCase):

    def test_1(self):
        s: str = "abbcccaa"
        expected_output: int = 13
        self.assertEqual(count_homogenous(s), expected_output)

    def test_2(self):
        s: str = "xy"
        expected_output: int = 2
        self.assertEqual(count_homogenous(s), expected_output)

    def test_3(self):
        s: str = "zzzzz"
        expected_output: int = 15
        self.assertEqual(count_homogenous(s), expected_output)

if __name__ == "__main__":
    unittest.main()
