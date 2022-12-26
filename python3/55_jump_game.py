import unittest

class Solution:

    def can_jump(self, nums: list[int]) -> bool:
        def aux(index: int) -> bool:
            if index == 0: return True
            can: bool = False
            for i, num in enumerate(nums[:index]):
                if i + num >= index:
                    can = can or aux(i)
                    if can: return True
            return False
        
        return aux(len(nums) - 1)

class TestSolution(unittest.TestCase):

    def test_1(self):
        nums: list[int] = [2,3,1,1,4]
        output: bool = True
        self.assertEqual(Solution().can_jump(nums), output)

    def test_2(self):
        nums: list[int] = [3,2,1,0,4]
        output: bool = False
        self.assertEqual(Solution().can_jump(nums), output)

if __name__ == "__main__":
    unittest.main()
