package utils

func SumMatrix(matrix [][]int) int {
	res := 0
	for _, row := range matrix {
		for _, elem := range row {
			res += elem
		}
	}
	return res
}

func TransposeMatrix(matrix [][]int) [][]int {
	resMatrix := make([][]int, len(matrix[0]))
	for i := range resMatrix{
		resMatrix[i] = make([]int, len(matrix))
	}
	for i, row := range matrix {
		for j, elem := range row {
			resMatrix[j][i] = elem
		}
	}
	return resMatrix
}
