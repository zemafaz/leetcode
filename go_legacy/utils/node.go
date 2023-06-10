package utils

import (
	"strings"
	"strconv"
)

type Node struct {
	Val int
	Children []*Node
}

func StringToNode(s string) *Node {
	s = s[1:len(s)-1]
	sSplit := strings.Split(s, ",")
	if len(sSplit) == 0 {
		return nil
	}
	val, err := strconv.Atoi(sSplit[0])
	if err != nil {
		panic(err)
	}
	root := &Node{
		Val: val,
		Children: []*Node{},
	}

	currLevel := []*Node{}	
	queue := []*Node{root}
	i := 2
	j := 0

	for i < len(sSplit) || j < len(queue) {
		for i < len(sSplit) && sSplit[i] != "null" {
			n, err := strconv.Atoi(sSplit[i])
			if err != nil {
				panic(err)
			}
			node := &Node{
				Val: n,
				Children: []*Node{},
			}
			currLevel = append(currLevel, node)
			queue = append(queue, node)
			i++
		}
		// copy(queue[j].Children, currLevel)
		queue[j].Children = append(queue[j].Children, currLevel...)
		currLevel = []*Node{}
		i++
		j++
	}
	return root
}
