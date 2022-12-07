package narytreelevelordertraversal

import "leetcode-solutions/utils"

func levelOrder(root *utils.Node) [][]int {
	if root == nil {
		return [][]int{}
	}
	res := [][]int{{root.Val}}
	queue := [][]*utils.Node{{root}}
	for {
		currLevel := &queue[len(queue)-1]
		nextRes := []int{}
		nextLevel := []*utils.Node{}
		for j:=0;j<len(*currLevel);j++ {
			for k:=0; k<len((*currLevel)[j].Children); k++ {
				nextRes = append(nextRes, (*currLevel)[j].Children[k].Val)
				nextLevel = append(nextLevel, (*currLevel)[j].Children[k])
			}
		}
		if len(nextRes) == 0 {
			break
		}
		queue = append(queue, nextLevel)
		res = append(res, nextRes)
	}
	return res
}
