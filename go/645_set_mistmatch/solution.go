package setmistmatch

import "sort"

func findErrorNums(nums []int) []int {
	sort.Slice(nums, func(i, j int) bool {
		return nums[i] < nums[j]
	})
	nums = append([]int{0}, nums...)

	res := make([]int, 2)
	found := false

	for i := 1; i < len(nums); i++ {
		if nums[i] == nums[i-1] {
			res[0] = nums[i]
			if found {
				break
			}
			found = true
		}
		if nums[i] != nums[i-1] + 1 {
			res[1] = nums[i-1] + 1
			if found {
				break
			}
			found = true
		}
	}

	return res
}
