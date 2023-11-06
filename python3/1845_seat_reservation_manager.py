import unittest
import heapq

class SeatManager:

    def __init__(self, n: int):
        self.n_rooms = n
        self.free_rooms = [-1]

    def reserve(self) -> int:
        if self.free_rooms[-1] == - (self.n_rooms + 1):
            return -1
        room = - self.free_rooms.pop()
        if len(self.free_rooms) == 0:
            heapq.heappush(self.free_rooms, - (room + 1))
        return room

    def unreserve(self, seat_number: int) -> None:
        heapq.heappush(self.free_rooms, - seat_number)

class TestSolution(unittest.TestCase):

    seat_manager = SeatManager(5)

    def test_1(self):
        self.assertEqual(self.seat_manager.reserve(), 1)

    def test_2(self):
        self.assertEqual(self.seat_manager.reserve(), 2)

    def test_3(self):
        self.seat_manager.unreserve(2)
        self.assertEqual(self.seat_manager.reserve(), 2)

    def test_4(self):
        self.assertEqual(self.seat_manager.reserve(), 3)

    def test_5(self):
        self.assertEqual(self.seat_manager.reserve(), 4)

    def test_6(self):
        self.assertEqual(self.seat_manager.reserve(), 5)

    def test_7(self):
        self.seat_manager.unreserve(5)
        self.assertEqual(self.seat_manager.reserve(), 5)

if __name__ == "__main__":
    unittest.main()
