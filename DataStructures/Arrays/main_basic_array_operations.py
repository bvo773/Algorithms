# [A] BASIC ARRAY OPERATIONS
'''
Array is a data structure which means it stores data into a specific format and supports certain
operations on the data it stored.

INSERT
DELETE
SEARCH

Example) Consider the DVD inventory management software. Some operations that are performed on the software
might be
  - INSERT a new DVD into the collection
  - DELETE a DVD from the exisiting collection if we dont it in the inventory anymore
  - SEARCH for a particular DVD from the inventory. One of the most commonly executed operations
'''

# [A] ARRAY INSERTIONS
'''
  - Inserting a new element at the 'end' of the Array
  - Inserting a new element at the 'beginning' of the Array
  - Inserting a new element at given 'index' inside the Array
'''

# INSERTING AT THE END OF AN ARRAY
'''
At any point in time, we know the last element of the Array, kept it track of it in our 
'length' variable. 
  - To insert the last element at the end, we assign the new element to one index past
  the current last element

          insert [8]
  [ 1 2 3 4 5 6 7   ]

  [ 1 2 3 4 5 6 7 8 ]
'''

# Make an Array that can hold up to 6 items, then add items in the first 3 indexes
intArray = [None] * 6
length = 0 # using length to keep track of the last element of the array

for i in range(0, 3):
  intArray[length] = i
  length += 1

# printArray function to help visualize
def printArray(arr):
  for i in range(0, len(arr)):
    print(f"Index {i} contains {arr[i]}")

# Insert a new element at the at the end of the array. Remember, it is important
# to ensure there is enough space in the array before inserting a new element
intArray[length] = 10
length += 1 # increment length since we just added nother lement
printArray(intArray)

#INSERTING AT THE START OF AN ARRAY
'''
To insert an element at the START of the Array, we have to shift all other elements in the Array to
the right by one index to create space for the new element.
  - Very costly operation since each of the existing elements has to be shifted one step to the right
  - The shift implies that this is not a constant time operation.
  - The time taken for insertion at the beginning of an Array will be proportional to the length of the Array
  - Complexity: linear complexity: O(N), where N is the length of the Array.
'''
'''
- First, we have to create space for a new element
- We do that by shifting each element one index to the right
- This will firstly move the element at index 3, then 2, then 1, then finally 0
- We need to go backwards to avoid overwritting any elements
'''

print("\nInserting at the START of an array")
for i in range(3, -1, -1):
  intArray[i + 1] = intArray[i]

# now we have created space for the new element, we can insert it at the beginning
intArray[0] = 20
length += 1
printArray(intArray)

#INSERTING ANYWHERE IN THE ARRAY
'''
Similarly, for inserting at any given index, we first need to shift all the elements from that 
'index onwards one position to the right'. Once the space is created for the new elment, we proceed with 
the insertion.

Basicially, insertion at the beginning is basically a special case for inserting an element at a given index-
in that case, the given index was 0.
  - Again, this is a costly operation. We could potentially have to shift almost all the other elements to
  the right before actually inserting the new element.
  - Shifting lots elements once place to the rights adds to the time complexity of the insertion task
'''

print("\nInserting ANYWHERE of an array, insert 30 at index 2")
# Let's insert at the element at index 2
# First, create space for the new element
for i in range(length-1, 1, -1):
  intArray[i + 1] = intArray[i] # shift each element one position to the right

# We have created space for the new element, we can insert it at the required index
intArray[2] = 30
length += 1
printArray(intArray)

'''
Leetcode 1089. Duplicate Zeros
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.
'''
arr1 = [1,0,2,3,0,4,5,0]
arr2 = [0, 0, 0]

def duplicateZeros(arr):
  """
  Do not return anything, modify arr in-place instead.
  """
  n = len(arr)
  i = 0
  while i < len(arr):
    # if 0, shift the elements to the right and decrement to remove the right most element
    if arr[i] == 0 and i + 1 < n:
      n -= 1
      for j in range(n-1, i, -1):
        arr[j + 1] = arr[j]

      # add duplicate 0 at i + 1, and increment i
      arr[i+1] = 0
      n += 1
      i += 1
    
    i += 1

'''
Leetcode 88. Merge Sorted Array
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
'''

def merge(nums1, m, nums2, n):
  """
  Do not return anything, modify nums1 in-place instead.
  
  Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
  p write pointer for nums1
  p1 read pointer for nums1Copy
  p2 read pointer for nums2
  
  compare between nums1copy and num2 and write the smallest values first             into nums1
  
            p
  nums1 = [1,2,3,0,0,0] 
                p1
  nums1Copy = [1 2 3]
          p2
  nums2 = [2 5 6]
  
  1 < 2 -> set nums1[0] = 1
  
  Output: [1,2,2,3,5,6]
  Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
  The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
  """

  # Time complexity: O ((n+m) log(n+m)) -> n + m is the size of the output array
  # N = n + m -> O ((N) log(N))   -> N where N is the total size of the array to sort all the elements
  # log(nm) = log(n) + log(m)
  # O (n + m) 

  '''
  # Approach 1: Add add elements from nums2 into nums1 and then sort it out. O( (N) log(N) )
  for i in range(n):
    nums1[i + m] = nums2[i]
  
  # O log(n+m) - best sorting algorithm run log n time
  nums1.sort()
  '''
  '''  
  # Approach 2: Three pointers (Start from the beginning)
  # Time Complexity: O (m+n)  where N = m + n total size -> O (N) - linear
  # Space Compexity: O (m)
  # Make a copy of the first m elements of nums1
  nums1Copy = nums1[:m]
  
  # Two read pointers to read from nums1Copy and nums2
  p1 = 0
  p2 = 0
  
  # if p2 is out of bounds, write the remaining elements from nums1Copy into nums1
  for p in range(m + n):
    if  p2 >= n or (p1 < m and nums1Copy[p1] <= nums2[p2]):
      nums1[p] = nums1Copy[p1]
      p1 += 1
    else:
      nums1[p] = nums2[p2]
      p2 += 1
  # O (n) - As the size of inputs increases, the time also increases linearly
  # O (1) - As the size input increases, the time does not change in relation to the inputs
  # O (log n) - As the size input increases, it will change logarithmic - Look it up
  # O (n^2) - As the size input increases, it will run quadraticly (longer)
  '''
  
  # Approach 3: Bemnet Two Pointers Start from the END comparing the elements and put them starting at the last index
  p1 = m - 1
  p2 = n - 1
  
  for i in range(m + n - 1, -1, -1):
    if p1 < 0:
      nums1[i] = nums2[p2]
      p2 -= 1
    elif p2 < 0:
      nums1[i] = nums1[p1]
      p1 -= 1
    elif nums1[p1] <= nums2[p2]:
      nums1[i] = nums2[p2]
      p2 -= 1
    else:
      nums1[i] = nums1[p1]
      p1 -= 1

        