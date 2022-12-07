package earliestpossibledayfullbloom

import (
	"sort"
)

func earliestFullBloom(plantTime []int, growTime []int) int {
	type auxTime struct {
		pos int
		time int
	}

	aux := make([]auxTime, len(growTime))

	for i, g := range growTime {
		aux[i] = auxTime{
			pos: i,
			time: g,
		}
	}

	sort.Slice(aux, func(i, j int) bool {
		return aux[i].time > aux[j].time
	})

	sum := 0
	res := 0

	for i := range aux {
		sum += plantTime[aux[i].pos]
		if sum + aux[i].time > res {
			res = sum + aux[i].time
		}
	}

	return res
}
