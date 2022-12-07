package numberweakcharactersingame

import "sort"

func numberOfWeakCharacters(properties [][]int) int {
	res := 0
	strongest := 0

	sort.Slice(properties, func(i, j int) bool {
		if properties[i][0] == properties[j][0] {
			return properties[i][1] < properties[j][1]
		}
		return properties[i][0] > properties[j][0] 
	})
	
	for _, character := range properties {
		if character[1] < strongest {
			res++
		 } else {
			 strongest = character[1]
		 }
	}

	return res
}
