package uniquemorsecodewords

import "testing"

type args struct{
    words []string
    output int
}

func TestUniqueMorseRepresentation(t *testing.T) {
    testArgs := []args{
        {
            words: []string{"gin","zen","gig","msg"},
            output: 2,
        },
        {
            words: []string{"a"},
            output: 1,
        },
    }

    for _, test := range testArgs{
        res := uniqueMorseRepresentation(test.words)
        if res != test.output {
            t.Error(res, test.output)
        }
    }
}
