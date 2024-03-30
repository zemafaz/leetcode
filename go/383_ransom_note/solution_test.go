package ransomnote

import (
	"testing"
)

type args struct {
	ransomNote string
	magazine string
	output bool
}

func TestSolution(t *testing.T) {
	testArgs := []args{
		{
			ransomNote: "a",
			magazine: "b",
			output: false,
		},
		{
			ransomNote: "aa",
			magazine: "ab",
			output: false,
		},
		{
			ransomNote: "aa",
			magazine: "aab",
			output: true,
		},
	}
	
	for i, test := range testArgs {
		res := canConstruct(test.ransomNote, test.magazine)
		if res != test.output {
			t.Errorf("Failed test %d: expected %v, returned %v", i+1, test.output, res)
		}
	}
}
