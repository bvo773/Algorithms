class Solution:
        
    # Runtime: O(N)
    # Space Complexity: O(1)
    # we have a stack to append every opening parentheses and a map to map closing parentheses and to opening parentheses
  def isValid(self, s: str) -> bool:
    stack = []
    close_to_open = {")":"(",
                     "}":"{",
                     "]":"[",
                     }

    for c in s:
      if c in close_to_open:
        if stack and close_to_open[c] == stack[-1]: 
          stack.pop()
        else:
          return False
      else:
        stack.append(c)
    
    return True if not stack else False
  
s = "()[]"
s2 = "[)[]"

solution = Solution()
print(solution.isValid(s))
print(solution.isValid(s2))