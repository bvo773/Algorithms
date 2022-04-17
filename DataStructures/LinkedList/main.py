from requests import head


class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

# Singly Linked List
# Insertion/Deletion: O(1)
# Accessing: O(N)
class LinkedList:
  def __init__(self):
    self.head = None

  def printList(self):
    curr = self.head
    while curr:
      print(f'|{curr.data}|{curr.next}')
      curr = curr.next


  def append(self, data):
    newNode = Node(data)
    #if list is empty
    if self.head is None:
      self.head = newNode
      return
    
    lastNode = self.head
    #similar to  while lastnNode.next is not None
    while lastNode.next:
      lastNode = lastNode.next
    lastNode.next = newNode

  def delete(self, data):
    curr = self.head
    

    
    



linkedList = LinkedList()
linkedList.append("A")
linkedList.append("B")
linkedList.append("C")
linkedList.printList()