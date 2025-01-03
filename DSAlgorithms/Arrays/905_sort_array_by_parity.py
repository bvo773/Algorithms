def sortArrayByParity(self, nums: List[int]) -> List[int]:
  '''
  Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
  Input: nums = [3,1,2,4]
  Output: [2,4,3,1]
  Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

  Time Complexity: O(N), where N is the length of A. Each step of the while loop makes j-i decrease by at least one. (Note that while quicksort is O(N log N) normally, 
  this is O(N) because we only need one pass to sort the elements.)
  Space Complexity: O(1) in additional space complexity.
  Method: Two pointers at the start and end
  
  Then, there are 4 cases for (A[i] % 2, A[j] % 2):

  If it is (0, 1), then everything is correct: i++ and j--.

  If it is (1, 0), we swap them so they are correct, then continue.

  If it is (0, 0), only the i place is correct, so we i++ and continue.

  If it is (1, 1), only the j place is correct, so we j-- and continue.
  '''
  
  i = 0
  j = len(nums) - 1
  
  while i < j:
    if nums[i] % 2 > nums[j] % 2:
      temp = nums[i]
      nums[i] = nums[j]
      nums[j] = temp
      
    if nums[i] % 2 == 0: 
      i += 1
    
    if nums[j] % 2 == 1:
      j -= 1
    
  return nums