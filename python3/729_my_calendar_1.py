import unittest
import bisect

class MyCalendar:
    def __init__(self):
       self.calendar = [] 
    
    def book(self, start: int, end: int) -> bool:
        new_el = (start, end)
        i = bisect.bisect_left(self.calendar, new_el)
        if i - 1 >= 0:
            if start < self.calendar[i-1][1]:
                return False
        if i < len(self.calendar): 
            if end >= self.calendar[i][0]:
                return False
        self.calendar.insert(i, new_el)
        return True

class TestSolution(unittest.TestCase):
    def test_1(self):
        my_calendar = MyCalendar()
        res = my_calendar.book(10, 20)
        self.assertEqual(res, True)
        res = my_calendar.book(15, 25)
        self.assertEqual(res, False)
        res = my_calendar.book(20, 30)
        self.assertEqual(res, True)

if __name__ == '__main__':
    unittest.main()
