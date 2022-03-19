def removeDuplicates(nums):
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