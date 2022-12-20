import unittest

class Solution:

    def can_visit_all_rooms(self, rooms: list[list[int]], current_room: int = 0, visited: set[int] = set()) -> bool:
        if current_room in visited: return False
        if len(visited) + 1  == len(rooms): return True
        
        found_all: bool = False
        
        for room in rooms[current_room]:
            found_all = found_all or Solution().can_visit_all_rooms(rooms, room, visited.union([current_room]))
            if found_all: break

        return found_all

class TestSolution(unittest.TestCase):

    def test_1(self):
        rooms: list[list[int]] = [[1],[2],[3],[]]
        output: bool = True
        self.assertEqual(Solution().can_visit_all_rooms(rooms), output)

    def test_2(self):
        rooms: list[list[int]] = [[1,3],[3,0,1],[2],[0]]
        output: bool = False
        self.assertEqual(Solution().can_visit_all_rooms(rooms), output)

if __name__ == "__main__":
    unittest.main()
