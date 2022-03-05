'''
  Leetcode 485. Max Consecutive Ones
  Worse Case: O(n)
  Given a binary array, find the maximum number of consecutive 1s in the array
'''
def findMaxConsecutiveOnes(nums):
  # Hint: Initialize and declare a variable here to 
  # keep track of how many 1's you seen in a row.
  # 0 1 1 0 1 1 1

  lengthOne = 0
  currentConsecutiveOne = 0
  for i in range(len(nums)):
    # Do something with element nums[i]
    if nums[i] == 1:
      lengthOne += 1
    elif nums[i] == 0:
      lengthOne = 0
    
    if lengthOne > currentConsecutiveOne:
      currentConsecutiveOne = lengthOne
  
  return currentConsecutiveOne

binary = [0, 1, 1, 1, 1, 0, 1, 1, 1]
print(findMaxConsecutiveOnes(binary))