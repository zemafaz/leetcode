import unittest
from collections import Counter
from functools import reduce

def reduction_operations(nums: list[int]) -> int:
    counter: Counter[int] = Counter(nums)
    elements: list[int] = list(counter)
    elements.sort()

    return reduce(lambda x, i: x + i*counter[elements[i]], range(len(elements)))

class TestSolution(unittest.TestCase):

    def test_1(self):
        nums: list[int] = [5,1,3]
        expected_output: int = 3
        self.assertEqual(reduction_operations(nums), expected_output)

    def test_2(self):
        nums: list[int] = [1,1,1]
        expected_output: int = 0
        self.assertEqual(reduction_operations(nums), expected_output)

    def test_3(self):
        nums: list[int] = [1,1,2,2,3]
        expected_output: int = 4
        self.assertEqual(reduction_operations(nums), expected_output)

if __name__ == "__main__":
    unittest.main()
