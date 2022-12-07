package ransomnote

func canConstruct(ransomNote string, magazine string) bool {
Loop:
	for _, char := range ransomNote {
		for i, char2 := range magazine {
			if char == char2 {
				magazine = magazine[:i] + magazine[i+1:]
				continue Loop
			}
		}
		return false
	}
	return true
}
