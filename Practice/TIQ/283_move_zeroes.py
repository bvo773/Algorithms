class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[pos] = nums[i]
                pos += 1
        
        # from pos we add the end with zeros
        for i in range(pos, len(nums)):
            nums[i] = 0
        
        return nums