'''
Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).
More formally check if there exists two indices i and j such that

Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.

Input: arr = [7,1,14,11]
Output: true
Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.

Input: arr = [3,1,7,11]
Output: false
Explanation: In this case does not exist N and M, such that N = 2 * M.
'''
'''
Run Time: O(N^2)
Algorithm: Two pointers i and j, we check if arr[i] == arr[j] * 2, return True
'''
def checkIfExist(arr):
  for i in range(len(arr)):
    for j in range(len(arr)):
      if arr[i] == arr[j] * 2 and i != j:
        return True

  return False


# Runtime: O(N)
# Space Complexity: O(N) for the set object, the set size is depended on the the size of the array
# Algorithm: Iterate over the array and check if the element in the array is multiplied by 2 or divided by 2 is equal to the set. If it existed, then return true. If not existed, add the element to the Set
def checkIfExist2(arr):
  mySet = set()

  for num in arr:
    if num * 2 in mySet or num/2 in mySet:
      return True
    else:
      mySet.add(num)
  return False