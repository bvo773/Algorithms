# [A] Search in an array
'''
- Searching means to find an occurence of a particular element in the Array and return its position
- If we know the index in the Array that may contain the element we are looking for, the search is constant time operation. 
We simply go the given index and check whether or not the element is there.
'''

'''
Linear Search
- If the index is not known, which is the case most of the time, then we can check every element in the Array.
- We continue checking elements until we find the element we are looking for, or we reach the end of the Array.
- Linear search: a technique to for finding an element by checking through all elements one by one
- In the worse case, a linear search ends up checking the entire Array. Therefore, the time complexity for a linear search is O(N)

- Edge case (Basically mean scenarios that you wouldn't expect to encounter)
- For example, element you're searching for might not even exist in the Array.
- Or the input Array doesn't contain any elements at all, or perhaps it is null.
- It's important to handle all of these edge cases within the code
'''

'''
Function to call to determine whether a particular element is in an Array.
Notice we took care of the edge cases before proceeding with the actrual search.
We don't check the rest of the elements once we have found the element we are looking for
'''
def linearSearch(array, length, element):
  # Check for edge cases. Is the array null or empty?
  # If it is, then we return false because th element we're 
  # searching for couldn't possibly be in it.
  if array == None or length == 0:
    return False
  
  # Carry out the linear search by checking each element, starting from the first one
  for i in range(length):
    # We found the element at index i
    # So we return true to say it exists
    if array[i] == element:
      return True

  # We didn't find the element in the array
  return False

# Declare a new array of 6 elements
arr = [None] * 6

# Variable to keep track of the length of the array
length = 0

for i in range(6):
  arr[length] = i
  length += 1

print(f"Does the array contain the element 4? - {linearSearch(array=arr, length=length, element=4)}")
print(f"Does the array contain the element 30? - {linearSearch(array=arr, length=length, element=30)}")

