package satisfiabilityequalityequations

func equationsPossible(equations []string) bool {
	dict := map[string]string{}
	for _, equation := range equations {
		if string(equation[1]) == "=" {
			dict[aux(dict, string(equation[0]))] = aux(dict, string(equation[3]))
		}
	}
	for _, equation := range equations {
		if string(equation[1]) == "!" {
			c1, exists1 := dict[string(equation[0])]
			c2, exists2 := dict[string(equation[3])]
			if exists1 && exists2 && c1 == c2 {
				return false
			}
		}
	}
	return true
}

func aux(dict map[string]string, c string) string {
	if _, exists := dict[c]; exists {
		if c != dict[c] {
			dict[c] = aux(dict, dict[c])
		}
	} else {
		dict[c] = c
	}
	return dict[c]
}
