class MinStack:

  def __init__(self):
    self.stack = []
    self.minStack = []
    self.size = 0
      
      
  def push(self, val: int) -> None:
    
    if not self.minStack: #if the min stack is empty, we just add the val
      self.minStack.append(val)
    else:
      if val < self.minStack[-1]:
        self.minStack.append(val)
      else:
        self.minStack.append(self.minStack[-1])

    self.stack.append(val)
    self.size += 1
  

  def pop(self) -> None:
    if self.stack and self.minStack:
      self.stack.pop()
      self.minStack.pop()
      self.size -= 1
      
  def top(self) -> int:
    if self.stack:
      return self.stack[-1]
      

  def getMin(self) -> int:
    if self.minStack:
      return self.minStack[-1]


solution = MinStack()
print(solution.getMin())
print(solution.minStack)
print(solution.stack)