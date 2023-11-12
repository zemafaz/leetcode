import unittest

def num_buses_to_destination(routes: list[list[int]], source: int, target: int) -> int:
    
    def check_stops(current: set[int], visited: set[int], number_buses_taken: int = 1) -> int:
        if len(current) == 0:
            return -1
        visited = visited.union(current)
        next: set[int] = set()
        for route in routes:
            route_set: set[int] = set(route)
            for stop in current:
                can_take_route: bool = stop in route
                if can_take_route:
                    if target in route:
                        return number_buses_taken + 1
                    else:
                        next = next.union(route_set.difference(visited))
        return check_stops(next, visited, number_buses_taken)
   
    return 0 if source == target else check_stops(set([source]), set())

class TestSolution(unittest.TestCase):

    def test_1(self):
        routes: list[list[int]] = [[1,2,7], [3,6,7]]
        source: int = 1
        target: int = 6
        expected_output: int = 2
        self.assertEqual(num_buses_to_destination(routes, source, target), expected_output)

    def test_2(self):
        routes: list[list[int]] = [[7,12], [4,5,15], [6], [15,19], [9,12,13]]
        source: int = 15
        target: int = 12
        expected_output: int = -1
        self.assertEqual(num_buses_to_destination(routes, source, target), expected_output)

if __name__ == "__main__":
    unittest.main()
