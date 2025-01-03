'''
Write a function, given a string containing only parentheses, determines(true/false) if every parentheses matches
Example:
  1. () 
  2. (() : x
  3. ()(())
  4. (())) : x

'''

class Solution:
  def validParentheses(self, s:int):
    stack = Stack()
    for ch in s:
      if ch == "(":
        stack.push(ch)
      elif not stack.isEmpty() and ch == ")":
        stack.pop()
      elif stack.isEmpty() and ch == ")":
        return False
      
    return stack.isEmpty()

class Stack:
  def __init__(self):
    self.size = 0
    self.arr = []

  def push(self, data):
    self.arr.append(data)
    self.size += 1

  def pop(self):
    if self.isEmpty(): return
    self.size -= 1
    return self.arr.pop()
  

  def isEmpty(self):
    return self.size == 0

  def size(self):
    return self.size
'''
solution = Solution()
print(solution.validParentheses("()"))
print(solution.validParentheses("())"))
print(solution.validParentheses("()(())"))
print(solution.validParentheses("(()))"))
'''
