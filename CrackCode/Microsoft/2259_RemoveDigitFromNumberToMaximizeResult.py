class Solution:
  def removeDigit(self, number, digit):
    best = ""

    for i, c in enumerate(number):
      if digit == c:
        current = number[:i] + number[i+1:]
        if best == "" or current > best:
          best = current
          
    return best 