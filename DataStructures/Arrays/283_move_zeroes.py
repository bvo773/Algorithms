'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
 
Constraints:
1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1
'''

# Time Complexity: O(N)
# Algorithm: Two pointers, k and p, 
# K at the beginning to maintain relative order of non-zero elements.
# P to traverse through nums
def moveZeroes(self, nums):
  """
  Do not return anything, modify nums in-place instead.
  """
  k = 0
  
  for p in range(len(nums)):
    if nums[p] != 0:
      nums[k] = nums[p]
      k += 1
  
  for p in range(k, len(nums)):
    nums[p] = 0


def moveZeroes2(nums) -> None:
  k = 0
  for p in range(1, len(nums)):
    if nums[k] == 0 and nums[p] != 0:
      nums[k] = nums[p]
      nums[p] = 0
      k += 1
      print(f"{p} : {nums}\n")

    elif nums[k] != 0:
      k += 1
      print(f"{p} : {nums}\n")
  
  

nums = [0,1,0,3,12]
moveZeroes2(nums)