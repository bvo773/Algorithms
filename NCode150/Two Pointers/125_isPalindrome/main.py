class Solution:
  '''
  Alphanumeric
    0 - 9
    A - Z
    a - z
    
  Built in Methods
  1) lower()
  2) isalnum() 
  3) ord(ch) -> returns ascii code of a char
  '''
  # Easy Way
  def isPalindrome(self, s: str) -> bool:
    newS = ""
    
    for ch in s:
      if ch.isalnum():
        newS += ch.lower()
    
    return newS == newS[::-1]


  # Time Complexity: O(N), where N is the length of s
  # Space Complexity: O(1)
  def isPalindrome2(self, s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
      while l < r and not self.alphaNum(s[l]):
        l += 1
      while l < r and not self.alphaNum(s[r]):
        r -= 1
      
      if s[l].lower() != s[r].lower():
        return False
      
      l += 1
      r -= 1
    
    return True
  
  # Could write own alpha-numeric function
  def alphaNum(self, ch):
    return (ord('A') <= ord(ch) <= ord('Z') or
            ord('a') <= ord(ch) <= ord('z') or
            ord('0') <= ord(ch) <= ord('9'))
