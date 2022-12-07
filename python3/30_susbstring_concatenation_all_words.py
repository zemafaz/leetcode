import unittest

class Solution:
    def find_susbstring(self, s: str, words: list[str]) -> list[int]:
        res = []
        words.sort()
        len_word = len(words[0])
        for i in range(len(s)):
            if s[i] in map(lambda x: x[0],words):
                if len(s) < len(words) * len(words[0]) + i:
                    break
                words2 = []
                for j in range(len(words)):
                    words2.append(s[i+j*len_word:i+(j+1)*len_word])
                words2.sort()
                if words == words2:
                    res.append(i)
        return res

class TestSolution(unittest.TestCase):
    def test1(self):
        s = "barfoothefoobarman"
        words = ["foo","bar"]
        output = [0,9]
        self.assertEqual(Solution().find_susbstring(s,words),output)

    def test2(self):
        s = "wordgoodgoodgoodbestword"
        words = ["word","good","best","word"]
        output = []
        self.assertEqual(Solution().find_susbstring(s,words),output)

    def test3(self):
        s = "barfoofoobarthefoobarman"
        words = ["bar","foo","the"]
        output = [6,9,12]
        self.assertEqual(Solution().find_susbstring(s,words),output)

if __name__ == "__main__":
    unittest.main()
