''' Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order. 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.



target = 4 - num1 = num2


'''

class Solution(object):
    def twoSum(self, nums, target):
        i = 0
        sumIndices = []
        while i < len(nums):
            num1 = nums[i]
            num2 = target - num1
            j = i + 1
            while j < len(nums):
                if (num2 == nums[j]):
                    print('i: {} j: {}'.format(i,j))
                    sumIndices.append(i)
                    sumIndices.append(j)
                j = j + 1
            i += 1
        
        return sumIndices
   
def main():
    sol = Solution()
    nums =  [5,2,3]
    target = 8
    print(sol.twoSum(nums,8))

if __name__  ==  '__main__':
    main()
        
        