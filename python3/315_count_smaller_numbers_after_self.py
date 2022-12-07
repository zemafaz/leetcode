import unittest

class Solution:
    def count_smaller(self, nums: list[int]) -> list[int]:
        def sort(l):
            half = len(l) // 2
            if half: 
                left, right = sort(l[:half]), sort(l[half:])
                for i in range(len(l))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        l[i] = left.pop()
                    else:
                        l[i] = right.pop()
            return l
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller

class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [5,2,6,1]
        output = [2,1,1,0]
        self.assertEqual(Solution().count_smaller(nums), output)

    def test_2(self):
        nums = [-1]
        output = [0]
        self.assertEqual(Solution().count_smaller(nums), output)

    def test_3(self):
        nums = [-1,-1]
        output = [0, 0]
        self.assertEqual(Solution().count_smaller(nums), output)

if __name__ == '__main__':
    unittest.main()