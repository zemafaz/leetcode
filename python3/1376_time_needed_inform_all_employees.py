import unittest

def num_of_minutes(n: int, head_id: int, manager: list[int], inform_time: list[int]) -> int:
    stack = [head_id]
    next_stack = []
    inform_time_all = 0
    inform_time_level = 0
    while True:
        for i in range(n):
            if manager[i] == stack[-1]:
                inform_time_level = max(inform_time_level, inform_time[stack[-1]])
                manager[i] = -1
                next_stack.append(i)
        stack.pop()
        if not stack:
            inform_time_all += inform_time_level
            inform_time_level = 0
            stack = next_stack
            if not stack:
                break
    return inform_time_all

class TestSolution(unittest.TestCase):
    
    def test_1(self):
        n = 1
        head_id = 0
        manager = [-1]
        inform_time = [0]
        expected_output = 0
        output = num_of_minutes(n, head_id, manager, inform_time)
        self.assertEqual(expected_output, output)
    
    def test_2(self):
        n = 6
        head_id = 2
        manager = [2,2,-1,2,2,2]
        inform_time = [0,0,1,0,0,0]
        expected_output = 1
        output = num_of_minutes(n, head_id, manager, inform_time)
        self.assertEqual(expected_output, output)

if __name__ == '__main__':
    unittest.main()
