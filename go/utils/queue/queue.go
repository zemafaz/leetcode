package queue

import "errors"

type Node struct {
	Val any
	Next *Node
}

type Queue struct {
	length int
	start *Node
	end *Node
}

func (q *Queue) Len() int {
	return q.length
}

func (q *Queue) Peek() (any, error) {
	if q.length == 0 {
		return 0, errors.New("Queue is Empty")
	}
	return q.start.Val, nil
}

func (q *Queue) Push(e any) {
	newNode := Node{
		Val: e,
	}	
	if q.length == 0 {
		q.start = &newNode
		q.end = q.start
	} else {
		q.end.Next = &newNode
		q.end = q.end.Next
	}
	q.length++
}

func (q *Queue) Pop() (any, error) {
	if q.length == 0 {
		return 0, errors.New("Queue is Empty")
	}
	res := q.start
	q.start = q.start.Next
	q.length--
	if q.length == 0 {
		q.end = nil
	}
	res.Next = nil
	return (*res).Val, nil
}
