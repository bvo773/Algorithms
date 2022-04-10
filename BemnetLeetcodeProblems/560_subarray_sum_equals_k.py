'''
Given an array of integers nums and an integer k, 
return the total number of subarrays whose sum equals to k.

Input: nums = [1,1,1], k = 2 
Output: 2

Input: nums = [1,2,3], k = 3
Output: 2

How many contiguous arrays sum up to k?

BRUTE FORCE - O(N^2) - We have n squared subarrays, check for every subarrays that add up to K, n squared time
Constraints: -1000 <= nums[i] <= 1000

If we use sliding windows, since the values can be negative, adding a value doesn't guaranteed we are increasing the size.
Or removing a value doesn't mean we are decreasing the size. For eg) 1- -2 = 3

'''
# 3/29/22 - 560. Subarray sum equals k
# Time Complexity: Brute Force O(N^3) For each index, we checked for every subArray
# starting from subArrayStart and subArryEnd

#  0 1  2 3
# [1 0 -1 1] k = 1
# len(array + 1) because sliding is not exclusive 
# counter = 5
      
# [1] == k
# [1 0] != k
# [1 0 -1 ] == k
# [1 0 -1 1] != k

#   [0] != k
#.  [0 -1] != k      
#   [0 -1 1] == k

#     [-1] != k
#     [-1 1] == k
#        [1] == k  

def subArraySum(nums, k):
  counter = 0

  for subSizeStart in range(0, len(nums)):
    for subSizeEnd in range(subSizeStart + 1, len(nums) + 1):
      S = sum(nums[subSizeStart:subSizeEnd])
      if S == k:
        counter += 1

  return counter

nums = [1, -1, 1]
k = 1
print(subArraySum2(nums, k))

# Bem's solution for O(N^3)
# Review, Trace
# lol same as above, but i feel yours is more efficient than mine haha, as i read it more and it makes sense
# [1 -1  1]
'''
subSize Outer loop: 1 - len(nums): 1 -> 3
subSizeStart Inner loop: 0 - len(nums) - subSize + 1

k = 1
        0  1  2
nums = [1 -1  1]

counter = 0

when subSize is 1

inner loop start from 0 to 3 - 1 + 1 = 3
1st iteration
subSize = 1
subSizeStart = 0 

S = sum of nums[subSizeStart:subSizeStart+subSize] 
S = sum of nums[0:0+1] -> S = nums[0:1] = 1
1 == k
counter = 1

2nd iteration
subSize = 1
subSizeStart = 1
S = sum of nums[1:1+1] = S = nums[1:2] = -1 
-1 != k
counter = 1

3rd iteration
subSize = 1
subSizeStart = 2
S = sum of nums[2:2+1] = S = nums[2:3] = 1
1 == k
counter = 2

===========================================
subSize = 2

inner loop start from 0 to 3 - 2 + 1 = 2
1st iteration
subSize = 2
subSizeStart = 0
S = sum of nums[0:0+2] = S = nums[0:2] = [1 -1] = 0
0 != k
counter = 2

2nd iteration
subSize = 2
subSizeStart = 1
S = sum of nums[1:1+2] = S = nums[1:3] = [-1 1] = 0 
0 != k
counter = 2
==============================================
subSize = 3

inner loop start from 0 to 3 - 3 + 1 = 1
subSize = 3
subSizeStart = 0
S = sum of nums[0:0+3] = nums[0:3] = [1 -1 1] = 1
1 == k
counter = 3
'''
def subArraySumBem(nums, k):
  counter = 0

  for subSize in range(1, len(nums)):
    for subSizeStart in range(0, len(nums) - subSize+1):
      S = sum(nums[subSizeStart:subSizeStart+subSize])
      if S == k:
        counter += 1

  return counter

# O(N^3) -> O(N^)
# [1 -1 1]
'''
k = 1
S = [1 -1 1]

subSize = 1
S = nums[0:1] = 1
subSizeStart = 0
S == k -> counter += 1
 0  1  2
[1 -1 1]
S = 1
S = nums[subSizeStart+subSize] - nums[subSizeStart] = nums[0+1] - nums[0] = -1 - 1 = -2
S != k

subSize = 1
subSizeStart = 1

'''
def subArraySumBem2(nums, k):
  counter = 0
  for subSize in range(1, len(nums)):
    S = sum(nums[0:subSize]) # window
    for subSizeStart in range(0, len(nums) - subSize): # calculate the next subarrays
      if S == k:
        counter += 1
      # window is moved to the right
      S += nums[subSizeStart+subSize] - nums[subSizeStart]

    if S == k:
      counter += 1

  return counter