"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.


Time Complexity: O(n)
Space Complexity: O(N), the extra space based on the number of items stored in the hash table.
"""

class Solution:
    def twoSum(self, nums, target):
        numsMap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in numsMap:
                return [numsMap[diff], i]
            numsMap[nums[i]] = i

nums = [2,7,11,15]
sol = Solution()
print(sol.twoSum(nums, 9))



