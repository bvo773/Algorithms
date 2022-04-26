
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

class MyLinkedList:

  def __init__(self):
    self.head = Node(0) # sentinel node as pseudo-head
    self.size = 0

  
  # int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
  def get(self, index: int) -> int:
    if index < 0 or index >= self.size:
      return -1
    
    curr = self.head
    for _ in range(index + 1):
      curr = curr.next
    
    return curr.val
      

  def addAtHead(self, val: int) -> None:

    self.addAtIndex(0, val)

  def addAtTail(self, val: int) -> None:
    self.addAtIndex(self.size, val)

  '''
  Add a node of value val before the index-th node in the linked list.
  If index equals to the length of linked list, the node will be appended to the end of linked list. 
  If index is greater than the length, the node will not be inserted.'''
  def addAtIndex(self, index: int, val: int) -> None:
    if index > self.size:
      return -1
    
    if index < 0:
      index = 0

    self.size += 1
     # find predecessor of the node to be added
    pred = self.head
    for _ in range(index):
      pred = pred.next
    
    newNode = Node(val)
    newNode.next = pred.next
    pred.next = newNode

  def deleteAtIndex(self, index: int) -> None:
    return