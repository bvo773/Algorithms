'''
Leetcode 977. Squares of sorted array

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1)
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2)
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constrainsts
1 <= nums.length <= 104
-10^4 <= nums[i] <= 10^4  is the same as -10000 <= nums[i] <= 10000
nums is sorted in non-decreasing order(smallest to largest)

[0 1 1]
  0  1 2 3 4
[-2 -1 0 3 4]
 l         r


if abs(l) < abs(r)
  abs(2) < abs(4) True right value is bigger, square it, and add it to result list starting at n-1, update right pointer
  abs
          
result = [       16]

Runtime O(n) - Look at every elements in the array exactly one time

'''

def sortedSquares(self, nums):
    n = len(nums)
    left = 0
    right = n - 1
    result = [None] * n
    
    # start at the last index
    for i in range(n-1, -1, -1):
      # compare absoluatet value of the left and right pointer, if left value pointer < right value pointter
      # right value pointer is greater, square it, and it to result list
      if abs(nums[left]) < abs(nums[right]):
        square = nums[right] ** 2
        result[i] = square
        right -= 1
      else:
        square = nums[left] ** 2
        result[i] = square
        left += 1
    
    return result