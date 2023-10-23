function isPowerOfFour(n: number): boolean {
    return n > 0 && ((n & (n-1)) == 0) && ((n-1) % 3 == 0)
}

function testSolution() {
    type Test = {
        n: number,
        expected_output: boolean
    }

    let tests: Test[] = [
        {
            n: 16,
            expected_output: true
        },
        {
            n: 5,
            expected_output: false
        },
        {
            n: 1,
            expected_output: true
        },
    ]

    let failed = false
    for (let i=0; i<tests.length; i++) {
        const test = tests[i]
        let res: boolean = isPowerOfFour(test.n)
        if (res != test.expected_output) {
            console.log("Failed test %d: expected %s, return %s", i+1, test.expected_output, res)
            failed = true
        }
    }

    if (!failed) {
        console.log("Passed all tests!")
    }
}

testSolution()
