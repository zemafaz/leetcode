package utf8validation

import "math"

func validUtf8(data []int) bool {
	trueLen := len(data) - 1
	if trueLen == 0 {
		return false
	} else if trueLen == 1 {
		if data[0] >= int(math.Pow(2, 7)) {
			return false
		}
	} else {
		n := 0
		for i := trueLen; i > 0; i-- {
			n += int(math.Pow(2, 8 - float64(i)))
		}
		if data[0] < n {
			return false
		}
		r := data[0] % n
		if r >= int(math.Pow(2, 7 - float64(trueLen))) {
			return false
		}
		for i := 1; i < trueLen; i++ {
			if data[i] < int(math.Pow(2, 7)) || data[i] >= int(math.Pow(2,7)) + int(math.Pow(2,6)) {
				return false
			}
		}
	}
	return true
}
