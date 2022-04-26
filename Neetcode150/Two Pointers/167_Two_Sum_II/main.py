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
  
  