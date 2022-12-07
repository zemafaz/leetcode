package uniquemorsecodewords

import "leetcode-solutions/utils"

func uniqueMorseRepresentation(words []string) int {
    MORSE := [...]string{".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."}
    trans := utils.Set[string]{}

    for _, word := range words {
        res := ""
        for _, char := range word {
            res += MORSE[int(char) - int('a')]
        }
        trans.Add(res)
    }
    return len(trans)
}
