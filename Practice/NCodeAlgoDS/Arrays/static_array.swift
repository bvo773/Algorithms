/*
    READING: O(1)
    INSERTION: O(N), if inserting at the end of array, O(1)
    DELETION: O(N), if deleting at the of the array, O(1)

*/


var arr: [Int?] = [1, 3, 5, 7, nil, nil, nil]


for i in 0..<arr.count {
    print("Element \(i): \(arr[i] ?? 0)")
}

/* DELETING FROM THE END OF AN ARRAY*/
func removeEnd(arr: inout[Int], length: Int) {
    if length > 0 {
        // Modifies original array when add 'inout' keyword
        // We would consider the length to be decreased by 1
        arr[length - 1] = 0 
    }
}

// removeEnd(arr: &arr, length: arr.count) // '&' passes the array by reference
// print(arr)


/* DELETING AT ith index*/
// Remove value at index i before shifting elements to the left
// Assuming i is a valid index
func removeMiddle(arr: inout [Int?], i: Int, length: Int) {
    for index in i+1..<length {
        arr[index-1] = arr[index]
    }
    // No need to 'remove' arr[i] since we already shifted
}

// removeMiddle(arr: &arr, i: 1, length: arr.count)

/* INSERTING AT THE END */

func insertEnd(_ arr: inout [Int?],_ n: Int,_ length: Int,_ capacity: Int) {
    if length < capacity {
        arr[length] = n
    }
}

/* INSERT AT THE MIDDLE */
// Insert n into index i after shifting elements to the right.
// Assuming i is a valid index and arr is not full
func insertMiddle(_ arr: inout [Int?], _ i: Int, _ n: Int, _ length: Int) {
    for index in stride(from: length - 1, through: i, by: -1) {
        arr[index + 1] = arr[index] // Shift elements to the right
    }
    arr[i] = n
}
insertMiddle(&arr, 1, 2, 4)
print(arr)