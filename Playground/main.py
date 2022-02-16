# Python dictionary comprehension. Using a {key:value} pairs to map 
# english aphabet characters to their ascii value
# ASCII values are displayed in Decimal, Hexadecimal, Octal and Character values for each ASCII character.
myDict = {}

for i in range(97, 97+26):
  # map character to ascii value
  myDict[chr(i)] = i

def getAsciiValue(alphabet):
  return myDict[alphabet]

print(myDict)

print("Ascii value of character a is " +  str(getAsciiValue(alphabet='a')))


# Using Python comprehension feature to make syntax similar by doing the same thing above
# {key : func(key) for key in something } or {func(val) : val for val in something}
myDict2 = {chr(i) : i for i in range(97, 97+26)}
print(myDict2)
