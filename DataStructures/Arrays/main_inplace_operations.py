'''
In-place Array operations are when we modify an Array, without creating a new Array.
  For example, inserting and deleting items by shifting existing items along.

Given an Array of integers, return an Array where every element at an even indexed position is squared
'''

def evenSquared(arr):
  for i in range(len(arr)):
    if i % 2 == 0:
      arr[i] = arr[i] ** 2
  
  return arr

arr = [9, -2, -9, 11, 56, -12, -3]
print(evenSquared(arr=arr))
