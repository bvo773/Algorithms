'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. 
More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k elements.
Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

'''
def removeElement(nums, val):
  '''
      k
        p  
  [1 1 2 3]
        k p         
  [1 2 3 3] 
  
  k moves slow because it only goes forward when the previous element is encountered by p is different
  where p is on or currently at
  
  p is a scout, someone ahead of the pack leading the charge to check if there is a repeated element
  
  we check the previous element p was on and we can easily figure out if an element is repeated or not
  
  if an element is repeated, k is going to stay there, k only moves when p encounters a new elment
  
  why two pointers
  1 correspond to the resulting array - slow pointer
  the other 1 correspond to the original array - fast pointer
  
  
  worse case scenario if every elements are the same in the original array, the resulting array would have only have the 
  first element, in any case the resulting will have the first element.
  '''
  n = len(nums)
  
  if n == 0:
    return 0
  
  k = 1
  for p in range(1, n):
    if nums[p] != nums[p-1]:
      nums[k] = nums[p]
      k += 1
    
  return k
        
  
