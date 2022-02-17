''' 
Given an array, find the max contiguous(next to each other) sub array with length K


k = 3
 0 1 2    
[1,5,3,0,0,4,0,1]
 i 

maxTotal = -1

maxList = [k length]
 
loop through len(array):
 i + k < len(array):
    slice the list to ge a subarray from myDict[i:i+k]
    subarray = [1 5 3]
    sum total subarray list
    
    if subarray total > current max value:
      update the maxList
      update current max value to subarray total


[1,5,3] = 9
[5,3,0] = 8
[3,0,0] = 3
[0,0,4] = 4
[0,4,0] = 4
[4,0,1] = 5

    
'''

def findMaxContiguous(nums, k):
  currentMaxSum = -1
  resultList = [None] * k
  
  i = 0
  while i + k < len(nums):
    subList = nums[i : i + k]
    sumList = sum(subList)

    if sumList > currentMaxSum:
      # Update result list if the sum of list is greater than currentMaxSum
      for i in range(len(resultList)):
        resultList[i] = subList[i]

      # Update current max sum  
      currentMaxSum = sumList

    i += 1

  return resultList

inputList = [1,5,3,0,0,4,0,1]
k = 4

print(findMaxContiguous(inputList, k))