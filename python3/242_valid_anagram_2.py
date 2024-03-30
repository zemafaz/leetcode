import unittest
from collections import defaultdict


def is_anagram(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False

    counter: dict[str, int] = defaultdict(lambda: 0)

    for c in s:
        counter[c] += 1

    for c in t:
        counter[c] -= 1

    return not any(counter.values())


class TestSolution(unittest.TestCase):

    def test_1(self):
        s: str = "anagram"
        t: str = "nagaram"
        expected_output: bool = True
        self.assertEqual(is_anagram(s, t), expected_output)

    def test_2(self):
        s: str = "rat"
        t: str = "car"
        expected_output: bool = False
        self.assertEqual(is_anagram(s, t), expected_output)


if __name__ == "__main__":
    unittest.main()
