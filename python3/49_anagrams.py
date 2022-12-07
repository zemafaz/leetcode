import unittest
from collections import Counter

class Solution:
    
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        def aux(s: str, c1: Counter) -> bool:
            for i in range(len(res)):
                c2 = Counter(res[i][0])
                if c1 == c2:
                    res[i].append(s)
                    return True
            return False

        res = []
        for s in strs:
            c1 = Counter(s)
            if aux(s, c1) == True:
                continue
            else:
                res.append([s])
        return res


class TestSolution(unittest.TestCase):

    def test_1(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        output = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        res = Solution().groupAnagrams(strs)
        for o in output:
            for r in res:
                if o[0] in r:
                    self.assertCountEqual(o, r)

    def test_2(self):
        strs = [""]
        output = [[""]]
        self.assertCountEqual(Solution().groupAnagrams(strs), output)

    def test_3(self):
        strs = ["a"]
        output = [["a"]]
        self.assertCountEqual(Solution().groupAnagrams(strs), output)

if __name__ == "__main__":
    unittest.main()
