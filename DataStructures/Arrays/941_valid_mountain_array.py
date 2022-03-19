# Runtime: O(n) - One Pass where N is the length of A
def validMountainArray(arr):
  inflection = None

  if len(arr) < 3:
    return False

  if len(arr) == 3:
    return arr[0] < arr[1] and arr[1] > arr[2]

  # get the inflection point when the difference is negative 
  # case: when difference is 0, mountain is neither strictly increasing or decreasing, thus, false
  for i in range(1, len(arr)):
    difference = arr[i] - arr[i-1]
    if difference < 0:
      inflection = i - 1
      break
    elif difference == 0:
      return False

  if inflection == None or inflection == 0:
    return False 

  for i in range(len(arr) - 2, inflection - 1, -1):
    difference = arr[i] - arr[i+1]
    if difference < 0:
      return False
    elif difference == 0:
      return False

  return True

def validMountainArray2(arr):
  N = len(arr)
  i = 0

  # walk up to find the inflection point or peak
  while i + 1 < N and arr[i] < arr[i+1]:
    i += 1
  
  # inflection point or peak can't be at first or last
  if i == 0 and i == N - 1:
    return False
  
  # walk down
  while i + 1 < N and arr[i] > arr[i+1]:
    i += 1
  
  return i == N - 1
  

