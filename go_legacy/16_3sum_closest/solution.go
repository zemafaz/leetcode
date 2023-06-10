package threesumclosest

import (
	"math"
	"sort"
)

func threeSumClosest(nums []int, target int) int {
	closestSum := nums[0] + nums[1] + nums[2]
	for i := 0; i < len(nums) - 2; i++ {
		for j := i + 1; j < len(nums) - 1; j++ {
			for k := j + 1; k < len(nums); k++ {
				sum := nums[i] + nums[j] + nums[k]
				if math.Abs(float64(target - sum)) < math.Abs(float64(target - closestSum)){
					closestSum = sum
				}
			}
		}
	}
	return closestSum
}

func threeSumClosestEfficient(nums []int, target int) int {
	sort.Slice(nums, func(i, j int) bool {
		return nums[i] < nums[j]
	})
	closestSum := nums[0] + nums[1] + nums[2]
	for i := 0; i < len(nums) - 2; i++ {

		j, k := i + 1, len(nums) - 1

		for j < k {
			sum := nums[i] + nums[j] + nums[k]
			
			if sum == target {
				return sum
			} else if sum < target {
				j++
			} else {
				k--
			}

			if math.Abs(float64(sum - target)) < math.Abs(float64(closestSum - target)) {
				closestSum = sum
			}
		}
	}
	return closestSum
}
