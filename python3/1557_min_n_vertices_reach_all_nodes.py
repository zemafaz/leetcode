import unittest

def find_smallest_set_of_vertices(n: int, edges: list[list[int]]) -> list[int]:
    return list({i for i in range(n)}.difference(set(map(lambda x: x[1], edges))))

class TestSolution(unittest.TestCase):

    def test_1(self):
        n = 6
        edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
        output = [0,3]
        res = find_smallest_set_of_vertices(n, edges)
        self.assertCountEqual(res, output)

    def test_2(self):
        n = 5
        edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
        output = [0,2,3]
        res = find_smallest_set_of_vertices(n, edges)
        self.assertCountEqual(res, output)

if __name__ == '__main__':
    unittest.main()
