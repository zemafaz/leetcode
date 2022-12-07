package utils

type ListNode struct {
	Val  int
	Next *ListNode
}

func ConvertToSlice(node *ListNode) []int {
	if node == nil {
		return []int{}
	} else {
		return append([]int{node.Val}, ConvertToSlice(node.Next)...)
	}
}

func ConvertToLinkedList(slice []int) *ListNode {
	if len(slice) == 0 {
		return nil
	}

	head := ListNode{
		Val: slice[0],
	}

	node := &head

	for i := 1; i < len(slice); i++ {
		node.Next = &ListNode{
			Val: slice[i],
		}
		node = node.Next
	}
	return &head
}

func Copy(node *ListNode) *ListNode {
	if node == nil {
		return nil
	}
	newNode := &ListNode{
		Val:  node.Val,
		Next: Copy(node.Next),
	}
	return newNode
}

func Equals(ll1 *ListNode, ll2 *ListNode) bool {
	if ll1 == nil && ll2 == nil {
		return true
	}
	if ll1 == nil || ll2 == nil {
		return false
	}
	if ll1.Val != ll2.Val {
		return false
	}
	return Equals(ll1.Next, ll2.Next)
}

func (node *ListNode) Get(i int) *ListNode {
    iter := node
    for i >= 0 {
        if iter == nil {
            break
        }
        if i == 0 {
            return iter
        }
        i--
        iter = iter.Next
    }
    panic("Index out of range")
}
