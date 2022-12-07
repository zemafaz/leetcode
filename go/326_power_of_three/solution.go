package powerofthree

import "math"

func isPowerOfThree(n int) bool {
    // 19 because 3 ** 20 > 2 ** 31 - 1
    return n > 0 && int(math.Pow(3, 19)) % n == 0
}
