import unittest

def kth_grammar(n: int, k: int) -> int:
    res = 0b0
    for i in range(1, n):
        shift_to_right = res << (1<<(i-1))
        mask = (1 << (1 << (i-1))) - 1
        res = shift_to_right | (res ^ mask)
    res = (res >> ((1 << (n-1)) - k)) & 1
    return res

class TestSolution(unittest.TestCase):

    def test_1(self):
        n = 1
        k = 1
        expected_output = 0
        self.assertEqual(kth_grammar(n, k), expected_output)

    def test_2(self):
        n = 2
        k = 1
        expected_output = 0
        self.assertEqual(kth_grammar(n, k), expected_output)

    def test_3(self):
        n = 2
        k = 2
        expected_output = 1
        self.assertEqual(kth_grammar(n, k), expected_output)

    def test_4(self):
        n = 5
        k = 10
        expected_output = 0
        self.assertEqual(kth_grammar(n, k), expected_output)

if __name__ == "__main__":
    unittest.main()
