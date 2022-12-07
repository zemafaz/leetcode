package integertoroman

import (
	"strings"
)

func intToRoman(num int) string {
	symbols := []string{"I", "V", "X", "L", "C", "D", "M"}
	res := ""
	i := 0
	for true{
		alg := num % 10
		current := ""
		if alg < 5 {
			if alg == 4 {
				current = symbols[i] + symbols[i + 1]
			} else {
				current = strings.Repeat(symbols[i], alg)
			}
		} else {	
			if alg == 9 {
				current = symbols[i] + symbols[i + 2]
			} else {
				current = symbols[i + 1] + strings.Repeat(symbols[i], alg - 5)
			}
		}
		res = current + res
		num = num / 10
		i += 2
		if num == 0 {
			break
		}
	}
	return res
}
