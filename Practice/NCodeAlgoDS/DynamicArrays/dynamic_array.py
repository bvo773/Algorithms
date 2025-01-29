class Array:
    def __init__(self):
        self.capacity = 2
        self.length = 0
        self.arr = [0] * 2
    
    # Insert n in the last position of the array
    def pushback(self, n):
        if self.length == self.capacity:
            self.resize()
        # insert at next empty position 
        self.arr[self.length] = n
        self.length += 1

    def resize(self):
        # Create new array of double capacity
        self.capacity = 2 * self.capacity
        newArr = [0] * self.capacity

        # Copy elements to newArr
        for i in range(self.length):
            newArr[i] = self.arr[i]
        
        self.arr = newArr
    
    # Remove the last element in the array
    def popback(self):
        if self.length > 0:
            self.length -= 1
        return -1
    
    # Get value at i-th index
    def get(self, i):
        if i < self.length:
            return self.arr[i]
        return -1 # out of bounds or throw exception
    
    # Insert n at i-th index
    def insert(self, i, n):
        if i < self.length:
            self.arr[i] = n
            return
    
    def print(self):
        for i in range(self.length):
            print(self.arr[i])
        print()

    