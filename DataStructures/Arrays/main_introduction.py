# Introduction to Data Structures: Arrays
# [A] WHAT IS AN ARRAY? An array is a collection of items. The items could be any data tyoes (strings, integers, booleans, books)

# Creating an Array
'''
On a computer. Array can hold up to N items. The value of N is decided by the time the person create the array. 
  - At the start, there are no DVDs in the array, we have to actually put them in.
  - If we get a 16th DVD, we need to make a new array
  - But we don't need to create an array to hold 10000 DVDs since we are wasting memory space on a computer if we
  only have 15 DVDs currently. The computer will reserve memory for 10000 DVDs even if we only put 15 DVDs in it
'''

N = 15
dvdCollection = [None] * N # An array called dvdCollection with 15 places in it. Each place can hold one DVD.

class DVD:
  # constructor to create a dvd with its properties
  def __init__(self, name, releaseYear, director):
    self.name = str(name) 
    self.releaseYear = int(releaseYear)
    self.director = str(director)

  def toString(self):
    return f"{self.name}, is directed by {self.director}, released in {self.releaseYear}"

#print(dvdCollection)

# [A] ACCESSING ELEMENTS IN ARRAYS
'''
The two most primitive Arrays operations are WRITING elements into them, and READING elements from them

- To put DVD into the Array, we need to decilde the place(indexes) we would like to go in. 
- Each of the places is identified using a number in the range of 0 to N - 1. 
  1st place 0, 2nd place is 1, 3rd place is 2... all the way up to 15th place, which is 14.
- These numbers are called indexes
'''

'''WRITING ITEMS INTO AN ARRAY''' 
# Let's put the DVD of the avengers into the 8th place of the array created above(dvdCollection)
avengersDVD = DVD("The Avengers", 2012, "Joss Whedon") # create DVD object for The Avengers
dvdCollection[7] = avengersDVD # Next, we put the DVD object in the 8th place of the Array. Starting from index 0, the index want is 7

# Put more DVDs in
incrediblesDVD = DVD("The incredibles", 2004, "Brad Bird")
findingDoryDVD = DVD("Finding Dory", 2016, "Andrew Stanton")
lionKingDVD = DVD("The Lion King", 2019, "Jon Favreau")

# Put "The incredibles" into the 4th place: index 3
dvdCollection[3] = incrediblesDVD

# Put "Finding Dory" into the 10th place: index 9
dvdCollection[9] = findingDoryDVD

# Put "The Lion King" into the 3rd place: index 2
dvdCollection[2] = lionKingDVD

# Notice we put The Incredibles at index 3(4th place). What happens if we run this next line?
starWarsDVD = DVD("Star Wars", 1977, "George Lucas")
dvdCollection[3] = starWarsDVD # The incrediblesDVD is overwritten with star wars at index 3

'''READING ITEMS FROM AN ARRAY'''
print(dvdCollection[7].toString())
print(dvdCollection[10]) # No item at index 10, the value it contains is None. Empty arrays slot has value None
print(dvdCollection[3].toString())
'''
Will print:
The Avengers, is directed by Joss Whedon, released in 2012
None
Star Wars, is directed by George Lucas, released in 1977
'''

'''WRITING ITEMS INTO AN ARRAY WITH A LOOP'''
# Commonly use a loop to put lot of values into an Array. 
# For example, create an array of int's and put the first 10 square numbers in it
squareNumbers = [None] * 10

# Go through each of the Array indexes, from 0 to 9
for i in range(len(squareNumbers)):
  # Be careful with 0-indexing. The next square number is given by (i+1)^2
  # Calculate it and insert it into the Array at index i
  square = (i + 1) ** 2 
  squareNumbers[i] = square

'''READING ITEMS FROM AN ARRAY WITH A LOOP'''
# Can also use a loop to print out everything that's in the Array.
# Go through each of the Array indexes, from 0 to 9.
for i in range(len(squareNumbers)):
  # Access and print what's at the i'th index.
  print(squareNumbers[i])

#  Will print:
#  1
#  4
#  9
#  16
#  25
#  36
#  49
#  64
#  81
#  100

# elegant way to do it "for each". We can use it whenever we don't need index values.
# For actually 'writing' the squares into the Array, it wouldnt work b/c we need the actual index numbers
for square in squareNumbers:
  print(square)

# [A] ARRAY CAPACITY VS LENGTH
'''
If somebody ask how long the DVD Array is, what would the answer be?
  Two different answers could be given.
    - The numbers of DVDs the array(box) could hold, if it was full, or (CAPACITY of the array)
    - The number of DVDs currently in the array(box) (LENGTH of the array)
  
  Both answers are correct but have different meanings!
  C
'''

'''ARRAY CAPACITY'''

dvdList = [None] * 6

# Not valid operation to insert element at dvdList[6] or dvdList[10].
# The List or array can hold up to 6 DVD's. This is array capacity.
# Trying to put an element greater than the list or array size, such as
# dvdList[6], dvdList[100] will cause code to crash ArrayIndexOutOfBounds exception!
# Array's Capacity is decided when the Array is created and cannot be changed later.

'''
If we get a 7th DVD, have to maker a larger Array or List and move the existing DVDs 
to the new array or list

The CAPACITY of an Array can be checked by looking at the length attribute.
In Python, its done by using len(arr) where arr is the name of the Array or List.
'''
capacity = len(dvdList)
print("The array has a capacity of " + str(capacity))

'''ARRAY LENGTH'''
# The other definition of 'length' is the number of DVDs, or other items currently in the Array.
# This is something you keep track of yourself, and you wont get any errors
# if you overwrite exisiting DVD, or if you leave a gap in the Array
array = [None] * 6 # array with a capacity of 6

length = 0 # Current length is 0, because it has 0 elements in it

for i in range(0, 3):
  array[i] = i * i
  length += 1 # Each time we add an element, the length goes up by one

print(f"The array has a capacity of {len(array)}")
print(f"The array has a length of {length}")

'''HANDLING ARRAY PARAMETERS'''
# Most Array questions on leetcode have an array passed as a parameter, with no 'length' or 'capacity' parameter
# When an Array is given as a parameter, without additional information, we can safely assume length == capacity
# That is, the Array is the exact size to hold all of itts data.
# Careful, since Arrays are 0-indexed. The capacity/length is the number of items, not a highest index.
# The highest index is .length - 1.

'''
  Leetcode 485. Max Consecutive Ones
  Worse Case: O(n)
  Given a binary array, find the maximum number of consecutive 1s in the array
'''
def findMaxConsecutiveOnes(nums):
  # Hint: Initialize and declare a variable here to 
  # keep track of how many 1's you seen in a row.
  # 0 1 1 0 1 1 1

  lengthOne = 0
  currentConsecutiveOne = 0
  for i in range(len(nums)):
    # Do something with element nums[i]
    if nums[i] == 1:
      lengthOne += 1
    elif nums[i] == 0:
      lengthOne = 0
    
    if lengthOne > currentConsecutiveOne:
      currentConsecutiveOne = lengthOne
  
  return currentConsecutiveOne

binary = [0, 1, 1, 1, 1, 0, 1, 1, 1]
print(findMaxConsecutiveOnes(binary))

'''
Leetcode 977. Squares of sorted array

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1)
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2)
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constrainsts
1 <= nums.length <= 104
-10^4 <= nums[i] <= 10^4  is the same as -10000 <= nums[i] <= 10000
nums is sorted in non-decreasing order(smallest to largest)

[0 1 1]
  0  1 2 3 4
[-2 -1 0 3 4]
 l         r


if abs(l) < abs(r)
  abs(2) < abs(4) True right value is bigger, square it, and add it to result list starting at n-1, update right pointer
  abs
          
result = [       16]

Runtime O(n) - Look at every elements in the array exactly one time

'''

def sortedSquares(self, nums):
    n = len(nums)
    left = 0
    right = n - 1
    result = [None] * n
    
    # start at the last index
    for i in range(n-1, -1, -1):
      # compare absoluatet value of the left and right pointer, if left value pointer < right value pointter
      # right value pointer is greater, square it, and it to result list
      if abs(nums[left]) < abs(nums[right]):
        square = nums[right] ** 2
        result[i] = square
        right -= 1
      else:
        square = nums[left] ** 2
        result[i] = square
        left += 1
    
    return result