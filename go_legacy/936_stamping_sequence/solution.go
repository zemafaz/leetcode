package stampingsequence

func movesToStamp(stamp string, target string) []int {
	len_stamp := len([]rune(stamp))
	len_target := len([]rune(target))
	res := []int{}

	allSubed := make([]rune, len_stamp)
	for i := range allSubed {
		allSubed[i] = '?'
	}
	allSubedTarget := make([]rune, len_target)
	for i := range allSubedTarget {
		allSubedTarget[i] = '?'
	}

	for i := 0; i < 10*len_target; i++ {
		subed := false
		// for j:=len_target - len_stamp; j >=0; j-- {
		for j := 0; j <= len_target-len_stamp; j++ {
			substring := target[j : j+len_stamp]
			if substring != string(allSubed) {
				if compareStrings(substring, stamp) {
					res = append(res, j)
					target = target[:j] + string(allSubed) + target[j+len_stamp:]
					subed = true
					break
				}
			}
		}
		if subed == false {
			break
		}
		allSubedTargetString := string(allSubedTarget)
		if target == string(allSubedTargetString) {
			for t1, t2 := 0, len(res)-1; t1 < t2; t1, t2 = t1+1, t2-1 {
				res[t1], res[t2] = res[t2], res[t1]
			}
			return res
		}
	}

	return []int{}
}

func compareStrings(a, b string) bool {
	if len([]rune(a)) != len([]rune(b)) {
		return false
	}
	for i := range a {
		if a[i] == '?' || b[i] == '?' {
			continue
		}
		if a[i] == b[i] {
			continue
		} else {
			return false
		}
	}
	return true
}
