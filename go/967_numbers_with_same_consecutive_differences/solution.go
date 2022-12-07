package numberswithsameconsecutivedifferences

import "math"

func numsSameConsecDiff(n int, k int) []int {
	res := []int{}
	for i:=1; i<10; i++ {
		for j:=0; j<10; j++ {
			if int(math.Abs(float64(i) - float64(j))) == k {
				num := 0
				alt := 1
				for l:=n-1; l >= 0; l-- {
					num += i * int(math.Pow10(l)) * alt + j * int(math.Pow10(l)) * (1 - alt)
					alt = 1 - alt
				}
				res = append(res, num)
			}
		}
	}
	return res
}
