'''
Given an array nums of integers, return how many of them contain an even number of digits.
Input: nums = [12,345,2,6,7896]
Output: 2

12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
'''
def findNumbers(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    evenDigits = 0
    for num in nums:  
      numString = str(num)
      length = len(numString)
      
      if length % 2 == 0:
        evenDigits += 1
        
    return evenDigits