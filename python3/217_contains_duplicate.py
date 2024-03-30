import unittest


def contains_duplicate(nums: list[int]) -> bool:

    unique_value: set[int] = set()

    for num in nums:
        previous_len: int = len(unique_value)
        unique_value.add(num)
        if len(unique_value) == previous_len:
            return True

    return False


class TestSolution(unittest.TestCase):

    def test_1(self):
        nums: list[int] = [1, 2, 3, 1]
        expected_output: bool = True
        self.assertEqual(contains_duplicate(nums), expected_output)

    def test_2(self):
        nums: list[int] = [1, 2, 3, 4]
        expected_output: bool = False
        self.assertEqual(contains_duplicate(nums), expected_output)

    def test_3(self):
        nums: list[int] = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        expected_output: bool = True
        self.assertEqual(contains_duplicate(nums), expected_output)


if __name__ == "__main__":
    unittest.main()
