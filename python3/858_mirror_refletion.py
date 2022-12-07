import unittest

class Solution:
    def mirror_refletion(self, p:int, q:int) -> int:
        side = p
        point = [0,0]
        corners = ([side,0], [side, side], [0, side])
        while True:
            point = [point[0] + p, point[1] + q]
            if point in corners:
                break

            p = -p 
            
            if point[1] + q > side or point[1] + q < 0:
                
                d = side - point[1] if point[1] + q > side else 0 - point[1]

                point[0] = point[0] + p
                point[1] = side - (q - d) if point[1] + q > side else 0 - (q - d)

                p, q = -p, -q
            
        return corners.index(point)

            
class TestSolution(unittest.TestCase):
    def test_1(self):
        p = 2
        q = 1
        output = 2
        self.assertEqual(Solution().mirror_refletion(p, q), output)

    def test_2(self):
        p = 3
        q = 1
        output = 1
        self.assertEqual(Solution().mirror_refletion(p, q), output)

if __name__ == "__main__":
    unittest.main()
