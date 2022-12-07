package sumevennumbersafterqueries

func sumEvenAfterQueries(nums []int, queries [][]int) []int {
	currentSum := 0
	for i := range nums {
		if nums[i] % 2 == 0 {
			currentSum += nums[i]
		}
	}
	res := []int{}
	for _, query := range queries {
		if nums[query[1]] % 2 == 0 {
			currentSum -= nums[query[1]]
		}
		nums[query[1]] += query[0]
		if nums[query[1]] % 2 == 0 {
			currentSum += nums[query[1]]
		}
		res = append(res, currentSum)
	}
	return res
}
