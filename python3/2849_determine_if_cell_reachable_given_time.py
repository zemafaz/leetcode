import unittest

def is_reachable_at_time(sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
    res = max(abs(fx-sx), abs(fy-sy))
    return ((res <= t and fx != sx and fy != sy) or
            (t != 1 and fx == sx and fy == sy))

class TestSolution(unittest.TestCase):

    def test_1(self):
        sx: int = 2
        sy: int = 4
        fx: int = 7
        fy: int = 7
        t: int = 6
        expected_output: bool = True
        self.assertEqual(is_reachable_at_time(sx, sy, fx, fy, t), expected_output)

    def test_2(self):
        sx: int = 3
        sy: int = 1
        fx: int = 7
        fy: int = 3
        t: int = 3
        expected_output: bool = False
        self.assertEqual(is_reachable_at_time(sx, sy, fx, fy, t), expected_output)

if __name__ == "__main__":
    unittest.main()
