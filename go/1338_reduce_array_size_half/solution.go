package reducearraysizehalf

import "sort"

func minSetSize(arr []int) int {
    count := make(map[int]int)
    for _, e := range arr{
        if _, ok := count[e]; ok {
            count[e]++
        } else {
            count[e] = 1
        }
    }
    countList := []int{}
    for key := range count {
        countList = append(countList, key)
    }
    sort.Slice(countList, func(i, j int) bool {
        return count[countList[i]] > count[countList[i]]
    })
    goal := 0
    for i, e := range countList {
        goal += count[e]
        if goal >= len(arr) / 2 {
            return i + 1
        }
    }
    return len(countList)
}
