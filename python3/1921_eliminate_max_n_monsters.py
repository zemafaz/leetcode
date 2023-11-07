import unittest
import math

def eliminate_maximum(dist: list[int], speed: list[int]) -> int:
    for i in range(len(dist)):
        dist[i] = math.ceil(dist[i] / speed[i])

    dist.sort()
    for i, t in enumerate(dist):
        if t <= i:
            return i

    return len(dist)
    

class TestSolution(unittest.TestCase):
    
    def test_1(self):
        dist: list[int] = [1,3,4]
        speed: list[int] = [1,1,1]
        expected_output: int = 3
        self.assertEqual(eliminate_maximum(dist, speed), expected_output)

    def test_2(self):
        dist: list[int] = [1,1,2,3]
        speed: list[int] = [1,1,1,1]
        expected_output: int = 1
        self.assertEqual(eliminate_maximum(dist, speed), expected_output)

    def test_3(self):
        dist: list[int] = [3,2,4]
        speed: list[int] = [5,3,2]
        expected_output: int = 1
        self.assertEqual(eliminate_maximum(dist, speed), expected_output)

if __name__ == "__main__":
    unittest.main()

