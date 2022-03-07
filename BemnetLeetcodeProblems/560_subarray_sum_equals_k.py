'''
Given an array of integers nums and an integer k, 
return the total number of subarrays whose sum equals to k.

Input: nums = [1,1,1], k = 2
Output: 2

Input: nums = [1,2,3], k = 3
Output: 2



'''
totalSumK = 0
myDict = {}
def subarray(nums, k):
  for num in nums:

    if num == k:
      totalSumK += 1
    elif myDict[num]
    else:
      other = num - k
      myDict[other] = num


