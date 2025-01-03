'''
INTRODUCTION
Similar to the array, the linked list is also a linear data structure. Here is an example:
   -----     -----     -----
  [23| -]-->[ 6| -]-->[15| -]--> null
   -----     -----     -----
Each element in the linked list is actually a separate object while all the objects are 
'linked together by the reference field' in each element.

There are two types of linked list: sing;y list and doubly linked list. The example is a singly linked list
and here is an example of doubly linked list. 
  # Look in OneNote for examples
'''

'''
INTRODUCTION - SINGLY LINKED LIST
Each node in a singly-linked list contains not only the value but also 'a reference field' to link the next node.
By this way, the singly-linked list organizes all the nodes in a sequence
'''
class SinglyListNode:
  def __init__(self, x):
    self.value = x
    self.next = None
# In most cases, we will use head node (the first node) to represent the whole list
'''
head = SinglyListNode(2)
print(head.value)
print(head.next)
'''

'''
OPERATIONS
Unlike the array, we are not able to access a random element in a singly-linked list in constant time.
If we want to get to the i^th element, we have to traverse from the head node one by one. It takes O(N) time on average
to visit an element, where N is the length of the linked list..
   head
   -----     -----     -----
  [23| -]-->[ 6| -]-->[15| -]--> null
   -----     -----     -----

For instance, in the example above, the head is the node 23. The only way to visit the 3rd node is to use the "next" field of the
head node to get to the 2nd node (node 6); Then with the "next" field of node 6, we are able to visit the 3rd node.

Even though a linked has such a bad performance (compared to the array) in accessing data by index, 
there are benefits using linked list when using operations such as "insert" and "delete".
'''

'''
ADD OPERATION - SINGLY LINKED LIST
If we want to add a new a value after a given node "prev", we should:

  1. Initialize a new node 'cur' with the given value
      # See ONENOTE
  2. Link the "next" field of cur to prev's next node next;
      # See ONENOTE
  3. Link the "next" field in prev to cur.
      # See ONENOTE
	
Unlike an array, we don’t need to move the all elements past the inserted element.
Therefore, you can insert a new node into a linked list O(1) time complexity, which is very efficient. 

AN EXAMPLE
# See OneNote

'''