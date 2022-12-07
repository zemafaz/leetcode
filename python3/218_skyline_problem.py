import unittest
import heapq

class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        events = [(l,-h,r) for l, r, h in buildings]
        events += list({(r,0,0) for _, r, _ in buildings})
        events.sort()

        skyline = [[0, 0]]
        live = [(0, float("inf"))]
        for l, rev_h, r in events:
            while live[0][1] <= l:
                heapq.heappop(live)
            if rev_h:
                heapq.heappush(live, (rev_h, r))
            if skyline[-1][1] != -live[0][0]:
                skyline.append([l, -live[0][0]])
        return skyline[1:] 

class TestSolution(unittest.TestCase):
    def test_1(self):
        buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
        output = [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
        self.assertEqual(Solution().getSkyline(buildings), output)

    def test_2(self):
        buildings = [[0,2,3],[2,5,3]]
        output = [[0,3],[5,0]]
        self.assertEqual(Solution().getSkyline(buildings), output)

if __name__ == "__main__":
    unittest.main()
