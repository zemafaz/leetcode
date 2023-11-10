import unittest

def restore_array(adjacent_pairs: list[list[int]]) -> list[int]:
    one_element: set[int] = set()
    for pair in adjacent_pairs:
        for num in pair:
            if num in one_element:
                one_element.remove(num)
            else:
                one_element.add(num)
    
    res: list[int] = [0 for _ in range(len(adjacent_pairs) + 1)]
    added: list[bool] = [False for _ in enumerate(adjacent_pairs)]

    for i, _ in enumerate(res):
        if i == 0:
            res[0] = one_element.pop()
            continue
        for k, pair in enumerate(adjacent_pairs):
            def aux(pair: list[int]) -> bool:
                for j, num in enumerate(pair):
                    if num == res[i-1] and not added[k]:
                        res[i] = pair[1-j]
                        added[k] = True
                        return True
                return False
            if aux(pair):
                continue

    return res
                    

class TestSolution(unittest.TestCase):
    
    def test_1(self):
        adjacent_pairs: list[list[int]] = [[2,1], [3,4], [3,2]]
        expected_output: list[list[int]] = [[1,2,3,4], [4,3,2,1]]
        res: list[int] = restore_array(adjacent_pairs)
        self.assertTrue(res in expected_output, f"Returned {res}, expected 1 of {expected_output}")

    def test_2(self):
        adjacent_pairs: list[list[int]] = [[4,-2], [1,4], [-3,1]]
        expected_output: list[list[int]] = [[-2,4,1,-3], [-3,1,4,-2]]
        res: list[int] = restore_array(adjacent_pairs)
        self.assertTrue(res in expected_output, f"Returned {res}, expected 1 of {expected_output}")

    def test_3(self):
        adjacent_pairs: list[list[int]] = [[100000, -100000]]
        expected_output: list[list[int]] = [[100000, -100000], [-100000, 100000]]
        res: list[int] = restore_array(adjacent_pairs)
        self.assertTrue(res in expected_output, f"Returned {res}, expected 1 of {expected_output}")

if __name__ == "__main__":
    unittest.main()
