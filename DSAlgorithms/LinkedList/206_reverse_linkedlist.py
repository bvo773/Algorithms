class Solution:
  # Recursively
  # Time Complexity: O(N)
  # Space Complexity: O(N)
  def reverseList(self, head):
    def reverse_rec(prev, curr):
      if not curr:
        return prev
      
      nxt = curr.next
      curr.next = prev
      return reverse_rec(curr, nxt)
    
    head = reverse_rec(prev=None, curr = head)
    return head
  
  # Iteratively
  # Time Complexity: O(N)
  # Space Complexity: O(1)
  def reverseListIteratively(self, head):
    prev, curr = None, head

    while curr:
      nxt = curr.next
      curr.next = prev
      prev = curr
      curr = nxt 
    
    return prev

class Node:
  def __init__(self, val, next = None):
    self.val = val
    self.next = next 

def printLinkedList(head):
  curr = head
  while curr:
    print (f"Value: {curr.val}|Address:{curr.next}")
    curr = curr.next 

node3 = Node(3, None)
node2 = Node(2, node3)
head = Node(1, node2)

s = Solution()
printLinkedList(s.reverseList(head))
