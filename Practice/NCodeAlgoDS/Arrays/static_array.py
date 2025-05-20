'''
[1, 3 , 5]
- Static because the size cannot change once declared. Common languages like Java, C++, and C#
- Once array is full, it cannot store additional elements
'''

''' Reading from an Array'''
# initialize array
myArray = [1, 3, 5, None, None]

# access an arbritary element, where i is the index of the desired value, O(1) complexity
#myArray[i]


# Traversing an array using loops
for i in range(len(myArray)):
    print(myArray[i])

# OR

i = 0
while i < len(myArray):
    print(myArray[i])
    i += 1

'''
To traverse through an array of size n the time complexity is O(n)
This means the number of operations grows linearly with the size of the array.

For example, with an array of size 10 we would have to perform 10 operations to traverse through it, 
with an array of size 100 we would have to perform 100 operations, and so on.
'''

'''DELETING FROM AN ARRAY'''
'''Deleting from the end of an array'''
# Remove from the last postion in the array if the array
# is not empty (i.e length is non-zero)
def removeEnd(arr, length):
    if length > 0:
        arr[length-1] = 0

'''
DELETING AT ith index
    1. We are give the index i.
    2. We iterate starting from i + 1 until the end of the array
    3. We shift each element to the left
    4. (Optional) We replace the last element with a or null to mark it empty, amd decrement the length by 1.
'''
# Remove value at index i before shifting elements to the left
# Assuming i is a valid index
def removeMiddle(arr, i, length):
    # Shift starting from i + 1 to the end
    for index in range(i+1, length):
        arr[index - 1] = arr[index]
'''
The worst case would be that we need to shift all of the elements to the left. 
This would occur if the target index is the first index of the array. Therefore, the code above is 
O(n).
'''
'''
TEST
print(f"{myArray}")
removeMiddle(myArray, 1, 3)
print(f"{myArray}")
'''

'''INSERT END'''
# Insert n into arr at the next open position
# Length is the number of 'real' values in arr, and capacity
# is the size (aka memory allocated for the fixed size array)
def insertEnd(arr, n, length, capacity):
    if length < capacity:
        arr[length] = n

'''
   Since we are writing a single value to the array, the time complexity is O(1)
   Note: length is the number of elements inside the array whereas capacity refers to the maximum number of elements the array can hold
'''

'''
INSERTING AT THE ith index
    consider arr = [4, 5, 6] -> insert at index i = 1, i = 0
    cannot overwrite original value, instead we shift all values
    starting at index i, one position to the right
'''

# Insert n into index i after shifting elements to the right
# Assuming i is a valid index and arr is not full
def insertMiddle(arr, i, n, length):
    for index in range(length - 1, i - 1, -1):
        arr[index + 1] = arr[index]

    arr[i] = n

print(myArray)
insertMiddle(myArray, 1, 2, 3)
print(myArray)
