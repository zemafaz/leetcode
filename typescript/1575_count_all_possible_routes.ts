function countRoutes(locations: number[], start: number, finish: number, fuel: number): number {
    let number_routes: number = 0 
    for (let i=0; i<locations.length; i++) {
        if (i != start) {
            let diff: number = Math.abs(locations[i] - locations[start])
            if (fuel - diff < 0) {
                continue
            }
            if (i == finish) {
                number_routes += 1
            }
            number_routes += countRoutes(locations, i, finish, fuel - diff)
        }
    }
    return number_routes
}

function testSolution() {
    type Test = {
        locations: number[],
        start: number,
        finish: number,
        fuel: number,
        expected_output: number
    }

    const tests: Test[] = [
        {
            locations: [2,3,6,8,4],
            start: 1,
            finish: 3,
            fuel: 5,
            expected_output: 4
        },
        {
            locations: [4,3,1],
            start: 1,
            finish: 0,
            fuel: 6,
            expected_output: 5
        },
        {
            locations: [5,2,1],
            start: 0,
            finish: 2,
            fuel: 3,
            expected_output: 0
        }
    ]

    let failed = false
    for (let i=0; i < tests.length; i++) {
        const test = tests[i]
        const res: number = countRoutes(test.locations, test.start, test.finish, test.fuel)
        if (res !== test.expected_output) {
            console.log("Failed test %d: expected %d, returned %d", i + 1, test.expected_output, res)
            failed = true
        }
    }

    if (!failed) {
        console.log("Passed all tests!")
    }

}

testSolution()
