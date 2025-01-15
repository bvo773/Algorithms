class Solution:
  
  def isAnagram(self, s: str, t: str) -> bool:
    # Solution 1: Count the characters of in the given string and see 
    # if the other string has the same characters and occurences using an Array or HashMap
    # Time Complexity: O(S + T) -> O(N)
    # Space Complexity: O(1) since our table stays constant no matter how large N grows 
    # O(S + T) since we are iterating both the strings
    if len(s) != len(t):
      return False
    
    countS, countT = {}, {}
    
    # For each char, everytime we see that char we increment the count by 1
    for i in range(len(s)):
      countS[s[i]] = 1 + countS.get(s[i], 0)
      countT[t[i]] = 1 + countT.get(t[i], 0)
    
  
    return countS == countT
    
    # Solution 2: We can sort the strings and compare them if they are equal to reduce space complexity
    # Usually interviewer assume sorting doesn't take extra space
    # Time Complexity: O(N log N)
    # Space Complexity: O(1)
    
    #return sorted(s) == sorted(t)