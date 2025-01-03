'''
In-place Array operations are when we modify an Array, without creating a new Array.
  For example, inserting and deleting items by shifting existing items along.

Given an Array of integers, return an Array where every element at an even indexed position is squared

Input: array = [9, -2, -9, 11, 56, -12, -3]
Output: [81, -2, 81, 11, 3136, -12, 9]
Explanation: The numbers at even indexes (0, 2, 4, 6) have been squared, 
whereas the numbers at odd indexes (1, 3, 5) have been left the same.


'''

# Inefficient way of solving problem b/c it uses O(length) extra space
def squareEven(arr):

  # Check for edge cases
  if arr == None:
    return None
  
  result = [None] * len(arr)

  for i in range(len(arr)):
    element = arr[i]

    # if the index is even number, square the element
    if i % 2 == 0:
      element *= element
    
    #Write the elemnt into the result array
    result.append(element)
  
  # return result array
  return result

'''
We could iterate over the original input Array, overwriting every even-indexed element with own square. This way, we won't need that extra space. 
It is this techinique of working directly in the input Array, and not creating a new Array, that we call "in-place".

Important in programming interview, where there is a focus on minimising both time and space complexity of algorithms. 
'''
def evenSquare(arr):
  if arr == None:
    return None

  # Iterate through the original array
  for i in range(len(arr)):
    # if index is even number, then we square the element and replace the original value in the Array
    if i % 2 == 0:
      arr[i] *= 2
    
    # Notice how we do not need to do anything for the 'odd' indexes? 

  # return the original array. Some problems on leetcode require you to return it, and other's don't 
  return arr

arr = [9, -2, -9, 11, 56, -12, -3]
print(evenSquare(arr=arr))
