'''
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23

'''

nums = [1, -1, 3]



class Solution:
  def maxSubArray(self, nums):
    maxSub = nums[0]
    curSum = 0
    for num in nums:
      if curSum < 0:
        curSum = 0
      curSum += num
      maxSub = max(curSum, maxSub)
    
    return maxSub
  # 
  # Time Complexity: O(N^2)
  # for (i = 0...n-1): # start 
  #   for(j = i....n-1) # end
  #     curSum += num[j]   

  # Algorithm

  # 1) Initialize a variable maxSubarray = -infinity to keep track of the best subarray.
  # We need to use negative infinity, not 0, because it is possible that there are only negative numbers in the array.

  # 2) Use a for loop that considers each index of the array as a starting point.

  # 3) For each starting point, create a variable currentSubarray = 0. Then, loop through the array from the starting index, adding each element to currentSubarray.
  # Every time we add an element it represents a possible subarray - so continuously update maxSubarray to contain the maximum out of the currentSubarray and itself.

  # Return maxSubarray.
  def maxSubArray2(self, nums):
      
      max_subarray = float('-inf')

      for i in range(0, len(nums)):
        cur_sum = 0
        for j in range(i, len(nums)):
          cur_sum += nums[j]
          max_subarray = max(cur_sum, max_subarray)
      return max_subarray


