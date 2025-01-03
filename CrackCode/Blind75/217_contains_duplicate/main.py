# Time Complexity: O(N) where N is the length of nums
# Space Complexity: O(N) where N is the length of nums
# Algorithm: For each number, we check if the number is already existed in the set, if it does return 
# True since its a duplicate, if not continue adding numbers to the set. If all numbers are distinct in the     set, return True
def containsDuplicate(nums: List[int]) -> bool:
  mySet = set()
  
  for num in nums:
      if num not in mySet:
          mySet.add(num)
      else:
          return True
      
  return False