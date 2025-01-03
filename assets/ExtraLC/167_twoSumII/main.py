
'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. 
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Example) Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].


HINTS
# If an array is sorted, what techniques we can use by having this clue
# non-decreasing order next number can be equal but cannot be less 0 1 1 2 3 4

        p1p2
[1 2 3 4 6]
if p1 moves forward, the sum increases
if p2 moves backward, the sum decreases
if p1==p2 there are no pairs
sum = p1 + p2 

target = 11
PATTERN = TWO POINTERS -> using two pointers to check if the pointers add up to the target value

if target < pointers, decrement p2
if target > pointers, increment p1
if target == pointers, 

Time complexity: O(N) how do we achieve this
'''

def twoSum(self, numbers: List[int], target: int) -> List[int]:
  p1 = 0
  p2 = len(numbers) - 1
  indices = []

  while p1 != p2:
    total = numbers[p1] + numbers[p2]

    if total < target:
      p1 += 1
    elif total > target:
      p2 -= 1
    else:
      indices.append(p1+1) # since list is empty
      indices.append(p2+1)
      return indices

  return indices  


def main():
  print("Hello World")

if __name__ == "__main__":
  main()