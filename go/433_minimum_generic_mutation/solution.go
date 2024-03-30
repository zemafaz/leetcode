package minimumgenericmutation

func minMutation(start string, end string, bank []string) int {
	for i, s := range bank {
		if s == end {
			break
		}
		if i == len(bank) - 1 {
			return -1
		}
	}
	res := 0
	for i := range start {
		if start[i] != end[i] {
			res++
		}
	}
	return res
}
