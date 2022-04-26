
class Node:
  def __init__(self, val, next = None):
    self.val = val
    self.next = next

# Write a function that prints the whole linked list
# Example:   1 -> 2 -> 3 -> 4 -> None
def print_list(head):
  curr = head
  if curr is None:
    return
  while curr:
    print(f"{curr.val}")
    curr = curr.next
  

def print_list_recursive(head):
  if head == None:
    return
  else:
    print(head.val)
    print_list_recursive(head.next) #recurse
    return

# Print list in a reverse order
def print_list_reverse_recursive(head):
  if head == None:
    return
  else:
    print_list_reverse_recursive(head.next)
    print(head.val)


# return length of list
def length_recursive(head):
  if head == None:
    return 0
  else:
    return 1 + length_recursive(head.next)

    


# Homework review function and trace recursive function calls
# Define functions and trace it.

# BY TUESDAY OKAY?

# Given a list, reverse it, and return the head
# of the reverse list
# Example input: 1 -> 2 -> 3 -> 4 -> None
# Example ouput: 4 -> 3 -> 2 -> 1 -> None
# amesegenalew
def reverse_linkedin_list_recursive(head):
  def reverse_recursive(curr, prev):
    if not curr:
      return prev

    nxt = curr.next
    curr.next = prev
    
    return reverse_recursive(nxt, curr)

  head = reverse_recursive(curr = head, prev=None)
  return head
  
def reverse_linkedin_list_iterative(head):
  # two pointers
  prev, curr = None, head

  while curr:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt

  return prev
  
# Example input: 1 -> 2 -> 3 -> 4 -> None
n4 = Node(4,None)
n3 = Node(3,n4)
n2 = Node(2,n3)
head = Node(1,n2)


#head_of_reverse = reverse_linkedin_list_iterative(head)
head_of_reverse = reverse_linkedin_list_recursive(head)

print_list_recursive(head_of_reverse) # should print 4,3,2,1

