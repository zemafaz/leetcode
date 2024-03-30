package reorderedpowerof2

func reorderedPowerOf2(n int) bool {
	counter := map[int]int{}
	for n > 0 {
		rem := n % 10
		_, exists := counter[rem]
		if exists {
			counter[rem] += 1
		} else {
			counter[rem] = 1
		}
		n = n / 10
	}
	Loop:
	for i:=0; i < 30; i++ {
		counter2 := map[int]int{}
		n = 1 << i
		for n > 0 {
			rem := n % 10
			_, exists := counter2[rem]
			if exists {
				counter2[rem] += 1
			} else {
				counter2[rem] = 1
			}
			n = n / 10
		}
		if len(counter) != len(counter2) {
			continue Loop
		}
		for j := range counter {
			if counter[j] != counter2[j] {
				continue Loop
			}
		}
		return true
	}
	return false
}
