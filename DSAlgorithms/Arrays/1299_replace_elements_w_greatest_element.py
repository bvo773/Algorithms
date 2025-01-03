# Time complexity: O(N^2)
# Space complexity: O(N)
def replaceElements(arr):
  N = len(arr)
  # for each index, we calculate the max element to the right 
  for i in range(N):
    if i == N-1:
      arr[i] = -1
    else:
      maxRight = max(arr[i+1:N])
      arr[i] = maxRight
      
  return arr