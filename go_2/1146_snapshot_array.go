package main

import "fmt"

type SnapshotArray struct {
    array [][]int
}

func Len(sArray SnapshotArray) int {
    return len(sArray.array[0])
}

func Constructor(length int) SnapshotArray {
    var first []int = make([]int, length)
    var snapArray SnapshotArray = SnapshotArray{}
    snapArray.array = append(snapArray.array, first)
    return snapArray
}

func (this *SnapshotArray) Set(index int, val int) {
    this.array[len(this.array) - 1][index] = val
}

func (this *SnapshotArray) Snap() int {
    var nextShot []int = make([]int, len(this.array[0]))
    copy(nextShot, this.array[len(this.array) - 1])
    this.array = append(this.array, nextShot)
    return len(this.array) - 2
}

func (this *SnapshotArray) Get(index int, snap_id int) int {
    return this.array[snap_id][index]
}

func main() {
    var expected_result int = 3
    var snapMachine SnapshotArray = Constructor(expected_result)
    if Len(snapMachine) != expected_result {
        fmt.Printf("Failed Constructor: expected len = %d, returned len = %d\n", expected_result, Len(snapMachine))
        return
    }

    snapMachine.Set(0,5)

    var snap int = snapMachine.Snap()
    expected_result = 0
    if snap != expected_result {
        fmt.Printf("Failed Snap: expected %d, returned %d\n", expected_result, snap)
        return
    }
    
    snapMachine.Set(0,6)
    var value int = snapMachine.Get(0,0)
    expected_result = 5
    if value != expected_result {
        fmt.Printf("Failed Get: expected %d, returned %d\n", expected_result, value)
        return
    }

    fmt.Println("Passed all tests!")
}
