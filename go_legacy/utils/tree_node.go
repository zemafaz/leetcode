package utils

import (
	"strconv"
	"strings"
)

type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}

func StringToTreeNode(s string) *TreeNode {
	s = s[1:len(s)-1]
	sSplit := strings.Split(s, ",")
	if len(sSplit) == 0 || sSplit[0] == "" {
		return nil
	}
	val, err := strconv.Atoi(sSplit[0])
	if err != nil {
		panic(err)
	}
	root := &TreeNode{
		Val: val,
	}
	queue := []*TreeNode{root}
	i := 1
	for i < len(sSplit) {
		child, err := strconv.Atoi(sSplit[i])
		if err == nil {
			left := &TreeNode {
				Val: child,
			}
			queue[0].Left = left
			queue = append(queue, left)
		}
		i++
		if i >= len(sSplit) {
			break
		}
		child, err = strconv.Atoi(sSplit[i])
		if err == nil {
			right := &TreeNode{
				Val: child,
			}
			queue[0].Right = right
			queue = append(queue, right)
		}
		i++
		queue = queue[1:]
	}
	return root	
}

func TreeNodeToString(t *TreeNode) string {
	s := "["
	output := ""
	if t != nil {
		q := []*TreeNode{t}
		for len(q) != 0 {
			if q[0] == nil {
				output += "null,"
				continue
			} else {
				output += strconv.Itoa(q[0].Val) + ","
			}
			q = append(q, q[0].Left, q[0].Right)
		}
	}
	if output != "" {
		output = output[:len(output)-1]
	}
	s += output + "]"
	return s
}

func TreeNodeEquals(t1 *TreeNode, t2 *TreeNode) bool {
	if t1 == nil && t2 == nil {
		return true
	}
	if (t1 == nil && t2 != nil) || (t1 != nil && t2 == nil) {
		return false
	}
	if t1.Val != t2.Val {
		return false
	}
	return TreeNodeEquals(t1.Left, t2.Left) && TreeNodeEquals(t1.Right, t2.Right)
}
