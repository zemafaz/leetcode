const prompt = require("prompt-sync")({sigint: true})
type NestedInteger = number | NestedInteger[]

class NestedIterator {

    private nestedList: NestedInteger[]
    private index: number[] = []

    constructor(nestedList: NestedInteger[]) {
        this.nestedList = nestedList
        this.index.push(0)
        let elem: NestedInteger = this.nestedList[0]
        while (elem instanceof Array) {
            this.index.push(0)
            elem = elem[0]
        }
        this.index[this.index.length-1] = -1
    }

    hasNext(): boolean {
        while (this.index.length != 0) {
            let elem: NestedInteger = this.nestedList
            for (let i=0; i < this.index.length - 1; i++) {
                const current_index = this.index[i]
                elem = elem[current_index] as NestedInteger[]
            }

            if (this.index[this.index.length-1] < elem.length - 1) {
                return true
            }
            this.index.pop()
        }
        return false
    }

    next(): number {
        this.index[this.index.length-1]++
        console.log("Index array: %j", this.index)
        let elem: NestedInteger = this.nestedList
        for (let i=0; i < this.index.length - 1; i++){
            const current_index: number = this.index[i]
            elem = elem[current_index] as NestedInteger[]
        }

        elem = elem[this.index[this.index.length - 1]]
        while (elem instanceof Array) {
            elem = elem[0]
            this.index.push(0)
        }
        return elem
    }
}

function testSolutionFunction(nestedList: NestedInteger[]): number[] {
    console.log("Nested List: %j", nestedList)
    var obj = new NestedIterator(nestedList)
    var a: number[] = []
    while (obj.hasNext()){
        a.push(obj.next())
        console.log("a: %j", a)
    }
    return a
}

function testSolution(): void {
    type Test = {
        nestedList: NestedInteger[],
        expected_output: number[]
    }

    let tests: Test[] = [
        {
            nestedList: [[1,1],2,[1,1]],
            expected_output: [1,1,2,1,1]
        },
        {
            nestedList: [1,[4,[6]]] ,
            expected_output: [1,4,6]
        }
    ]

    let failed: boolean = false

    for (let i=0; i<tests.length; i++) {
        const test: Test = tests[i]
        console.log("\n------- Test %d -------", i + 1)
        let res: number[] = testSolutionFunction(test.nestedList)
        if (!(res.length == test.expected_output.length &&
                res.every((v, i) => { return v == test.expected_output[i]}))) { 
            console.log("\nFailed test %d: expected %j, returned %j", i + 1, test.expected_output, res)
            failed = true
        }
    }

    if (!failed) {
        console.log("\nPassed all tests!")
    }
}

testSolution()
