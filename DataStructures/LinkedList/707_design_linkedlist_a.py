
class Node:
  def __init__(self, val, next = None):
    self.val = val
    self.next = next
    
class MyLinkedList:
  def __init__(self):
    self.head = None
    self.size = 0

  def get(self, index: int) -> int:
    if index < 0 or index >= self.size:
      return -1
    
    if self.head is None:
      return
    
    curr = self.head
    for i in range(self.size):
      if i == index:
        return curr.val
      curr = curr.next

  def addAtHead(self, val: int) -> None:
    newNode = Node(val)
    if self.head is None:
      self.head = newNode
      self.size += 1
      return
      
    newNode.next = self.head
    self.head = newNode
    self.size += 1

  def addAtTail(self, val: int) -> None:
    newNode = Node(val)
    lastNode = self.head
    if lastNode is None:
      newNode.next = lastNode
      self.head = newNode
      self.size += 1
      return
    
    while lastNode.next:
      lastNode = lastNode.next
    lastNode.next = newNode
    self.size += 1

  def addAtIndex(self, index: int, val: int) -> None:
    if index < 0 and index > self.size:
      return
    
    newNode = Node(val)
    curr = self.head
    
    if curr is None:
      self.head = newNode
      self.size += 1
      return

    #  If index same as the size, append to end of linked list
    if index == self.size:
      lastNode = self.head

      while lastNode.next:
        lastNode = lastNode.next
      lastNode.next = newNode
      self.size += 1
      return
    
    position = index - 1
    for i in range(self.size):
      if index == 0:
        newNode.next = self.head
        self.head = newNode
        self.size += 1
        return      
      elif i == position:
        nextNode = curr.next
        curr.next = newNode
        newNode.next = nextNode
        self.size += 1
        return 
      curr = curr.next
  
  # TODO: HELP ME DELETE
  def deleteAtIndex(self, index):
    if index < 0 or index >= self.size:
      return
    
    if index == 0:
      self.head = self.head.next
    else:
      sentinelNode = Node(0, next = self.head)
      curr = sentinelNode
      for i in range(self.size):
        if i == index:
          curr.next = curr.next.next
          return
        else: 
          curr = curr.next
        
        
  def printList(self):
    curr = self.head
    index = 0
    while curr:
      print(f"index: {index}|{curr.val}|{curr.next}")
      curr = curr.next
      index += 1


linkedList = MyLinkedList()
linkedList.addAtTail(1)
print(linkedList.get(0))