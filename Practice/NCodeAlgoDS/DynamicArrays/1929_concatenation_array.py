class Solution:
    def getConcatenation(self, nums):
        capacity = len(nums) * 2
        ans = [0] * capacity
        
        i, j = 0, 0
        while i < len(ans):
            if j == len(nums):
                j = 0
            ans[i] = nums[j]
            i += 1 
            j += 1
        return ans

nums = [1, 2, 3]
sol = Solution()
print(sol.getConcatenation(nums))