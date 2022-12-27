import unittest
from bisect import insort_left

class Solution:
    
    def maximum_bags(self, capacity: list[int], rocks: list[int], additional_rocks: int) -> int:
        difference: list[int] = []
        for i in range(len(capacity)):
            insort_left(difference, capacity[i] - rocks[i])
        
        res: int = 0
        for d in difference:
            additional_rocks -= d
            if additional_rocks >= 0:
                res += 1
            else:
                break
        return res

class TestSolution(unittest.TestCase):

    def test_1(self):
        capacity: list[int] = [2,3,4,5]
        rocks: list[int] = [1,2,4,4]
        additional_rocks: int = 2
        output: int = 3
        self.assertEqual(Solution().maximum_bags(capacity, rocks, additional_rocks), output)

    def test_2(self):
        capacity: list[int] = [10,2,2]
        rocks: list[int] = [2,2,0]
        additional_rocks: int = 100
        output: int = 3
        self.assertEqual(Solution().maximum_bags(capacity, rocks, additional_rocks), output)

if __name__ == "__main__":
    unittest.main()
