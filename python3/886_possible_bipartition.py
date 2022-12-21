from collections import defaultdict
import unittest

class Solution:

    def possible_bipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        NOT_COLORED, BLUE, GREEN = 0, 1, -1

        def helper(person: int, color: int):
            color_table[person] = color

            for other in dislike_table[person]:
                if color_table[other] == color:
                    return False
                if color_table[other] == NOT_COLORED and (not helper(other, -color)):
                    return False
            return True

        if n == 1 or not dislikes: return True
        dislike_table: dict[int, list[int]] = defaultdict(list[int])
        color_table: dict[int, int] = defaultdict(int)
        
        for p1, p2 in dislikes:
            dislike_table[p1].append(p2)
            dislike_table[p2].append(p1)

        for person in range(1, n+1):
            if color_table[person] == NOT_COLORED and (not helper(person, BLUE)):
                return False

        return True

class TestSolution(unittest.TestCase):

    def test_1(self):
        n: int = 4
        dislikes: list[list[int]] = [[1,2],[1,3],[2,4]]
        output: bool = True
        self.assertEqual(Solution().possible_bipartition(n, dislikes), output)

    def test_2(self):
        n: int = 3
        dislikes: list[list[int]] = [[1,2],[1,3],[2,3]]
        output: bool = False
        self.assertEqual(Solution().possible_bipartition(n, dislikes), output)

    def test_3(self):
        n: int = 5
        dislikes: list[list[int]] = [[1,2],[2,3],[3,4],[4,5],[1,5]]
        output: bool = False
        self.assertEqual(Solution().possible_bipartition(n, dislikes), output)

if __name__ == "__main__":
    unittest.main()
