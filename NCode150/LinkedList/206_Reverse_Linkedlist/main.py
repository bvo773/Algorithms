class Solution:
  # Recursively
  # Time Complexity: O(N)
  # Space Complexity: O(N)
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
