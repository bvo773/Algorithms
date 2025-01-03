class Node:
  def __init__(self, val, next = None):
    self.val = val
    self.next = next

def print_list(head):
  curr = head
  while curr:
    print(f"|Val: {curr.val} | Address {curr.next}")
    curr = curr.next

# TODO: Write a function that prints the whole linked list
def print_list_iterative(head):
  curr = head
  while curr:
    print(f"|Val: {curr.val} | Address: {curr.next}")
    curr = curr.next

# TODO: Write a funtion that print the whole linked list recursive
def print_list_recursive(head):
  if not head:
    return
  print(f"Val: {head.val} | Address: {head.next}")
  print_list_recursive(head.next)

# TODO:Write a function that print the list in reverse order (recursive)
def print_list_reverse_order(head):
  if not head:
    return
  print_list_reverse_order(head.next)
  print(f"|Val: {head.val} | Address {head.next}")

# TODO: Write a function that return the length of the linked list (recursive)
def get_list_length(head):
  if not head:
    return 0

  return 1 + get_list_length(head.next)

# TODO: Write a function that given a list, reverse it, and return the head (iterative)
def reverse_list_iterative(head):
  prev, curr = None, head
  while curr:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt

  return prev

# TODO: Write a function that given a list, reverse it, and return the head (recursive)
def reverse_list_recursive(head):
  def recurse(prev, curr):
    if not curr:
      return prev
    
    nxt = curr.next
    curr.next = prev
    return recurse(curr, nxt)
  
  reversed_list = recurse(prev = None, curr = head)
  return reversed_list

# Linked List 1 -> 2 -> 3 -> 4 -> None
node4 = Node(4)
node3 = Node(3, next = node4)
node2 = Node(2, next = node3)
head = Node(1, next = node2)

# FUNCTIONS CALLING START HERE
#print_list_iterative(head)
#print_list_recursive(head)
#print_list_reverse_order(head)
#print(get_list_length(head))
#print_list(reverse_list(head))
print_list(reverse_list_recursive(head))