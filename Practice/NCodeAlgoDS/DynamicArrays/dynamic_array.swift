// Swift arrays are dynamic when using 'var' to declare the array, but this is an example of resizing
class Array {
    var capacity = 2
    var length = 0
    var arr = Swift.Array(repeating: 0, count: 2) // Array of capacity 2

    func pushback(_ n: Int) {

        if self.length == self.capacity {
            resize()
        }
        self.arr[length] = n
        self.length += 1
    }

    func resize() {
        // Create a new array of double capacity
        var newArray = Swift.Array(repeating: 0, count: self.capacity * 2) 
        
        // Copy elements to newArr
        for i in 0..<self.length {
            newArray[i] = self.arr[i]
        }
        self.arr = newArray
    }

    // Remove the last element in the array
    func popback() {
        if self.length > 0 {
            self.length -= 1
        }
    }

    // Get value at i-th index
    func get(_ i: Int) -> Int {
        if i < self.length {
            return self.arr[i]
        }
        return -1 // Out of bounds
    }

    func print() {
        for i in 0..<self.length {
            Swift.print(arr[i], terminator: " ")
        }
        Swift.print()
    }
}