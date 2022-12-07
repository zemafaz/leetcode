import unittest
from sortedcontainers import SortedDict, SortedList
from collections import Counter

class MyCalendarThree1:
    def __init__(self):
        self.diff = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.diff[start] = self.diff.get(start, 0) + 1
        self.diff[end] = self.diff.get(end, 0) - 1
        cur = res = 0
        for delta in self.diff.values():
            cur += delta
            res = max(cur, res)
        return res

class MyCalendarThree2:
    def __init__(self):
        self.vals = Counter()
        self.lazy = Counter()

    def update(self, start: int, end: int, left: int = 0,
            right: int = 10**9, idx: int = 1) -> None:
        if start > right or end < left:
            return

        if start <= left <= right <= end:
            self.vals[idx] += 1
            self.lazy[idx] += 1
        else:
            mid = (left + right) // 2
            self.update(start, end, left, mid, idx * 2)
            self.update(start, end, mid + 1, right, idx * 2 + 1)
            self.vals[idx] = (self.lazy[idx] +
                    max(self.vals[2*idx], self.vals[2*idx+1]))

    def book(self, start: int, end: int) -> int:
        self.update(start, end-1)
        return self.vals[1]

class MyCalendarThree3:
    def __init__(self):
        self.starts = SortedList([[0,0]])
        self.res = 0

    def split(self, x: int) -> None:
        idx = self.starts.bisect_left([x, 0])
        if idx < len(self.starts) and self.starts[idx][0] == x:
            return 
        self.starts.add([x,self.starts[idx-1][1]])

    def book(self, start: int, end: int) -> int:
        self.split(start)
        self.split(end)
        for interval in self.starts.irange([start, 0], [end, 0], (True, False)):
            interval[1] += 1
            self.res = max(self.res, interval[1])
        return self.res

class TestSolution(unittest.TestCase):
    def test_1(self):
        myCalendar = MyCalendarThree1()
        self.assertEqual(myCalendar.book(10, 20), 1)
        self.assertEqual(myCalendar.book(50, 60), 1)
        self.assertEqual(myCalendar.book(10, 40), 2)
        self.assertEqual(myCalendar.book(5, 15), 3)
        self.assertEqual(myCalendar.book(5, 10), 3)
        self.assertEqual(myCalendar.book(25, 55), 3)

    def test_2(self):
        myCalendar = MyCalendarThree2()
        self.assertEqual(myCalendar.book(10, 20), 1)
        self.assertEqual(myCalendar.book(50, 60), 1)
        self.assertEqual(myCalendar.book(10, 40), 2)
        self.assertEqual(myCalendar.book(5, 15), 3)
        self.assertEqual(myCalendar.book(5, 10), 3)
        self.assertEqual(myCalendar.book(25, 55), 3)

    def test_3(self):
        myCalendar = MyCalendarThree3()
        self.assertEqual(myCalendar.book(10, 20), 1)
        self.assertEqual(myCalendar.book(50, 60), 1)
        self.assertEqual(myCalendar.book(10, 40), 2)
        self.assertEqual(myCalendar.book(5, 15), 3)
        self.assertEqual(myCalendar.book(5, 10), 3)
        self.assertEqual(myCalendar.book(25, 55), 3)
        
if __name__ == "__main__":
    unittest.main()
