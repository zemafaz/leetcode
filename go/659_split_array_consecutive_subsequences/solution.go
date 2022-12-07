package splitarrayconsecutivesubsequences

type res struct {
    last_n int
    count int
}

func isPossible(nums []int) bool {
    left := map[int]int{}
    end := map[int]int{}

    for _, num := range nums {
        if _, ok := left[num]; ok {
            left[num]++
        } else {
            left[num] = 1
        }
    }

    for _, num := range nums {
        if left[num] == 0 {
            continue
        }
        left[num]--
        if end[num - 1] > 0 {
            end[num-1]-- 
            end[num]++
        } else if left[num+1] > 0 && left[num+2] > 0 {
            left[num+1]--
            left[num+2]--
            end[num+2]++
        } else {
            return false
        }
    }
    return true
}
