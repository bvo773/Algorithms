def numOfSubarrays(arr, k, threshold):
  # find sum of the first k ints
    
  totalSum = 0
  for i in range(0, k):
    totalSum += arr[i]
  
  intAverage = int(totalSum/k)
  counter = 0
  
  # update counter (add to counter if the average >= threshold)
  if intAverage >= threshold:
    counter += 1
  
  # for the rest of the array
  for j in range(k, len(arr)):
      # slide the window up by one element
      totalSum = totalSum - arr[j-k]
      totalSum = totalSum + arr[j]
      # calculate the average of these k elements
      currAverage = int(totalSum/k)
      # update counter
      if currAverage >= threshold:
        counter += 1
  
  # return counter
  return counter