package pacificatlanticwaterflow

type found struct {
	pacific bool
	atlantic bool
}

var foundState = found{
	pacific: false,
	atlantic: false,
}

func pacificAtlantic(heights [][]int) [][]int {
	res := [][]int{}
	for i := range heights {
		for j := range heights[i] {
			foundState.atlantic = false
			foundState.pacific = false
			if spread(heights, [][]int{{i,j}}) {
				res = append(res, []int{i,j})
			}
		}
	}
	return res
}

var directions = [][]int{{1,0}, {-1,0}, {0,1}, {0,-1}}

func spread(heights [][]int, visited [][]int) bool {
	i, j := visited[len(visited) - 1][0], visited[len(visited) - 1][1]
	currHeight := heights[i][j]
	if i - 1 < 0 || j - 1 < 0 {
		foundState.pacific = true
	}
	if i + 1 == len(heights) || j + 1 == len(heights[i]) {
		foundState.atlantic = true
	}
	if foundState.pacific && foundState.atlantic {
		return true
	}
	for _, elem := range directions {
		nextI := i + elem[0]
		nextJ := j + elem[1]
		if nextI >= 0 &&
			nextI < len(heights) &&
			nextJ >= 0 &&
			nextJ < len(heights[i]) &&
			heights[nextI][nextJ] <= currHeight &&
			!wasVisited([]int{nextI, nextJ}, visited) {
				spread(heights, append(visited, []int{nextI,nextJ}))
			}
	}
	return foundState.pacific && foundState.atlantic
}

func wasVisited(pos []int, slice [][]int) bool {
	for _, elem := range slice {
		if pos[0] == elem[0] && pos[1] == elem[1] {
			return true
		}
	}
	return false
}
