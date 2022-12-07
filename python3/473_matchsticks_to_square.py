import unittest

class Solution:
    def make_square(self, matchsticks: list[int]) -> bool:
        if not matchsticks: return False

        L = len(matchsticks)
        perimeter = sum(matchsticks)
        possible_side = perimeter // 4

        if possible_side * 4 != perimeter: return False

        matchsticks.sort(reverse=True)

        sums = [0 for _ in range(4)]

        def dfs(index):
            if index == L:
                return sums[0] == sums[1] == sums[2] == sums[3]
            for i in range(4):
                if sums[i] + matchsticks[index] <= possible_side:
                    sums[i] += matchsticks[index]
                    if dfs(index + 1):
                        return True
                    sums[i] -= matchsticks[index]
            return False
        return dfs(0)

class TestSolution(unittest.TestCase):
    def test_1(self):
        matchsticks = [1,1,2,2,2]
        self.assertEqual(Solution().make_square(matchsticks), True)
    
    def test_2(self):
        matchsticks = [3,3,3,3,4]
        self.assertEqual(Solution().make_square(matchsticks), False)
    
if __name__ == '__main__':
    unittest.main() 