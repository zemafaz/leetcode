package utils

import "testing"

func TestCopyLinkedList(t *testing.T) {
    linkedList := ConvertToLinkedList([]int{1,2,3,4,5})
    copyList := Copy(linkedList)

    if !Equals(linkedList, copyList) {
        t.Error("Failed copy test") 
    }
}

func TestEqualsLinkedList(t *testing.T) {
    linkedList := ConvertToLinkedList([]int{1,2,3,4,5})
    copyList := Copy(linkedList)
    copyList.Next.Val = 9
    want := ConvertToLinkedList([]int{1,9,3,4,5})
    if !Equals(want, copyList) {
        t.Errorf("Failed equals test")
    }
}

func TestGetLinkedList(t *testing.T) {
    linkedList := ConvertToLinkedList([]int{1,2,3})
    res := linkedList.Get(2)
    want := 3
    if res.Val != want {
        t.Errorf("Failed get test")
    }
}

func TestStringToNode(t *testing.T) {
	root := "[1,null,3,2,4,null,5,6]"
	StringToNode(root)
}
