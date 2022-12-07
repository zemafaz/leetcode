import unittest
import math

class Solution:
    def poor_pigs(self, buckets:int, minutes_to_die: int, minutes_to_test: int) -> int:
        res = math.log10(buckets) / math.log10(minutes_to_test // minutes_to_die + 1)
        return math.ceil(res)

class TestSolution(unittest.TestCase):
    def test_1(self):
        buckets = 1000
        minutes_to_die = 15
        minutes_to_test = 60
        output = 5
        self.assertEqual(Solution().poor_pigs(buckets, minutes_to_die, minutes_to_test), output)
    
    def test_2(self):
        buckets = 4
        minutes_to_die = 15
        minutes_to_test = 15
        output = 2
        self.assertEqual(Solution().poor_pigs(buckets, minutes_to_die, minutes_to_test), output)
    
    def test_3(self):
        buckets = 4
        minutes_to_die = 15
        minutes_to_test = 30
        output = 2
        self.assertEqual(Solution().poor_pigs(buckets, minutes_to_die, minutes_to_test), output)
    
if __name__ == '__main__':
    unittest.main()
