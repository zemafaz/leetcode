import unittest
from collections import Counter, defaultdict


def num_identical_pairs(nums: list[int]) -> int:
    encontered = defaultdict(lambda: 0)
    good_pairs = 0

    for num in nums:
        good_pairs += encontered[num]
        encontered[num] += 1

    return good_pairs

def num_identical_pairs_alt(nums: list[int]) -> int:
    count_nums = Counter(nums)
    return sum(map(lambda key: count_nums[key] * (count_nums[key] - 1) // 2,
                   count_nums))
    

class TestSolution(unittest.TestCase):

    def test_1(self):
        nums = [1,2,3,1,1,3]
        output = 4
        self.assertEqual(num_identical_pairs(nums), output)

    def test_2(self):
        nums = [1,1,1,1]
        output = 6
        self.assertEqual(num_identical_pairs(nums), output)

    def test_3(self):
        nums = [1,2,3]
        output = 0
        self.assertEqual(num_identical_pairs(nums), output)

    def test_1_alt(self):
        nums = [1,2,3,1,1,3]
        output = 4
        self.assertEqual(num_identical_pairs_alt(nums), output)

    def test_2_alt(self):
        nums = [1,1,1,1]
        output = 6
        self.assertEqual(num_identical_pairs_alt(nums), output)

    def test_3_alt(self):
        nums = [1,2,3]
        output = 0
        self.assertEqual(num_identical_pairs_alt(nums), output)

if __name__ == "__main__":
    unittest.main()
