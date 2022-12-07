package findoriginalarraydoubledarray

import "sort"

func findOriginalArray(changed []int) []int {
	if len(changed) % 2 == 1 {
		return []int{}
	}
	sort.Ints(changed)
	changedLen := len(changed)
	for i:=0; i < changedLen; i++{
		j := sort.SearchInts(changed, changed[i] * 2)
		if  j == changedLen || changed[j] != changed[i] * 2 || (changed[j] == 0 && changed[j+1] != 0) {
			return []int{}
		}
		changed = append(changed[:j], changed[j+1:]...)
		changedLen--
	}
	return changed
}
