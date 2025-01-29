from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int):
        count = {} #key: each number in nums # number of times num appears as its value
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        arr = []
        for num, cnt in count.items(): #num is a number in nums, cnt is its frequency 
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res  
    

nums = [1,2,2,3,3,3]
k = 2
sol = Solution()
print(sol.topKFrequent(nums, k))
