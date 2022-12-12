import unittest

class Solution:
    
    def climb_stairs(self, n: int) -> int:
        current_step: int = 1
        next_step: int = 1
        for _ in range(n):
            current_step, next_step = next_step, current_step + next_step
        return current_step

class TestSolution(unittest.TestCase):

    def test_1(self):
        n: int = 2
        output: int = 2
        self.assertEqual(Solution().climb_stairs(n), output)

    def test_2(self):
        n: int = 3
        output: int = 3
        self.assertEqual(Solution().climb_stairs(n), output)

    def test_3(self):
        n: int = 4
        output: int = 5
        self.assertEqual(Solution().climb_stairs(n), output)

if __name__ == "__main__":
    unittest.main()
