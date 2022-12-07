import unittest

class Solution:

    def candy(self, ratings: list[int]) -> int:
        candy = []
        
        def adjust(i):
            candy[i] += 1
            if i-1 >= 0:
                if ratings[i-1] > ratings[i] and candy[i-1] == candy[i]:
                    adjust(i-1)
        
        for i in range(len(ratings)):
            if i - 1 >= 0:
                if ratings[i] > ratings[i-1]:
                    candy.append(candy[i-1] + 1)
                else:
                    if candy[i-1] == 1:
                        adjust(i-1)
                    candy.append(1)
            else:
                candy.append(1)

        
        return sum(candy)

class TestSolution(unittest.TestCase):
    def test_1(self):
        ratings = [1, 0, 2]
        self.assertEqual(Solution().candy(ratings), 5)
    
    def test_2(self):
        ratings = [1,2,2]
        self.assertEqual(Solution().candy(ratings), 4)
    
if __name__ == '__main__':
    unittest.main()