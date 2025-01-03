# [A] Array Deletions
'''
Deletion in an Array works smilimar to insertion, and has the same three different cases:

  1. Deleting the last element of the Array - O(1) Least consuming time of three cases0
  2. Deleting the first element of the Array - O(N) Costlieth
  3. Deletion at any given index
'''

# DELETING FROM THE END OF AN ARRAY
'''
- Deletion at the end of an Array is similar to people standing in a line, aka a queue.
- The person who recently joined the queue(at the end) can leave any time. 
- Deleting from the end is the least time consuming of the three cases.
- Recall insertion at the end of an array was also the least time consuming case.
- We can use the 'length' variable to keep track of the current elements added into the array.
The variable keeps track of the next index that is free for inserting a new element
'''
#Declare an array of 10 elements
intArray = [None] * 10 

# The array currently cotains 0 elements
length = 0

# Add elements at the first 6 indexes of the Array
for i in range(6):
  intArray[i] = i
  length += 1

# length = len(arr) - we are looking every valid index of the Array
def printArray(arr):
  for i in range(len(arr)):
    print(f"Index {i} contains {arr[i]}")

# length variable - We only want to look at the ones the we have put values into. 
def printArray2(arr):
  for i in range(0, length):
    print(f"Index {i} contains {arr[i]}")

print("DELETING FROM THE END ON AN ARRAY - INITIAL")
printArray2(intArray)

# Deletion from the end is simple as reducing the length of the array by 1
length -= 1
print("DELETING FROM THE END ON AN ARRAY - AFTER")
printArray2(intArray)

'''
Yup, that's it! Even though we call it a deletion, its not like we actually freed up the space for a new element, right? 
This is because we don't actually need to free up any space. Simply overwriting the value at a certain index deletes the element at that 
index. Seeing as the length variable in our examples tells us the next index where we can insert a new element, 
reducing it by one ensures the next new element is written over the deleted one. 
This also indicates that the Array now contains one less element, which is exactly what we want programmatically.
'''

# DELETING FROM THE START OF AN ARRAY
'''    
Costliest of all deletion operations for an Array- deleting the first element.
- Delete the first element of the Array to create a vacant spot at the 0th index.
- To fill that spot, we will shift the elements at "index 1 one step to the left".
- Every element all the way to the last one will be shifted one place to the left, hence there
is an empty space at the end of the array
- The shift elements takes O(N) time, where N is the number of elements in the Array.
'''
print("DELETING FROM THE START ON AN ARRAY - INITIAL")
printArray2(intArray)
# Starting at index 1, we shift each element one position to the left
for i in range(1, len(intArray)):
  # Shift each element one position to the left
  intArray[i-1] = intArray[i]

# Note that it's important to reduce the length of the array by 1.
# Otherwise, we'll lose consistency of the size. This length
# variable is the only thing controlling where new elements might
# get added.
length -= 1
print("DELETING FROM THE START ON AN ARRAY - AFTER")
printArray2(intArray)

# DELETING FROM ANYWHERE IN THE ARRAY
'''
- For Deletion at any given index, the empty space created by the deleted item need to be filled
- Each of the elements to right of the index will need to be shifted to the left by one.
- Deleting the first element of an Array is a special case of deletion at a given index, where the index is 0.
- This shift takes O(K) times where K is the number of elements to the right of the given index.
- Since potentially K = N, the time complexity of this operation is also O(N)
'''

print("DELETING FROM ANYWHERE IN THE ARRAY (Deleting index 1) - INITIAL")
printArray2(intArray)
# Delete the element at index 1
for i in range(2, len(intArray)):
  # Shift each element one position to the left
  intArray[i-1] = intArray[i]

# Again the length needs to be consistent with the current state of the array
length -= 1
print("DELETING FROM ANYWHERE IN THE ARRAY (Deleting index 1) - AFTER")
printArray2(intArray)