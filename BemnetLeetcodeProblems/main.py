# Given an array, find the max contiguous(next to each other) sub array with length K
# [1,5,3,0,0,4,0,1]
# K = 3

# [1,5,3] = 9
# [5,3,0] = 8
# [3,0,0] = 3
# [0,0,4] = 4
# [0,4,0] = 4
# [4,0,1] = 5

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
'''
# [1,5,3,0,0,4,0,1]
#          [    ]

# K = 3


1 + 5 + 3 + 0 + 0 + 4 + 0 + 1
1 + 5 + 3 = 9
    5 + 3 + 0 = 9 - 1 + 0 = 8
        3 + 0 + 0 = 8 - 5 + 0 = 3
            0 + 0 + 4 = 3 - 3 + 4 = 4
                0 + 4 + 0 = 4 - 0 + 0 = 4
                    4 + 0 + 1 = 4 - 0 + 1 = 5


# [1,5,3] = 9 
# [5,3,0] = 8 = 9 - 1 + 0
# [3,0,0] = 3 = 8 - 5 + 0
# [0,0,4] = 4
# [0,4,0] = 4
# [4,0,1] = 5
'''

def findMaxContiguous(nums, k):
  currentMaxSum = -1
  resultList = [None] * k
  
  i = 0

  #(n-k)k = O(nk)
  while i + k < len(nums): 
    subList = nums[i : i + k]
    sumList = sum(subList)

    if sumList > currentMaxSum:
      # Update result list if the sum of list is greater than currentMaxSum
      for i in range(len(resultList)): # k times
        resultList[i] = subList[i]

      # Update current max sum  
      currentMaxSum = sumList

    i += 1

  return resultList

def findMaxContiguous2(nums, k):
  currentMaxSum = -1
  totalSum = 0
  # find sum of the first k ints
  for i in range(0, k):
    totalSum += nums[i]

  # Update current max sum if the sum of sublist is greater than previous calculated list
  if totalSum > currentMaxSum:
    currentMaxSum = totalSum
  
  # for the rest of the array
  for j in range(k, len(nums)):
    totalSum -= nums[j-k]
    totalSum += nums[j]

    if totalSum > currentMaxSum:
      currentMaxSum = totalSum
  
  return currentMaxSum


def findMaxContiguous3(nums, k):
  currentMaxSum = float('-inf')
  totalSum = 0

  totalSum = sum(nums[:k])
  
  if totalSum > currentMaxSum:
    currentMaxSum = totalSum
  
  for j in range(k, len(nums)):
    totalSum = totalSum - nums[j-k]
    totalSum = totalSum + nums[j]

    if totalSum > currentMaxSum:
      currentMaxSum = totalSum

  return currentMaxSum

inputList = [1,5,3,0,0,4,0,1]
k = 4

print(findMaxContiguous2(inputList, k))