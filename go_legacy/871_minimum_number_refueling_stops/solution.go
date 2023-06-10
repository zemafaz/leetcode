package minimumnumberrefuelingstops

import "sort"

func minRefuelStops(target int, startFuel int, stations [][]int) int {
    stations = append(stations, []int{target,0})
    dp := make([]int, len(stations))
    prevDist := 0

    for i := range dp {
        startFuel -= stations[i][0] - prevDist
        prevDist = stations[i][0]
        if i > 0 {
            dp[i] = dp[i-1]
        }
        if startFuel >= 0 {
            continue
        }
        sort.Slice(stations[:i], func(j, k int) bool {
           return stations[j][1] > stations[k][1] 
        })
        for j := range stations[:i] {
            startFuel += stations[j][1]
            stations[j][1] = 0
            dp[i] += 1
            if startFuel >= 0 {
                break
            }
        }
        if startFuel < 0 {
            return -1
        }
    }

    return dp[len(dp)-1]
}
