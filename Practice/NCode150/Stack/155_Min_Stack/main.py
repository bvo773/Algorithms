"""
All functions run in O(1) time :)
  push(val)
  pop()
  top()
  getMin()
"""

class MinStack:

  def __init__(self):
    self.stack = []
    self.minStack = []
      
  def push(self, val: int) -> None:
    self.stack.append(val)
    #if stack is not empty, compare the val and the top value of the minstack to keep track of the current min, 
    # else if stack is empty initially compare it to the val itself
    val = min(val, self.minStack[-1] if self.minStack else val) 
    self.minStack.append(val)
    
  # We pop both stacks
  def pop(self) -> None:
    self.stack.pop()
    self.minStack.pop()

  # only be call when our stack is non-empty, so we dont have to take care of the edge case if it is empty
  def top(self) -> int:
    return self.stack[-1]
      

  def getMin(self) -> int:
    return self.minStack[-1]

