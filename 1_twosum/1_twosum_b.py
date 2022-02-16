# Brute force: O (n^2)
# Space complexity: O (1) because extra space use does not grow as size on input grows, for example indices always has two constant elements 
class Solution:
  # don't consider given memory space in problem already. For eg, nums list
    def twoSum(self, nums, target):
      indices = []
      i = 0
      while i < len(nums):
        num_1 = nums[i]
        num_2 = target - num_1
        
        j = i + 1
        while j < len(nums):
          if (num_2 == nums[j]):
            indices.append(i)
            indices.append(j)
            break        
          j += 1

        if (len(indices) == 2):
          return indices
        else:
          i += 1

# Time complexity: O(n)
# Space complexity: O(n) because you're adding the element in the dictionary
    def twoSum2(self, nums, target):
      indices = []
      numsDict = {}
      
      for i in range(0, len(nums)):
        
        other = target - nums[i]
        if other in numsDict:
          index = numsDict[other]      
          indices.append(i)
          indices.append(index)
          break
        
        # We add element if the other pair doesn't exist
        numsDict[nums[i]] = i
     
      return indices

# Use space to reduce time complexity by saving data
# By using a hashmap(dictionary), set you can reduce access time to O(1) 


def main():
  answer = Solution()
  nums = [3,3]
  target = 6
  print(answer.twoSum2(nums, target))


if __name__ == "__main__":
  main()