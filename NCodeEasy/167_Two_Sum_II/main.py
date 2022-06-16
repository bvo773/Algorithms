class Solution:

  # Brute Force solution, we check combination of numbers that add up to the target
  # Time Complexity: O(N^2)
  # Space Complexity: O(1)
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    result = []
    
    for i in range(len(numbers)):
      for j in range(i+1, len(numbers)):
        if numbers[i] + numbers[j] == target:
          result.append(i+1)
          result.append(j+1)
          return result
        elif numbers[i] + numbers[j] > target:
          break
    
    return result
  
  # [1 2 4] target = 3
  # Time Complexity: O(N), we are visiting each element once in nums and check the difference
  # Space Compelxity: O(N), we are storing the prev value and index in a hash map so we can access it O(1) time for the
  # difference in value
  def twoSumNC(self, nums, target):
    prev_map = {}

    for index, value in enumerate(nums):
      diff = target - value
      if diff in prev_map:
        return [prev_map[diff], index]
      prev_map[value] = index
    return
  