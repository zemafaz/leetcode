package sortmatrixdiagonally

import "sort"

func diagonalSort(mat [][]int) [][]int {
	for x := range mat[0] {
		sortDiag(mat, 0, x)
	}
	for y := 1; y < len(mat); y++ {
		sortDiag(mat, y, 0)
	}
	return mat
}

func sortDiag(mat [][]int, y int, x int) {
	diag := []int{}
	i := 0
	j := 0
	for x + i < len(mat[0]) && y + j < len(mat) {
		diag = append(diag, mat[y+j][x+i])
		i++
		j++
	}
	sort.Slice(diag, func(i2, j2 int) bool {
		return diag[i2] < diag[j2]
	})
	i = 0
	j = 0
	for x + i < len(mat[0]) && y + j < len(mat) {
		mat[y+j][x+i] = diag[i]
		i++
		j++
	}
}
