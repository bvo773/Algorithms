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

