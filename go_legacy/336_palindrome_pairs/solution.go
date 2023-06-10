package palindromepairs

func palindromePairs(words []string) [][]int {
	res := [][]int{}
	for i := range words {
	Loop:
		for j := range words {
			if j != i {
				s := words[i] + words[j]
				for x, y := 0, len(s)-1; x < y; x, y = x+1, y-1 {
					if s[x] != s[y] {
						continue Loop
					}
				}
				res = append(res, []int{i, j})
			}
		}
	}
	return res
}

func palindromePairsMoreEficient(words []string) [][]int {
	res := [][]int{}
	for i := range words {
		j := 0
		NotPalindrome:
		for j < len(words[i]) {
			prefix := words[i][:j]
			for x, y := 0, len(prefix)-1; x < y; x, y = x+1, y-1 {
				if prefix[x] != prefix[y] {
					break NotPalindrome
				}
			}
			j++
		}
		back := ""
		for k := len(words[i]) - 1; k >= 0; k-- {
			back += string(words[i][k])
		}
		for l := 0; l <= j; l++ {
			prefix := back[:len(back) - l]
			for k := 0; k < len(words); k++ {
				if prefix == words[k] && i != k {
					res = append(res, []int{k, i})
					if words[k] == "" {
						res = append(res, []int{i, k})
					}
				}
			}
		}	
	}
	return res
}
