function binarySearch(elem: number, array: number[], leftmost: boolean = true,  low: number = 0, high: number = array.length - 1): number {

    if (elem <= array[low]) {
        return low
    }
    if (elem >= array[high]) {
        return array.length
    }
    while (low < high - 1) {
        let middle: number = low + Math.floor((high - low) / 2)

        if (leftmost) {
            if (elem <= array[middle]) {
                high = middle
            } else {
                low = middle
            }
        }
        else {
            if (elem < array[middle]) {
                high = middle
            } else {
                low = middle
            }

        }
    }

    return high
}

function fullBloomFlowers(flowers: number[][], people: number[]): number[] {
    console.group("fullBloomFlowers(flowers = %j, people = %j)", flowers, people)
    let flowers_begin: number[] = flowers.map((flower) => flower[0]).sort((a,b) => a - b)
    let flowers_end: number[] = flowers.map((flower) => flower[1]).sort((a,b) => a - b)

    console.log("Flowers begin: %j", flowers_begin)
    console.log("Flowers end: %j", flowers_end)
    
    people = people.map(element => {
        let flowers_bloomed = binarySearch(element, flowers_begin, false)
        let flowers_dead = binarySearch(element, flowers_end, true)

        console.log("Person: %d", element)
        console.log("Flowers bloomed: %d", flowers_bloomed)
        console.log("Flowers end: %d", flowers_dead)

        return flowers_bloomed - flowers_dead
    });

    console.groupEnd()
    return people
}

type Test = {
    flowers: number[][],
    people: number[],
    expected_output: number[],
}

function testSolution(): void {
    const tests: Test[] = [
        {
            flowers: [[1,6],[3,7],[9,12],[4,13]],
            people: [2,3,7,11],
            expected_output: [1,2,2,2]
        },
        {
            flowers: [[1,10],[3,3]],
            people: [3,3,2],
            expected_output: [2,2,1]
        },
    ]

    let failed = false
    for (let i = 0; i < tests.length; i++) {
        const t = tests[i]
        const res = fullBloomFlowers(t.flowers, t.people)
        if (res.toString() !== t.expected_output.toString()) {
            console.log("Failed test %d: expected %j, returned %j", i+1, t.expected_output, res)
            failed = true
        }
    }

    if (!failed) {
        console.log("Passed all tests!")
    }
}

testSolution()

