function backspaceCompare(s: string, t: string): boolean {
    const cleanup = function(text: string): string {
        let res = ""
        for (let c of text) {
            res = c == "#" ? res.slice(0, -1): res + c
        }
        return res
    }
    return cleanup(s) == cleanup(t)
}

function testSolution() {
    type Test = {
        s: string,
        t: string,
        expected_output: boolean
    }

    let tests: Test[] = [
        {
            s: "ab#c",
            t: "ad#c",
            expected_output: true
        },
        {
            s: "ab##",
            t: "c#d#",
            expected_output: true
        },
        {
            s: "a#c",
            t: "b",
            expected_output: false
        }
    ]

    let failed: boolean = false
    for (let i=0; i<tests.length; i++) {
        const test = tests[i]
        let res = backspaceCompare(test.s, test.t)
        if (res != test.expected_output) {
            console.log("Failed test %d: expected %s, returned %s", i+1, test.expected_output, res)
            failed = true
        }
    }

    if (!failed) {
        console.log("Passed all tests!")
    }
}

testSolution()
