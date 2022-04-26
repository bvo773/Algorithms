
from ast import List


def reverse_nums(nums: List):
  result = []
  i = len(nums) - 1

  def reverse(i: int, result: List, nums: List):
    if i == 0:
      result.append(nums[0])
      return
    
    result.append(nums[i])
    reverse(i-1, result, nums)

  reverse(i, result, nums)
  return result

nums = [1, 2, 3, 4]
reversed_nums = reverse_nums(nums)
print(reversed_nums)