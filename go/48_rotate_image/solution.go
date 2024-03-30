package rotateimage

func rotate(matrix [][]int) {
	for i, j := 0, len(matrix) - 1; i<j; i, j = i + 1, j - 1 {
		for k := range matrix[i] {
			matrix[i][k], matrix[j][k] = matrix[j][k], matrix[i][k]
		}
	}
	for i := range matrix {
		for j := range matrix[i] {
			if i < j {
				matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
			} 
		}
	}
}
