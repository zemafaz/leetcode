import unittest

class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        left = 0
        right = len(arr) - 1
        i = -1
        
        while True:
            if x <= arr[left]:
                i = left
                break
            if x >= arr[right]:
                i = right
                break
            if right - left == 1:
                i = left if x - arr[left] <= arr[right] - x else right
                break
            middle = left + (right - left) // 2
            if arr[middle] == x:
                i = middle
                break
            elif arr[midde] < x:
                left = middle
            else:
                right = middle

        left = i
        right = i

        for i in range(1, k):
            if left - 1 < 0 and right + 1 == len(arr):
                return arr
            if left - 1 < 0:
                right += 1
            elif right + 1 == len(arr):
                left -= 1
            else:
                if x - arr[left] <= arr[right] - x:
                    left -= 1
                else:
                    right += 1
                
        return arr[left:right+1]

class TestSolution(unittest.TestCase):
    def test_1(self):
        arr = [1,2,3,4,5]
        k = 4
        x = 3
        output = [1,2,3,4]
        self.assertEqual(Solution().findClosestElements(arr, k, x), output)

    def test_2(self):
        arr = [1,2,3,4,5]
        k = 4
        x = -1
        output = [1,2,3,4]
        self.assertEqual(Solution().findClosestElements(arr, k, x), output)

if __name__ == "__main__":
    unittest.main()
