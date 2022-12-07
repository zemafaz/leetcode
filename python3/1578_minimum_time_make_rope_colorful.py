import unittest

class Solution:
    def minCost(self, colors: str, needTime: list[int]) -> int:
        needTime.append(0)
        colors += "A"
        res = 0
        current_color = ""
        dp = {}

        for i in range(len(colors)):
            if colors[i] != current_color:
                current_color = colors[i]
                if 0 in dp and 1 in dp:
                    res += min(dp[0], dp[1])
                dp = {}
                dp[i%2] = needTime[i]
            else:
                if i%2 in dp:
                    dp[i%2] += needTime[i]
                else:
                    dp[i%2] = needTime[i]
        return res

class TestSolution(unittest.TestCase):
    def test_1(self):
        colors = "abaac"
        neededTime = [1,2,3,4,5]
        output = 3
        self.assertEqual(Solution().minCost(colors, neededTime), output)

    def test_2(self):
        colors = "abc"
        neededTime = [1,2,3]
        output = 0
        self.assertEqual(Solution().minCost(colors, neededTime), output)

    def test_3(self):
        colors = "aabaa"
        neededTime = [1,2,3,4,1]
        output = 2
        self.assertEqual(Solution().minCost(colors, neededTime), output)

if __name__ == "__main__":
    unittest.main()
