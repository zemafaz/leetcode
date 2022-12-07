import unittest

class Solution:
    def k_inverse_pairs(self, n: int, k: int) -> int:
        MOD = 10**9 +7
        ds = [0] + [1] * (k+1)
        for n in range(2, n+1):
            new = [0]
            for k in range(k+1):
                v = ds[k+1]
                v -= ds[k-n+1] if k>=n else 0
                new.append((new[-1]+v)%MOD)
            ds = new
        return (ds[k+1] - ds[k]) % MOD

class TestSolution(unittest.TestCase):
    def test_1(self):
        n, k = 3, 0
        self.assertEqual(Solution().k_inverse_pairs(n, k), 1)

    def test_2(self):
        n, k = 3, 1
        self.assertEqual(Solution().k_inverse_pairs(n, k), 2)

if __name__ == '__main__':
    unittest.main()