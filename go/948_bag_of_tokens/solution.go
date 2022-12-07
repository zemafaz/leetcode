package bagoftokens

import "sort"

func bagOfTokensScore(tokens []int, power int) int {
	score := 0
	sort.Slice(tokens, func(i, j int) bool {
		return tokens[i] < tokens[j]
	})
	for len(tokens) > 0 && (power >= tokens[0] || score > 0) {
		if score == 0 {
			power -= tokens[0]
			tokens = tokens[1:]
			score++
		 } else {
			 nSacrifices := 0
			 sumSacrifices := 0
			 for i := 0; i < len(tokens); i++ {
				 if sumSacrifices + tokens[i] <= power {
					 nSacrifices++
					 sumSacrifices += tokens[i]
				 } else {
					 break
				 }
			 }
			 if nSacrifices == len(tokens) {
				 score += nSacrifices
				 break
			 }
			 if len(tokens) > 1 {
				 power += tokens[len(tokens) - 1]
				 tokens = tokens[:len(tokens) - 1]
				 score--
			 } else {
				 break
			 }
		 }
	}
	return score
}
