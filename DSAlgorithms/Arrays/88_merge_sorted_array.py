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