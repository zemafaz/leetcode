package queue

import (
	"testing"
)

func TestQueue(t *testing.T) {
	q := Queue{}
	testPush(&q, 1, t)	
	testPeek(&q, 1, t)
	testLen(&q, 1, t)
	testPop(&q, 1, t)
	testPopEmpty(&q, t)
}

func testPush(q *Queue, val any, t *testing.T) {
	initialLen := q.length
	// currentEnd := q.end
	q.Push(val)
	if q.start.Val != val || q.length != initialLen + 1 {
		t.Errorf("Failed Push")
	}
}

func testPeek(q *Queue, val any, t *testing.T) {
	e, _ := q.Peek()
	if e != val {
		t.Errorf("Failed Peek")
	}
}

func testLen(q *Queue, l int, t *testing.T) {
	if q.Len() != l {
		t.Errorf("Failed Len")
	}
}

func testPop(q *Queue, val any, t *testing.T) {
	initialLen := q.length
	nextStart := q.start.Next
	e, _ := q.Pop()	
	if e != val || q.length != initialLen - 1 || q.start != nextStart{
		t.Errorf("Failed Pop")
	}
}

func testPopEmpty(q *Queue, t *testing.T) {
	_, err := q.Pop()
	if err == nil {
		t.Errorf("Failed Pop Empty")
	}
}
