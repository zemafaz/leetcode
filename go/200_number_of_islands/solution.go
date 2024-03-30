package numberofislands

func numIslands(grid [][]byte) int {
	res := 0
	for y, row := range grid {
		for x, elem := range row {
			if elem == 1 {
				res += 1
				removeIsland(grid, x, y)
			}
		}
	}
	return res
}

func removeIsland(grid [][]byte, x, y int){
	grid[y][x] = 0
	switch {
	case y - 1 >= 0 && grid[y-1][x] == 1:
		removeIsland(grid, x, y-1)
	case y + 1 < len(grid) && grid[y+1][x] == 1:
		removeIsland(grid, x, y+1)
	case x - 1 >= 0 && grid[y][x-1] == 1:
		removeIsland(grid, x-1, y)
	case x + 1 < len(grid[0]) && grid[y][x+1] == 1:
		removeIsland(grid, x+1, y)
	}
}
