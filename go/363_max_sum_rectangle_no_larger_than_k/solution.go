package maxsumrectanglenolargerthank

import (
	"leetcode-solutions/utils"
	"math"
)

func maxSumSubmatrix(matrix [][]int, k int) int {
	row := len(matrix)
	col := len(matrix[0])
	if col > row {
		matrix = utils.TransposeMatrix(matrix)
		row, col = col, row
	}
	res := math.MinInt
	for i := 0; i < col; i++ {
		sums := make([]int, row)
		for j := i; j < col; j++ {
			for l := 0; l < row; l++ {
				sums[l] += matrix[l][j]	
			}

			accuSet := utils.Set[int]{}
			accuSet.Add(0)
			curSum, curMax := 0, math.MinInt
			for _, sum := range sums {
				curSum += sum
				_, exists := accuSet[curSum - k]
				var lowerBound int = math.MaxInt
				if exists {
					lowerBound = curSum - k
				} else {
					for elem := range accuSet {
						if elem > curSum - k && elem < lowerBound {
							lowerBound = elem
						}
					}
				} 
				if lowerBound != math.MaxInt {
					curMax = int(math.Max(float64(curMax), float64(curSum - lowerBound)))
				}
				accuSet.Add(curSum)
			}
			res = int(math.Max(float64(res), float64(curMax)))
		}
	}
	return res
}
