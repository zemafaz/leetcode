import unittest
import random

class RandomizedCollection:

    def __init__(self):
        self.vals: list[int] = []
        self.collection: dict[int, set[int]] = {}

    def insert(self, val: int) -> bool:
        self.vals.append(val)
        if val in self.collection:
            self.collection[val].add(len(self.vals) - 1)
            return False
        else:
            self.collection[val] = set()
            self.collection[val].add(len(self.vals) - 1)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.collection:
            return False
        to_remove_index = self.collection[val].pop()
        if len(self.collection[val]) == 0:
            self.collection.pop(val)
        temp = self.vals.pop()
        if to_remove_index != len(self.vals):
            self.vals[to_remove_index] = temp
        return True

    def get_random(self) -> int:
        return random.choice(self.vals)

class TestSolution(unittest.TestCase):

    random_collection = RandomizedCollection()

    def test_1(self) -> None:
        self.assertEqual(self.random_collection.insert(1), True)

    def test_2(self) -> None:
        self.assertEqual(self.random_collection.insert(1), False)

    def test_3(self) -> None:
        self.assertEqual(self.random_collection.insert(2), True)

    def test_4(self) -> None:
        n_2 = 0
        for _ in range(1000000):
            res = self.random_collection.get_random()
            n_2 += 1 if res == 2 else 0
        self.assertAlmostEqual(n_2/1000000, 0.33, delta=0.1)

    def test_5(self) -> None:
        self.assertEqual(self.random_collection.remove(1), True)

    def test_6(self) -> None:
        n_2 = 0
        for _ in range(1000000):
            res = self.random_collection.get_random()
            n_2 += 1 if res == 2 else 0
        self.assertAlmostEqual(n_2/1000000, 0.5, delta=0.1)

if __name__ == '__main__':
    unittest.main()
