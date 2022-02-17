# Introduction to Data Structures: Arrays
# [A] What is an Array? An array is a collection of items. The items could be any data tyoes (strings, integers, booleans, books)

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

print(dvdCollection)

# [A] ACCESSING ELEMENTS IN ARRAYS
'''
The two most primitive Arrays operations are WRITING elements into them, and READING elements from them

- To put DVD into the Array, we need to decilde the place(indexes) we would like to go in. 
- Each of the places is identified using a number in the range of 0 to N - 1. 
  1st place 0, 2nd place is 1, 3rd place is 2... all the way up to 15th place, which is 14.
- These numbers are called indexes
'''

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

print(dvdCollection)