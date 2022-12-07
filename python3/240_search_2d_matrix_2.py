import unittest

class Solution:
    def search_matrix(self, matrix: list[list[int]], target: int) -> bool:
        if target == matrix[0][0]: return True
        lower = 0
        upper = len(matrix)
        while lower != upper and lower != upper - 1:
            middle = lower + (upper - lower) // 2
            if matrix[middle][middle] >= target:
                upper = middle
                matrix = list(map(lambda x: x[:upper+1], matrix[:upper + 1]))
            else:
                lower = middle
        
        def search(t: int, l:list[int]) -> bool:
            if not l: 
                return False
            middle = len(l) // 2
            if l[middle] == t:
                return True
            if len(l) == 1:
                return False
            if l[middle] > target:
                return search(t, l[:middle])
            else:
                return search(t, l[middle+1:])

        return search(target, matrix[-1]) or search(target, list(map(lambda x:x[-1],matrix)))

class TestSolution(unittest.TestCase):
    def test_1(self):
        matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
        target = 5
        output = True
        self.assertEqual(Solution().search_matrix(matrix, target), output)
    
    def test_2(self):
        matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
        target = 20
        output = False
        self.assertEqual(Solution().search_matrix(matrix, target), output)
    
if __name__ == "__main__":
    unittest.main()