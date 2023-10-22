function constrainedSubsetSum(nums: number[], k: number): number {
    const aux = (i: number, l: number): number => {
        if (i == nums.length) {
            return l == 0 ? -Infinity : 0
        }
        if (l == 1) {
            return Math.max(
                nums[i] + aux(i+1, k),
                0,
            )
        }
        if (l == 0) {
            return Math.max(
                nums[i] + aux(i+1, k),
                aux(i+1, 0)
            )
        }
        return Math.max(
            nums[i] + aux(i+1, k),
            aux(i+1, l-1),
            0
        )
    }
    return aux(0, 0)
}

function testSolution() {
    type Test = {
        nums: number[],
        k: number,
        expected_output: number
    }

    let tests: Test[] = [
        {
            nums: [10,2,-10,5,20],
            k: 2,
            expected_output: 37
        },
        {
            nums: [-1,-2,-3],
            k: 1,
            expected_output: -1
        },
        {
            nums: [10,-2,-10,-5,20],
            k: 2,
            expected_output: 23
        }
    ]

    let failed: boolean = false
    for (let i=0; i<tests.length; i++) {
        const test: Test = tests[i]
        let res: number = constrainedSubsetSum(test.nums, test.k)
        if (res != test.expected_output) {
            console.log("Failed test %d: expected %d, returned %d", i+1, test.expected_output, res)
            failed = true
        }
    }

    if (!failed) {
        console.log("Passed all tests!")
    }
}

testSolution()
