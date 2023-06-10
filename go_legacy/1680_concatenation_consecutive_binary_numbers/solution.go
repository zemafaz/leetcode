package concatenationconsecutivebinarynumbers

import "math"

func concatenatedBinary(n int) int {
	res := 1
	for i := 2; i <= n; i++ {
		l := int(math.Log2(float64(i))) + 1
		res = res << l | i
	}
	return res % (int(math.Pow10(9) + 7))
}
