package findduplicatefilesystem

import (
	"regexp"
	"strings"
)

func findDuplicate(paths []string) [][]string {
	res := map[string][]string{}
	for _, dir := range paths {
		args := strings.Split(dir, " ")
		for i := 1; i < len(args); i++ {
			r := regexp.MustCompile(`(.+)\((.+)\)$`)
			m := r.FindStringSubmatch(args[i])
			if len(m) != 3 {
				panic("This is not right!")
			}
			path := args[0] + "/" + m[1]
			content := m[2]
			r, m = nil, nil
			if _, exists := res[content]; exists {
				res[content] = append(res[content], path)	
			} else {
				res[content] = []string{path}
			}
		}
	}
	sliceRes := [][]string{}
	for i := range res {
		sliceRes = append(sliceRes, res[i])
	}
	return sliceRes
}
