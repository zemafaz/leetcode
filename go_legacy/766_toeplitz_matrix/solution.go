package toeplitzmatrix

func isToeplitzMatrix(matrix [][]int) bool {

	for i := range matrix {
		first := matrix[i][0]
		n := 1
		for i + n < len(matrix) && n < len(matrix[0]) {
			if matrix[i+n][n] != first {
				return false
			}
			n++
		}
	}

	for i := range matrix[0] {
		first := matrix[0][i]
		n := 1
		for i + n < len(matrix[0]) && n < len(matrix) {
			if matrix[n][i+n] != first {
				return false
			}
			n++
		}
	}
	return true
}
