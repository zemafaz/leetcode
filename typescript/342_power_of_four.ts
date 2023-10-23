function isPowerOfFour(n: number): boolean {
    return n > 0 && ((n & (n-1)) == 0) && ((n-1) % 3 == 0)
}

function isPowerOfFourRec(n: number): boolean {
    if (n <= 0) return false
    if (n == 1) return true
    if (n % 4 != 0) return false
    return isPowerOfFourRec(n / 4)
}

function testSolution() {
    type Test = {
        n: number,
        expected_output: boolean
    }

    type functionTest = (n: number) => boolean

    let functions: functionTest[] = [
        isPowerOfFour,
        isPowerOfFourRec
    ]

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
    for (const f of functions) {
        for (let i=0; i<tests.length; i++) {
            const test = tests[i]
            let res: boolean = f(test.n)
            if (res != test.expected_output) {
                console.log("Failed function %s, test %d: expected %s, return %s", f.name, i+1, test.expected_output, res)
                failed = true
            }
        }
    }

    if (!failed) {
        console.log("Passed all tests!")
    }
}

testSolution()
