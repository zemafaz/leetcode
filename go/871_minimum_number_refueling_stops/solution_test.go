package minimumnumberrefuelingstops

import "testing"

type args struct {
    target int
    startFuel int
    stations [][]int
    output int
}

func TestSolution(t *testing.T) {
    testArgs := [3]args{
        {
            target: 1,
            startFuel: 1,
            stations: [][]int{},
            output: 0,
        },
        {
            target: 100,
            startFuel: 1,
            stations: [][]int{{10,100}},
            output: -1,
        },
        {
            target: 100,
            startFuel: 10,
            stations: [][]int{{10,60},{20,30},{30,30},{60,40}},
            output: 2,
        },
    }

    for i, test := range testArgs {
        res := minRefuelStops(test.target,test.startFuel,test.stations)
        if res != test.output {
            t.Errorf("Test %d failed: wanted %v, returned %v", i+1, test.output, res)
        }
    }
}
