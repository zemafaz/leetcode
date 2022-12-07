import unittest
import bisect

class TimeMap:
    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            bisect.insort_right(self.timeMap[key], (timestamp,value))
        else:
            self.timeMap[key] = [(timestamp, value)]

    def get(self, key: str, timestamp:int) -> str:
        if key in self.timeMap:
            index = bisect.bisect_left(list(map(lambda x: x[0], self.timeMap[key])), timestamp)
            if index < len(self.timeMap[key]) and self.timeMap[key][index][0] == timestamp:
                    return self.timeMap[key][index][1]
            elif index <= len(self.timeMap[key]):
                return self.timeMap[key][index-1][1]
            else:
                return ""
        else:
            return ""

class TestSolution(unittest.TestCase):
    def test(self):
        timeMap: TimeMap = TimeMap()
        timeMap.set("foo", "bar", 1)
        self.assertEqual(timeMap.get("foo", 1), "bar")
        self.assertEqual(timeMap.get("foo", 3), "bar")
        timeMap.set("foo", "bar2", 4)
        self.assertEqual(timeMap.get("foo", 4), "bar2")
        self.assertEqual(timeMap.get("foo", 5), "bar2")

if __name__ == "__main__":
    unittest.main()
