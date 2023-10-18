import unittest
import heapq

def minimum_time(n: int, relations: list[list[int]], time: list[int]) -> int:
    heap = []
    res = 0

    restricted = set()
    for i, relation in enumerate(relations):
        restricted.add(relation[1])
    for i in range(len(time)):
        if i + 1 not in restricted:
            unrestricted = (time[i], i+1)
            time[i] = 0
            heapq.heappush(heap, unrestricted)

    while n != 0:
        current = heapq.heappop(heap)

        res += current[0]
        n -= 1

        for i in range(len(heap)):
            heap[i] = (heap[i][0] - current[0], heap[i][1])

        restricted = set()
        for i, relation in enumerate(relations):
            if relation[0] == current[1]:
                relations[i] = [0, 0]
            else:
                restricted.add(relation[1])

        for i in range(len(time)):
            if i + 1 not in restricted and time[i] != 0:
                unrestricted = (time[i], i+1)
                time[i] = 0
                heapq.heappush(heap, unrestricted)

    
    return res


class TestSolution(unittest.TestCase):

    def test_1(self):
        n = 3
        relations = [[1,3],[2,3]]
        time = [3,2,5]
        expected_output = 8
        self.assertEqual(minimum_time(n, relations, time), expected_output)

    def test_2(self):
        n = 5
        relations = [[1,5],[2,5],[3,5],[3,4],[4,5]]
        time = [1,2,3,4,5]
        expected_output = 12
        self.assertEqual(minimum_time(n, relations, time), expected_output)

if __name__ == "__main__":
    unittest.main()
