import unittest

class Solution:
    def schedule_course(self, courses:list[list[int]]) -> int:
        courses.sort(key=lambda e: e[1])
        now = 0
        res = 0

        for c in courses:
            if now + c[0] <= c[1]:
                now += c[0]
                res += 1
        
        return res

class TestSolution(unittest.TestCase):
    def test_1(self):
        courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
        self.assertEqual(Solution().schedule_course(courses), 3)
    
    def test_2(self):
        courses = [[1,2]]
        self.assertEqual(Solution().schedule_course(courses), 1)
    
    def test_3(self):
        courses = [[3,2],[4,3]]
        self.assertEqual(Solution().schedule_course(courses), 0)
    
if __name__ == '__main__':
    unittest.main()
