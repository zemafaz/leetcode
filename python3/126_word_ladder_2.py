import collections
import unittest

class Solution:
    def find_ladders(self, begin_word:str, end_word:str, word_list:list[str]) -> list[list[str]]:
        word_set = set(word_list)
        res = []
        layer = {}
        layer[begin_word] = [[begin_word]]

        while layer:
            new_layer = collections.defaultdict(list)
            for w in layer:
                if w == end_word:
                    res.extend(k for k in layer[w])
                else:
                    for i in range(len(w)):
                        for c in "abcdefghijklmnopqrstuvwxyz":
                            new_word = w[:i] + c + w[i+1:]
                            if new_word in word_set:
                                new_layer[new_word] += [j + [new_word] for j in layer[w]]
            word_set -= set(new_layer.keys())
            layer = new_layer
        return res

class TestSolution(unittest.TestCase):
    def test1(self):
        begin_word = "hit"
        end_word = "cog"
        word_list = ["hot","dot","dog","lot","log","cog"]
        output = [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
        self.assertEqual(Solution().find_ladders(begin_word,end_word,word_list),output)

    def test2(self):
        begin_word = "hit"
        end_word = "cog"
        word_list = ["hot","dot","dog","lot","log"]
        output = []
        self.assertEqual(Solution().find_ladders(begin_word,end_word,word_list),output)

if __name__=="__main__":
    unittest.main()
